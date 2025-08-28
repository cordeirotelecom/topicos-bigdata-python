// Analysis Tool JavaScript - Advanced data analysis functionality
let currentDataset = null;
let analysisCharts = {};

// Initialize the analysis tool
function initializeAnalysisTool() {
    console.log('Initializing Analysis Tool...');
    
    setupFileUpload();
    setupSampleDataButtons();
    setupExportButtons();
    
    console.log('Analysis Tool initialized successfully!');
}

// Setup file upload functionality
function setupFileUpload() {
    const uploadArea = document.getElementById('upload-area');
    const fileInput = document.getElementById('file-input');
    const uploadStatus = document.getElementById('upload-status');
    
    if (!uploadArea || !fileInput) return;
    
    // Click to upload
    uploadArea.addEventListener('click', () => {
        fileInput.click();
    });
    
    // Drag and drop
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
            handleFileUpload(files[0]);
        }
    });
    
    // File input change
    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleFileUpload(e.target.files[0]);
        }
    });
}

// Handle file upload
function handleFileUpload(file) {
    const uploadStatus = document.getElementById('upload-status');
    const allowedTypes = ['text/csv', 'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/json'];
    const maxSize = 50 * 1024 * 1024; // 50MB
    
    // Validate file type
    if (!allowedTypes.includes(file.type) && !file.name.endsWith('.csv')) {
        showUploadError('Tipo de arquivo não suportado. Use CSV, Excel ou JSON.');
        return;
    }
    
    // Validate file size
    if (file.size > maxSize) {
        showUploadError('Arquivo muito grande. Máximo: 50MB.');
        return;
    }
    
    showUploadProgress('Carregando arquivo...');
    
    // Process file based on type
    const extension = Utils.getFileExtension(file.name).toLowerCase();
    
    if (extension === 'csv') {
        processCSVFile(file);
    } else if (extension === 'json') {
        processJSONFile(file);
    } else if (extension === 'xlsx' || extension === 'xls') {
        showUploadError('Arquivos Excel requerem conversão para CSV. Use a ferramenta de conversão ou salve como CSV.');
    } else {
        showUploadError('Formato de arquivo não reconhecido.');
    }
}

// Process CSV file
function processCSVFile(file) {
    Papa.parse(file, {
        complete: function(results) {
            if (results.errors.length > 0) {
                console.error('CSV parsing errors:', results.errors);
                showUploadError('Erro ao processar arquivo CSV. Verifique o formato.');
                return;
            }
            
            try {
                const dataset = processDataset(results.data, file.name);
                currentDataset = dataset;
                showUploadSuccess(`Arquivo carregado: ${file.name} (${dataset.rows} linhas, ${dataset.columns.length} colunas)`);
                displayAnalysis(dataset);
            } catch (error) {
                console.error('Data processing error:', error);
                showUploadError('Erro ao processar os dados. Verifique o formato do arquivo.');
            }
        },
        header: true,
        skipEmptyLines: true,
        dynamicTyping: true,
        encoding: 'UTF-8'
    });
}

// Process JSON file
function processJSONFile(file) {
    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const jsonData = JSON.parse(e.target.result);
            
            // Convert JSON to tabular format
            let data;
            if (Array.isArray(jsonData)) {
                data = jsonData;
            } else if (typeof jsonData === 'object' && jsonData !== null) {
                // If it's an object, try to find an array property
                const arrayKeys = Object.keys(jsonData).filter(key => Array.isArray(jsonData[key]));
                if (arrayKeys.length > 0) {
                    data = jsonData[arrayKeys[0]];
                } else {
                    data = [jsonData];
                }
            } else {
                throw new Error('Invalid JSON structure');
            }
            
            const dataset = processDataset(data, file.name);
            currentDataset = dataset;
            showUploadSuccess(`Arquivo carregado: ${file.name} (${dataset.rows} linhas, ${dataset.columns.length} colunas)`);
            displayAnalysis(dataset);
            
        } catch (error) {
            console.error('JSON parsing error:', error);
            showUploadError('Erro ao processar arquivo JSON. Verifique o formato.');
        }
    };
    reader.readAsText(file);
}

// Process dataset
function processDataset(rawData, filename) {
    if (!rawData || rawData.length === 0) {
        throw new Error('Dataset vazio');
    }
    
    // Get columns from first row
    const firstRow = rawData[0];
    const columns = Object.keys(firstRow);
    
    // Process data
    const processedData = rawData.map(row => {
        const processedRow = {};
        columns.forEach(col => {
            let value = row[col];
            
            // Handle different data types
            if (value === null || value === undefined || value === '') {
                processedRow[col] = null;
            } else if (typeof value === 'string') {
                // Try to convert to number
                const numValue = parseFloat(value.replace(',', '.'));
                processedRow[col] = !isNaN(numValue) ? numValue : value;
            } else {
                processedRow[col] = value;
            }
        });
        return processedRow;
    });
    
    // Analyze columns
    const columnAnalysis = {};
    columns.forEach(col => {
        const values = processedData.map(row => row[col]).filter(val => val !== null);
        const numericValues = values.filter(val => Utils.isNumeric(val));
        
        columnAnalysis[col] = {
            name: col,
            type: numericValues.length > values.length * 0.8 ? 'numeric' : 'categorical',
            total_count: processedData.length,
            valid_count: values.length,
            missing_count: processedData.length - values.length,
            unique_count: new Set(values).size,
            stats: Utils.calculateStats(values)
        };
    });
    
    return {
        filename: filename,
        rows: processedData.length,
        columns: columns,
        data: processedData,
        analysis: columnAnalysis
    };
}

// Display analysis results
function displayAnalysis(dataset) {
    // Show dashboard
    document.getElementById('analysis-dashboard').style.display = 'block';
    
    // Populate data overview
    populateDataOverview(dataset);
    
    // Populate statistical summary
    populateStatisticalSummary(dataset);
    
    // Populate data quality metrics
    populateDataQuality(dataset);
    
    // Generate correlation analysis
    generateCorrelationAnalysis(dataset);
    
    // Setup distribution analysis
    setupDistributionAnalysis(dataset);
    
    // Detect outliers
    detectAndDisplayOutliers(dataset);
    
    // Scroll to dashboard
    document.getElementById('analysis-dashboard').scrollIntoView({ behavior: 'smooth' });
}

// Populate data overview
function populateDataOverview(dataset) {
    const container = document.getElementById('data-overview');
    if (!container) return;
    
    const numericColumns = Object.values(dataset.analysis).filter(col => col.type === 'numeric').length;
    const categoricalColumns = Object.values(dataset.analysis).filter(col => col.type === 'categorical').length;
    const totalMissing = Object.values(dataset.analysis).reduce((sum, col) => sum + col.missing_count, 0);
    
    container.innerHTML = `
        <div class="overview-item">
            <div class="overview-value">${Utils.formatNumber(dataset.rows)}</div>
            <div class="overview-label">Linhas</div>
        </div>
        <div class="overview-item">
            <div class="overview-value">${dataset.columns.length}</div>
            <div class="overview-label">Colunas</div>
        </div>
        <div class="overview-item">
            <div class="overview-value">${numericColumns}</div>
            <div class="overview-label">Numéricas</div>
        </div>
        <div class="overview-item">
            <div class="overview-value">${categoricalColumns}</div>
            <div class="overview-label">Categóricas</div>
        </div>
        <div class="overview-item">
            <div class="overview-value">${Utils.formatNumber(totalMissing)}</div>
            <div class="overview-label">Valores Ausentes</div>
        </div>
        <div class="overview-item">
            <div class="overview-value">${Utils.formatFileSize(JSON.stringify(dataset.data).length)}</div>
            <div class="overview-label">Tamanho Estimado</div>
        </div>
    `;
}

// Populate statistical summary
function populateStatisticalSummary(dataset) {
    const container = document.getElementById('stats-container');
    if (!container) return;
    
    const numericColumns = Object.values(dataset.analysis).filter(col => col.type === 'numeric');
    
    if (numericColumns.length === 0) {
        container.innerHTML = '<p>Nenhuma variável numérica encontrada para análise estatística.</p>';
        return;
    }
    
    let tableHTML = `
        <table class="stats-table">
            <thead>
                <tr>
                    <th>Variável</th>
                    <th>Contagem</th>
                    <th>Média</th>
                    <th>Mediana</th>
                    <th>Desvio Padrão</th>
                    <th>Mínimo</th>
                    <th>Máximo</th>
                    <th>Ausentes</th>
                </tr>
            </thead>
            <tbody>
    `;
    
    numericColumns.forEach(col => {
        const stats = col.stats;
        tableHTML += `
            <tr>
                <td><strong>${col.name}</strong></td>
                <td>${Utils.formatNumber(stats.numeric_count)}</td>
                <td>${stats.mean !== null ? stats.mean.toFixed(2) : 'N/A'}</td>
                <td>${stats.median !== null ? stats.median.toFixed(2) : 'N/A'}</td>
                <td>${stats.std !== null ? stats.std.toFixed(2) : 'N/A'}</td>
                <td>${stats.min !== null ? stats.min.toFixed(2) : 'N/A'}</td>
                <td>${stats.max !== null ? stats.max.toFixed(2) : 'N/A'}</td>
                <td>${Utils.formatNumber(stats.missing)}</td>
            </tr>
        `;
    });
    
    tableHTML += '</tbody></table>';
    container.innerHTML = tableHTML;
}

// Populate data quality metrics
function populateDataQuality(dataset) {
    const container = document.getElementById('quality-metrics');
    if (!container) return;
    
    const totalCells = dataset.rows * dataset.columns.length;
    const totalMissing = Object.values(dataset.analysis).reduce((sum, col) => sum + col.missing_count, 0);
    const completenessPercent = ((totalCells - totalMissing) / totalCells * 100).toFixed(1);
    
    const duplicateRows = findDuplicateRows(dataset.data);
    const duplicatePercent = (duplicateRows / dataset.rows * 100).toFixed(1);
    
    let qualityClass = 'good';
    if (parseFloat(completenessPercent) < 90 || parseFloat(duplicatePercent) > 5) {
        qualityClass = 'warning';
    }
    if (parseFloat(completenessPercent) < 70 || parseFloat(duplicatePercent) > 15) {
        qualityClass = 'danger';
    }
    
    container.innerHTML = `
        <div class="quality-item ${qualityClass}">
            <div class="quality-label">Completude dos Dados</div>
            <div class="quality-value ${qualityClass}">${completenessPercent}%</div>
        </div>
        <div class="quality-item ${duplicatePercent > 5 ? 'warning' : 'good'}">
            <div class="quality-label">Linhas Duplicadas</div>
            <div class="quality-value ${duplicatePercent > 5 ? 'warning' : 'good'}">${duplicatePercent}%</div>
        </div>
        <div class="quality-item good">
            <div class="quality-label">Colunas Válidas</div>
            <div class="quality-value good">${dataset.columns.length}</div>
        </div>
        <div class="quality-item ${totalMissing > 0 ? 'warning' : 'good'}">
            <div class="quality-label">Valores Ausentes</div>
            <div class="quality-value ${totalMissing > 0 ? 'warning' : 'good'}">${Utils.formatNumber(totalMissing)}</div>
        </div>
    `;
}

// Find duplicate rows
function findDuplicateRows(data) {
    const seen = new Set();
    let duplicates = 0;
    
    data.forEach(row => {
        const rowString = JSON.stringify(row);
        if (seen.has(rowString)) {
            duplicates++;
        } else {
            seen.add(rowString);
        }
    });
    
    return duplicates;
}

// Generate correlation analysis
function generateCorrelationAnalysis(dataset) {
    const canvas = document.getElementById('correlation-heatmap');
    if (!canvas) return;
    
    const numericColumns = Object.values(dataset.analysis).filter(col => col.type === 'numeric');
    
    if (numericColumns.length < 2) {
        canvas.parentNode.innerHTML = '<p>Pelo menos 2 variáveis numéricas são necessárias para análise de correlação.</p>';
        return;
    }
    
    // Calculate correlation matrix
    const correlationMatrix = {};
    numericColumns.forEach(col1 => {
        correlationMatrix[col1.name] = {};
        numericColumns.forEach(col2 => {
            const values1 = dataset.data.map(row => row[col1.name]).filter(val => Utils.isNumeric(val));
            const values2 = dataset.data.map(row => row[col2.name]).filter(val => Utils.isNumeric(val));
            
            if (col1.name === col2.name) {
                correlationMatrix[col1.name][col2.name] = 1;
            } else {
                const correlation = Utils.calculateCorrelation(values1, values2);
                correlationMatrix[col1.name][col2.name] = correlation !== null ? correlation : 0;
            }
        });
    });
    
    // Create heatmap
    createCorrelationHeatmap(canvas, correlationMatrix, numericColumns.map(col => col.name));
}

// Create correlation heatmap
function createCorrelationHeatmap(canvas, correlationMatrix, columnNames) {
    const ctx = canvas.getContext('2d');
    
    // Destroy existing chart
    if (analysisCharts.correlation) {
        analysisCharts.correlation.destroy();
    }
    
    // Prepare data for Chart.js heatmap (we'll use a scatter plot as approximation)
    const dataPoints = [];
    const annotations = [];
    
    columnNames.forEach((col1, i) => {
        columnNames.forEach((col2, j) => {
            const correlation = correlationMatrix[col1][col2];
            const intensity = Math.abs(correlation);
            
            dataPoints.push({
                x: i,
                y: j,
                v: correlation
            });
            
            annotations.push({
                x: i,
                y: j,
                text: correlation.toFixed(2),
                color: intensity > 0.7 ? '#fff' : '#000'
            });
        });
    });
    
    // Since Chart.js doesn't have native heatmap, we'll create a matrix visualization
    canvas.width = Math.max(400, columnNames.length * 60);
    canvas.height = Math.max(400, columnNames.length * 60);
    
    const cellSize = Math.min(canvas.width / columnNames.length, canvas.height / columnNames.length);
    
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw heatmap
    columnNames.forEach((col1, i) => {
        columnNames.forEach((col2, j) => {
            const correlation = correlationMatrix[col1][col2];
            const intensity = Math.abs(correlation);
            
            // Color based on correlation strength and direction
            let color;
            if (correlation > 0) {
                color = `rgba(37, 99, 235, ${intensity})`;
            } else {
                color = `rgba(239, 68, 68, ${intensity})`;
            }
            
            ctx.fillStyle = color;
            ctx.fillRect(i * cellSize, j * cellSize, cellSize, cellSize);
            
            // Draw border
            ctx.strokeStyle = '#e2e8f0';
            ctx.strokeRect(i * cellSize, j * cellSize, cellSize, cellSize);
            
            // Draw correlation value
            ctx.fillStyle = intensity > 0.5 ? '#fff' : '#000';
            ctx.font = `${Math.max(10, cellSize / 6)}px Arial`;
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(
                correlation.toFixed(2),
                i * cellSize + cellSize / 2,
                j * cellSize + cellSize / 2
            );
        });
    });
    
    // Draw labels
    ctx.fillStyle = '#1e293b';
    ctx.font = `${Math.max(10, cellSize / 8)}px Arial`;
    ctx.textAlign = 'center';
    
    columnNames.forEach((col, i) => {
        // X-axis labels (bottom)
        ctx.save();
        ctx.translate(i * cellSize + cellSize / 2, canvas.height + 20);
        ctx.rotate(-Math.PI / 4);
        ctx.fillText(col.substring(0, 15) + (col.length > 15 ? '...' : ''), 0, 0);
        ctx.restore();
        
        // Y-axis labels (left)
        ctx.textAlign = 'right';
        ctx.fillText(
            col.substring(0, 15) + (col.length > 15 ? '...' : ''),
            -10,
            i * cellSize + cellSize / 2
        );
        ctx.textAlign = 'center';
    });
}

// Setup distribution analysis
function setupDistributionAnalysis(dataset) {
    const selector = document.getElementById('variable-selector');
    const canvas = document.getElementById('distribution-chart');
    
    if (!selector || !canvas) return;
    
    // Populate variable selector
    selector.innerHTML = '<option value="">Selecione uma variável</option>';
    
    Object.values(dataset.analysis).forEach(col => {
        const option = document.createElement('option');
        option.value = col.name;
        option.textContent = `${col.name} (${col.type})`;
        selector.appendChild(option);
    });
    
    // Handle variable selection
    selector.addEventListener('change', function() {
        const selectedVar = this.value;
        if (selectedVar) {
            createDistributionChart(canvas, dataset, selectedVar);
        }
    });
}

// Create distribution chart
function createDistributionChart(canvas, dataset, variableName) {
    const ctx = canvas.getContext('2d');
    
    // Destroy existing chart
    if (analysisCharts.distribution) {
        analysisCharts.distribution.destroy();
    }
    
    const columnInfo = dataset.analysis[variableName];
    const values = dataset.data.map(row => row[variableName]).filter(val => val !== null);
    
    if (columnInfo.type === 'numeric') {
        // Create histogram for numeric data
        const numericValues = values.filter(val => Utils.isNumeric(val)).map(val => parseFloat(val));
        
        if (numericValues.length === 0) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#64748b';
            ctx.font = '16px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('Nenhum valor numérico encontrado', canvas.width / 2, canvas.height / 2);
            return;
        }
        
        // Calculate bins
        const bins = Math.min(20, Math.ceil(Math.sqrt(numericValues.length)));
        const min = Math.min(...numericValues);
        const max = Math.max(...numericValues);
        const binSize = (max - min) / bins;
        
        const histogram = new Array(bins).fill(0);
        const binLabels = [];
        
        for (let i = 0; i < bins; i++) {
            const binStart = min + i * binSize;
            const binEnd = min + (i + 1) * binSize;
            binLabels.push(`${binStart.toFixed(1)}-${binEnd.toFixed(1)}`);
            
            numericValues.forEach(value => {
                if (value >= binStart && (value < binEnd || i === bins - 1)) {
                    histogram[i]++;
                }
            });
        }
        
        analysisCharts.distribution = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: binLabels,
                datasets: [{
                    label: 'Frequência',
                    data: histogram,
                    backgroundColor: 'rgba(37, 99, 235, 0.7)',
                    borderColor: 'rgba(37, 99, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: `Distribuição de ${variableName}`
                    },
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Frequência'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: variableName
                        }
                    }
                }
            }
        });
        
    } else {
        // Create bar chart for categorical data
        const valueCounts = {};
        values.forEach(value => {
            valueCounts[value] = (valueCounts[value] || 0) + 1;
        });
        
        // Sort by frequency and take top 20
        const sortedEntries = Object.entries(valueCounts)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 20);
        
        const labels = sortedEntries.map(entry => entry[0]);
        const data = sortedEntries.map(entry => entry[1]);
        
        analysisCharts.distribution = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Frequência',
                    data: data,
                    backgroundColor: 'rgba(16, 185, 129, 0.7)',
                    borderColor: 'rgba(16, 185, 129, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: `Distribuição de ${variableName} (Top 20)`
                    },
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Frequência'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: variableName
                        }
                    }
                }
            }
        });
    }
}

// Detect and display outliers
function detectAndDisplayOutliers(dataset) {
    const container = document.getElementById('outliers-container');
    if (!container) return;
    
    const numericColumns = Object.values(dataset.analysis).filter(col => col.type === 'numeric');
    
    if (numericColumns.length === 0) {
        container.innerHTML = '<p>Nenhuma variável numérica encontrada para detecção de outliers.</p>';
        return;
    }
    
    let outliersHTML = '<div class="outliers-grid">';
    
    numericColumns.forEach(col => {
        const values = dataset.data.map(row => row[col.name]).filter(val => Utils.isNumeric(val));
        const outliers = Utils.detectOutliers(values);
        
        const outlierClass = outliers.length > values.length * 0.05 ? 'warning' : 'good';
        
        outliersHTML += `
            <div class="quality-item ${outlierClass}">
                <div class="quality-label">${col.name}</div>
                <div class="quality-value ${outlierClass}">${outliers.length} outliers</div>
                <div style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 4px;">
                    ${(outliers.length / values.length * 100).toFixed(1)}% dos dados
                </div>
            </div>
        `;
    });
    
    outliersHTML += '</div>';
    
    if (numericColumns.some(col => {
        const values = dataset.data.map(row => row[col.name]).filter(val => Utils.isNumeric(val));
        return Utils.detectOutliers(values).length > 0;
    })) {
        outliersHTML += `
            <div style="margin-top: 1rem; padding: 1rem; background-color: var(--bg-secondary); border-radius: var(--border-radius);">
                <h5 style="margin-bottom: 0.5rem; color: var(--primary-color);">
                    <i class="fas fa-info-circle"></i> Sobre Outliers
                </h5>
                <p style="margin: 0; color: var(--text-secondary); font-size: 0.9rem;">
                    Outliers são detectados usando o método IQR (Interquartile Range). 
                    Valores fora do intervalo [Q1 - 1.5×IQR, Q3 + 1.5×IQR] são considerados outliers.
                    Mais de 5% de outliers pode indicar problemas na qualidade dos dados.
                </p>
            </div>
        `;
    }
    
    container.innerHTML = outliersHTML;
}

// Setup sample data buttons
function setupSampleDataButtons() {
    const sampleButtons = document.querySelectorAll('.sample-btn');
    
    sampleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const sampleType = this.getAttribute('data-sample');
            loadSampleData(sampleType);
        });
    });
}

// Load sample data
function loadSampleData(sampleType) {
    showUploadProgress('Carregando dados de exemplo...');
    
    let sampleData;
    let filename;
    
    switch (sampleType) {
        case 'covid':
            sampleData = generateCovidSampleData();
            filename = 'covid_sample_data.csv';
            break;
        case 'climate':
            sampleData = generateClimateSampleData();
            filename = 'climate_sample_data.csv';
            break;
        case 'sales':
            sampleData = generateSalesSampleData();
            filename = 'sales_sample_data.csv';
            break;
        default:
            showUploadError('Tipo de amostra não reconhecido.');
            return;
    }
    
    try {
        const dataset = processDataset(sampleData, filename);
        currentDataset = dataset;
        showUploadSuccess(`Dados de exemplo carregados: ${filename} (${dataset.rows} linhas, ${dataset.columns.length} colunas)`);
        displayAnalysis(dataset);
    } catch (error) {
        console.error('Sample data processing error:', error);
        showUploadError('Erro ao processar dados de exemplo.');
    }
}

// Generate COVID sample data
function generateCovidSampleData() {
    const data = [];
    const startDate = new Date('2020-03-01');
    
    for (let i = 0; i < 100; i++) {
        const date = new Date(startDate);
        date.setDate(startDate.getDate() + i);
        
        const baseValue = 50 + Math.sin(i * 0.1) * 30;
        
        data.push({
            Data: date.toISOString().split('T')[0],
            PM25: Math.max(5, baseValue + Math.random() * 20 - 10),
            PM10: Math.max(10, baseValue * 1.5 + Math.random() * 30 - 15),
            Temperatura: 20 + Math.sin(i * 0.05) * 10 + Math.random() * 4 - 2,
            Umidade: 60 + Math.cos(i * 0.08) * 20 + Math.random() * 10 - 5,
            Casos_Confirmados: Math.max(0, Math.floor(baseValue * 2 + Math.random() * 50 - 25)),
            Mortes: Math.max(0, Math.floor(baseValue * 0.05 + Math.random() * 3 - 1)),
            Isolamento: 50 + Math.sin(i * 0.03) * 30 + Math.random() * 10 - 5
        });
    }
    
    return data;
}

// Generate climate sample data
function generateClimateSampleData() {
    const data = [];
    const startDate = new Date('2023-01-01');
    
    for (let i = 0; i < 365; i++) {
        const date = new Date(startDate);
        date.setDate(startDate.getDate() + i);
        
        const dayOfYear = i;
        const seasonalTemp = 20 + 15 * Math.sin((dayOfYear - 80) * 2 * Math.PI / 365);
        
        data.push({
            Data: date.toISOString().split('T')[0],
            Temperatura_Max: seasonalTemp + Math.random() * 8 - 4,
            Temperatura_Min: seasonalTemp - 8 + Math.random() * 4 - 2,
            Precipitacao: Math.random() < 0.3 ? Math.random() * 50 : 0,
            Umidade: 60 + Math.random() * 30,
            Velocidade_Vento: 5 + Math.random() * 15,
            Pressao: 1013 + Math.random() * 20 - 10,
            Radiacao_Solar: Math.max(0, 200 + 100 * Math.sin(dayOfYear * 2 * Math.PI / 365) + Math.random() * 100 - 50)
        });
    }
    
    return data;
}

// Generate sales sample data
function generateSalesSampleData() {
    const data = [];
    const products = ['Produto_A', 'Produto_B', 'Produto_C', 'Produto_D', 'Produto_E'];
    const regions = ['Norte', 'Sul', 'Leste', 'Oeste', 'Centro'];
    const months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'];
    
    for (let i = 0; i < 200; i++) {
        const product = products[Math.floor(Math.random() * products.length)];
        const region = regions[Math.floor(Math.random() * regions.length)];
        const month = months[Math.floor(Math.random() * months.length)];
        
        const basePrice = 50 + Math.random() * 100;
        const quantity = Math.floor(10 + Math.random() * 90);
        
        data.push({
            Produto: product,
            Regiao: region,
            Mes: month,
            Quantidade: quantity,
            Preco_Unitario: parseFloat(basePrice.toFixed(2)),
            Receita: parseFloat((quantity * basePrice).toFixed(2)),
            Custo_Marketing: parseFloat((Math.random() * 1000).toFixed(2)),
            Taxa_Conversao: parseFloat((Math.random() * 10 + 2).toFixed(2))
        });
    }
    
    return data;
}

// Setup export buttons
function setupExportButtons() {
    const exportSummaryBtn = document.getElementById('export-summary');
    const exportProcessedBtn = document.getElementById('export-processed');
    
    if (exportSummaryBtn) {
        exportSummaryBtn.addEventListener('click', exportAnalysisSummary);
    }
    
    if (exportProcessedBtn) {
        exportProcessedBtn.addEventListener('click', exportProcessedData);
    }
}

// Export analysis summary
function exportAnalysisSummary() {
    if (!currentDataset) {
        Utils.showNotification('Nenhum dataset carregado para exportar.', 'warning');
        return;
    }
    
    const summary = generateAnalysisSummary(currentDataset);
    const timestamp = new Date().toISOString().slice(0, 19).replace(/:/g, '-');
    const filename = `analise_${currentDataset.filename.split('.')[0]}_${timestamp}.txt`;
    
    Utils.downloadFile(summary, filename, 'text/plain');
    Utils.showNotification('Relatório de análise exportado com sucesso!', 'success');
}

// Generate analysis summary
function generateAnalysisSummary(dataset) {
    let summary = `RELATÓRIO DE ANÁLISE DE DADOS\n`;
    summary += `=====================================\n\n`;
    summary += `Arquivo: ${dataset.filename}\n`;
    summary += `Data da Análise: ${new Date().toLocaleString('pt-BR')}\n`;
    summary += `Linhas: ${Utils.formatNumber(dataset.rows)}\n`;
    summary += `Colunas: ${dataset.columns.length}\n\n`;
    
    summary += `RESUMO ESTATÍSTICO\n`;
    summary += `------------------\n`;
    
    Object.values(dataset.analysis).forEach(col => {
        summary += `\n${col.name} (${col.type}):\n`;
        summary += `  Valores válidos: ${Utils.formatNumber(col.valid_count)}\n`;
        summary += `  Valores ausentes: ${Utils.formatNumber(col.missing_count)}\n`;
        summary += `  Valores únicos: ${Utils.formatNumber(col.unique_count)}\n`;
        
        if (col.type === 'numeric' && col.stats.mean !== null) {
            summary += `  Média: ${col.stats.mean.toFixed(4)}\n`;
            summary += `  Mediana: ${col.stats.median.toFixed(4)}\n`;
            summary += `  Desvio padrão: ${col.stats.std.toFixed(4)}\n`;
            summary += `  Mínimo: ${col.stats.min.toFixed(4)}\n`;
            summary += `  Máximo: ${col.stats.max.toFixed(4)}\n`;
            
            const values = dataset.data.map(row => row[col.name]).filter(val => Utils.isNumeric(val));
            const outliers = Utils.detectOutliers(values);
            summary += `  Outliers: ${outliers.length} (${(outliers.length / values.length * 100).toFixed(1)}%)\n`;
        }
    });
    
    // Quality metrics
    const totalCells = dataset.rows * dataset.columns.length;
    const totalMissing = Object.values(dataset.analysis).reduce((sum, col) => sum + col.missing_count, 0);
    const completenessPercent = ((totalCells - totalMissing) / totalCells * 100).toFixed(1);
    const duplicates = findDuplicateRows(dataset.data);
    
    summary += `\n\nQUALIDADE DOS DADOS\n`;
    summary += `-------------------\n`;
    summary += `Completude: ${completenessPercent}%\n`;
    summary += `Linhas duplicadas: ${duplicates} (${(duplicates / dataset.rows * 100).toFixed(1)}%)\n`;
    summary += `Total de valores ausentes: ${Utils.formatNumber(totalMissing)}\n`;
    
    summary += `\n\nCORRELAÇÕES (variáveis numéricas)\n`;
    summary += `--------------------------------\n`;
    
    const numericColumns = Object.values(dataset.analysis).filter(col => col.type === 'numeric');
    if (numericColumns.length >= 2) {
        numericColumns.forEach((col1, i) => {
            numericColumns.slice(i + 1).forEach(col2 => {
                const values1 = dataset.data.map(row => row[col1.name]).filter(val => Utils.isNumeric(val));
                const values2 = dataset.data.map(row => row[col2.name]).filter(val => Utils.isNumeric(val));
                const correlation = Utils.calculateCorrelation(values1, values2);
                
                if (correlation !== null) {
                    summary += `${col1.name} × ${col2.name}: ${correlation.toFixed(4)}\n`;
                }
            });
        });
    } else {
        summary += `Menos de 2 variáveis numéricas disponíveis.\n`;
    }
    
    summary += `\n\n=====================================\n`;
    summary += `Relatório gerado por DataScience Pro\n`;
    summary += `=====================================`;
    
    return summary;
}

// Export processed data
function exportProcessedData() {
    if (!currentDataset) {
        Utils.showNotification('Nenhum dataset carregado para exportar.', 'warning');
        return;
    }
    
    const csv = convertToCSV(currentDataset.data);
    const timestamp = new Date().toISOString().slice(0, 19).replace(/:/g, '-');
    const filename = `dados_processados_${currentDataset.filename.split('.')[0]}_${timestamp}.csv`;
    
    Utils.downloadFile(csv, filename, 'text/csv');
    Utils.showNotification('Dados processados exportados com sucesso!', 'success');
}

// Convert data to CSV
function convertToCSV(data) {
    if (!data || data.length === 0) return '';
    
    const headers = Object.keys(data[0]);
    const csvContent = [
        headers.join(','),
        ...data.map(row => 
            headers.map(header => {
                const value = row[header];
                if (value === null || value === undefined) return '';
                if (typeof value === 'string' && (value.includes(',') || value.includes('\n') || value.includes('"'))) {
                    return `"${value.replace(/"/g, '""')}"`;
                }
                return value;
            }).join(',')
        )
    ].join('\n');
    
    return csvContent;
}

// Upload status functions
function showUploadProgress(message) {
    const uploadStatus = document.getElementById('upload-status');
    if (uploadStatus) {
        uploadStatus.innerHTML = `<i class="fas fa-spinner fa-spin"></i> ${message}`;
        uploadStatus.className = 'upload-status';
        uploadStatus.style.display = 'block';
    }
}

function showUploadSuccess(message) {
    const uploadStatus = document.getElementById('upload-status');
    if (uploadStatus) {
        uploadStatus.innerHTML = `<i class="fas fa-check-circle"></i> ${message}`;
        uploadStatus.className = 'upload-status success';
        uploadStatus.style.display = 'block';
    }
}

function showUploadError(message) {
    const uploadStatus = document.getElementById('upload-status');
    if (uploadStatus) {
        uploadStatus.innerHTML = `<i class="fas fa-exclamation-circle"></i> ${message}`;
        uploadStatus.className = 'upload-status error';
        uploadStatus.style.display = 'block';
    }
}

// Make function available globally
window.initializeAnalysisTool = initializeAnalysisTool;
