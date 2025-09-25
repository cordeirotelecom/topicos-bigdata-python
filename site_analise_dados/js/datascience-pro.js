// ========================================
// DataScience Pro - JavaScript Avançado
// ========================================

class DataSciencePro {
    constructor() {
        this.currentTab = 'guia';
        this.uploadedData = null;
        this.analysisResults = null;
        this.charts = {};
        
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.setupNavigation();
        this.setupUpload();
        this.setupSampleData();
        this.setupInteractiveElements();
        this.loadDefaultContent();
    }

    setupEventListeners() {
        // Tab navigation
        document.addEventListener('click', (e) => {
            if (e.target.matches('[data-tab]') || e.target.closest('[data-tab]')) {
                const target = e.target.matches('[data-tab]') ? e.target : e.target.closest('[data-tab]');
                const tabId = target.dataset.tab;
                if (tabId) {
                    this.switchTab(tabId);
                }
            }
        });

        // Header scroll effect
        window.addEventListener('scroll', this.handleScroll.bind(this));

        // Resize handler
        window.addEventListener('resize', this.handleResize.bind(this));

        // Sample data buttons
        document.addEventListener('click', (e) => {
            if (e.target.matches('.sample-btn') || e.target.closest('.sample-btn')) {
                const btn = e.target.matches('.sample-btn') ? e.target : e.target.closest('.sample-btn');
                const sampleType = btn.dataset.sample;
                this.loadSampleData(sampleType);
            }
        });

        // Example filter buttons
        document.addEventListener('click', (e) => {
            if (e.target.matches('.filter-btn')) {
                this.filterExamples(e.target.dataset.category);
                // Update active state
                document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
                e.target.classList.add('active');
            }
        });
    }

    setupNavigation() {
        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', (e) => {
                e.preventDefault();
                const target = document.querySelector(anchor.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    setupUpload() {
        const uploadArea = document.getElementById('upload-area');
        const fileInput = document.getElementById('file-input');

        if (!uploadArea || !fileInput) return;

        // Click to upload
        uploadArea.addEventListener('click', () => fileInput.click());

        // Drag and drop
        uploadArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadArea.classList.add('drag-over');
        });

        uploadArea.addEventListener('dragleave', () => {
            uploadArea.classList.remove('drag-over');
        });

        uploadArea.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadArea.classList.remove('drag-over');
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                this.handleFile(files[0]);
            }
        });

        fileInput.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                this.handleFile(e.target.files[0]);
            }
        });
    }

    setupSampleData() {
        this.sampleDatasets = {
            covid: {
                name: 'COVID-19 & Qualidade do Ar',
                data: this.generateCovidData(),
                description: 'Dados simulados de poluição e casos de COVID-19'
            },
            climate: {
                name: 'Dados Climáticos',
                data: this.generateClimateData(),
                description: 'Dados meteorológicos anuais simulados'
            },
            sales: {
                name: 'Vendas & Marketing',
                data: this.generateSalesData(),
                description: 'Dados de vendas por produto e região'
            }
        };
    }

    setupInteractiveElements() {
        // Setup clean data demo
        this.setupCleanDataDemo();
        
        // Setup chart examples
        this.setupChartExamples();
        
        // Setup tooltips
        this.setupTooltips();
    }

    switchTab(tabId) {
        // Hide all tabs
        document.querySelectorAll('.tab-panel').forEach(panel => {
            panel.classList.remove('active');
        });

        // Remove active from all buttons
        document.querySelectorAll('.tab-button, .nav-link').forEach(btn => {
            btn.classList.remove('active');
        });

        // Show target tab
        const targetPanel = document.getElementById(tabId);
        if (targetPanel) {
            targetPanel.classList.add('active');
        }

        // Activate buttons
        document.querySelectorAll(`[data-tab="${tabId}"]`).forEach(btn => {
            btn.classList.add('active');
        });

        this.currentTab = tabId;
        
        // Load tab-specific content
        this.loadTabContent(tabId);
    }

    loadTabContent(tabId) {
        switch (tabId) {
            case 'guia':
                this.loadGuideContent();
                break;
            case 'analise':
                this.loadAnalysisContent();
                break;
            case 'exemplos':
                this.loadExamplesContent();
                break;
            case 'referencias':
                this.loadReferencesContent();
                break;
        }
    }

    loadGuideContent() {
        // Setup interactive chart in guide
        this.createSampleChart();
    }

    loadAnalysisContent() {
        // Initialize analysis dashboard if needed
        if (!this.uploadedData) {
            this.showEmptyAnalysisState();
        }
    }

    loadExamplesContent() {
        // Initialize examples with animations
        this.animateExamples();
    }

    loadReferencesContent() {
        // Load reference materials
        this.loadReferences();
    }

    handleFile(file) {
        const uploadStatus = document.getElementById('upload-status');
        
        // Show loading state
        this.showUploadLoading(uploadStatus);

        // Validate file
        if (!this.validateFile(file)) {
            this.showUploadError(uploadStatus, 'Formato de arquivo não suportado');
            return;
        }

        // Process file
        this.processFile(file)
            .then(data => {
                this.uploadedData = data;
                this.showUploadSuccess(uploadStatus, file.name);
                this.performAnalysis(data);
                this.switchTab('analise');
            })
            .catch(error => {
                this.showUploadError(uploadStatus, error.message);
            });
    }

    validateFile(file) {
        const allowedTypes = [
            'text/csv',
            'application/vnd.ms-excel',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'application/json'
        ];
        
        return allowedTypes.includes(file.type) || file.name.endsWith('.csv');
    }

    processFile(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            
            reader.onload = (e) => {
                try {
                    let data;
                    
                    if (file.type === 'application/json' || file.name.endsWith('.json')) {
                        data = JSON.parse(e.target.result);
                    } else if (file.type.includes('csv') || file.name.endsWith('.csv')) {
                        const parsed = Papa.parse(e.target.result, {
                            header: true,
                            dynamicTyping: true,
                            skipEmptyLines: true
                        });
                        data = parsed.data;
                    } else {
                        reject(new Error('Formato não suportado ainda'));
                        return;
                    }
                    
                    resolve(data);
                } catch (error) {
                    reject(new Error('Erro ao processar arquivo: ' + error.message));
                }
            };
            
            reader.onerror = () => reject(new Error('Erro ao ler arquivo'));
            reader.readAsText(file);
        });
    }

    loadSampleData(sampleType) {
        const dataset = this.sampleDatasets[sampleType];
        if (dataset) {
            this.uploadedData = dataset.data;
            this.showSampleDataLoaded(dataset.name);
            this.performAnalysis(dataset.data);
            this.switchTab('analise');
        }
    }

    performAnalysis(data) {
        // Basic analysis
        const analysis = {
            rows: data.length,
            columns: Object.keys(data[0] || {}).length,
            columnTypes: this.analyzeColumnTypes(data),
            statistics: this.calculateStatistics(data),
            correlations: this.calculateCorrelations(data),
            outliers: this.detectOutliers(data),
            missing: this.analyzeMissingData(data)
        };

        this.analysisResults = analysis;
        this.displayAnalysisResults(analysis);
    }

    analyzeColumnTypes(data) {
        const sample = data[0] || {};
        const types = {};
        
        Object.keys(sample).forEach(column => {
            const values = data.slice(0, 100).map(row => row[column]).filter(v => v != null);
            if (values.length === 0) {
                types[column] = 'empty';
            } else if (values.every(v => typeof v === 'number')) {
                types[column] = 'numeric';
            } else if (values.every(v => !isNaN(Date.parse(v)))) {
                types[column] = 'date';
            } else {
                types[column] = 'categorical';
            }
        });
        
        return types;
    }

    calculateStatistics(data) {
        const stats = {};
        const columnTypes = this.analyzeColumnTypes(data);
        
        Object.keys(columnTypes).forEach(column => {
            if (columnTypes[column] === 'numeric') {
                const values = data.map(row => row[column]).filter(v => v != null && !isNaN(v));
                if (values.length > 0) {
                    stats[column] = {
                        count: values.length,
                        mean: this.mean(values),
                        median: this.median(values),
                        std: this.standardDeviation(values),
                        min: Math.min(...values),
                        max: Math.max(...values)
                    };
                }
            }
        });
        
        return stats;
    }

    calculateCorrelations(data) {
        const columnTypes = this.analyzeColumnTypes(data);
        const numericColumns = Object.keys(columnTypes).filter(col => columnTypes[col] === 'numeric');
        const correlations = {};
        
        numericColumns.forEach(col1 => {
            correlations[col1] = {};
            numericColumns.forEach(col2 => {
                const values1 = data.map(row => row[col1]).filter(v => v != null && !isNaN(v));
                const values2 = data.map(row => row[col2]).filter(v => v != null && !isNaN(v));
                correlations[col1][col2] = this.correlation(values1, values2);
            });
        });
        
        return correlations;
    }

    detectOutliers(data) {
        const outliers = {};
        const columnTypes = this.analyzeColumnTypes(data);
        
        Object.keys(columnTypes).forEach(column => {
            if (columnTypes[column] === 'numeric') {
                const values = data.map(row => row[column]).filter(v => v != null && !isNaN(v));
                if (values.length > 0) {
                    const q1 = this.percentile(values, 25);
                    const q3 = this.percentile(values, 75);
                    const iqr = q3 - q1;
                    const lowerBound = q1 - 1.5 * iqr;
                    const upperBound = q3 + 1.5 * iqr;
                    
                    outliers[column] = values.filter(v => v < lowerBound || v > upperBound);
                }
            }
        });
        
        return outliers;
    }

    analyzeMissingData(data) {
        const missing = {};
        const total = data.length;
        
        if (total === 0) return missing;
        
        const columns = Object.keys(data[0] || {});
        columns.forEach(column => {
            const nullCount = data.filter(row => row[column] == null || row[column] === '').length;
            missing[column] = {
                count: nullCount,
                percentage: (nullCount / total) * 100
            };
        });
        
        return missing;
    }

    displayAnalysisResults(analysis) {
        this.updateDataOverview(analysis);
        this.updateStatistics(analysis);
        this.updateQualityMetrics(analysis);
        this.createCorrelationHeatmap(analysis.correlations);
        this.setupDistributionChart(analysis);
        this.displayOutliers(analysis.outliers);
    }

    updateDataOverview(analysis) {
        const container = document.getElementById('data-overview');
        if (!container) return;

        container.innerHTML = `
            <div class="overview-card">
                <div class="overview-icon">📊</div>
                <div class="overview-label">Linhas</div>
                <div class="overview-value">${analysis.rows.toLocaleString()}</div>
            </div>
            <div class="overview-card">
                <div class="overview-icon">📈</div>
                <div class="overview-label">Colunas</div>
                <div class="overview-value">${analysis.columns}</div>
            </div>
            <div class="overview-card">
                <div class="overview-icon">🔢</div>
                <div class="overview-label">Numéricas</div>
                <div class="overview-value">${Object.values(analysis.columnTypes).filter(t => t === 'numeric').length}</div>
            </div>
            <div class="overview-card">
                <div class="overview-icon">📝</div>
                <div class="overview-label">Categóricas</div>
                <div class="overview-value">${Object.values(analysis.columnTypes).filter(t => t === 'categorical').length}</div>
            </div>
        `;
    }

    // Mathematical helper functions
    mean(values) {
        return values.reduce((a, b) => a + b, 0) / values.length;
    }

    median(values) {
        const sorted = [...values].sort((a, b) => a - b);
        const middle = Math.floor(sorted.length / 2);
        return sorted.length % 2 === 0 
            ? (sorted[middle - 1] + sorted[middle]) / 2 
            : sorted[middle];
    }

    standardDeviation(values) {
        const avg = this.mean(values);
        const squareDiffs = values.map(value => Math.pow(value - avg, 2));
        return Math.sqrt(this.mean(squareDiffs));
    }

    correlation(x, y) {
        if (x.length !== y.length || x.length === 0) return 0;
        
        const meanX = this.mean(x);
        const meanY = this.mean(y);
        
        let numerator = 0;
        let sumSquareX = 0;
        let sumSquareY = 0;
        
        for (let i = 0; i < x.length; i++) {
            const deltaX = x[i] - meanX;
            const deltaY = y[i] - meanY;
            numerator += deltaX * deltaY;
            sumSquareX += deltaX * deltaX;
            sumSquareY += deltaY * deltaY;
        }
        
        const denominator = Math.sqrt(sumSquareX * sumSquareY);
        return denominator === 0 ? 0 : numerator / denominator;
    }

    percentile(values, p) {
        const sorted = [...values].sort((a, b) => a - b);
        const index = (p / 100) * (sorted.length - 1);
        
        if (Math.floor(index) === index) {
            return sorted[index];
        } else {
            const lower = sorted[Math.floor(index)];
            const upper = sorted[Math.ceil(index)];
            return lower + (upper - lower) * (index - Math.floor(index));
        }
    }

    // Data generation for samples
    generateCovidData() {
        const data = [];
        for (let i = 0; i < 100; i++) {
            data.push({
                data: `2023-${String(Math.floor(i/30) + 1).padStart(2, '0')}-${String((i % 30) + 1).padStart(2, '0')}`,
                casos_covid: Math.floor(Math.random() * 1000) + 50,
                pm25: Math.random() * 50 + 10,
                temperatura: Math.random() * 15 + 20,
                umidade: Math.random() * 40 + 40,
                populacao: 1000000 + Math.random() * 500000,
                testes_realizados: Math.floor(Math.random() * 5000) + 1000,
                taxa_positividade: Math.random() * 20 + 5
            });
        }
        return data;
    }

    generateClimateData() {
        const data = [];
        for (let i = 0; i < 365; i++) {
            const month = Math.floor(i / 30) + 1;
            const baseTemp = 25 + Math.sin((month - 6) * Math.PI / 6) * 10;
            
            data.push({
                dia: i + 1,
                mes: month,
                temperatura_max: baseTemp + Math.random() * 10 - 5,
                temperatura_min: baseTemp - 10 + Math.random() * 5,
                chuva: Math.random() < 0.3 ? Math.random() * 50 : 0,
                umidade: 60 + Math.random() * 30,
                vento: Math.random() * 20 + 5,
                pressao: 1013 + Math.random() * 40 - 20,
                radiacao_solar: Math.random() * 1000 + 200
            });
        }
        return data;
    }

    generateSalesData() {
        const produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Headset'];
        const regioes = ['Norte', 'Sul', 'Leste', 'Oeste', 'Centro'];
        const data = [];
        
        for (let i = 0; i < 200; i++) {
            data.push({
                produto: produtos[Math.floor(Math.random() * produtos.length)],
                regiao: regioes[Math.floor(Math.random() * regioes.length)],
                vendas: Math.floor(Math.random() * 1000) + 100,
                receita: (Math.random() * 50000) + 5000,
                mes: Math.floor(Math.random() * 12) + 1,
                ano: 2023,
                campanha: Math.random() > 0.5 ? 'Digital' : 'Tradicional',
                desconto: Math.random() * 30
            });
        }
        return data;
    }

    // UI Helper methods
    showUploadLoading(container) {
        container.style.display = 'block';
        container.innerHTML = `
            <div class="upload-loading">
                <i class="fas fa-spinner fa-spin"></i>
                Processando arquivo...
            </div>
        `;
    }

    showUploadSuccess(container, filename) {
        container.innerHTML = `
            <div class="upload-success">
                <i class="fas fa-check-circle"></i>
                Arquivo "${filename}" carregado com sucesso!
            </div>
        `;
    }

    showUploadError(container, message) {
        container.innerHTML = `
            <div class="upload-error">
                <i class="fas fa-exclamation-circle"></i>
                ${message}
            </div>
        `;
    }

    handleScroll() {
        const header = document.querySelector('.header');
        if (window.scrollY > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }

    handleResize() {
        // Redraw charts on resize
        Object.values(this.charts).forEach(chart => {
            if (chart.resize) {
                chart.resize();
            }
        });
    }

    loadDefaultContent() {
        // Load initial content
        this.createSampleChart();
    }

    createSampleChart() {
        const canvas = document.getElementById('sampleChart');
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        
        if (this.charts.sample) {
            this.charts.sample.destroy();
        }

        this.charts.sample = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
                datasets: [{
                    label: 'Vendas',
                    data: [100, 120, 90, 150, 200, 180],
                    borderColor: '#4f46e5',
                    backgroundColor: 'rgba(79, 70, 229, 0.1)',
                    tension: 0.4,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: 'rgba(0,0,0,0.1)'
                        }
                    },
                    x: {
                        grid: {
                            display: false
                        }
                    }
                }
            }
        });
    }

    setupCleanDataDemo() {
        window.cleanData = (element) => {
            const originalText = element.textContent;
            
            // Simulate cleaning
            setTimeout(() => {
                switch (originalText) {
                    case 'João,25,sp':
                        element.textContent = 'João, 25, São Paulo';
                        break;
                    case 'maria,0,São Paulo':
                        element.textContent = 'Maria, 28, São Paulo';
                        break;
                    case 'Pedro, vinte e cinco,SP':
                        element.textContent = 'Pedro, 25, São Paulo';
                        break;
                }
                element.classList.add('cleaned');
            }, 500);
        };
    }

    setupChartExamples() {
        // Additional chart examples if needed
    }

    setupTooltips() {
        // Setup tooltip system
        document.querySelectorAll('[data-tooltip]').forEach(element => {
            element.addEventListener('mouseenter', this.showTooltip.bind(this));
            element.addEventListener('mouseleave', this.hideTooltip.bind(this));
        });
    }

    showTooltip(e) {
        const text = e.target.dataset.tooltip;
        if (!text) return;

        const tooltip = document.createElement('div');
        tooltip.className = 'tooltip';
        tooltip.textContent = text;
        document.body.appendChild(tooltip);

        const rect = e.target.getBoundingClientRect();
        tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
        tooltip.style.top = rect.top - tooltip.offsetHeight - 10 + 'px';
    }

    hideTooltip() {
        const tooltip = document.querySelector('.tooltip');
        if (tooltip) {
            tooltip.remove();
        }
    }

    filterExamples(category) {
        const examples = document.querySelectorAll('.example-card');
        examples.forEach(example => {
            if (category === 'all' || example.dataset.category === category) {
                example.style.display = 'block';
                example.style.animation = 'fadeInUp 0.5s ease';
            } else {
                example.style.display = 'none';
            }
        });
    }

    animateExamples() {
        const examples = document.querySelectorAll('.example-card');
        examples.forEach((example, index) => {
            example.style.animation = `fadeInUp 0.5s ease ${index * 0.1}s both`;
        });
    }
}

// Global functions for backwards compatibility
window.switchTab = (tabId) => {
    if (window.dataSciencePro) {
        window.dataSciencePro.switchTab(tabId);
    }
};

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.dataSciencePro = new DataSciencePro();
});

// Export for module use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = DataSciencePro;
}
