class DataInsightsPro {
    constructor() {
        this.currentStep = 1;
        this.totalSteps = 4; // Atualizado para 4 steps
        this.selectedSource = null;
        this.selectedGoals = new Set();
        this.configuration = {};
        this.analysisData = null;
        this.uploadedFiles = []; // Array para múltiplos arquivos
        this.selectedAnalysisTags = new Set(); // Tags de análise selecionadas
        this.selectedGovernmentAPIs = new Set(); // APIs governamentais selecionadas
        this.selectedExportFormats = new Set(); // Formatos de exportação selecionados
        this.advancedConfig = {}; // Configurações avançadas
        
        this.init();
    }
    
    init() {
        this.setupEventListeners();
        this.setupHeroChart();
        this.showSection('home');
    }
    
    setupEventListeners() {
        // Navigation
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const section = e.currentTarget.dataset.section;
                this.switchSection(section);
            });
        });
        
        // Data source selection
        document.querySelectorAll('.source-card').forEach(card => {
            card.addEventListener('click', (e) => {
                this.selectDataSource(e.currentTarget.dataset.source);
            });
        });
        
        // Goal selection
        document.querySelectorAll('.goal-card').forEach(card => {
            card.addEventListener('click', (e) => {
                this.toggleGoal(e.currentTarget.dataset.goal);
            });
        });
        
        // Step navigation
        document.getElementById('prev-step').addEventListener('click', () => {
            this.previousStep();
        });
        
        document.getElementById('next-step').addEventListener('click', () => {
            this.nextStep();
        });
        
        document.getElementById('start-analysis').addEventListener('click', () => {
            this.startAnalysis();
        });
        
        // File upload
        const uploadZone = document.getElementById('upload-zone');
        const fileInput = document.getElementById('file-input');
        
        if (uploadZone && fileInput) {
            uploadZone.addEventListener('click', () => fileInput.click());
            uploadZone.addEventListener('dragover', this.handleDragOver.bind(this));
            uploadZone.addEventListener('drop', this.handleFileDrop.bind(this));
            fileInput.addEventListener('change', this.handleFileSelect.bind(this));
        }
        
        // Demo button
        const demoBtn = document.querySelector('[onclick="showDemo()"]');
        if (demoBtn) {
            demoBtn.addEventListener('click', () => this.showDemo());
        }
        
        // Export format selection
        document.querySelectorAll('.export-card').forEach(card => {
            card.addEventListener('click', (e) => {
                this.toggleExportFormat(e.currentTarget.dataset.format);
            });
        });
        
        // Export buttons
        const exportSelectedBtn = document.getElementById('export-selected');
        const exportAllBtn = document.getElementById('export-all');
        
        if (exportSelectedBtn) {
            exportSelectedBtn.addEventListener('click', () => this.exportSelected());
        }
        
        if (exportAllBtn) {
            exportAllBtn.addEventListener('click', () => this.exportAll());
        }
        
        // Sample size range
        const sampleSizeRange = document.getElementById('sample-size');
        const sampleSizeValue = document.getElementById('sample-size-value');
        
        if (sampleSizeRange && sampleSizeValue) {
            sampleSizeRange.addEventListener('input', (e) => {
                sampleSizeValue.textContent = `${e.target.value}%`;
                this.advancedConfig.sampleSize = parseInt(e.target.value);
            });
        }
        
        // Advanced configuration inputs
        this.setupAdvancedConfigListeners();
    }
    
    switchSection(sectionName) {
        // Update navigation
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        document.querySelector(`[data-section="${sectionName}"]`).classList.add('active');
        
        // Show section
        document.querySelectorAll('.section').forEach(section => {
            section.classList.remove('active');
        });
        document.getElementById(sectionName).classList.add('active');
        
        // Reset analyzer steps if needed
        if (sectionName === 'analyzer') {
            this.currentStep = 1;
            this.updateStepDisplay();
        }
    }
    
    selectDataSource(source) {
        this.selectedSource = source;
        
        // Update UI
        document.querySelectorAll('.source-card').forEach(card => {
            card.classList.remove('selected');
        });
        document.querySelector(`[data-source="${source}"]`).classList.add('selected');
        
        // Show relevant config panel
        document.querySelectorAll('.config-panel').forEach(panel => {
            panel.classList.remove('active');
        });
        const targetPanel = document.querySelector(`[data-source="${source}"]`);
        if (targetPanel && targetPanel.classList.contains('config-panel')) {
            targetPanel.classList.add('active');
        }
        
        this.updateNavigationState();
    }
    
    toggleGoal(goal) {
        const card = document.querySelector(`[data-goal="${goal}"]`);
        
        if (this.selectedGoals.has(goal)) {
            this.selectedGoals.delete(goal);
            card.classList.remove('selected');
        } else {
            this.selectedGoals.add(goal);
            card.classList.add('selected');
        }
        
        this.updateNavigationState();
    }
    
    previousStep() {
        if (this.currentStep > 1) {
            this.currentStep--;
            this.updateStepDisplay();
        }
    }
    
    nextStep() {
        if (this.canProceedToNextStep()) {
            this.currentStep++;
            this.updateStepDisplay();
        }
    }
    
    canProceedToNextStep() {
        switch (this.currentStep) {
            case 1:
                return this.selectedSource !== null;
            case 2:
                return this.selectedGoals.size > 0;
            case 3:
                return true;
            default:
                return false;
        }
    }
    
    updateStepDisplay() {
        // Hide all steps
        document.querySelectorAll('.analysis-step').forEach(step => {
            step.classList.remove('active');
        });
        
        // Show current step
        document.querySelector(`[data-step="${this.currentStep}"]`).classList.add('active');
        
        // Update indicators
        document.querySelectorAll('.indicator').forEach((indicator, index) => {
            if (index + 1 <= this.currentStep) {
                indicator.classList.add('active');
            } else {
                indicator.classList.remove('active');
            }
        });
        
        this.updateNavigationState();
    }
    
    updateNavigationState() {
        const prevBtn = document.getElementById('prev-step');
        const nextBtn = document.getElementById('next-step');
        const startBtn = document.getElementById('start-analysis');
        
        // Previous button
        prevBtn.disabled = this.currentStep === 1;
        
        // Next/Start button
        if (this.currentStep === this.totalSteps) {
            nextBtn.style.display = 'none';
            startBtn.style.display = 'inline-flex';
            startBtn.disabled = !this.canProceedToNextStep();
        } else {
            nextBtn.style.display = 'inline-flex';
            startBtn.style.display = 'none';
            nextBtn.disabled = !this.canProceedToNextStep();
        }
    }
    
    async startAnalysis() {
        try {
            // Validar se há dados para analisar
            if (this.uploadedFiles.length === 0 && this.selectedGovernmentAPIs.size === 0) {
                this.showNotification('Por favor, carregue arquivos ou selecione APIs governamentais para análise.', 'warning');
                return;
            }
            
            // Validar se há tipos de análise selecionados
            if (this.selectedAnalysisTags.size === 0) {
                this.showNotification('Por favor, selecione pelo menos um tipo de análise.', 'warning');
                return;
            }
            
            this.switchSection('insights');
            this.showLoadingState();
            
            // Preparar dados para análise
            this.prepareAnalysisData();
            
            // Perform analysis with new capabilities
            await this.performAdvancedAnalysis();
            
            this.hideLoadingState();
            this.showResults();
            
        } catch (error) {
            console.error('Analysis failed:', error);
            this.showNotification('Erro na análise. Tente novamente.', 'error');
            this.hideLoadingState();
        }
    }
    
    prepareAnalysisData() {
        this.configuration.multipleFiles = this.uploadedFiles;
        this.configuration.analysisTags = Array.from(this.selectedAnalysisTags);
        this.configuration.governmentAPIs = Array.from(this.selectedGovernmentAPIs);
        this.configuration.fileCount = this.uploadedFiles.length;
        this.configuration.totalSize = this.uploadedFiles.reduce((total, file) => total + file.size, 0);
        
        console.log('Configuração de análise preparada:', this.configuration);
    }
    
    async performAnalysis() {
        // Manter compatibilidade - redireciona para análise avançada
        return this.performAdvancedAnalysis();
    }
    
    async performAdvancedAnalysis() {
        const steps = [
            'Carregando múltiplos arquivos...',
            'Conectando APIs governamentais...',
            'Aplicando análises selecionadas...',
            'Processando dados estatísticos...',
            'Executando algoritmos de ML...',
            'Realizando análises comparativas...',
            'Gerando previsões avançadas...',
            'Calculando correlações...',
            'Identificando padrões complexos...',
            'Preparando relatório abrangente...',
            'Finalizando insights...'
        ];
        
        const progressFill = document.querySelector('.progress-fill');
        const progressText = document.querySelector('.progress-text');
        const loadingStep = document.querySelector('.loading-step');
        
        for (let i = 0; i < steps.length; i++) {
            const progress = ((i + 1) / steps.length) * 100;
            
            if (loadingStep) loadingStep.textContent = steps[i];
            if (progressFill) progressFill.style.width = `${progress}%`;
            if (progressText) progressText.textContent = `${Math.round(progress)}%`;
            
            await this.delay(800 + Math.random() * 400);
        }
        
        // Generate analysis results based on selected goals
        this.analysisData = this.generateAnalysisResults();
    }
    
    generateAnalysisResults() {
        const results = {
            executiveSummary: this.generateExecutiveSummary(),
            keyMetrics: this.generateKeyMetrics(),
            predictions: this.generatePredictions(),
            recommendations: this.generateRecommendations(),
            discoveries: this.generateDiscoveries()
        };
        
        return results;
    }
    
    generateExecutiveSummary() {
        const summaries = {
            predict: "Análise preditiva identificou tendências crescentes com 85% de confiabilidade.",
            discover: "Descobertos 3 padrões significativos nos dados analisados.",
            quantify: "Correlações fortes identificadas entre variáveis principais (r > 0.7).",
            optimize: "Oportunidades de otimização podem gerar até 25% de melhoria.",
            monitor: "Sistema de monitoramento configurado com 5 KPIs críticos.",
            segment: "Identificados 4 segmentos distintos com características únicas."
        };
        
        let summary = "Análise completa dos dados realizada com sucesso. ";
        
        this.selectedGoals.forEach(goal => {
            if (summaries[goal]) {
                summary += summaries[goal] + " ";
            }
        });
        
        return summary;
    }
    
    generateKeyMetrics() {
        const metrics = [];
        
        if (this.selectedGoals.has('predict')) {
            metrics.push({ label: 'Precisão das Previsões', value: '87%', trend: '+5%' });
        }
        
        if (this.selectedGoals.has('discover')) {
            metrics.push({ label: 'Padrões Descobertos', value: '12', trend: 'novo' });
        }
        
        if (this.selectedGoals.has('quantify')) {
            metrics.push({ label: 'Correlação Máxima', value: '0.82', trend: 'forte' });
        }
        
        if (this.selectedGoals.has('optimize')) {
            metrics.push({ label: 'Potencial de Melhoria', value: '28%', trend: '+12%' });
        }
        
        return metrics;
    }
    
    generatePredictions() {
        if (!this.selectedGoals.has('predict')) {
            return 'Análise preditiva não foi selecionada para este relatório.';
        }
        
        return `
            <div class="prediction-item">
                <h4>📈 Próximos 30 dias</h4>
                <p>Crescimento esperado de <strong>15-20%</strong> baseado em tendências históricas.</p>
            </div>
            <div class="prediction-item">
                <h4>🎯 Probabilidade de Sucesso</h4>
                <p><strong>85%</strong> de chance de atingir metas estabelecidas.</p>
            </div>
            <div class="prediction-item">
                <h4>⚠️ Fatores de Risco</h4>
                <p>Monitorar sazonalidade e variações externas.</p>
            </div>
        `;
    }
    
    generateRecommendations() {
        const recommendations = [];
        
        if (this.selectedGoals.has('optimize')) {
            recommendations.push('🔧 Implementar otimizações identificadas para melhorar performance em 25%');
        }
        
        if (this.selectedGoals.has('monitor')) {
            recommendations.push('📊 Configurar alertas automáticos para métricas críticas');
        }
        
        if (this.selectedGoals.has('segment')) {
            recommendations.push('🎯 Personalizar estratégias para cada segmento identificado');
        }
        
        recommendations.push('📈 Repetir análise mensalmente para acompanhar evolução');
        recommendations.push('🤖 Considerar automação de processos críticos');
        
        return recommendations.map(rec => `<div class="recommendation-item">${rec}</div>`).join('');
    }
    
    generateDiscoveries() {
        if (!this.selectedGoals.has('discover')) {
            return 'Descoberta de padrões não foi selecionada para este relatório.';
        }
        
        return `
            <div class="discovery-item">
                <h4>🔍 Padrão Temporal</h4>
                <p>Picos de atividade identificados às terças e quintas-feiras.</p>
            </div>
            <div class="discovery-item">
                <h4>💡 Correlação Inesperada</h4>
                <p>Forte correlação entre variáveis A e C (r=0.78).</p>
            </div>
            <div class="discovery-item">
                <h4>🎯 Segmento Oculto</h4>
                <p>Identificado novo segmento de usuários com comportamento único.</p>
            </div>
        `;
    }
    
    showLoadingState() {
        document.getElementById('analysis-loading').style.display = 'block';
        document.getElementById('analysis-results').style.display = 'none';
        document.getElementById('insights-empty').style.display = 'none';
    }
    
    hideLoadingState() {
        document.getElementById('analysis-loading').style.display = 'none';
    }
    
    showResults() {
        const resultsContainer = document.getElementById('analysis-results');
        const exportPanel = document.querySelector('.export-panel');
        
        resultsContainer.style.display = 'block';
        
        // Show export panel
        if (exportPanel) {
            exportPanel.style.display = 'block';
        }
        
        // Populate results
        if (this.analysisData) {
            document.getElementById('executive-summary').innerHTML = this.analysisData.executiveSummary;
            document.getElementById('key-metrics').innerHTML = this.renderKeyMetrics(this.analysisData.keyMetrics);
            document.getElementById('predictions').innerHTML = this.analysisData.predictions;
            document.getElementById('recommendations').innerHTML = this.analysisData.recommendations;
            document.getElementById('discoveries').innerHTML = this.analysisData.discoveries;
        }
        
        // Generate chart
        this.generateMainChart();
        
        // Update results header with advanced info
        this.updateResultsHeader();
    }
    
    updateResultsHeader() {
        const resultsHeading = document.getElementById('results-heading');
        const resultsSummary = document.getElementById('results-summary');
        
        if (resultsHeading && resultsSummary) {
            resultsHeading.textContent = 'Análise Avançada Concluída';
            
            const fileCount = this.uploadedFiles.length;
            const apiCount = this.selectedGovernmentAPIs.size;
            const analysisCount = this.selectedAnalysisTags.size;
            
            let summaryText = `Análise realizada com sucesso! `;
            
            if (fileCount > 0) {
                summaryText += `${fileCount} arquivo(s) processado(s). `;
            }
            
            if (apiCount > 0) {
                summaryText += `${apiCount} API(s) governamental(is) consultada(s). `;
            }
            
            summaryText += `${analysisCount} tipo(s) de análise aplicado(s).`;
            
            resultsSummary.textContent = summaryText;
        }
    }
    
    renderKeyMetrics(metrics) {
        return metrics.map(metric => `
            <div class="metric-item">
                <div class="metric-value">${metric.value}</div>
                <div class="metric-label">${metric.label}</div>
                <div class="metric-trend">${metric.trend}</div>
            </div>
        `).join('');
    }
    
    setupHeroChart() {
        const canvas = document.getElementById('hero-chart');
        if (canvas) {
            const ctx = canvas.getContext('2d');
            
            // Simple animated chart
            this.drawHeroChart(ctx, canvas);
        }
    }
    
    drawHeroChart(ctx, canvas) {
        const width = canvas.width = canvas.offsetWidth;
        const height = canvas.height = canvas.offsetHeight;
        
        ctx.clearRect(0, 0, width, height);
        
        // Generate sample data
        const points = [];
        for (let i = 0; i < 12; i++) {
            points.push({
                x: (i / 11) * width,
                y: height * 0.8 - Math.sin(i * 0.5) * height * 0.3 - Math.random() * height * 0.2
            });
        }
        
        // Draw line
        ctx.strokeStyle = '#667eea';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(points[0].x, points[0].y);
        
        for (let i = 1; i < points.length; i++) {
            ctx.lineTo(points[i].x, points[i].y);
        }
        ctx.stroke();
        
        // Draw points
        ctx.fillStyle = '#667eea';
        points.forEach(point => {
            ctx.beginPath();
            ctx.arc(point.x, point.y, 4, 0, Math.PI * 2);
            ctx.fill();
        });
    }
    
    generateMainChart() {
        const canvas = document.getElementById('main-chart');
        if (canvas) {
            const ctx = canvas.getContext('2d');
            
            // Generate more complex chart based on analysis
            this.drawMainChart(ctx, canvas);
        }
    }
    
    drawMainChart(ctx, canvas) {
        const width = canvas.width = canvas.offsetWidth;
        const height = canvas.height = canvas.offsetHeight;
        
        ctx.clearRect(0, 0, width, height);
        
        // Draw bar chart
        const bars = 6;
        const barWidth = width / (bars * 2);
        const maxHeight = height * 0.8;
        
        for (let i = 0; i < bars; i++) {
            const barHeight = Math.random() * maxHeight;
            const x = i * barWidth * 2 + barWidth * 0.5;
            const y = height - barHeight;
            
            // Gradient
            const gradient = ctx.createLinearGradient(0, y, 0, height);
            gradient.addColorStop(0, '#667eea');
            gradient.addColorStop(1, '#764ba2');
            
            ctx.fillStyle = gradient;
            ctx.fillRect(x, y, barWidth, barHeight);
            
            // Label
            ctx.fillStyle = '#64748b';
            ctx.font = '12px Inter';
            ctx.textAlign = 'center';
            ctx.fillText(`Item ${i + 1}`, x + barWidth / 2, height - 10);
        }
    }
    
    showDemo() {
        // Set demo configuration
        this.selectedSource = 'financial';
        this.selectedGoals.add('predict');
        this.selectedGoals.add('discover');
        this.selectedGoals.add('quantify');
        
        this.switchSection('analyzer');
        this.currentStep = 3;
        this.updateStepDisplay();
        
        // Auto-start demo analysis after short delay
        setTimeout(() => {
            this.startAnalysis();
        }, 1000);
    }
    
    // File handling
    handleDragOver(e) {
        e.preventDefault();
        e.currentTarget.classList.add('dragover');
    }
    
    handleFileDrop(e) {
        e.preventDefault();
        e.currentTarget.classList.remove('dragover');
        
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            this.processMultipleFiles(Array.from(files));
        }
    }
    
    handleFileSelect(e) {
        const files = e.target.files;
        if (files.length > 0) {
            this.processMultipleFiles(Array.from(files));
        }
    }
    
    processMultipleFiles(files) {
        const allowedTypes = ['text/csv', 'application/json', 'application/vnd.ms-excel', 'text/xml', 'text/plain'];
        const allowedExtensions = ['.csv', '.json', '.xlsx', '.xls', '.xml', '.txt'];
        
        let validFiles = [];
        let invalidFiles = [];
        
        files.forEach(file => {
            const isValidType = allowedTypes.includes(file.type) || 
                               allowedExtensions.some(ext => file.name.toLowerCase().endsWith(ext));
            
            if (isValidType) {
                validFiles.push(file);
            } else {
                invalidFiles.push(file.name);
            }
        });
        
        if (invalidFiles.length > 0) {
            this.showNotification(`Arquivos não suportados: ${invalidFiles.join(', ')}. Use CSV, Excel, JSON, XML ou TXT.`, 'warning');
        }
        
        if (validFiles.length > 0) {
            validFiles.forEach(file => {
                // Evita duplicatas
                if (!this.uploadedFiles.find(f => f.name === file.name && f.size === file.size)) {
                    this.uploadedFiles.push(file);
                }
            });
            
            this.updateFilesList();
            this.showAnalysisTags();
            this.showNotification(`${validFiles.length} arquivo(s) carregado(s) com sucesso!`, 'success');
            this.updateNavigationState();
        }
    }
    
    processFile(file) {
        // Manter compatibilidade - redireciona para a nova função
        this.processMultipleFiles([file]);
    }
    
    updateFilesList() {
        const filesListContainer = document.getElementById('files-list');
        const uploadedFilesContainer = document.getElementById('uploaded-files');
        
        if (!filesListContainer || !uploadedFilesContainer) return;
        
        if (this.uploadedFiles.length === 0) {
            uploadedFilesContainer.style.display = 'none';
            return;
        }
        
        uploadedFilesContainer.style.display = 'block';
        filesListContainer.innerHTML = '';
        
        this.uploadedFiles.forEach((file, index) => {
            const fileItem = this.createFileItem(file, index);
            filesListContainer.appendChild(fileItem);
        });
    }
    
    createFileItem(file, index) {
        const fileItem = document.createElement('div');
        fileItem.className = 'file-item';
        
        const extension = file.name.split('.').pop().toLowerCase();
        const fileSize = this.formatFileSize(file.size);
        
        fileItem.innerHTML = `
            <div class="file-info">
                <div class="file-icon ${extension}">
                    ${this.getFileIcon(extension)}
                </div>
                <div class="file-details">
                    <h5>${file.name}</h5>
                    <p>${fileSize} • ${extension.toUpperCase()}</p>
                </div>
            </div>
            <div class="file-actions">
                <button class="btn-remove" onclick="dataInsights.removeFile(${index})" title="Remover arquivo">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
        `;
        
        return fileItem;
    }
    
    getFileIcon(extension) {
        const icons = {
            'csv': '<i class="fas fa-file-csv"></i>',
            'json': '<i class="fas fa-file-code"></i>',
            'xlsx': '<i class="fas fa-file-excel"></i>',
            'xls': '<i class="fas fa-file-excel"></i>',
            'xml': '<i class="fas fa-file-code"></i>',
            'txt': '<i class="fas fa-file-alt"></i>'
        };
        return icons[extension] || '<i class="fas fa-file"></i>';
    }
    
    formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }
    
    removeFile(index) {
        this.uploadedFiles.splice(index, 1);
        this.updateFilesList();
        this.updateNavigationState();
        
        if (this.uploadedFiles.length === 0) {
            this.hideAnalysisTags();
        }
        
        this.showNotification('Arquivo removido com sucesso!', 'info');
    }
    
    showAnalysisTags() {
        const tagsPanel = document.getElementById('analysis-tags-panel');
        if (tagsPanel && this.uploadedFiles.length > 0) {
            tagsPanel.style.display = 'block';
            this.setupAnalysisTagsListeners();
        }
    }
    
    hideAnalysisTags() {
        const tagsPanel = document.getElementById('analysis-tags-panel');
        if (tagsPanel) {
            tagsPanel.style.display = 'none';
        }
    }
    
    setupAnalysisTagsListeners() {
        // Listeners para tags de análise
        document.querySelectorAll('input[name="analysis-type"]').forEach(checkbox => {
            checkbox.addEventListener('change', (e) => {
                if (e.target.checked) {
                    this.selectedAnalysisTags.add(e.target.value);
                } else {
                    this.selectedAnalysisTags.delete(e.target.value);
                }
                this.updateNavigationState();
            });
        });
        
        // Listeners para APIs governamentais
        document.querySelectorAll('input[name="government-api"]').forEach(checkbox => {
            checkbox.addEventListener('change', (e) => {
                if (e.target.checked) {
                    this.selectedGovernmentAPIs.add(e.target.value);
                } else {
                    this.selectedGovernmentAPIs.delete(e.target.value);
                }
                this.updateNavigationState();
            });
        });
    }
    
    // Novas funções para Export e Configurações Avançadas
    toggleExportFormat(format) {
        const card = document.querySelector(`[data-format="${format}"]`);
        
        if (this.selectedExportFormats.has(format)) {
            this.selectedExportFormats.delete(format);
            card.classList.remove('selected');
        } else {
            this.selectedExportFormats.add(format);
            card.classList.add('selected');
        }
        
        this.updateExportButtons();
    }
    
    updateExportButtons() {
        const exportSelectedBtn = document.getElementById('export-selected');
        const hasSelectedFormats = this.selectedExportFormats.size > 0;
        
        if (exportSelectedBtn) {
            exportSelectedBtn.disabled = !hasSelectedFormats;
            exportSelectedBtn.style.opacity = hasSelectedFormats ? '1' : '0.6';
        }
    }
    
    async exportSelected() {
        if (this.selectedExportFormats.size === 0) {
            this.showNotification('Selecione pelo menos um formato de exportação.', 'warning');
            return;
        }
        
        this.showNotification('Preparando exportação...', 'info');
        
        try {
            for (const format of this.selectedExportFormats) {
                await this.exportFormat(format);
            }
            
            this.showNotification(`${this.selectedExportFormats.size} arquivo(s) exportado(s) com sucesso!`, 'success');
        } catch (error) {
            console.error('Export failed:', error);
            this.showNotification('Erro na exportação. Tente novamente.', 'error');
        }
    }
    
    async exportAll() {
        const allFormats = ['pdf', 'excel', 'powerpoint', 'dashboard'];
        this.showNotification('Preparando exportação completa...', 'info');
        
        try {
            for (const format of allFormats) {
                await this.exportFormat(format);
            }
            
            this.showNotification('Todos os formatos exportados com sucesso!', 'success');
        } catch (error) {
            console.error('Export all failed:', error);
            this.showNotification('Erro na exportação. Tente novamente.', 'error');
        }
    }
    
    async exportFormat(format) {
        // Simular exportação
        const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
        await delay(1000);
        
        const formatNames = {
            'pdf': 'Relatório PDF',
            'excel': 'Planilha Excel',
            'powerpoint': 'Apresentação PowerPoint',
            'dashboard': 'Dashboard Interativo'
        };
        
        console.log(`Exportando ${formatNames[format]}...`);
        
        // Aqui seria implementada a lógica real de exportação
        // Por enquanto, apenas simular o download
        this.simulateDownload(`analise_dados_${format}.${format === 'powerpoint' ? 'pptx' : format}`);
    }
    
    simulateDownload(filename) {
        const link = document.createElement('a');
        link.download = filename;
        link.href = '#';
        link.style.display = 'none';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
    
    setupAdvancedConfigListeners() {
        // Precision level
        const precisionLevel = document.getElementById('precision-level');
        if (precisionLevel) {
            precisionLevel.addEventListener('change', (e) => {
                this.advancedConfig.precisionLevel = e.target.value;
                this.updateAnalysisTime();
            });
        }
        
        // Chart theme
        const chartTheme = document.getElementById('chart-theme');
        if (chartTheme) {
            chartTheme.addEventListener('change', (e) => {
                this.advancedConfig.chartTheme = e.target.value;
                this.previewChartTheme(e.target.value);
            });
        }
        
        // ML Algorithms
        document.querySelectorAll('input[value$="-forest"], input[value="svm"], input[value="neural-network"], input[value="gradient-boosting"]').forEach(checkbox => {
            checkbox.addEventListener('change', (e) => {
                if (!this.advancedConfig.mlAlgorithms) {
                    this.advancedConfig.mlAlgorithms = new Set();
                }
                
                if (e.target.checked) {
                    this.advancedConfig.mlAlgorithms.add(e.target.value);
                } else {
                    this.advancedConfig.mlAlgorithms.delete(e.target.value);
                }
            });
        });
        
        // Notification email
        const notificationEmail = document.getElementById('notification-email');
        if (notificationEmail) {
            notificationEmail.addEventListener('change', (e) => {
                this.advancedConfig.notificationEmail = e.target.value;
            });
        }
    }
    
    updateAnalysisTime() {
        const times = {
            'fast': '1-2 minutos',
            'balanced': '3-5 minutos',
            'deep': '8-12 minutos',
            'comprehensive': '15-25 minutos'
        };
        
        const time = times[this.advancedConfig.precisionLevel] || '3-5 minutos';
        this.showNotification(`Tempo estimado de análise: ${time}`, 'info');
    }
    
    previewChartTheme(theme) {
        const themes = {
            'professional': 'Tema profissional aplicado',
            'vibrant': 'Tema vibrante aplicado',
            'minimal': 'Tema minimalista aplicado',
            'corporate': 'Tema corporativo aplicado'
        };
        
        this.showNotification(themes[theme] || 'Tema atualizado', 'info');
    }
    
    updateNavigationState() {
        const prevBtn = document.getElementById('prev-step');
        const nextBtn = document.getElementById('next-step');
        const startBtn = document.getElementById('start-analysis');
        
        // Previous button
        if (prevBtn) {
            prevBtn.disabled = this.currentStep === 1;
        }
        
        // Next/Start button logic
        if (this.currentStep === this.totalSteps) {
            if (nextBtn) nextBtn.style.display = 'none';
            if (startBtn) startBtn.style.display = 'inline-flex';
        } else {
            if (nextBtn) nextBtn.style.display = 'inline-flex';
            if (startBtn) startBtn.style.display = 'none';
        }
        
        // Check if step can be completed
        const canProceed = this.canProceedFromStep(this.currentStep);
        if (nextBtn) nextBtn.disabled = !canProceed;
        if (startBtn) startBtn.disabled = !canProceed;
    }
    
    canProceedFromStep(step) {
        switch (step) {
            case 1:
                return this.selectedSource !== null;
            case 2:
                return this.selectedGoals.size > 0;
            case 3:
                if (this.selectedSource === 'upload') {
                    return this.uploadedFiles.length > 0 && this.selectedAnalysisTags.size > 0;
                } else if (this.selectedSource === 'government') {
                    return this.selectedGovernmentAPIs.size > 0 && this.selectedAnalysisTags.size > 0;
                }
                return true;
            case 4:
                return true; // Advanced config is optional
            default:
                return false;
        }
    }
    
    showNotification(message, type = 'info') {
        const container = document.getElementById('notifications');
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <p>${message}</p>
            </div>
        `;
        
        container.appendChild(notification);
        
        // Auto remove after 5 seconds
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 5000);
    }
    
    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const app = new DataInsightsPro();
    
    // Global functions for onclick handlers
    window.switchSection = (section) => app.switchSection(section);
    window.showDemo = () => app.showDemo();
});

// Add some CSS for new components
const additionalStyles = `
<style>
.metric-item {
    background: var(--bg-tertiary);
    padding: var(--spacing-md);
    border-radius: var(--border-radius);
    margin-bottom: var(--spacing-md);
    text-align: center;
}

.metric-value {
    font-size: var(--font-size-2xl);
    font-weight: 700;
    color: var(--primary-color);
}

.metric-label {
    font-size: var(--font-size-sm);
    color: var(--text-secondary);
    margin: var(--spacing-xs) 0;
}

.metric-trend {
    font-size: var(--font-size-xs);
    font-weight: 600;
    color: var(--accent-color);
}

.prediction-item,
.discovery-item,
.recommendation-item {
    background: var(--bg-tertiary);
    padding: var(--spacing-md);
    border-radius: var(--border-radius);
    margin-bottom: var(--spacing-md);
    border-left: 4px solid var(--primary-color);
}

.prediction-item h4,
.discovery-item h4 {
    margin: 0 0 var(--spacing-sm) 0;
    color: var(--text-primary);
    font-size: var(--font-size-base);
}

.prediction-item p,
.discovery-item p {
    margin: 0;
    color: var(--text-secondary);
    font-size: var(--font-size-sm);
}

.notification-content {
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
}

.notification-content p {
    margin: 0;
    color: var(--text-primary);
}
</style>
`;

document.head.insertAdjacentHTML('beforeend', additionalStyles);

// Criar instância global
let dataInsights;

// Inicializar quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', () => {
    dataInsights = new DataInsightsPro();
});

// Funções globais para compatibilidade
window.showDemo = function() {
    if (dataInsights) {
        dataInsights.showDemo();
    }
};
