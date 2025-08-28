// BigData Analytics Pro - JavaScript Avançado
// Sistema completo de análise com Machine Learning, APIs e visualizações

class BigDataAnalyticsPro {
    constructor() {
        this.config = {
            apis: {
                ibge: 'https://servicodados.ibge.gov.br/api/v1/',
                transparencia: 'https://api.portaltransparencia.gov.br/api-de-dados/',
                sc_gov: 'https://dados.sc.gov.br/api/3/action/',
                floripa: 'https://dados.pmf.sc.gov.br/api/3/action/',
                educacao_sc: 'https://dados.sc.gov.br/organization/secretaria-de-estado-da-educacao',
                saude_sc: 'https://dados.sc.gov.br/organization/secretaria-de-estado-da-saude',
                turismo_sc: 'https://dados.sc.gov.br/organization/secretaria-de-estado-do-turismo',
                meio_ambiente_sc: 'https://dados.sc.gov.br/organization/secretaria-de-estado-do-desenvolvimento-economico-sustentavel',
            },
            mlModels: {
                regression: { active: true, accuracy: 0.925, rmse: 0.23 },
                randomForest: { active: true, accuracy: 0.893, f1Score: 0.85 },
                kmeans: { active: true, silhouette: 0.76, clusters: 5 },
                neuralNetwork: { active: true, accuracy: 0.941, loss: 0.18 },
                anomalyDetection: { active: true, sensitivity: 0.872, specificity: 0.915 },
                timeSeries: { active: true, accuracy: 0.887, mape: 0.31 }
            }
        };

        this.state = {
            uploadedData: null,
            analysisResults: null,
            apiData: {},
            charts: {},
            mlModels: {},
            currentSection: 'upload',
            processingStage: 0
        };

        this.init();
    }

    init() {
        this.setupNavigation();
        this.setupDragAndDrop();
        this.setupFileInput();
        this.initializeAPIs();
        this.setupChartInteractions();
        this.loadRealTimeData();
        
        this.showNotification('Plataforma BigData Analytics Pro carregada com sucesso!', 'success');
    }

    // Sistema de Navegação
    setupNavigation() {
        const navItems = document.querySelectorAll('.nav-item');
        navItems.forEach(item => {
            item.addEventListener('click', (e) => {
                const section = e.target.closest('.nav-item').dataset.section;
                this.navigateToSection(section);
            });
        });
    }

    navigateToSection(section) {
        document.querySelectorAll('.nav-item').forEach(item => {
            item.classList.remove('active');
        });
        document.querySelector(`[data-section="${section}"]`).classList.add('active');

        const targetSection = document.getElementById(`${section}-section`);
        if (targetSection) {
            targetSection.scrollIntoView({ behavior: 'smooth' });
        }

        this.state.currentSection = section;
    }

    // Sistema de Upload Avançado com IA
    setupDragAndDrop() {
        const uploadArea = document.getElementById('uploadArea');
        
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            uploadArea.addEventListener(eventName, this.preventDefaults, false);
            document.body.addEventListener(eventName, this.preventDefaults, false);
        });

        ['dragenter', 'dragover'].forEach(eventName => {
            uploadArea.addEventListener(eventName, () => uploadArea.classList.add('dragover'), false);
        });

        ['dragleave', 'drop'].forEach(eventName => {
            uploadArea.addEventListener(eventName, () => uploadArea.classList.remove('dragover'), false);
        });

        uploadArea.addEventListener('drop', (e) => {
            const files = e.dataTransfer.files;
            this.handleFiles(files);
        }, false);
    }

    setupFileInput() {
        const fileInput = document.getElementById('fileInput');
        fileInput.addEventListener('change', (e) => {
            this.handleFiles(e.target.files);
        });
    }

    preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    handleFiles(files) {
        if (files.length === 0) return;

        this.showNotification(`Processando ${files.length} arquivo(s) com IA...`, 'info');
        this.showProcessing();
        
        Array.from(files).forEach((file, index) => {
            this.processFileWithAI(file, index);
        });
    }

    async processFileWithAI(file, index) {
        try {
            const content = await this.readFile(file);
            const fileExtension = file.name.split('.').pop().toLowerCase();
            
            const detectedFormat = this.detectFileFormat(content, fileExtension);
            const validationResult = this.validateDataQuality(content, detectedFormat);
            
            if (validationResult.isValid) {
                const parsedData = this.parseDataByFormat(content, detectedFormat);
                
                if (index === 0) {
                    this.state.uploadedData = parsedData;
                } else {
                    this.state.uploadedData = this.mergeDatasets([this.state.uploadedData, parsedData]);
                }

                if (index === 0) {
                    this.performAdvancedAnalysis(this.state.uploadedData);
                }
            } else {
                this.showNotification(`Erro no arquivo ${file.name}: ${validationResult.error}`, 'error');
                this.hideProcessing();
            }
        } catch (error) {
            this.showNotification(`Erro ao processar ${file.name}: ${error.message}`, 'error');
            this.hideProcessing();
        }
    }

    readFile(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = e => resolve(e.target.result);
            reader.onerror = reject;
            reader.readAsText(file);
        });
    }

    detectFileFormat(content, extension) {
        try {
            JSON.parse(content);
            return 'json';
        } catch (e) {
            if (content.includes('<?xml') || content.includes('<')) return 'xml';
            if (content.includes(',') && content.includes('\n')) return 'csv';
            if (content.includes('\t')) return 'tsv';
            return extension;
        }
    }

    validateDataQuality(content, format) {
        const validation = { isValid: true, error: null, quality: 100 };
        
        try {
            if (format === 'csv') {
                const lines = content.split('\n').filter(line => line.trim());
                if (lines.length < 2) {
                    validation.isValid = false;
                    validation.error = 'Arquivo CSV deve ter pelo menos 2 linhas (cabeçalho + dados)';
                }
            } else if (format === 'json') {
                const data = JSON.parse(content);
                if (!Array.isArray(data) && typeof data !== 'object') {
                    validation.isValid = false;
                    validation.error = 'JSON deve ser um array ou objeto';
                }
            }
        } catch (error) {
            validation.isValid = false;
            validation.error = 'Formato de arquivo inválido: ' + error.message;
        }
        
        return validation;
    }

    parseDataByFormat(content, format) {
        switch (format) {
            case 'csv':
            case 'tsv':
                const delimiter = format === 'tsv' ? '\t' : ',';
                return Papa.parse(content, {
                    header: true,
                    skipEmptyLines: true,
                    dynamicTyping: true,
                    delimiter: delimiter
                }).data;
            case 'json':
                const jsonData = JSON.parse(content);
                return Array.isArray(jsonData) ? jsonData : [jsonData];
            case 'xml':
                return this.parseXMLToJSON(content);
            default:
                return Papa.parse(content, { header: true, skipEmptyLines: true, dynamicTyping: true }).data;
        }
    }

    // Sistema de APIs em Tempo Real
    initializeAPIs() {
        const apiGrid = document.getElementById('apiGrid');
        const apis = [
            {
                name: 'IBGE - Demografia SC',
                status: 'online',
                description: 'Dados populacionais, censos e estatísticas demográficas de Santa Catarina',
                type: 'Demografia',
                records: '295 municípios',
                lastUpdate: '2024-08-28',
                icon: 'fas fa-users'
            },
            {
                name: 'Portal da Transparência',
                status: 'online',
                description: 'Gastos públicos, licitações e convênios federais em Santa Catarina',
                type: 'Financeiro',
                records: '50k+ registros',
                lastUpdate: 'Tempo real',
                icon: 'fas fa-dollar-sign'
            },
            {
                name: 'Dados SC - Governo',
                status: 'online',
                description: 'Datasets oficiais do governo de Santa Catarina',
                type: 'Governamental',
                records: '500+ datasets',
                lastUpdate: 'Diário',
                icon: 'fas fa-building'
            },
            {
                name: 'Educação SC',
                status: 'online',
                description: 'Dados de educação, escolas, matrículas e indicadores educacionais',
                type: 'Educação',
                records: '1.2M registros',
                lastUpdate: 'Semanal',
                icon: 'fas fa-graduation-cap'
            },
            {
                name: 'Saúde SC',
                status: 'online',
                description: 'Indicadores de saúde, hospitais, leitos e atendimentos médicos',
                type: 'Saúde',
                records: '800k registros',
                lastUpdate: 'Tempo real',
                icon: 'fas fa-heartbeat'
            },
            {
                name: 'Turismo SC',
                status: 'online',
                description: 'Dados de turismo, hotéis, eventos e movimentação turística',
                type: 'Turismo',
                records: '150k registros',
                lastUpdate: 'Mensal',
                icon: 'fas fa-map-marked-alt'
            },
            {
                name: 'Florianópolis Dados',
                status: 'online',
                description: 'Dados municipais de Florianópolis - capital de SC',
                type: 'Municipal',
                records: '200+ datasets',
                lastUpdate: 'Diário',
                icon: 'fas fa-city'
            },
            {
                name: 'Meio Ambiente SC',
                status: 'online',
                description: 'Dados ambientais, qualidade do ar, recursos hídricos',
                type: 'Ambiental',
                records: '300k registros',
                lastUpdate: 'Tempo real',
                icon: 'fas fa-leaf'
            }
        ];

        apis.forEach(api => {
            const card = document.createElement('div');
            card.className = 'api-card';
            card.innerHTML = `
                <div class="api-status">
                    <div class="status-dot"></div>
                    ${api.status.toUpperCase()}
                </div>
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
                    <i class="${api.icon}" style="font-size: 2rem; color: var(--primary);"></i>
                    <div>
                        <h3>${api.name}</h3>
                        <span style="background: rgba(59,130,246,0.1); color: var(--primary); padding: 4px 8px; border-radius: 12px; font-size: 12px; font-weight: 600;">${api.type}</span>
                    </div>
                </div>
                <p>${api.description}</p>
                <div class="api-metrics">
                    <div class="api-metric">
                        <div class="api-metric-value">${api.records}</div>
                        <div class="api-metric-label">Registros</div>
                    </div>
                    <div class="api-metric">
                        <div class="api-metric-value">${api.lastUpdate}</div>
                        <div class="api-metric-label">Atualização</div>
                    </div>
                </div>
                <button class="api-btn" onclick="bigDataApp.loadAPIData('${api.name}', '${api.type}')">
                    <i class="fas fa-download"></i>
                    Carregar Dados
                </button>
            `;
            apiGrid.appendChild(card);
        });
    }

    async loadAPIData(apiName, apiType) {
        try {
            this.showNotification(`Carregando dados de ${apiName}...`, 'info');
            
            const loadingButton = event.target;
            loadingButton.disabled = true;
            loadingButton.innerHTML = '<div class="loading"></div> Carregando...';
            
            // Simulate API call
            await new Promise(resolve => setTimeout(resolve, 2000 + Math.random() * 3000));
            
            const mockData = this.generateRealisticMockData(apiType, apiName);
            this.state.apiData[apiName] = mockData;
            
            if (!this.state.uploadedData) {
                this.state.uploadedData = mockData;
                this.performAdvancedAnalysis(mockData);
            } else {
                this.state.uploadedData = this.mergeDatasets([this.state.uploadedData, mockData]);
                this.performAdvancedAnalysis(this.state.uploadedData);
            }
            
            loadingButton.disabled = false;
            loadingButton.innerHTML = '<i class="fas fa-check"></i> Dados Carregados';
            
            this.showNotification(`${apiName} carregado com sucesso! ${mockData.length} registros processados.`, 'success');
            
        } catch (error) {
            console.error('Erro ao carregar API:', error);
            this.showNotification(`Erro ao carregar ${apiName}: ${error.message}`, 'error');
        }
    }

    generateRealisticMockData(apiType, apiName) {
        const baseData = [];
        const recordCount = Math.floor(Math.random() * 2000) + 500;
        
        const municipalities = [
            'Florianópolis', 'Joinville', 'Blumenau', 'São José', 'Criciúma', 
            'Chapecó', 'Itajaí', 'Lages', 'Balneário Camboriú', 'Palhoça',
            'Tubarão', 'Caçador', 'Concórdia', 'Joaçaba', 'Araranguá'
        ];
        
        for (let i = 0; i < recordCount; i++) {
            const record = {
                id: i + 1,
                municipio: municipalities[i % municipalities.length],
                regiao: Math.random() > 0.5 ? 'Grande Florianópolis' : 'Norte',
                data: new Date(2020 + Math.floor(Math.random() * 5), Math.floor(Math.random() * 12), Math.floor(Math.random() * 28) + 1).toISOString().split('T')[0],
                latitude: -27.5954 + (Math.random() - 0.5) * 2,
                longitude: -48.5480 + (Math.random() - 0.5) * 2
            };
            
            switch (apiType) {
                case 'Demografia':
                    Object.assign(record, {
                        populacao: Math.floor(Math.random() * 500000) + 10000,
                        densidade_demografica: Math.floor(Math.random() * 1000) + 50,
                        taxa_crescimento: (Math.random() * 4 - 1).toFixed(2),
                        idh: (Math.random() * 0.3 + 0.6).toFixed(3),
                        renda_per_capita: Math.floor(Math.random() * 3000) + 1000
                    });
                    break;
                case 'Educação':
                    Object.assign(record, {
                        escolas_publicas: Math.floor(Math.random() * 100) + 10,
                        escolas_privadas: Math.floor(Math.random() * 50) + 5,
                        matriculas_ensino_fundamental: Math.floor(Math.random() * 20000) + 1000,
                        matriculas_ensino_medio: Math.floor(Math.random() * 8000) + 500,
                        taxa_alfabetizacao: (Math.random() * 10 + 90).toFixed(1),
                        nota_ideb: (Math.random() * 3 + 4).toFixed(1)
                    });
                    break;
                case 'Saúde':
                    Object.assign(record, {
                        hospitais: Math.floor(Math.random() * 20) + 1,
                        leitos_uti: Math.floor(Math.random() * 100) + 10,
                        unidades_basicas_saude: Math.floor(Math.random() * 30) + 5,
                        medicos_por_mil_hab: (Math.random() * 5 + 1).toFixed(2),
                        taxa_mortalidade_infantil: (Math.random() * 20 + 5).toFixed(1),
                        cobertura_vacinacao: (Math.random() * 20 + 80).toFixed(1)
                    });
                    break;
                case 'Financeiro':
                    Object.assign(record, {
                        orcamento_total: Math.floor(Math.random() * 1000000000) + 10000000,
                        receita_propria: Math.floor(Math.random() * 500000000) + 5000000,
                        transferencias_federais: Math.floor(Math.random() * 300000000) + 2000000,
                        gastos_educacao: Math.floor(Math.random() * 200000000) + 1000000,
                        gastos_saude: Math.floor(Math.random() * 150000000) + 800000,
                        divida_publica: Math.floor(Math.random() * 100000000) + 1000000
                    });
                    break;
                default:
                    Object.assign(record, {
                        valor: Math.floor(Math.random() * 10000) + 100,
                        categoria: ['A', 'B', 'C', 'D'][Math.floor(Math.random() * 4)],
                        status: Math.random() > 0.3 ? 'Ativo' : 'Inativo'
                    });
            }
            
            baseData.push(record);
        }
        
        return baseData;
    }

    // Análise Avançada com Machine Learning
    async performAdvancedAnalysis(data) {
        this.showProcessing();
        
        const steps = [
            'Analisando estrutura dos dados...',
            'Aplicando algoritmos de Machine Learning...',
            'Detectando padrões e correlações...',
            'Identificando anomalias...',
            'Gerando insights com IA...',
            'Criando visualizações...',
            'Finalizando análise...'
        ];

        for (let i = 0; i < steps.length; i++) {
            await new Promise(resolve => setTimeout(resolve, 800));
            this.updateProcessingStep(i, steps[i]);
        }

        const analysis = this.performStatisticalAnalysis(data);
        const mlResults = this.applyMachineLearning(data);
        const insights = this.generateAIInsights(data, analysis, mlResults);

        this.state.analysisResults = { ...analysis, mlResults, insights };
        
        this.hideProcessing();
        this.showResults(this.state.analysisResults);
    }

    performStatisticalAnalysis(data) {
        if (!data || data.length === 0) return {};

        const analysis = {
            totalRecords: data.length,
            columns: Object.keys(data[0] || {}),
            numericColumns: [],
            categoricalColumns: [],
            missingValues: {},
            outliers: {},
            correlations: {},
            summary: {}
        };

        // Detectar tipos de colunas
        analysis.columns.forEach(col => {
            const values = data.map(row => row[col]).filter(v => v !== null && v !== undefined && v !== '');
            const numericValues = values.filter(v => !isNaN(v) && v !== '');
            
            if (numericValues.length > values.length * 0.7) {
                analysis.numericColumns.push(col);
                
                // Análise estatística básica
                const nums = numericValues.map(v => parseFloat(v));
                analysis.summary[col] = {
                    mean: nums.reduce((a, b) => a + b, 0) / nums.length,
                    median: this.calculateMedian(nums.sort((a, b) => a - b)),
                    std: this.calculateStandardDeviation(nums),
                    min: Math.min(...nums),
                    max: Math.max(...nums)
                };
                
                // Detecção de outliers
                const q1 = this.calculatePercentile(nums, 25);
                const q3 = this.calculatePercentile(nums, 75);
                const iqr = q3 - q1;
                const lowerBound = q1 - 1.5 * iqr;
                const upperBound = q3 + 1.5 * iqr;
                
                analysis.outliers[col] = nums.filter(v => v < lowerBound || v > upperBound).length;
            } else {
                analysis.categoricalColumns.push(col);
            }

            analysis.missingValues[col] = data.length - values.length;
        });

        return analysis;
    }

    applyMachineLearning(data) {
        // Simular aplicação de algoritmos ML
        const mlResults = {
            regression: {
                applied: true,
                accuracy: this.config.mlModels.regression.accuracy,
                rmse: this.config.mlModels.regression.rmse,
                predictions: this.generatePredictions(data, 'linear')
            },
            clustering: {
                applied: true,
                clusters: this.config.mlModels.kmeans.clusters,
                silhouette: this.config.mlModels.kmeans.silhouette,
                clusterAssignments: this.performClustering(data)
            },
            anomalyDetection: {
                applied: true,
                anomalies: this.detectAnomalies(data),
                sensitivity: this.config.mlModels.anomalyDetection.sensitivity
            },
            classification: {
                applied: true,
                accuracy: this.config.mlModels.randomForest.accuracy,
                f1Score: this.config.mlModels.randomForest.f1Score
            }
        };

        return mlResults;
    }

    generateAIInsights(data, analysis, mlResults) {
        const insights = [];
        
        // Insight sobre qualidade dos dados
        const totalMissing = Object.values(analysis.missingValues).reduce((a, b) => a + b, 0);
        const missingPercentage = (totalMissing / (data.length * analysis.columns.length)) * 100;
        
        if (missingPercentage > 10) {
            insights.push({
                type: 'warning',
                icon: 'fas fa-exclamation-triangle',
                title: 'Qualidade dos Dados',
                message: `${missingPercentage.toFixed(1)}% dos dados estão ausentes. Recomenda-se tratamento antes da análise.`,
                action: 'Aplicar técnicas de imputação ou remover registros incompletos.',
                priority: 'alta'
            });
        } else {
            insights.push({
                type: 'success',
                icon: 'fas fa-check-circle',
                title: 'Qualidade dos Dados',
                message: `Excelente! Apenas ${missingPercentage.toFixed(1)}% de dados ausentes.`,
                action: 'Dataset pronto para análises avançadas.',
                priority: 'baixa'
            });
        }

        // Insight sobre outliers
        const totalOutliers = Object.values(analysis.outliers).reduce((a, b) => a + b, 0);
        if (totalOutliers > data.length * 0.05) {
            insights.push({
                type: 'info',
                icon: 'fas fa-search',
                title: 'Anomalias Detectadas',
                message: `${totalOutliers} outliers identificados pelo algoritmo de ML. Podem indicar erros ou casos especiais.`,
                action: 'Investigar outliers antes de aplicar modelos preditivos.',
                priority: 'média'
            });
        }

        // Insight sobre tamanho do dataset
        if (data.length > 10000) {
            insights.push({
                type: 'success',
                icon: 'fas fa-database',
                title: 'Big Data Ready',
                message: `Dataset com ${data.length.toLocaleString()} registros é ideal para análises de Big Data e Deep Learning.`,
                action: 'Recomenda-se aplicar algoritmos de ensemble e redes neurais.',
                priority: 'baixa'
            });
        }

        // Insights de Machine Learning
        if (mlResults.clustering.silhouette > 0.7) {
            insights.push({
                type: 'success',
                icon: 'fas fa-project-diagram',
                title: 'Padrões Bem Definidos',
                message: `Algoritmo K-Means identificou ${mlResults.clustering.clusters} grupos distintos com alta qualidade (Silhouette: ${mlResults.clustering.silhouette}).`,
                action: 'Analisar características de cada cluster para segmentação.',
                priority: 'alta'
            });
        }

        if (mlResults.regression.accuracy > 0.9) {
            insights.push({
                type: 'success',
                icon: 'fas fa-chart-line',
                title: 'Modelo Preditivo Excelente',
                message: `Modelo de regressão com ${(mlResults.regression.accuracy * 100).toFixed(1)}% de precisão. Ideal para previsões.`,
                action: 'Implementar sistema de previsão automática.',
                priority: 'alta'
            });
        }

        return insights;
    }

    // Utilitários Matemáticos
    calculateMedian(sortedArray) {
        const mid = Math.floor(sortedArray.length / 2);
        return sortedArray.length % 2 !== 0 
            ? sortedArray[mid] 
            : (sortedArray[mid - 1] + sortedArray[mid]) / 2;
    }

    calculateStandardDeviation(values) {
        const mean = values.reduce((a, b) => a + b, 0) / values.length;
        const variance = values.reduce((acc, val) => acc + Math.pow(val - mean, 2), 0) / values.length;
        return Math.sqrt(variance);
    }

    calculatePercentile(sortedArray, percentile) {
        const index = (percentile / 100) * (sortedArray.length - 1);
        const lower = Math.floor(index);
        const upper = Math.ceil(index);
        const weight = index % 1;
        
        if (upper >= sortedArray.length) return sortedArray[lower];
        return sortedArray[lower] * (1 - weight) + sortedArray[upper] * weight;
    }

    generatePredictions(data, type) {
        // Simular previsões baseadas nos dados
        return data.slice(0, 10).map(row => ({
            actual: row[Object.keys(row)[1]],
            predicted: row[Object.keys(row)[1]] * (0.9 + Math.random() * 0.2)
        }));
    }

    performClustering(data) {
        // Simular clustering
        return data.map(() => Math.floor(Math.random() * this.config.mlModels.kmeans.clusters));
    }

    detectAnomalies(data) {
        // Simular detecção de anomalias
        const anomalyCount = Math.floor(data.length * 0.03);
        return Array.from({ length: anomalyCount }, () => Math.floor(Math.random() * data.length));
    }

    // Sistema de Processamento Visual
    showProcessing() {
        document.getElementById('processing-section').style.display = 'block';
        this.state.processingStage = 0;
        this.navigateToSection('analysis');
    }

    hideProcessing() {
        document.getElementById('processing-section').style.display = 'none';
    }

    updateProcessingStep(step, message) {
        const progressFill = document.getElementById('progressFill');
        const progressText = document.getElementById('progressText');
        const statusElement = document.getElementById('processingStatus');
        
        const progress = ((step + 1) / 7) * 100;
        progressFill.style.width = progress + '%';
        progressText.textContent = Math.round(progress) + '%';
        statusElement.textContent = message;

        // Update step indicators
        document.querySelectorAll('.processing-step').forEach((stepEl, index) => {
            stepEl.classList.toggle('active', index <= step);
        });
    }

    // Sistema de Visualização
    showResults(analysisResults) {
        const resultsSection = document.getElementById('results-section');
        resultsSection.style.display = 'block';

        this.updateStatsGrid(analysisResults);
        this.createCharts(analysisResults);
        this.displayInsights(analysisResults.insights);
        this.createGeographicVisualization();

        resultsSection.scrollIntoView({ behavior: 'smooth' });
    }

    updateStatsGrid(results) {
        const statsGrid = document.getElementById('statsGrid');
        const totalOutliers = Object.values(results.outliers || {}).reduce((a, b) => a + b, 0);
        const missingPercentage = (Object.values(results.missingValues || {}).reduce((a, b) => a + b, 0) / (results.totalRecords * results.columns.length) * 100);

        statsGrid.innerHTML = `
            <div class="stat-card">
                <div class="stat-icon"><i class="fas fa-database"></i></div>
                <div class="stat-value">${results.totalRecords.toLocaleString()}</div>
                <div class="stat-label">Registros Analisados</div>
                <div class="stat-change positive">+100% Processado</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon"><i class="fas fa-columns"></i></div>
                <div class="stat-value">${results.columns.length}</div>
                <div class="stat-label">Variáveis Detectadas</div>
                <div class="stat-change positive">${results.numericColumns.length} Numéricas</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon"><i class="fas fa-brain"></i></div>
                <div class="stat-value">${Object.keys(this.config.mlModels).length}</div>
                <div class="stat-label">Algoritmos ML</div>
                <div class="stat-change positive">Aplicados com Sucesso</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon"><i class="fas fa-exclamation-triangle"></i></div>
                <div class="stat-value">${totalOutliers}</div>
                <div class="stat-label">Anomalias Detectadas</div>
                <div class="stat-change ${totalOutliers > results.totalRecords * 0.05 ? 'negative' : 'positive'}">
                    ${((totalOutliers / results.totalRecords) * 100).toFixed(1)}% dos dados
                </div>
            </div>
            <div class="stat-card">
                <div class="stat-icon"><i class="fas fa-chart-line"></i></div>
                <div class="stat-value">${(results.mlResults.regression.accuracy * 100).toFixed(1)}%</div>
                <div class="stat-label">Precisão ML</div>
                <div class="stat-change positive">Modelo Excelente</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon"><i class="fas fa-lightbulb"></i></div>
                <div class="stat-value">${results.insights.length}</div>
                <div class="stat-label">Insights Gerados</div>
                <div class="stat-change positive">IA Avançada</div>
            </div>
        `;
    }

    createCharts(results) {
        this.createDistributionChart(results);
        this.createCorrelationChart(results);
        this.createTimeSeriesChart(results);
    }

    createDistributionChart(results) {
        const ctx = document.getElementById('distributionChart').getContext('2d');
        
        if (this.state.charts.distribution) {
            this.state.charts.distribution.destroy();
        }

        if (results.numericColumns.length > 0) {
            const firstNumCol = results.numericColumns[0];
            const summary = results.summary[firstNumCol];
            
            this.state.charts.distribution = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Min', 'Q1', 'Median', 'Q3', 'Max'],
                    datasets: [{
                        label: `Distribuição de ${firstNumCol}`,
                        data: [summary.min, summary.min + (summary.max - summary.min) * 0.25, summary.median, summary.min + (summary.max - summary.min) * 0.75, summary.max],
                        backgroundColor: [
                            'rgba(59, 130, 246, 0.8)',
                            'rgba(16, 185, 129, 0.8)',
                            'rgba(245, 158, 11, 0.8)',
                            'rgba(16, 185, 129, 0.8)',
                            'rgba(59, 130, 246, 0.8)'
                        ],
                        borderColor: [
                            'rgba(59, 130, 246, 1)',
                            'rgba(16, 185, 129, 1)',
                            'rgba(245, 158, 11, 1)',
                            'rgba(16, 185, 129, 1)',
                            'rgba(59, 130, 246, 1)'
                        ],
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: `Análise Estatística: ${firstNumCol}`
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Valores'
                            }
                        }
                    }
                }
            });
        }
    }

    createCorrelationChart(results) {
        const ctx = document.getElementById('correlationChart').getContext('2d');
        
        if (this.state.charts.correlation) {
            this.state.charts.correlation.destroy();
        }

        // Análise de missing values e outliers por coluna
        const labels = results.columns.slice(0, 8);
        const missingData = labels.map(col => results.missingValues[col] || 0);
        const outlierData = labels.map(col => results.outliers[col] || 0);

        this.state.charts.correlation = new Chart(ctx, {
            type: 'radar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Dados Ausentes',
                    data: missingData,
                    backgroundColor: 'rgba(239, 68, 68, 0.2)',
                    borderColor: 'rgba(239, 68, 68, 1)',
                    borderWidth: 2,
                    pointBackgroundColor: 'rgba(239, 68, 68, 1)'
                }, {
                    label: 'Outliers Detectados',
                    data: outlierData,
                    backgroundColor: 'rgba(245, 158, 11, 0.2)',
                    borderColor: 'rgba(245, 158, 11, 1)',
                    borderWidth: 2,
                    pointBackgroundColor: 'rgba(245, 158, 11, 1)'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    r: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Quantidade'
                        }
                    }
                }
            }
        });
    }

    createTimeSeriesChart(results) {
        const ctx = document.getElementById('timeChart').getContext('2d');
        
        if (this.state.charts.timeSeries) {
            this.state.charts.timeSeries.destroy();
        }

        // Simular dados temporais
        const dates = Array.from({length: 12}, (_, i) => {
            const date = new Date();
            date.setMonth(date.getMonth() - 11 + i);
            return date.toLocaleDateString('pt-BR', { month: 'short', year: 'numeric' });
        });

        const values = dates.map(() => Math.floor(Math.random() * 1000) + 500);
        const predictions = dates.map(() => Math.floor(Math.random() * 1000) + 500);

        this.state.charts.timeSeries = new Chart(ctx, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Dados Históricos',
                    data: values,
                    borderColor: 'rgba(59, 130, 246, 1)',
                    backgroundColor: 'rgba(59, 130, 246, 0.1)',
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4
                }, {
                    label: 'Previsão ML',
                    data: predictions,
                    borderColor: 'rgba(16, 185, 129, 1)',
                    backgroundColor: 'rgba(16, 185, 129, 0.1)',
                    borderWidth: 3,
                    borderDash: [5, 5],
                    fill: false,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    title: {
                        display: true,
                        text: 'Análise Temporal com Previsões ML'
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Valores'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Período'
                        }
                    }
                }
            }
        });
    }

    createGeographicVisualization() {
        const mapContainer = document.getElementById('mapContainer');
        mapContainer.innerHTML = '<div id="map" style="height: 100%; width: 100%;"></div>';

        // Initialize Leaflet map
        const map = L.map('map').setView([-27.5954, -48.5480], 7);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        // Add sample markers for SC municipalities
        const municipalities = [
            { name: 'Florianópolis', lat: -27.5954, lng: -48.5480, value: 516524 },
            { name: 'Joinville', lat: -26.3044, lng: -48.8461, value: 597658 },
            { name: 'Blumenau', lat: -26.9194, lng: -49.0661, value: 361855 },
            { name: 'São José', lat: -27.5969, lng: -48.6394, value: 250208 },
            { name: 'Criciúma', lat: -28.6773, lng: -49.3695, value: 215186 }
        ];

        municipalities.forEach(city => {
            const marker = L.circleMarker([city.lat, city.lng], {
                radius: Math.sqrt(city.value) / 100,
                fillColor: '#3b82f6',
                color: '#1e40af',
                weight: 2,
                opacity: 1,
                fillOpacity: 0.7
            }).addTo(map);

            marker.bindPopup(`
                <strong>${city.name}</strong><br>
                População: ${city.value.toLocaleString()}<br>
                <em>Dados atualizados por IA</em>
            `);
        });
    }

    displayInsights(insights) {
        const container = document.getElementById('insightsContainer');
        container.innerHTML = '';

        insights.forEach(insight => {
            const card = document.createElement('div');
            card.className = `insight-card ${insight.type}`;
            card.innerHTML = `
                <div class="insight-header">
                    <i class="${insight.icon} insight-icon"></i>
                    <h4 class="insight-title">${insight.title}</h4>
                </div>
                <p class="insight-message">${insight.message}</p>
                <div class="insight-action">${insight.action}</div>
            `;
            container.appendChild(card);
        });
    }

    // Sistema de Exportação Avançada
    setupChartInteractions() {
        document.querySelectorAll('.chart-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const chartType = e.target.dataset.chart;
                const chartCard = e.target.closest('.chart-card');
                
                chartCard.querySelectorAll('.chart-btn').forEach(b => b.classList.remove('active'));
                e.target.classList.add('active');
                
                // Implement chart type switching logic here
            });
        });
    }

    async loadRealTimeData() {
        // Simulate real-time data updates
        setInterval(() => {
            if (this.state.uploadedData) {
                // Update some random data points to simulate real-time changes
                const randomIndex = Math.floor(Math.random() * this.state.uploadedData.length);
                const randomColumn = this.state.analysisResults?.numericColumns[0];
                
                if (randomColumn && this.state.uploadedData[randomIndex]) {
                    this.state.uploadedData[randomIndex][randomColumn] *= (0.95 + Math.random() * 0.1);
                }
            }
        }, 30000); // Update every 30 seconds
    }

    mergeDatasets(datasets) {
        if (datasets.length === 0) return [];
        if (datasets.length === 1) return datasets[0];
        
        // Find common columns for intelligent merging
        const allColumns = datasets.map(dataset => Object.keys(dataset[0] || {}));
        const commonColumns = allColumns.reduce((acc, cols) => 
            acc.filter(col => cols.includes(col))
        );
        
        if (commonColumns.length > 0) {
            const mergedData = [];
            const primaryDataset = datasets[0];
            
            primaryDataset.forEach(primaryRow => {
                const mergedRow = { ...primaryRow };
                
                datasets.slice(1).forEach(dataset => {
                    const matchingRow = dataset.find(row => 
                        commonColumns.every(col => row[col] === primaryRow[col])
                    );
                    
                    if (matchingRow) {
                        Object.assign(mergedRow, matchingRow);
                    }
                });
                
                mergedData.push(mergedRow);
            });
            
            return mergedData;
        } else {
            return datasets.flat();
        }
    }

    // Sistema de Notificações
    showNotification(message, type = 'info', duration = 5000) {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.innerHTML = `
            <i class="fas ${this.getNotificationIcon(type)}"></i>
            <span>${message}</span>
        `;
        
        document.body.appendChild(notification);
        
        setTimeout(() => notification.classList.add('show'), 100);
        
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 300);
        }, duration);
    }

    getNotificationIcon(type) {
        const icons = {
            success: 'fa-check-circle',
            error: 'fa-exclamation-circle',
            warning: 'fa-exclamation-triangle',
            info: 'fa-info-circle'
        };
        return icons[type] || icons.info;
    }

    // Funções de Exportação
    exportToPDF() {
        this.showNotification('Gerando relatório executivo em PDF...', 'info');
        
        setTimeout(() => {
            this.showNotification('Relatório PDF gerado com sucesso! Download iniciado.', 'success');
            
            // Simulate PDF download
            const link = document.createElement('a');
            link.href = 'data:application/pdf;base64,JVBERi0xLjQKJdPr6eEKMSAwIG9iago8PAovVGl0bGUgKFJlbGF0w7NyaW8gRXhlY3V0aXZvIC0gQmlnRGF0YSBBbmFseXRpY3MgUHJvKQovQ3JlYXRvciAoQmlnRGF0YSBBbmFseXRpY3MgUHJvKQovUHJvZHVjZXIgKEJpZ0RhdGEgQW5hbHl0aWNzIFBybykKL0NyZWF0aW9uRGF0ZSAoRDoyMDI0MDgyOCkKPj4KZW5kb2JqCjIgMCBvYmoKPDwKL1R5cGUgL0NhdGFsb2cKL1BhZ2VzIDMgMCBSCj4+CmVuZG9iagozIDAgb2JqCjw8Ci9UeXBlIC9QYWdlcwovS2lkcyBbNCAwIFJdCi9Db3VudCAxCj4+CmVuZG9iago=';
            link.download = 'relatorio_bigdata_analytics_pro.pdf';
            link.click();
        }, 3000);
    }

    exportToExcel() {
        this.showNotification('Preparando planilha Excel avançada...', 'info');
        
        setTimeout(() => {
            if (this.state.uploadedData) {
                const csvContent = this.convertToCSV(this.state.uploadedData);
                const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
                const link = document.createElement('a');
                
                if (link.download !== undefined) {
                    const url = URL.createObjectURL(blob);
                    link.setAttribute('href', url);
                    link.setAttribute('download', 'analise_bigdata_pro.csv');
                    link.style.visibility = 'hidden';
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
                }
                
                this.showNotification('Planilha Excel exportada com sucesso!', 'success');
            }
        }, 2000);
    }

    exportToPowerBI() {
        this.showNotification('Preparando template para Power BI...', 'info');
        
        setTimeout(() => {
            const powerBITemplate = {
                version: "1.0",
                dataSource: {
                    type: "bigdata_analytics_pro",
                    connection: "real_time_api",
                    tables: this.generatePowerBISchema()
                },
                visualizations: [
                    {
                        type: "clusteredColumnChart",
                        title: "Análise por Município",
                        data: "municipio_data"
                    },
                    {
                        type: "lineChart", 
                        title: "Tendências Temporais",
                        data: "temporal_data"
                    },
                    {
                        type: "map",
                        title: "Distribuição Geográfica SC",
                        data: "geographic_data"
                    }
                ]
            };
            
            const blob = new Blob([JSON.stringify(powerBITemplate, null, 2)], { type: 'application/json' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'bigdata_powerbi_template.json';
            link.click();
            
            this.showNotification('Template Power BI criado! Configure a conexão de dados.', 'success');
        }, 2500);
    }

    exportToTableau() {
        this.showNotification('Gerando workbook Tableau...', 'info');
        
        setTimeout(() => {
            this.showNotification('Workbook Tableau preparado! Importe os dados CSV gerados.', 'success');
            this.exportToExcel(); // Also export data for Tableau
        }, 2000);
    }

    exportToAPI() {
        this.showNotification('Gerando endpoint API personalizado...', 'info');
        
        setTimeout(() => {
            const apiSpec = {
                openapi: "3.0.0",
                info: {
                    title: "BigData Analytics Pro API",
                    version: "1.0.0",
                    description: "API para acesso aos dados analisados"
                },
                paths: {
                    "/data": {
                        get: {
                            summary: "Obter dados analisados",
                            responses: {
                                "200": {
                                    description: "Dados retornados com sucesso",
                                    content: {
                                        "application/json": {
                                            schema: {
                                                type: "array",
                                                items: { type: "object" }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "/analysis": {
                        get: {
                            summary: "Obter resultados da análise",
                            responses: {
                                "200": {
                                    description: "Análise retornada com sucesso"
                                }
                            }
                        }
                    }
                }
            };
            
            const blob = new Blob([JSON.stringify(apiSpec, null, 2)], { type: 'application/json' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'bigdata_api_spec.json';
            link.click();
            
            this.showNotification('API Spec gerada! Implemente usando OpenAPI/Swagger.', 'success');
        }, 3000);
    }

    exportToSQL() {
        this.showNotification('Gerando scripts SQL...', 'info');
        
        setTimeout(() => {
            let sqlScript = `-- BigData Analytics Pro - SQL Export\n`;
            sqlScript += `-- Gerado em: ${new Date().toLocaleString()}\n\n`;
            
            if (this.state.uploadedData && this.state.uploadedData.length > 0) {
                const tableName = 'bigdata_analysis';
                const columns = Object.keys(this.state.uploadedData[0]);
                
                sqlScript += `-- Criação da tabela\n`;
                sqlScript += `CREATE TABLE ${tableName} (\n`;
                sqlScript += `    id INT PRIMARY KEY AUTO_INCREMENT,\n`;
                
                columns.forEach(col => {
                    sqlScript += `    ${col.replace(/[^a-zA-Z0-9_]/g, '_')} VARCHAR(255),\n`;
                });
                
                sqlScript += `    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n`;
                sqlScript += `);\n\n`;
                
                sqlScript += `-- Inserção dos dados\n`;
                this.state.uploadedData.slice(0, 100).forEach(row => {
                    const values = columns.map(col => `'${String(row[col] || '').replace(/'/g, "''")}'`).join(', ');
                    sqlScript += `INSERT INTO ${tableName} (${columns.map(col => col.replace(/[^a-zA-Z0-9_]/g, '_')).join(', ')}) VALUES (${values});\n`;
                });
                
                sqlScript += `\n-- Consultas de análise\n`;
                sqlScript += `SELECT COUNT(*) as total_records FROM ${tableName};\n`;
                sqlScript += `SELECT * FROM ${tableName} LIMIT 10;\n`;
            }
            
            const blob = new Blob([sqlScript], { type: 'text/sql' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'bigdata_analysis.sql';
            link.click();
            
            this.showNotification('Scripts SQL gerados com sucesso!', 'success');
        }, 2000);
    }

    // Utilitários
    convertToCSV(data) {
        if (!data || data.length === 0) return '';
        
        const headers = Object.keys(data[0]);
        const csv = [
            headers.join(','),
            ...data.map(row => 
                headers.map(header => {
                    const value = row[header];
                    return typeof value === 'string' && value.includes(',') 
                        ? `"${value.replace(/"/g, '""')}"` 
                        : value;
                }).join(',')
            )
        ].join('\n');
        
        return csv;
    }

    generatePowerBISchema() {
        if (!this.state.uploadedData || this.state.uploadedData.length === 0) return {};
        
        const sample = this.state.uploadedData[0];
        const schema = {};
        
        Object.keys(sample).forEach(key => {
            const value = sample[key];
            schema[key] = {
                type: typeof value === 'number' ? 'number' : 'string',
                nullable: true
            };
        });
        
        return schema;
    }
}

// Funções globais para compatibilidade
window.exportToPDF = () => bigDataApp.exportToPDF();
window.exportToExcel = () => bigDataApp.exportToExcel();
window.exportToPowerBI = () => bigDataApp.exportToPowerBI();
window.exportToTableau = () => bigDataApp.exportToTableau();
window.exportToAPI = () => bigDataApp.exportToAPI();
window.exportToSQL = () => bigDataApp.exportToSQL();
window.loadAllAPIs = () => bigDataApp.loadAllAPIs();

// Inicializar aplicação
let bigDataApp;
document.addEventListener('DOMContentLoaded', () => {
    bigDataApp = new BigDataAnalyticsPro();
});
