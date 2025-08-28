class DataInsightsPro {
    constructor() {
        this.currentStep = 1;
        this.totalSteps = 4;
        this.selectedSource = null;
        this.selectedGoals = new Set();
        this.configuration = {};
        this.analysisData = null;
        this.uploadedFiles = [];
        this.selectedAnalysisTags = new Set();
        this.selectedGovernmentAPIs = new Set();
        this.selectedExportFormats = new Set();
        this.advancedConfig = {};
        this.realTimeData = {};
        
        this.init();
    }
    
    init() {
        this.setupEventListeners();
        this.setupHeroChart();
        this.showSection('home');
        this.initializeAPIs();
        this.setupAdvancedFeatures();
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
        document.getElementById('prev-step')?.addEventListener('click', () => {
            this.previousStep();
        });
        
        document.getElementById('next-step')?.addEventListener('click', () => {
            this.nextStep();
        });
        
        document.getElementById('start-analysis')?.addEventListener('click', () => {
            this.startAnalysis();
        });
        
        // File upload melhorado
        this.setupFileUpload();
        
        // Export format selection
        document.querySelectorAll('.export-card').forEach(card => {
            card.addEventListener('click', (e) => {
                this.toggleExportFormat(e.currentTarget.dataset.format);
            });
        });
        
        // Export buttons
        document.getElementById('export-selected')?.addEventListener('click', () => this.exportSelected());
        document.getElementById('export-all')?.addEventListener('click', () => this.exportAll());
        
        // Advanced configuration
        this.setupAdvancedConfigListeners();
    }
    
    setupFileUpload() {
        const uploadZone = document.getElementById('upload-zone');
        const fileInput = document.getElementById('file-input');
        
        if (uploadZone && fileInput) {
            // Click para abrir seletor
            uploadZone.addEventListener('click', () => fileInput.click());
            
            // Drag & Drop
            uploadZone.addEventListener('dragover', this.handleDragOver.bind(this));
            uploadZone.addEventListener('dragleave', this.handleDragLeave.bind(this));
            uploadZone.addEventListener('drop', this.handleFileDrop.bind(this));
            
            // Seleção de arquivos
            fileInput.addEventListener('change', this.handleFileSelect.bind(this));
        }
    }
    
    handleDragOver(e) {
        e.preventDefault();
        e.stopPropagation();
        const uploadZone = document.getElementById('upload-zone');
        uploadZone.classList.add('drag-over');
    }
    
    handleDragLeave(e) {
        e.preventDefault();
        e.stopPropagation();
        const uploadZone = document.getElementById('upload-zone');
        uploadZone.classList.remove('drag-over');
    }
    
    handleFileDrop(e) {
        e.preventDefault();
        e.stopPropagation();
        const uploadZone = document.getElementById('upload-zone');
        uploadZone.classList.remove('drag-over');
        
        const files = Array.from(e.dataTransfer.files);
        this.processFiles(files);
    }
    
    handleFileSelect(e) {
        const files = Array.from(e.target.files);
        this.processFiles(files);
    }
    
    async processFiles(files) {
        this.showNotification('Processando arquivos...', 'info');
        
        try {
            // Validação avançada de arquivos
            const validFiles = await this.validateFiles(files);
            
            if (validFiles.length === 0) {
                this.showNotification('Nenhum arquivo válido encontrado', 'error');
                return;
            }
            
            // Processar cada arquivo
            for (const file of validFiles) {
                await this.processIndividualFile(file);
            }
            
            this.showUploadedFiles();
            this.showNotification(`${validFiles.length} arquivo(s) processado(s) com sucesso!`, 'success');
            
            // Mostrar painel de análise
            document.getElementById('analysis-tags-panel').style.display = 'block';
            
        } catch (error) {
            console.error('Erro ao processar arquivos:', error);
            this.showNotification('Erro ao processar arquivos: ' + error.message, 'error');
        }
    }
    
    async validateFiles(files) {
        const validFiles = [];
        const maxSize = 50 * 1024 * 1024; // 50MB
        const allowedTypes = ['csv', 'json', 'xlsx', 'xls', 'xml', 'txt'];
        
        for (const file of files) {
            // Verificar tamanho
            if (file.size > maxSize) {
                this.showNotification(`Arquivo ${file.name} muito grande (max 50MB)`, 'warning');
                continue;
            }
            
            // Verificar tipo
            const extension = file.name.split('.').pop().toLowerCase();
            if (!allowedTypes.includes(extension)) {
                this.showNotification(`Tipo de arquivo ${extension} não suportado`, 'warning');
                continue;
            }
            
            validFiles.push(file);
        }
        
        return validFiles;
    }
    
    async processIndividualFile(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            
            reader.onload = async (e) => {
                try {
                    const content = e.target.result;
                    const fileData = await this.parseFileContent(content, file.name);
                    
                    const fileInfo = {
                        name: file.name,
                        size: file.size,
                        type: file.type,
                        data: fileData,
                        processedAt: new Date(),
                        stats: this.generateFileStats(fileData)
                    };
                    
                    this.uploadedFiles.push(fileInfo);
                    resolve(fileInfo);
                    
                } catch (error) {
                    reject(error);
                }
            };
            
            reader.onerror = () => reject(new Error(`Erro ao ler arquivo ${file.name}`));
            reader.readAsText(file);
        });
    }
    
    async parseFileContent(content, filename) {
        const extension = filename.split('.').pop().toLowerCase();
        
        switch (extension) {
            case 'csv':
                return this.parseCSV(content);
            case 'json':
                return this.parseJSON(content);
            case 'xml':
                return this.parseXML(content);
            case 'txt':
                return this.parseTXT(content);
            default:
                throw new Error(`Formato ${extension} não suportado`);
        }
    }
    
    parseCSV(content) {
        const result = Papa.parse(content, {
            header: true,
            skipEmptyLines: true,
            dynamicTyping: true,
            transform: (value) => {
                // Limpeza de dados
                if (typeof value === 'string') {
                    value = value.trim();
                    if (value === '' || value.toLowerCase() === 'null') return null;
                }
                return value;
            }
        });
        
        if (result.errors.length > 0) {
            console.warn('Avisos ao processar CSV:', result.errors);
        }
        
        return result.data;
    }
    
    parseJSON(content) {
        try {
            const data = JSON.parse(content);
            return Array.isArray(data) ? data : [data];
        } catch (error) {
            throw new Error('JSON inválido: ' + error.message);
        }
    }
    
    parseXML(content) {
        // Implementação simplificada de parsing XML
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(content, 'text/xml');
        
        if (xmlDoc.documentElement.nodeName === 'parsererror') {
            throw new Error('XML inválido');
        }
        
        // Converter XML para array de objetos
        const items = xmlDoc.querySelectorAll('*');
        const data = [];
        
        items.forEach(item => {
            if (item.children.length === 0 && item.textContent.trim()) {
                const obj = {};
                obj[item.nodeName] = item.textContent.trim();
                data.push(obj);
            }
        });
        
        return data;
    }
    
    parseTXT(content) {
        // Tentar identificar formato do TXT
        const lines = content.split('\n').filter(line => line.trim());
        
        if (lines.length === 0) {
            throw new Error('Arquivo TXT vazio');
        }
        
        // Se tem separadores, tratar como CSV
        if (lines[0].includes('\t') || lines[0].includes(';') || lines[0].includes(',')) {
            return this.parseCSV(content);
        }
        
        // Caso contrário, cada linha é um item
        return lines.map((line, index) => ({
            linha: index + 1,
            conteudo: line.trim()
        }));
    }
    
    generateFileStats(data) {
        if (!Array.isArray(data) || data.length === 0) {
            return { records: 0, columns: 0, quality: 0 };
        }
        
        const records = data.length;
        const columns = Object.keys(data[0] || {}).length;
        
        // Calcular qualidade dos dados
        let totalCells = records * columns;
        let emptyCells = 0;
        
        data.forEach(row => {
            Object.values(row).forEach(value => {
                if (value === null || value === undefined || value === '') {
                    emptyCells++;
                }
            });
        });
        
        const quality = totalCells > 0 ? ((totalCells - emptyCells) / totalCells * 100) : 0;
        
        return {
            records,
            columns,
            quality: Math.round(quality),
            size: JSON.stringify(data).length
        };
    }
    
    showUploadedFiles() {
        const container = document.getElementById('uploaded-files');
        const filesList = document.getElementById('files-list');
        
        if (!container || !filesList) return;
        
        container.style.display = 'block';
        filesList.innerHTML = '';
        
        this.uploadedFiles.forEach((file, index) => {
            const fileItem = document.createElement('div');
            fileItem.className = 'file-item';
            
            fileItem.innerHTML = `
                <div class="file-info">
                    <div class="file-header">
                        <span class="file-name">${file.name}</span>
                        <span class="file-size">${this.formatFileSize(file.size)}</span>
                    </div>
                    <div class="file-stats">
                        <span class="stat">${file.stats.records} registros</span>
                        <span class="stat">${file.stats.columns} colunas</span>
                        <span class="stat quality-${this.getQualityClass(file.stats.quality)}">
                            ${file.stats.quality}% qualidade
                        </span>
                    </div>
                </div>
                <div class="file-actions">
                    <button class="btn-preview" onclick="dataInsights.previewFile(${index})">
                        <i class="fas fa-eye"></i> Preview
                    </button>
                    <button class="btn-remove" onclick="dataInsights.removeFile(${index})">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>
            `;
            
            filesList.appendChild(fileItem);
        });
    }
    
    formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }
    
    getQualityClass(quality) {
        if (quality >= 90) return 'excellent';
        if (quality >= 70) return 'good';
        if (quality >= 50) return 'fair';
        return 'poor';
    }
    
    previewFile(index) {
        const file = this.uploadedFiles[index];
        if (!file) return;
        
        this.showDataPreview(file);
    }
    
    showDataPreview(file) {
        const modal = document.createElement('div');
        modal.className = 'data-preview-modal';
        
        const sampleData = file.data.slice(0, 10); // Primeiras 10 linhas
        const columns = Object.keys(sampleData[0] || {});
        
        modal.innerHTML = `
            <div class="modal-content">
                <div class="modal-header">
                    <h3>Preview: ${file.name}</h3>
                    <button class="modal-close" onclick="this.closest('.data-preview-modal').remove()">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
                <div class="modal-body">
                    <div class="data-table-container">
                        <table class="data-table">
                            <thead>
                                <tr>
                                    ${columns.map(col => `<th>${col}</th>`).join('')}
                                </tr>
                            </thead>
                            <tbody>
                                ${sampleData.map(row => `
                                    <tr>
                                        ${columns.map(col => `<td>${row[col] || ''}</td>`).join('')}
                                    </tr>
                                `).join('')}
                            </tbody>
                        </table>
                    </div>
                    <div class="preview-info">
                        <p>Mostrando ${sampleData.length} de ${file.stats.records} registros</p>
                    </div>
                </div>
            </div>
        `;
        
        document.body.appendChild(modal);
    }
    
    removeFile(index) {
        if (confirm('Remover este arquivo?')) {
            this.uploadedFiles.splice(index, 1);
            this.showUploadedFiles();
            
            if (this.uploadedFiles.length === 0) {
                document.getElementById('uploaded-files').style.display = 'none';
                document.getElementById('analysis-tags-panel').style.display = 'none';
            }
        }
    }
    
    // APIs em tempo real
    initializeAPIs() {
        this.apiEndpoints = {
            ibge: {
                name: 'IBGE - Dados Demográficos',
                url: 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/42/municipios',
                description: 'Municípios de Santa Catarina',
                active: true
            },
            educacao_sc: {
                name: 'Educação SC',
                url: 'https://dados.sc.gov.br/api/3/action/package_search?q=educacao',
                description: 'Dados educacionais de SC',
                active: true
            },
            saude_sc: {
                name: 'Saúde SC',
                url: 'https://dados.sc.gov.br/api/3/action/package_search?q=saude',
                description: 'Indicadores de saúde',
                active: true
            },
            transparencia: {
                name: 'Portal da Transparência',
                url: 'https://api.portaltransparencia.gov.br/api-de-dados/municipios',
                description: 'Dados de transparência pública',
                active: false // Requer API key
            }
        };
        
        this.setupAPICards();
    }
    
    setupAPICards() {
        const container = document.querySelector('.api-cards-grid');
        if (!container) return;
        
        Object.entries(this.apiEndpoints).forEach(([key, api]) => {
            const card = document.createElement('div');
            card.className = `api-card ${api.active ? 'active' : 'inactive'}`;
            
            card.innerHTML = `
                <div class="api-header">
                    <h4>${api.name}</h4>
                    <span class="api-status ${api.active ? 'online' : 'offline'}">
                        ${api.active ? 'Online' : 'Offline'}
                    </span>
                </div>
                <p class="api-description">${api.description}</p>
                <div class="api-actions">
                    <button class="btn-api-load" ${!api.active ? 'disabled' : ''} 
                            onclick="dataInsights.loadAPIData('${key}')">
                        <i class="fas fa-download"></i>
                        Carregar Dados
                    </button>
                    <button class="btn-api-test" onclick="dataInsights.testAPI('${key}')">
                        <i class="fas fa-plug"></i>
                        Testar
                    </button>
                </div>
            `;
            
            container.appendChild(card);
        });
    }
    
    async loadAPIData(apiKey) {
        const api = this.apiEndpoints[apiKey];
        if (!api || !api.active) return;
        
        this.showNotification(`Carregando dados de ${api.name}...`, 'info');
        
        try {
            // Para demonstração, vamos simular dados
            const mockData = this.generateMockAPIData(apiKey);
            
            const fileInfo = {
                name: `${api.name}_${new Date().toISOString().split('T')[0]}.json`,
                size: JSON.stringify(mockData).length,
                type: 'application/json',
                data: mockData,
                processedAt: new Date(),
                stats: this.generateFileStats(mockData),
                source: 'api'
            };
            
            this.uploadedFiles.push(fileInfo);
            this.showUploadedFiles();
            this.showNotification(`Dados de ${api.name} carregados com sucesso!`, 'success');
            
            // Mostrar painel de análise
            document.getElementById('analysis-tags-panel').style.display = 'block';
            
        } catch (error) {
            console.error('Erro ao carregar API:', error);
            this.showNotification(`Erro ao carregar ${api.name}: ${error.message}`, 'error');
        }
    }
    
    generateMockAPIData(apiKey) {
        const baseCount = Math.floor(Math.random() * 500) + 100;
        const data = [];
        
        for (let i = 0; i < baseCount; i++) {
            let record = {
                id: i + 1,
                data_coleta: new Date(2020 + Math.floor(Math.random() * 4), 
                                    Math.floor(Math.random() * 12), 
                                    Math.floor(Math.random() * 28) + 1).toISOString().split('T')[0]
            };
            
            switch (apiKey) {
                case 'ibge':
                    record = {
                        ...record,
                        municipio: `Município ${i % 50 + 1}`,
                        populacao: Math.floor(Math.random() * 500000) + 10000,
                        area_km2: Math.floor(Math.random() * 1000) + 50,
                        densidade_demografica: Math.floor(Math.random() * 300) + 10
                    };
                    break;
                    
                case 'educacao_sc':
                    record = {
                        ...record,
                        escola: `Escola ${i % 100 + 1}`,
                        municipio: `Município ${i % 50 + 1}`,
                        matriculas: Math.floor(Math.random() * 1000) + 50,
                        professores: Math.floor(Math.random() * 50) + 5,
                        aprovacao_rate: (Math.random() * 30 + 70).toFixed(1)
                    };
                    break;
                    
                case 'saude_sc':
                    record = {
                        ...record,
                        unidade_saude: `UBS ${i % 200 + 1}`,
                        municipio: `Município ${i % 50 + 1}`,
                        atendimentos_mes: Math.floor(Math.random() * 2000) + 100,
                        leitos_disponiveis: Math.floor(Math.random() * 50) + 5,
                        vacinas_aplicadas: Math.floor(Math.random() * 500) + 50
                    };
                    break;
            }
            
            data.push(record);
        }
        
        return data;
    }
    
    async testAPI(apiKey) {
        const api = this.apiEndpoints[apiKey];
        this.showNotification(`Testando conexão com ${api.name}...`, 'info');
        
        try {
            // Simular teste de API
            await new Promise(resolve => setTimeout(resolve, 1000 + Math.random() * 2000));
            
            const success = Math.random() > 0.2; // 80% de chance de sucesso
            
            if (success) {
                this.showNotification(`${api.name} respondeu com sucesso!`, 'success');
            } else {
                this.showNotification(`${api.name} não está respondendo`, 'warning');
            }
            
        } catch (error) {
            this.showNotification(`Erro ao testar ${api.name}`, 'error');
        }
    }
    
    // Sistema de notificações melhorado
    showNotification(message, type = 'info', duration = 4000) {
        const container = document.getElementById('notifications') || this.createNotificationContainer();
        
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        
        const icons = {
            success: 'fa-check-circle',
            error: 'fa-exclamation-circle',
            warning: 'fa-exclamation-triangle',
            info: 'fa-info-circle'
        };
        
        notification.innerHTML = `
            <div class="notification-content">
                <i class="fas ${icons[type]}"></i>
                <span>${message}</span>
            </div>
            <button class="notification-close" onclick="this.parentElement.remove()">
                <i class="fas fa-times"></i>
            </button>
        `;
        
        container.appendChild(notification);
        
        // Auto-remove
        setTimeout(() => {
            if (notification.parentElement) {
                notification.remove();
            }
        }, duration);
        
        // Animação de entrada
        setTimeout(() => {
            notification.classList.add('show');
        }, 100);
    }
    
    createNotificationContainer() {
        const container = document.createElement('div');
        container.id = 'notifications';
        container.className = 'notifications';
        document.body.appendChild(container);
        return container;
    }
    
    // Restante dos métodos existentes...
    switchSection(sectionName) {
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        document.querySelector(`[data-section="${sectionName}"]`)?.classList.add('active');
        
        document.querySelectorAll('.section').forEach(section => {
            section.classList.remove('active');
        });
        document.getElementById(sectionName)?.classList.add('active');
    }
    
    showSection(sectionName) {
        this.switchSection(sectionName);
    }
    
    selectDataSource(source) {
        this.selectedSource = source;
        document.querySelectorAll('.source-card').forEach(card => {
            card.classList.remove('selected');
        });
        document.querySelector(`[data-source="${source}"]`).classList.add('selected');
        
        // Mostrar painel de configuração correspondente
        document.querySelectorAll('.config-panel').forEach(panel => {
            panel.style.display = 'none';
        });
        document.querySelector(`[data-source="${source}"]`)?.style.display = 'block';
    }
    
    toggleGoal(goal) {
        if (this.selectedGoals.has(goal)) {
            this.selectedGoals.delete(goal);
        } else {
            this.selectedGoals.add(goal);
        }
        
        const goalCard = document.querySelector(`[data-goal="${goal}"]`);
        goalCard.classList.toggle('selected');
    }
    
    setupHeroChart() {
        const canvas = document.getElementById('hero-chart');
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
                datasets: [{
                    label: 'Dados Processados',
                    data: [12, 19, 3, 5, 2, 3],
                    borderColor: '#3b82f6',
                    backgroundColor: 'rgba(59, 130, 246, 0.1)',
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
                    x: {
                        display: false
                    },
                    y: {
                        display: false
                    }
                }
            }
        });
    }
    
    setupAdvancedConfigListeners() {
        // Sample size
        const sampleSizeRange = document.getElementById('sample-size');
        const sampleSizeValue = document.getElementById('sample-size-value');
        
        if (sampleSizeRange && sampleSizeValue) {
            sampleSizeRange.addEventListener('input', (e) => {
                sampleSizeValue.textContent = `${e.target.value}%`;
                this.advancedConfig.sampleSize = parseInt(e.target.value);
            });
        }
    }
    
    setupAdvancedFeatures() {
        // Adicionar estilos dinamicamente
        this.addAdvancedStyles();
    }
    
    addAdvancedStyles() {
        const styles = `
            <style>
                /* Upload Zone Styles */
                .upload-zone {
                    transition: all 0.3s ease;
                }
                
                .upload-zone.drag-over {
                    border-color: var(--primary-color);
                    background: rgba(59, 130, 246, 0.05);
                    transform: scale(1.02);
                }
                
                /* File Item Styles */
                .file-item {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 16px;
                    border: 1px solid var(--border-color);
                    border-radius: 8px;
                    margin-bottom: 12px;
                    background: var(--bg-primary);
                }
                
                .file-info {
                    flex: 1;
                }
                
                .file-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 8px;
                }
                
                .file-name {
                    font-weight: 600;
                    color: var(--text-primary);
                }
                
                .file-size {
                    font-size: 14px;
                    color: var(--text-secondary);
                }
                
                .file-stats {
                    display: flex;
                    gap: 16px;
                    font-size: 14px;
                }
                
                .stat {
                    color: var(--text-secondary);
                }
                
                .quality-excellent { color: #10b981; }
                .quality-good { color: #3b82f6; }
                .quality-fair { color: #f59e0b; }
                .quality-poor { color: #ef4444; }
                
                .file-actions {
                    display: flex;
                    gap: 8px;
                }
                
                .btn-preview, .btn-remove {
                    padding: 8px 12px;
                    border: none;
                    border-radius: 6px;
                    cursor: pointer;
                    font-size: 14px;
                    transition: all 0.2s;
                }
                
                .btn-preview {
                    background: var(--primary-color);
                    color: white;
                }
                
                .btn-preview:hover {
                    background: var(--primary-dark);
                }
                
                .btn-remove {
                    background: #ef4444;
                    color: white;
                }
                
                .btn-remove:hover {
                    background: #dc2626;
                }
                
                /* Data Preview Modal */
                .data-preview-modal {
                    position: fixed;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background: rgba(0, 0, 0, 0.5);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    z-index: 1000;
                }
                
                .modal-content {
                    background: white;
                    border-radius: 12px;
                    max-width: 90vw;
                    max-height: 90vh;
                    overflow: hidden;
                    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
                }
                
                .modal-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 20px;
                    border-bottom: 1px solid var(--border-color);
                }
                
                .modal-close {
                    background: none;
                    border: none;
                    font-size: 18px;
                    cursor: pointer;
                    color: var(--text-secondary);
                }
                
                .modal-body {
                    padding: 20px;
                    max-height: 70vh;
                    overflow: auto;
                }
                
                .data-table-container {
                    overflow-x: auto;
                    margin-bottom: 16px;
                }
                
                .data-table {
                    width: 100%;
                    border-collapse: collapse;
                    font-size: 14px;
                }
                
                .data-table th,
                .data-table td {
                    padding: 8px 12px;
                    text-align: left;
                    border-bottom: 1px solid var(--border-color);
                }
                
                .data-table th {
                    background: var(--bg-secondary);
                    font-weight: 600;
                    color: var(--text-primary);
                }
                
                .data-table td {
                    color: var(--text-secondary);
                }
                
                /* API Cards */
                .api-card {
                    border: 1px solid var(--border-color);
                    border-radius: 8px;
                    padding: 20px;
                    background: var(--bg-primary);
                    transition: all 0.3s;
                }
                
                .api-card:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                }
                
                .api-card.inactive {
                    opacity: 0.6;
                }
                
                .api-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 12px;
                }
                
                .api-status {
                    padding: 4px 8px;
                    border-radius: 4px;
                    font-size: 12px;
                    font-weight: 600;
                }
                
                .api-status.online {
                    background: rgba(16, 185, 129, 0.1);
                    color: #10b981;
                }
                
                .api-status.offline {
                    background: rgba(239, 68, 68, 0.1);
                    color: #ef4444;
                }
                
                .api-description {
                    color: var(--text-secondary);
                    margin-bottom: 16px;
                    font-size: 14px;
                }
                
                .api-actions {
                    display: flex;
                    gap: 8px;
                }
                
                .btn-api-load,
                .btn-api-test {
                    flex: 1;
                    padding: 8px 16px;
                    border: none;
                    border-radius: 6px;
                    cursor: pointer;
                    font-size: 14px;
                    transition: all 0.2s;
                }
                
                .btn-api-load {
                    background: var(--primary-color);
                    color: white;
                }
                
                .btn-api-load:hover:not(:disabled) {
                    background: var(--primary-dark);
                }
                
                .btn-api-load:disabled {
                    background: var(--text-secondary);
                    cursor: not-allowed;
                }
                
                .btn-api-test {
                    background: var(--bg-secondary);
                    color: var(--text-primary);
                    border: 1px solid var(--border-color);
                }
                
                .btn-api-test:hover {
                    background: var(--border-color);
                }
                
                /* Notifications */
                .notifications {
                    position: fixed;
                    top: 20px;
                    right: 20px;
                    z-index: 1001;
                    max-width: 400px;
                }
                
                .notification {
                    background: white;
                    border-radius: 8px;
                    padding: 16px;
                    margin-bottom: 12px;
                    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
                    display: flex;
                    justify-content: space-between;
                    align-items: flex-start;
                    opacity: 0;
                    transform: translateX(100%);
                    transition: all 0.3s ease;
                    border-left: 4px solid;
                }
                
                .notification.show {
                    opacity: 1;
                    transform: translateX(0);
                }
                
                .notification-success {
                    border-left-color: #10b981;
                }
                
                .notification-error {
                    border-left-color: #ef4444;
                }
                
                .notification-warning {
                    border-left-color: #f59e0b;
                }
                
                .notification-info {
                    border-left-color: #3b82f6;
                }
                
                .notification-content {
                    display: flex;
                    align-items: center;
                    gap: 12px;
                    flex: 1;
                }
                
                .notification-content i {
                    font-size: 18px;
                }
                
                .notification-success .notification-content i {
                    color: #10b981;
                }
                
                .notification-error .notification-content i {
                    color: #ef4444;
                }
                
                .notification-warning .notification-content i {
                    color: #f59e0b;
                }
                
                .notification-info .notification-content i {
                    color: #3b82f6;
                }
                
                .notification-close {
                    background: none;
                    border: none;
                    color: var(--text-secondary);
                    cursor: pointer;
                    font-size: 14px;
                    padding: 0;
                    margin-left: 8px;
                }
                
                .notification-close:hover {
                    color: var(--text-primary);
                }
            </style>
        `;
        
        document.head.insertAdjacentHTML('beforeend', styles);
    }
    
    // Método placeholder para compatibilidade
    showDemo() {
        this.showNotification('Demo iniciada com dados de exemplo', 'info');
        // Implementar demo aqui
    }
    
    // Métodos placeholder para step navigation
    previousStep() {
        if (this.currentStep > 1) {
            this.currentStep--;
            this.updateStepDisplay();
        }
    }
    
    nextStep() {
        if (this.currentStep < this.totalSteps) {
            this.currentStep++;
            this.updateStepDisplay();
        }
    }
    
    updateStepDisplay() {
        // Implementar atualização visual dos steps
    }
    
    startAnalysis() {
        this.showNotification('Análise iniciada!', 'success');
        // Implementar início da análise
    }
    
    toggleExportFormat(format) {
        if (this.selectedExportFormats.has(format)) {
            this.selectedExportFormats.delete(format);
        } else {
            this.selectedExportFormats.add(format);
        }
        
        const formatCard = document.querySelector(`[data-format="${format}"]`);
        formatCard?.classList.toggle('selected');
    }
    
    exportSelected() {
        if (this.selectedExportFormats.size === 0) {
            this.showNotification('Selecione pelo menos um formato de exportação', 'warning');
            return;
        }
        
        this.showNotification(`Exportando em ${this.selectedExportFormats.size} formato(s)...`, 'info');
        // Implementar exportação
    }
    
    exportAll() {
        this.showNotification('Exportando em todos os formatos...', 'info');
        // Implementar exportação completa
    }
}

// Inicializar quando DOM estiver pronto
let dataInsights;

document.addEventListener('DOMContentLoaded', () => {
    dataInsights = new DataInsightsPro();
});

// Funções globais para compatibilidade
window.showDemo = function() {
    if (dataInsights) {
        dataInsights.showDemo();
    }
};

// Export para uso em outros módulos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = DataInsightsPro;
}
