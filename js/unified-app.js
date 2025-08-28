// DataScience Pro - Unified Application JavaScript
// All functionality in a single, organized file to prevent conflicts

class DataSciencePro {
    constructor() {
        this.currentDataset = null;
        this.analysisCharts = {};
        this.initialized = false;
        this.references = [];
        
        this.init();
    }
    
    init() {
        if (this.initialized) return;
        
        document.addEventListener('DOMContentLoaded', () => {
            console.log('DataScience Pro - Initializing...');
            
            this.initNavigation();
            this.initSmoothScrolling();
            this.initTooltips();
            this.initAnimations();
            this.initAnalysisTool();
            this.initReferences();
            
            this.initialized = true;
            
            setTimeout(() => {
                this.showNotification('Bem-vindo ao DataScience Pro! Explore nossos guias e ferramentas.', 'success');
            }, 1000);
            
            console.log('DataScience Pro initialized successfully!');
        });
    }
    
    // Navigation functionality
    initNavigation() {
        const navToggle = document.getElementById('nav-toggle');
        const navMenu = document.getElementById('nav-menu');
        const navLinks = document.querySelectorAll('.nav-link');
        
        if (navToggle && navMenu) {
            navToggle.addEventListener('click', () => {
                navMenu.classList.toggle('active');
                navToggle.classList.toggle('active');
            });
        }
        
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                
                const targetTab = link.getAttribute('data-tab');
                if (targetTab) {
                    this.switchTab(targetTab);
                    
                    navLinks.forEach(l => l.classList.remove('active'));
                    link.classList.add('active');
                    
                    if (navMenu && navToggle) {
                        navMenu.classList.remove('active');
                        navToggle.classList.remove('active');
                    }
                }
            });
        });
        
        document.addEventListener('click', (e) => {
            if (navMenu && navToggle && 
                !navMenu.contains(e.target) && 
                !navToggle.contains(e.target)) {
                navMenu.classList.remove('active');
                navToggle.classList.remove('active');
            }
        });
    }
    
    switchTab(tabName) {
        const tabContents = document.querySelectorAll('.tab-content');
        tabContents.forEach(content => {
            content.classList.remove('active');
        });
        
        const targetTab = document.getElementById(tabName);
        if (targetTab) {
            targetTab.classList.add('active');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    }
    
    initSmoothScrolling() {
        const anchorLinks = document.querySelectorAll('a[href^="#"]');
        
        anchorLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                const href = link.getAttribute('href');
                
                if (link.hasAttribute('data-tab')) return;
                
                const targetElement = document.querySelector(href);
                if (targetElement) {
                    e.preventDefault();
                    const offsetTop = targetElement.offsetTop - 100;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }
    
    initTooltips() {
        const tooltipElements = document.querySelectorAll('[data-tooltip]');
        
        tooltipElements.forEach(element => {
            element.addEventListener('mouseenter', () => {
                this.showTooltip(element, element.getAttribute('data-tooltip'));
            });
            
            element.addEventListener('mouseleave', () => {
                this.hideTooltip();
            });
        });
    }
    
    showTooltip(element, text) {
        this.hideTooltip(); // Remove any existing tooltip
        
        const tooltip = document.createElement('div');
        tooltip.className = 'custom-tooltip';
        tooltip.textContent = text;
        tooltip.id = 'active-tooltip';
        
        document.body.appendChild(tooltip);
        
        const rect = element.getBoundingClientRect();
        tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
        tooltip.style.top = rect.top - tooltip.offsetHeight - 10 + 'px';
        
        setTimeout(() => {
            tooltip.classList.add('show');
        }, 10);
    }
    
    hideTooltip() {
        const tooltip = document.getElementById('active-tooltip');
        if (tooltip) {
            tooltip.remove();
        }
    }
    
    initAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        }, observerOptions);
        
        const animateElements = document.querySelectorAll(
            '.content-section, .concept-card, .step-card, .technique-card, .model-card'
        );
        animateElements.forEach(el => observer.observe(el));
    }
    
    // Analysis Tool functionality
    initAnalysisTool() {
        this.setupFileUpload();
        this.setupSampleDataButtons();
        this.setupExportButtons();
    }
    
    setupFileUpload() {
        const uploadArea = document.getElementById('upload-area');
        const fileInput = document.getElementById('file-input');
        
        if (!uploadArea || !fileInput) return;
        
        uploadArea.addEventListener('click', () => {
            fileInput.click();
        });
        
        uploadArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadArea.classList.add('dragover');
        });
        
        uploadArea.addEventListener('dragleave', () => {
            uploadArea.classList.remove('dragover');
        });
        
        uploadArea.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadArea.classList.remove('dragover');
            
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
    
    handleFileUpload(file) {
        const allowedTypes = ['text/csv', 'application/json'];
        const maxSize = 50 * 1024 * 1024; // 50MB
        
        if (!allowedTypes.includes(file.type) && !file.name.endsWith('.csv')) {
            this.showUploadError('Tipo de arquivo não suportado. Use CSV ou JSON.');
            return;
        }
        
        if (file.size > maxSize) {
            this.showUploadError('Arquivo muito grande. Máximo: 50MB.');
            return;
        }
        
        this.showUploadProgress('Carregando arquivo...');
        
        const extension = this.getFileExtension(file.name).toLowerCase();
        
        if (extension === 'csv') {
            this.processCSVFile(file);
        } else if (extension === 'json') {
            this.processJSONFile(file);
        }
    }
    
    processCSVFile(file) {
        if (typeof Papa === 'undefined') {
            this.showUploadError('Biblioteca Papa Parse não carregada. Recarregue a página.');
            return;
        }
        
        Papa.parse(file, {
            complete: (results) => {
                if (results.errors.length > 0) {
                    console.error('CSV parsing errors:', results.errors);
                    this.showUploadError('Erro ao processar arquivo CSV.');
                    return;
                }
                
                this.currentDataset = {
                    name: file.name,
                    data: results.data,
                    headers: results.data[0] || [],
                    rows: results.data.slice(1)
                };
                
                this.displayDataPreview();
                this.showUploadSuccess(`Arquivo ${file.name} carregado com sucesso!`);
            },
            header: false,
            skipEmptyLines: true
        });
    }
    
    processJSONFile(file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const jsonData = JSON.parse(e.target.result);
                
                this.currentDataset = {
                    name: file.name,
                    data: jsonData,
                    headers: Object.keys(jsonData[0] || {}),
                    rows: jsonData
                };
                
                this.displayDataPreview();
                this.showUploadSuccess(`Arquivo ${file.name} carregado com sucesso!`);
            } catch (error) {
                this.showUploadError('Erro ao processar arquivo JSON. Verifique o formato.');
            }
        };
        reader.readAsText(file);
    }
    
    displayDataPreview() {
        const previewContainer = document.getElementById('data-preview');
        if (!previewContainer || !this.currentDataset) return;
        
        const { headers, rows } = this.currentDataset;
        const maxRows = 10;
        
        let html = `
            <div class="preview-header">
                <h3>Prévia dos Dados</h3>
                <p>Mostrando ${Math.min(maxRows, rows.length)} de ${rows.length} linhas</p>
            </div>
            <div class="table-container">
                <table class="data-table">
                    <thead>
                        <tr>
                            ${headers.map(header => `<th>${header}</th>`).join('')}
                        </tr>
                    </thead>
                    <tbody>
                        ${rows.slice(0, maxRows).map(row => 
                            `<tr>${headers.map((_, i) => `<td>${row[i] || ''}</td>`).join('')}</tr>`
                        ).join('')}
                    </tbody>
                </table>
            </div>
        `;
        
        previewContainer.innerHTML = html;
        previewContainer.style.display = 'block';
        
        // Generate basic statistics
        this.generateBasicStats();
    }
    
    generateBasicStats() {
        if (!this.currentDataset) return;
        
        const statsContainer = document.getElementById('basic-stats');
        if (!statsContainer) return;
        
        const { headers, rows } = this.currentDataset;
        const stats = {};
        
        headers.forEach((header, index) => {
            const column = rows.map(row => row[index]).filter(val => val !== null && val !== '');
            const numericData = column.filter(val => !isNaN(parseFloat(val))).map(val => parseFloat(val));
            
            stats[header] = {
                total: column.length,
                numeric: numericData.length,
                missing: rows.length - column.length,
                mean: numericData.length > 0 ? (numericData.reduce((a, b) => a + b, 0) / numericData.length).toFixed(2) : 'N/A',
                min: numericData.length > 0 ? Math.min(...numericData) : 'N/A',
                max: numericData.length > 0 ? Math.max(...numericData) : 'N/A'
            };
        });
        
        let html = `
            <div class="stats-header">
                <h3>Estatísticas Básicas</h3>
            </div>
            <div class="stats-grid">
                ${Object.entries(stats).map(([column, stat]) => `
                    <div class="stat-card">
                        <h4>${column}</h4>
                        <div class="stat-item">
                            <span class="stat-label">Total:</span>
                            <span class="stat-value">${stat.total}</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-label">Numéricos:</span>
                            <span class="stat-value">${stat.numeric}</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-label">Média:</span>
                            <span class="stat-value">${stat.mean}</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-label">Min/Max:</span>
                            <span class="stat-value">${stat.min}/${stat.max}</span>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
        
        statsContainer.innerHTML = html;
        statsContainer.style.display = 'block';
    }
    
    setupSampleDataButtons() {
        const sampleButtons = document.querySelectorAll('.sample-data-btn');
        sampleButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                const sampleType = btn.getAttribute('data-sample');
                this.loadSampleData(sampleType);
            });
        });
    }
    
    loadSampleData(type) {
        let sampleData;
        
        switch (type) {
            case 'vendas':
                sampleData = this.generateSalesData();
                break;
            case 'financeiro':
                sampleData = this.generateFinancialData();
                break;
            default:
                this.showNotification('Tipo de amostra não encontrado', 'error');
                return;
        }
        
        this.currentDataset = sampleData;
        this.displayDataPreview();
        this.showNotification(`Dados de exemplo "${type}" carregados com sucesso!`, 'success');
    }
    
    generateSalesData() {
        const headers = ['Data', 'Produto', 'Vendedor', 'Quantidade', 'Valor', 'Região'];
        const produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam'];
        const vendedores = ['Ana Silva', 'João Santos', 'Maria Costa', 'Pedro Lima'];
        const regioes = ['Norte', 'Sul', 'Leste', 'Oeste'];
        
        const rows = [];
        for (let i = 0; i < 100; i++) {
            const data = new Date(2024, Math.floor(Math.random() * 12), Math.floor(Math.random() * 28) + 1);
            rows.push([
                data.toLocaleDateString('pt-BR'),
                produtos[Math.floor(Math.random() * produtos.length)],
                vendedores[Math.floor(Math.random() * vendedores.length)],
                Math.floor(Math.random() * 10) + 1,
                (Math.random() * 1000 + 100).toFixed(2),
                regioes[Math.floor(Math.random() * regioes.length)]
            ]);
        }
        
        return {
            name: 'dados_vendas_exemplo.csv',
            data: [headers, ...rows],
            headers,
            rows
        };
    }
    
    generateFinancialData() {
        const headers = ['Data', 'Categoria', 'Tipo', 'Valor', 'Descrição'];
        const categorias = ['Alimentação', 'Transporte', 'Saúde', 'Educação', 'Lazer'];
        const tipos = ['Receita', 'Despesa'];
        
        const rows = [];
        for (let i = 0; i < 80; i++) {
            const data = new Date(2024, Math.floor(Math.random() * 12), Math.floor(Math.random() * 28) + 1);
            const tipo = tipos[Math.floor(Math.random() * tipos.length)];
            const valor = tipo === 'Receita' ? 
                (Math.random() * 5000 + 1000).toFixed(2) : 
                -(Math.random() * 500 + 50).toFixed(2);
            
            rows.push([
                data.toLocaleDateString('pt-BR'),
                categorias[Math.floor(Math.random() * categorias.length)],
                tipo,
                valor,
                `Transação ${tipo.toLowerCase()} ${i + 1}`
            ]);
        }
        
        return {
            name: 'dados_financeiros_exemplo.csv',
            data: [headers, ...rows],
            headers,
            rows
        };
    }
    
    setupExportButtons() {
        const exportBtn = document.getElementById('export-data');
        const exportResultsBtn = document.getElementById('export-results');
        
        if (exportBtn) {
            exportBtn.addEventListener('click', () => {
                this.exportData();
            });
        }
        
        if (exportResultsBtn) {
            exportResultsBtn.addEventListener('click', () => {
                this.exportResults();
            });
        }
    }
    
    exportData() {
        if (!this.currentDataset) {
            this.showNotification('Nenhum dado carregado para exportar', 'warning');
            return;
        }
        
        const csv = this.currentDataset.data.map(row => 
            row.map(cell => `"${cell}"`).join(',')
        ).join('\n');
        
        this.downloadFile(csv, `export_${Date.now()}.csv`, 'text/csv');
        this.showNotification('Dados exportados com sucesso!', 'success');
    }
    
    exportResults() {
        if (!this.currentDataset) {
            this.showNotification('Nenhum resultado para exportar', 'warning');
            return;
        }
        
        const results = {
            timestamp: new Date().toISOString(),
            dataset: this.currentDataset.name,
            summary: {
                total_rows: this.currentDataset.rows.length,
                total_columns: this.currentDataset.headers.length,
                columns: this.currentDataset.headers
            }
        };
        
        this.downloadFile(JSON.stringify(results, null, 2), `analysis_results_${Date.now()}.json`, 'application/json');
        this.showNotification('Resultados exportados com sucesso!', 'success');
    }
    
    // References functionality
    initReferences() {
        const searchInput = document.getElementById('ref-search');
        const categoryFilter = document.getElementById('category-filter');
        const referencesList = document.getElementById('references-list');
        
        if (!searchInput || !categoryFilter || !referencesList) return;
        
        this.references = this.getReferenceData();
        this.displayReferences(this.references, referencesList);
        
        const performSearch = () => {
            const searchTerm = searchInput.value.toLowerCase();
            const selectedCategory = categoryFilter.value;
            
            const filteredRefs = this.references.filter(ref => {
                const matchesSearch = !searchTerm || 
                    ref.title.toLowerCase().includes(searchTerm) ||
                    ref.description.toLowerCase().includes(searchTerm) ||
                    ref.authors.some(author => author.toLowerCase().includes(searchTerm));
                
                const matchesCategory = !selectedCategory || ref.category === selectedCategory;
                
                return matchesSearch && matchesCategory;
            });
            
            this.displayReferences(filteredRefs, referencesList);
        };
        
        searchInput.addEventListener('input', this.debounce(performSearch, 300));
        categoryFilter.addEventListener('change', performSearch);
    }
    
    getReferenceData() {
        return [
            {
                title: "Introduction to Statistical Learning",
                authors: ["Gareth James", "Daniela Witten", "Trevor Hastie", "Robert Tibshirani"],
                year: 2021,
                category: "machine-learning",
                description: "Um guia abrangente para aprendizado estatístico com aplicações em R e Python.",
                url: "https://www.statlearning.com/"
            },
            {
                title: "Python for Data Analysis",
                authors: ["Wes McKinney"],
                year: 2022,
                category: "python",
                description: "Análise de dados com pandas, NumPy e IPython.",
                url: "https://wesmckinney.com/book/"
            },
            {
                title: "The Elements of Statistical Learning",
                authors: ["Trevor Hastie", "Robert Tibshirani", "Jerome Friedman"],
                year: 2016,
                category: "estatistica",
                description: "Referência fundamental para mineração de dados, inferência e predição.",
                url: "https://hastie.su.stanford.edu/ElemStatLearn/"
            }
        ];
    }
    
    displayReferences(references, container) {
        if (references.length === 0) {
            container.innerHTML = '<p class="no-results">Nenhuma referência encontrada.</p>';
            return;
        }
        
        const html = references.map(ref => `
            <div class="reference-card">
                <div class="reference-header">
                    <h3 class="reference-title">${ref.title}</h3>
                    <span class="reference-year">${ref.year}</span>
                </div>
                <div class="reference-authors">
                    ${ref.authors.join(', ')}
                </div>
                <div class="reference-description">
                    ${ref.description}
                </div>
                <div class="reference-footer">
                    <span class="reference-category">${this.getCategoryName(ref.category)}</span>
                    ${ref.url ? `<a href="${ref.url}" target="_blank" class="reference-link">
                        <i class="fas fa-external-link-alt"></i> Acessar
                    </a>` : ''}
                </div>
            </div>
        `).join('');
        
        container.innerHTML = html;
    }
    
    getCategoryName(category) {
        const categories = {
            'machine-learning': 'Machine Learning',
            'python': 'Python',
            'estatistica': 'Estatística',
            'bigdata': 'Big Data',
            'visualization': 'Visualização'
        };
        return categories[category] || category;
    }
    
    // Utility methods
    showUploadProgress(message) {
        const statusEl = document.getElementById('upload-status');
        if (statusEl) {
            statusEl.innerHTML = `<div class="upload-progress">${message}</div>`;
            statusEl.style.display = 'block';
        }
    }
    
    showUploadSuccess(message) {
        const statusEl = document.getElementById('upload-status');
        if (statusEl) {
            statusEl.innerHTML = `<div class="upload-success">${message}</div>`;
            statusEl.style.display = 'block';
        }
        setTimeout(() => {
            if (statusEl) statusEl.style.display = 'none';
        }, 3000);
    }
    
    showUploadError(message) {
        const statusEl = document.getElementById('upload-status');
        if (statusEl) {
            statusEl.innerHTML = `<div class="upload-error">${message}</div>`;
            statusEl.style.display = 'block';
        }
    }
    
    getFileExtension(filename) {
        return filename.slice((filename.lastIndexOf(".") - 1 >>> 0) + 2);
    }
    
    formatNumber(num) {
        return new Intl.NumberFormat('pt-BR').format(num);
    }
    
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    downloadFile(content, filename, contentType = 'text/plain') {
        const blob = new Blob([content], { type: contentType });
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        window.URL.revokeObjectURL(url);
    }
    
    showNotification(message, type = 'info', duration = 5000) {
        // Remove any existing notifications
        const existingNotifications = document.querySelectorAll('.app-notification');
        existingNotifications.forEach(n => n.remove());
        
        const notification = document.createElement('div');
        notification.className = `app-notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <span class="notification-message">${message}</span>
                <button class="notification-close">&times;</button>
            </div>
        `;
        
        const colors = {
            success: '#22c55e',
            error: '#ef4444',
            warning: '#f59e0b',
            info: '#2563eb'
        };
        
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${colors[type] || colors.info};
            color: white;
            padding: 16px 20px;
            border-radius: 8px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            z-index: 10000;
            max-width: 400px;
            animation: slideInRight 0.3s ease-out;
        `;
        
        document.body.appendChild(notification);
        
        const closeBtn = notification.querySelector('.notification-close');
        closeBtn.addEventListener('click', () => {
            notification.remove();
        });
        
        setTimeout(() => {
            if (notification.parentNode) {
                notification.style.animation = 'slideOutRight 0.3s ease-in';
                setTimeout(() => notification.remove(), 300);
            }
        }, duration);
    }
}

// Initialize the application
const dataSciencePro = new DataSciencePro();

// Add required CSS animations
const appStyles = document.createElement('style');
appStyles.textContent = `
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOutRight {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
    
    .notification-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 12px;
    }
    
    .notification-close {
        background: none;
        border: none;
        color: white;
        font-size: 20px;
        cursor: pointer;
        padding: 0;
        width: 24px;
        height: 24px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        transition: background-color 0.2s;
    }
    
    .notification-close:hover {
        background-color: rgba(255, 255, 255, 0.2);
    }
    
    .custom-tooltip {
        position: absolute;
        background-color: #1a1a1a;
        color: white;
        padding: 8px 12px;
        border-radius: 6px;
        font-size: 14px;
        z-index: 10000;
        opacity: 0;
        transition: opacity 0.2s;
        pointer-events: none;
        white-space: nowrap;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .custom-tooltip.show {
        opacity: 1;
    }
    
    .custom-tooltip::after {
        content: '';
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%);
        border: 5px solid transparent;
        border-top-color: #1a1a1a;
    }
    
    .animate-in {
        animation: fadeInUp 0.6s ease-out;
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .upload-progress {
        color: #2563eb;
        font-weight: 500;
    }
    
    .upload-success {
        color: #22c55e;
        font-weight: 500;
    }
    
    .upload-error {
        color: #ef4444;
        font-weight: 500;
    }
    
    .dragover {
        border-color: #2563eb !important;
        background-color: rgba(37, 99, 235, 0.05) !important;
    }
`;

document.head.appendChild(appStyles);
