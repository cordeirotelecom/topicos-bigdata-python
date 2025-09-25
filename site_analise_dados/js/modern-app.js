class DataInsightsPro {
    constructor() {
        this.currentAnalysis = null;
        this.charts = {};
        this.apiKeys = {
            alphavantage: 'demo', // Em produção, usar chave real
            openweather: 'demo',   // Em produção, usar chave real
            newsapi: 'demo'        // Em produção, usar chave real
        };
        
        this.init();
    }

    init() {
        document.addEventListener('DOMContentLoaded', () => {
            this.setupNavigation();
            this.setupAnalysisControls();
            this.setupQuickActions();
            this.setupUploadModal();
            this.setupTemplates();
            
            console.log('DataInsights Pro initialized successfully!');
        });
    }

    // Navigation
    setupNavigation() {
        const navItems = document.querySelectorAll('.nav-item');
        const sections = document.querySelectorAll('.section');

        navItems.forEach(item => {
            item.addEventListener('click', () => {
                const targetSection = item.getAttribute('data-section');
                
                // Update active nav item
                navItems.forEach(nav => nav.classList.remove('active'));
                item.classList.add('active');
                
                // Show target section
                sections.forEach(section => section.classList.remove('active'));
                document.getElementById(targetSection).classList.add('active');
            });
        });
    }

    // Quick Actions
    setupQuickActions() {
        const actionCards = document.querySelectorAll('.action-card');
        
        actionCards.forEach(card => {
            card.addEventListener('click', () => {
                const action = card.getAttribute('data-action');
                this.handleQuickAction(action);
            });
        });
    }

    handleQuickAction(action) {
        switch (action) {
            case 'financial':
                this.switchToAnalysis('stocks');
                break;
            case 'weather':
                this.switchToAnalysis('weather');
                break;
            case 'social':
                this.switchToAnalysis('news');
                break;
            case 'business':
                this.switchToAnalysis('demographic');
                break;
            case 'upload':
                this.openUploadModal();
                break;
            case 'demo':
                this.runDemo();
                break;
        }
    }

    switchToAnalysis(dataSource) {
        // Switch to analysis tab
        document.querySelectorAll('.nav-item').forEach(nav => nav.classList.remove('active'));
        document.querySelector('[data-section="analysis"]').classList.add('active');
        
        document.querySelectorAll('.section').forEach(section => section.classList.remove('active'));
        document.getElementById('analysis').classList.add('active');
        
        // Set data source
        document.getElementById('data-source').value = dataSource;
        this.handleDataSourceChange();
    }

    // Analysis Controls
    setupAnalysisControls() {
        const dataSourceSelect = document.getElementById('data-source');
        const startButton = document.getElementById('start-analysis');

        dataSourceSelect.addEventListener('change', () => {
            this.handleDataSourceChange();
        });

        startButton.addEventListener('click', () => {
            this.startAnalysis();
        });

        // Setup config change listeners
        this.setupConfigListeners();
    }

    setupConfigListeners() {
        const inputs = document.querySelectorAll('#stock-symbol, #weather-city');
        inputs.forEach(input => {
            input.addEventListener('input', () => {
                this.validateAnalysisForm();
            });
        });

        const selects = document.querySelectorAll('#stock-period, #crypto-symbol, #crypto-currency, #weather-type');
        selects.forEach(select => {
            select.addEventListener('change', () => {
                this.validateAnalysisForm();
            });
        });
    }

    handleDataSourceChange() {
        const source = document.getElementById('data-source').value;
        
        // Hide all config groups
        document.querySelectorAll('[id$="-config"]').forEach(group => {
            group.style.display = 'none';
        });

        // Show relevant config group
        if (source) {
            const configGroup = document.getElementById(`${source.replace('stocks', 'stock')}-config`);
            if (configGroup) {
                configGroup.style.display = 'block';
            }
        }

        this.validateAnalysisForm();
    }

    validateAnalysisForm() {
        const source = document.getElementById('data-source').value;
        const startButton = document.getElementById('start-analysis');
        let isValid = false;

        switch (source) {
            case 'stocks':
                isValid = document.getElementById('stock-symbol').value.trim() !== '';
                break;
            case 'crypto':
                isValid = true; // All fields have default values
                break;
            case 'weather':
                isValid = document.getElementById('weather-city').value.trim() !== '';
                break;
            case 'news':
            case 'demographic':
                isValid = true; // No additional inputs required
                break;
        }

        startButton.disabled = !isValid;
    }

    // Analysis Execution
    async startAnalysis() {
        const source = document.getElementById('data-source').value;
        
        this.showLoadingState();
        
        try {
            let data;
            let analysisType;

            switch (source) {
                case 'stocks':
                    data = await this.fetchStockData();
                    analysisType = 'Análise de Ações';
                    break;
                case 'crypto':
                    data = await this.fetchCryptoData();
                    analysisType = 'Análise de Criptomoedas';
                    break;
                case 'weather':
                    data = await this.fetchWeatherData();
                    analysisType = 'Análise Climática';
                    break;
                case 'news':
                    data = await this.fetchNewsData();
                    analysisType = 'Análise de Tendências';
                    break;
                case 'demographic':
                    data = await this.fetchDemographicData();
                    analysisType = 'Análise Demográfica';
                    break;
            }

            this.displayResults(data, analysisType);
            this.showNotification('Análise concluída com sucesso!', 'success');

        } catch (error) {
            console.error('Analysis error:', error);
            this.showNotification('Erro ao realizar análise. Tente novamente.', 'error');
            this.showEmptyState();
        }
    }

    showLoadingState() {
        document.getElementById('analysis-empty').style.display = 'none';
        document.getElementById('analysis-results').style.display = 'none';
        document.getElementById('analysis-loading').style.display = 'block';
    }

    showEmptyState() {
        document.getElementById('analysis-loading').style.display = 'none';
        document.getElementById('analysis-results').style.display = 'none';
        document.getElementById('analysis-empty').style.display = 'block';
    }

    // Data Fetching Methods
    async fetchStockData() {
        const symbol = document.getElementById('stock-symbol').value;
        const period = document.getElementById('stock-period').value;
        
        // Simulate API call with realistic data
        return new Promise(resolve => {
            setTimeout(() => {
                const basePrice = 50 + Math.random() * 100;
                const data = this.generateTimeSeriesData(basePrice, this.getPeriodDays(period));
                resolve({
                    symbol,
                    period,
                    data,
                    currentPrice: data[data.length - 1].value,
                    change: ((data[data.length - 1].value - data[0].value) / data[0].value * 100).toFixed(2)
                });
            }, 2000);
        });
    }

    async fetchCryptoData() {
        const symbol = document.getElementById('crypto-symbol').value;
        const currency = document.getElementById('crypto-currency').value;
        
        // Simulate crypto API
        return new Promise(resolve => {
            setTimeout(() => {
                const basePrice = symbol === 'bitcoin' ? 150000 : 8000;
                const data = this.generateTimeSeriesData(basePrice, 30);
                resolve({
                    symbol,
                    currency,
                    data,
                    currentPrice: data[data.length - 1].value,
                    marketCap: '1.2T',
                    volume24h: '25.8B'
                });
            }, 2000);
        });
    }

    async fetchWeatherData() {
        const city = document.getElementById('weather-city').value;
        const type = document.getElementById('weather-type').value;
        
        return new Promise(resolve => {
            setTimeout(() => {
                const data = this.generateWeatherData(type);
                resolve({
                    city,
                    type,
                    data,
                    current: {
                        temp: 24,
                        humidity: 65,
                        pressure: 1013,
                        windSpeed: 12
                    }
                });
            }, 1500);
        });
    }

    async fetchNewsData() {
        return new Promise(resolve => {
            setTimeout(() => {
                resolve({
                    trends: ['Tecnologia', 'Sustentabilidade', 'IA', 'Blockchain'],
                    sentiment: 'Positivo',
                    articles: 1247,
                    engagement: '85%'
                });
            }, 1500);
        });
    }

    async fetchDemographicData() {
        return new Promise(resolve => {
            setTimeout(() => {
                resolve({
                    population: '215.3M',
                    growth: '0.77%',
                    urbanization: '87.1%',
                    medianAge: 33.2,
                    data: this.generateDemographicData()
                });
            }, 1500);
        });
    }

    // Data Generation Helpers
    generateTimeSeriesData(basePrice, days) {
        const data = [];
        let currentPrice = basePrice;
        
        for (let i = 0; i < days; i++) {
            const change = (Math.random() - 0.5) * 0.1; // ±5% daily variation
            currentPrice = currentPrice * (1 + change);
            
            data.push({
                date: new Date(Date.now() - (days - i) * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
                value: parseFloat(currentPrice.toFixed(2))
            });
        }
        
        return data;
    }

    generateWeatherData(type) {
        if (type === 'forecast') {
            return Array.from({length: 5}, (_, i) => ({
                date: new Date(Date.now() + i * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
                temp: 20 + Math.random() * 15,
                humidity: 50 + Math.random() * 30,
                condition: ['sunny', 'cloudy', 'rainy'][Math.floor(Math.random() * 3)]
            }));
        }
        
        return Array.from({length: 30}, (_, i) => ({
            date: new Date(Date.now() - (30 - i) * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
            temp: 18 + Math.random() * 12,
            humidity: 40 + Math.random() * 40
        }));
    }

    generateDemographicData() {
        return {
            ageGroups: [
                {group: '0-14', percentage: 21.1},
                {group: '15-64', percentage: 70.2},
                {group: '65+', percentage: 8.7}
            ],
            regions: [
                {name: 'Sudeste', population: 88.4},
                {name: 'Nordeste', population: 57.1},
                {name: 'Sul', population: 30.2},
                {name: 'Norte', population: 18.9},
                {name: 'Centro-Oeste', population: 16.7}
            ]
        };
    }

    getPeriodDays(period) {
        const periods = {'1mo': 30, '3mo': 90, '6mo': 180, '1y': 365};
        return periods[period] || 30;
    }

    // Results Display
    displayResults(data, analysisType) {
        document.getElementById('analysis-loading').style.display = 'none';
        document.getElementById('analysis-empty').style.display = 'none';
        document.getElementById('analysis-results').style.display = 'block';
        
        document.getElementById('results-title').textContent = analysisType;
        
        this.populateExecutiveSummary(data, analysisType);
        this.populateKeyMetrics(data, analysisType);
        this.createMainChart(data, analysisType);
        this.generateInsights(data, analysisType);
        this.generateRecommendations(data, analysisType);
    }

    populateExecutiveSummary(data, type) {
        const container = document.getElementById('executive-summary');
        let summary = '';
        
        switch (type) {
            case 'Análise de Ações':
                summary = `
                    <div class="summary-card">
                        <h4>${data.symbol.toUpperCase()}</h4>
                        <p class="summary-text">A ação apresentou ${data.change >= 0 ? 'valorização' : 'desvalorização'} de 
                        <strong>${Math.abs(data.change)}%</strong> no período analisado.</p>
                        <div class="summary-highlight">
                            <span class="label">Preço Atual:</span>
                            <span class="value">R$ ${data.currentPrice.toFixed(2)}</span>
                        </div>
                    </div>
                `;
                break;
            case 'Análise de Criptomoedas':
                summary = `
                    <div class="summary-card">
                        <h4>${data.symbol.toUpperCase()}</h4>
                        <p class="summary-text">Criptomoeda com alta volatilidade e volume significativo de negociação.</p>
                        <div class="summary-highlight">
                            <span class="label">Market Cap:</span>
                            <span class="value">${data.marketCap}</span>
                        </div>
                    </div>
                `;
                break;
            default:
                summary = `
                    <div class="summary-card">
                        <p class="summary-text">Análise completada com sucesso. Dados processados e insights gerados automaticamente.</p>
                    </div>
                `;
        }
        
        container.innerHTML = summary;
    }

    populateKeyMetrics(data, type) {
        const container = document.getElementById('key-metrics');
        let metrics = '';
        
        switch (type) {
            case 'Análise de Ações':
                const volatility = this.calculateVolatility(data.data);
                metrics = `
                    <div class="metrics-grid">
                        <div class="metric-item">
                            <span class="metric-label">Volatilidade</span>
                            <span class="metric-value">${volatility.toFixed(2)}%</span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">Variação</span>
                            <span class="metric-value ${data.change >= 0 ? 'positive' : 'negative'}">${data.change}%</span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">Pontos Analisados</span>
                            <span class="metric-value">${data.data.length}</span>
                        </div>
                    </div>
                `;
                break;
            case 'Análise Climática':
                metrics = `
                    <div class="metrics-grid">
                        <div class="metric-item">
                            <span class="metric-label">Temperatura</span>
                            <span class="metric-value">${data.current.temp}°C</span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">Umidade</span>
                            <span class="metric-value">${data.current.humidity}%</span>
                        </div>
                        <div class="metric-item">
                            <span class="metric-label">Vento</span>
                            <span class="metric-value">${data.current.windSpeed} km/h</span>
                        </div>
                    </div>
                `;
                break;
            default:
                metrics = `
                    <div class="metrics-grid">
                        <div class="metric-item">
                            <span class="metric-label">Status</span>
                            <span class="metric-value">Concluído</span>
                        </div>
                    </div>
                `;
        }
        
        container.innerHTML = metrics;
    }

    createMainChart(data, type) {
        const canvas = document.getElementById('main-chart');
        const ctx = canvas.getContext('2d');
        
        // Destroy existing chart
        if (this.charts.main) {
            this.charts.main.destroy();
        }
        
        let chartConfig;
        
        if (type === 'Análise de Ações' || type === 'Análise de Criptomoedas') {
            chartConfig = {
                type: 'line',
                data: {
                    labels: data.data.map(d => d.date),
                    datasets: [{
                        label: 'Preço',
                        data: data.data.map(d => d.value),
                        borderColor: '#2563eb',
                        backgroundColor: 'rgba(37, 99, 235, 0.1)',
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: false,
                            grid: {
                                color: '#f1f5f9'
                            }
                        },
                        x: {
                            grid: {
                                color: '#f1f5f9'
                            }
                        }
                    }
                }
            };
        } else if (type === 'Análise Climática') {
            chartConfig = {
                type: 'bar',
                data: {
                    labels: data.data.slice(0, 7).map(d => d.date),
                    datasets: [{
                        label: 'Temperatura (°C)',
                        data: data.data.slice(0, 7).map(d => d.temp),
                        backgroundColor: '#06b6d4',
                        borderRadius: 6
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false
                        }
                    }
                }
            };
        }
        
        this.charts.main = new Chart(ctx, chartConfig);
    }

    generateInsights(data, type) {
        const container = document.getElementById('auto-insights');
        let insights = '';
        
        switch (type) {
            case 'Análise de Ações':
                const trend = data.change >= 0 ? 'alta' : 'baixa';
                insights = `
                    <div class="insights-list">
                        <div class="insight-item">
                            <i class="fas fa-trend-up"></i>
                            <span>Tendência de <strong>${trend}</strong> identificada no período</span>
                        </div>
                        <div class="insight-item">
                            <i class="fas fa-chart-bar"></i>
                            <span>Volume de negociação dentro da média histórica</span>
                        </div>
                        <div class="insight-item">
                            <i class="fas fa-shield-alt"></i>
                            <span>Volatilidade ${this.calculateVolatility(data.data) > 5 ? 'alta' : 'moderada'} detectada</span>
                        </div>
                    </div>
                `;
                break;
            default:
                insights = `
                    <div class="insights-list">
                        <div class="insight-item">
                            <i class="fas fa-check-circle"></i>
                            <span>Dados processados com sucesso</span>
                        </div>
                        <div class="insight-item">
                            <i class="fas fa-chart-line"></i>
                            <span>Padrões identificados automaticamente</span>
                        </div>
                    </div>
                `;
        }
        
        container.innerHTML = insights;
    }

    generateRecommendations(data, type) {
        const container = document.getElementById('recommendations');
        let recommendations = '';
        
        switch (type) {
            case 'Análise de Ações':
                recommendations = `
                    <div class="recommendations-list">
                        <div class="recommendation-item">
                            <h5>Monitoramento</h5>
                            <p>Acompanhe indicadores técnicos adicionais para confirmação de tendência</p>
                        </div>
                        <div class="recommendation-item">
                            <h5>Diversificação</h5>
                            <p>Considere diversificar portfolio para reduzir exposição ao risco</p>
                        </div>
                    </div>
                `;
                break;
            default:
                recommendations = `
                    <div class="recommendations-list">
                        <div class="recommendation-item">
                            <h5>Análise Contínua</h5>
                            <p>Configure alertas automáticos para monitoramento em tempo real</p>
                        </div>
                    </div>
                `;
        }
        
        container.innerHTML = recommendations;
    }

    calculateVolatility(data) {
        if (data.length < 2) return 0;
        
        const returns = [];
        for (let i = 1; i < data.length; i++) {
            returns.push((data[i].value - data[i-1].value) / data[i-1].value);
        }
        
        const mean = returns.reduce((sum, r) => sum + r, 0) / returns.length;
        const variance = returns.reduce((sum, r) => sum + Math.pow(r - mean, 2), 0) / returns.length;
        
        return Math.sqrt(variance) * 100;
    }

    // Upload Modal
    setupUploadModal() {
        const modal = document.getElementById('upload-modal');
        const uploadZone = document.getElementById('upload-zone');
        const fileInput = document.getElementById('file-input');
        const closeBtn = document.querySelector('.modal-close');

        closeBtn.addEventListener('click', () => {
            modal.classList.remove('active');
        });

        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
            }
        });

        uploadZone.addEventListener('click', () => {
            fileInput.click();
        });

        // Drag and drop
        uploadZone.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadZone.classList.add('dragover');
        });

        uploadZone.addEventListener('dragleave', () => {
            uploadZone.classList.remove('dragover');
        });

        uploadZone.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadZone.classList.remove('dragover');
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                this.handleFileUpload(files[0]);
            }
        });

        fileInput.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                this.handleFileUpload(e.target.files[0]);
            }
        });
    }

    openUploadModal() {
        document.getElementById('upload-modal').classList.add('active');
    }

    handleFileUpload(file) {
        if (file.size > 10 * 1024 * 1024) { // 10MB limit
            this.showNotification('Arquivo muito grande. Máximo: 10MB', 'error');
            return;
        }

        const allowedTypes = ['text/csv', 'application/json', 'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'];
        if (!allowedTypes.includes(file.type) && !file.name.endsWith('.csv')) {
            this.showNotification('Tipo de arquivo não suportado', 'error');
            return;
        }

        this.showNotification('Arquivo carregado com sucesso!', 'success');
        document.getElementById('upload-modal').classList.remove('active');
        
        // Switch to analysis with custom data
        this.switchToAnalysis('custom');
    }

    // Templates
    setupTemplates() {
        const templateCards = document.querySelectorAll('.template-card');
        
        templateCards.forEach(card => {
            card.addEventListener('click', () => {
                const template = card.getAttribute('data-template');
                this.useTemplate(template);
            });
        });
    }

    useTemplate(template) {
        this.showNotification(`Template "${template}" selecionado!`, 'success');
        
        // Switch to analysis with template configuration
        this.switchToAnalysis('stocks'); // Default to stocks for demo
    }

    // Demo
    runDemo() {
        this.showNotification('Iniciando demonstração...', 'info');
        
        setTimeout(() => {
            this.switchToAnalysis('stocks');
            document.getElementById('stock-symbol').value = 'PETR4.SA';
            document.getElementById('stock-period').value = '3mo';
            this.validateAnalysisForm();
            
            setTimeout(() => {
                this.startAnalysis();
            }, 1000);
        }, 500);
    }

    // Notifications
    showNotification(message, type = 'info', duration = 5000) {
        const container = document.getElementById('notifications');
        
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <div class="notification-message">${message}</div>
                <button class="notification-close">&times;</button>
            </div>
        `;
        
        container.appendChild(notification);
        
        const closeBtn = notification.querySelector('.notification-close');
        closeBtn.addEventListener('click', () => {
            notification.remove();
        });
        
        setTimeout(() => {
            if (notification.parentNode) {
                notification.style.animation = 'slideOut 0.3s ease-in';
                setTimeout(() => notification.remove(), 300);
            }
        }, duration);
    }
}

// Initialize the application
const app = new DataInsightsPro();

// Add notification close animation
const style = document.createElement('style');
style.textContent = `
    .notification-content {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
    }
    
    .notification-close {
        background: none;
        border: none;
        color: inherit;
        cursor: pointer;
        font-size: 1.2rem;
        padding: 0.25rem;
        border-radius: 0.25rem;
        transition: background-color 0.2s;
    }
    
    .notification-close:hover {
        background: rgba(0, 0, 0, 0.1);
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    .summary-card,
    .metrics-grid,
    .insights-list,
    .recommendations-list {
        margin-top: 1rem;
    }
    
    .summary-highlight {
        display: flex;
        justify-content: space-between;
        padding: 0.75rem;
        background: #f8fafc;
        border-radius: 0.5rem;
        margin-top: 1rem;
    }
    
    .label {
        color: #64748b;
        font-weight: 500;
    }
    
    .value {
        color: #1e293b;
        font-weight: 600;
    }
    
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 1rem;
    }
    
    .metric-item {
        text-align: center;
        padding: 1rem;
        background: #f8fafc;
        border-radius: 0.5rem;
        border: 1px solid #e2e8f0;
    }
    
    .metric-label {
        display: block;
        color: #64748b;
        font-size: 0.875rem;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        display: block;
        color: #1e293b;
        font-size: 1.25rem;
        font-weight: 700;
    }
    
    .metric-value.positive {
        color: #10b981;
    }
    
    .metric-value.negative {
        color: #ef4444;
    }
    
    .insights-list,
    .recommendations-list {
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
    }
    
    .insight-item {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.75rem;
        background: #f0f9ff;
        border-radius: 0.5rem;
        border-left: 3px solid #2563eb;
    }
    
    .insight-item i {
        color: #2563eb;
        font-size: 1rem;
    }
    
    .recommendation-item {
        padding: 1rem;
        background: #f0fdf4;
        border-radius: 0.5rem;
        border-left: 3px solid #10b981;
    }
    
    .recommendation-item h5 {
        margin: 0 0 0.5rem 0;
        color: #059669;
        font-size: 1rem;
        font-weight: 600;
    }
    
    .recommendation-item p {
        margin: 0;
        color: #374151;
        font-size: 0.875rem;
        line-height: 1.5;
    }
`;

document.head.appendChild(style);
