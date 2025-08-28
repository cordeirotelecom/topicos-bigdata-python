// Sistema de Explicações de Algoritmos e Metodologias
class AlgorithmExplainerSystem {
    constructor() {
        this.explanations = {
            // Estatísticas Descritivas
            'descriptive': {
                name: 'Estatísticas Descritivas',
                icon: 'fas fa-chart-bar',
                category: 'Análise Estatística',
                description: 'Resumo básico dos dados usando medidas centrais e de dispersão',
                whatItDoes: 'Calcula médias, medianas, desvios-padrão e outras medidas básicas para entender a distribuição dos dados',
                whenToUse: 'Use quando quiser entender o comportamento geral dos seus dados, identificar valores típicos e variações',
                output: 'Tabelas com estatísticas resumidas, histogramas e box plots',
                example: 'Para dados de vendas: mostra a venda média mensal, o mês com maior venda, variação das vendas ao longo do tempo',
                difficulty: 'Iniciante',
                timeToRun: '1-2 minutos',
                benefits: [
                    'Rápido e fácil de interpretar',
                    'Base para análises mais complexas',
                    'Identifica outliers e padrões básicos'
                ],
                limitations: [
                    'Não mostra relações entre variáveis',
                    'Limitado para previsões',
                    'Pode mascarar padrões complexos'
                ]
            },
            
            'correlation': {
                name: 'Análise de Correlação',
                icon: 'fas fa-link',
                category: 'Análise Estatística',
                description: 'Mede a força e direção da relação linear entre duas ou mais variáveis',
                whatItDoes: 'Calcula coeficientes de correlação (Pearson, Spearman) para identificar se variáveis se movem juntas',
                whenToUse: 'Quando quiser descobrir se existe relação entre fatores (ex: vendas vs publicidade)',
                output: 'Matriz de correlação, gráficos de dispersão, heatmaps',
                example: 'Descobrir se aumento de temperatura correlaciona com aumento de vendas de sorvete',
                difficulty: 'Iniciante',
                timeToRun: '2-3 minutos',
                benefits: [
                    'Identifica relações ocultas entre variáveis',
                    'Ajuda na seleção de features para ML',
                    'Fácil de visualizar e interpretar'
                ],
                limitations: [
                    'Só detecta relações lineares',
                    'Correlação não implica causalidade',
                    'Sensível a outliers'
                ]
            },
            
            'distribution': {
                name: 'Análise de Distribuição',
                icon: 'fas fa-bell-curve',
                category: 'Análise Estatística',
                description: 'Examina como os valores estão distribuídos nos dados',
                whatItDoes: 'Identifica se os dados seguem distribuições conhecidas (normal, uniforme, etc.)',
                whenToUse: 'Para entender a forma dos dados e escolher técnicas estatísticas apropriadas',
                output: 'Histogramas, gráficos Q-Q, testes de normalidade',
                example: 'Verificar se salários dos funcionários seguem distribuição normal ou são enviesados',
                difficulty: 'Intermediário',
                timeToRun: '3-5 minutos',
                benefits: [
                    'Base para escolha de testes estatísticos',
                    'Identifica assimetrias nos dados',
                    'Detecta múltiplas populações'
                ],
                limitations: [
                    'Requer conhecimento de estatística',
                    'Interpretação pode ser complexa',
                    'Limitado para dados categóricos'
                ]
            },
            
            // Previsões
            'time-series': {
                name: 'Análise de Série Temporal',
                icon: 'fas fa-chart-line',
                category: 'Previsão',
                description: 'Analisa dados ordenados no tempo para identificar tendências e fazer previsões',
                whatItDoes: 'Identifica tendências, sazonalidade e ciclos em dados temporais para prever valores futuros',
                whenToUse: 'Para dados com componente temporal (vendas mensais, visitantes diários, etc.)',
                output: 'Gráficos de tendência, previsões futuras, decomposição sazonal',
                example: 'Prever vendas do próximo trimestre baseado no histórico de vendas mensais',
                difficulty: 'Intermediário',
                timeToRun: '5-10 minutos',
                benefits: [
                    'Previsões baseadas em padrões históricos',
                    'Identifica sazonalidade',
                    'Útil para planejamento'
                ],
                limitations: [
                    'Assume que padrões passados continuarão',
                    'Sensível a mudanças estruturais',
                    'Requer dados históricos suficientes'
                ]
            },
            
            'regression': {
                name: 'Regressão Linear',
                icon: 'fas fa-line-chart',
                category: 'Previsão',
                description: 'Modela relação linear entre variáveis para fazer previsões',
                whatItDoes: 'Encontra a melhor linha que descreve a relação entre variáveis independentes e dependente',
                whenToUse: 'Quando quer prever um valor contínuo baseado em outros fatores',
                output: 'Equação da reta, R², gráficos de resíduos, previsões',
                example: 'Prever preço de casa baseado em área, localização e idade da construção',
                difficulty: 'Intermediário',
                timeToRun: '3-7 minutos',
                benefits: [
                    'Interpretação clara dos coeficientes',
                    'Rápido de calcular',
                    'Base para modelos mais complexos'
                ],
                limitations: [
                    'Assume relação linear',
                    'Sensível a outliers',
                    'Limitado para relações complexas'
                ]
            },
            
            'trend': {
                name: 'Análise de Tendências',
                icon: 'fas fa-trending-up',
                category: 'Previsão',
                description: 'Identifica direção e magnitude de mudanças ao longo do tempo',
                whatItDoes: 'Detecta se uma variável está aumentando, diminuindo ou permanecendo estável',
                whenToUse: 'Para identificar padrões de crescimento ou declínio em séries temporais',
                output: 'Gráficos de tendência, taxa de crescimento, pontos de inflexão',
                example: 'Identificar se vendas online estão crescendo e a que taxa',
                difficulty: 'Iniciante',
                timeToRun: '2-4 minutos',
                benefits: [
                    'Fácil de interpretar',
                    'Útil para tomada de decisões',
                    'Identifica mudanças de direção'
                ],
                limitations: [
                    'Pode ser influenciado por outliers',
                    'Não considera fatores externos',
                    'Limitado para tendências não-lineares'
                ]
            },
            
            // Machine Learning
            'clustering': {
                name: 'Agrupamento (Clustering)',
                icon: 'fas fa-object-group',
                category: 'Machine Learning',
                description: 'Agrupa dados similares automaticamente sem supervisão prévia',
                whatItDoes: 'Identifica grupos naturais nos dados baseado em similaridades',
                whenToUse: 'Para segmentar clientes, agrupar produtos similares ou identificar padrões ocultos',
                output: 'Grupos identificados, gráficos de clusters, perfis dos grupos',
                example: 'Segmentar clientes em grupos (jovens urbanos, famílias tradicionais, etc.)',
                difficulty: 'Intermediário',
                timeToRun: '5-15 minutos',
                benefits: [
                    'Descobre padrões não óbvios',
                    'Não precisa de dados rotulados',
                    'Útil para segmentação'
                ],
                limitations: [
                    'Número de clusters pode ser subjetivo',
                    'Sensível à escala dos dados',
                    'Interpretação pode ser desafiadora'
                ]
            },
            
            'classification': {
                name: 'Classificação',
                icon: 'fas fa-tags',
                category: 'Machine Learning',
                description: 'Prevê categoria ou classe de novos dados baseado em exemplos',
                whatItDoes: 'Aprende padrões de dados rotulados para classificar novos casos',
                whenToUse: 'Para categorizar emails (spam/não-spam), prever aprovação de crédito, diagnósticos',
                output: 'Modelo treinado, acurácia, matriz de confusão, previsões',
                example: 'Classificar emails como spam ou legítimos baseado no conteúdo',
                difficulty: 'Avançado',
                timeToRun: '10-30 minutos',
                benefits: [
                    'Alta acurácia para dados categóricos',
                    'Automatiza decisões complexas',
                    'Escalável para grandes volumes'
                ],
                limitations: [
                    'Precisa de dados rotulados',
                    'Pode ser "caixa preta"',
                    'Requer validação cuidadosa'
                ]
            },
            
            'anomaly': {
                name: 'Detecção de Anomalias',
                icon: 'fas fa-exclamation-triangle',
                category: 'Machine Learning',
                description: 'Identifica pontos de dados que diferem significativamente do padrão normal',
                whatItDoes: 'Detecta automaticamente valores atípicos, fraudes ou comportamentos anômalos',
                whenToUse: 'Para detectar fraudes, falhas em equipamentos, comportamentos suspeitos',
                output: 'Pontos anômalos identificados, score de anomalia, alertas',
                example: 'Detectar transações fraudulentas em cartão de crédito',
                difficulty: 'Avançado',
                timeToRun: '7-20 minutos',
                benefits: [
                    'Detecta problemas automaticamente',
                    'Funciona em tempo real',
                    'Reduz riscos e perdas'
                ],
                limitations: [
                    'Pode gerar falsos positivos',
                    'Definir "normal" pode ser subjetivo',
                    'Requer ajuste fino'
                ]
            },
            
            // Análises Comparativas
            'comparison': {
                name: 'Comparação entre Datasets',
                icon: 'fas fa-balance-scale',
                category: 'Análise Comparativa',
                description: 'Compara múltiplos conjuntos de dados para identificar diferenças e similaridades',
                whatItDoes: 'Analisa diferenças estatísticas entre grupos ou períodos diferentes',
                whenToUse: 'Para comparar performance entre regiões, períodos ou grupos',
                output: 'Testes estatísticos, gráficos comparativos, métricas de diferença',
                example: 'Comparar vendas antes e depois de uma campanha publicitária',
                difficulty: 'Intermediário',
                timeToRun: '5-10 minutos',
                benefits: [
                    'Identifica diferenças significativas',
                    'Base para tomada de decisões',
                    'Valida hipóteses de negócio'
                ],
                limitations: [
                    'Requer dados comparáveis',
                    'Pode ser afetado por fatores externos',
                    'Interpretação requer cuidado'
                ]
            },
            
            'benchmarking': {
                name: 'Benchmarking',
                icon: 'fas fa-trophy',
                category: 'Análise Comparativa',
                description: 'Compara performance com padrões de referência ou concorrentes',
                whatItDoes: 'Avalia performance relativa usando métricas de mercado ou melhores práticas',
                whenToUse: 'Para avaliar posição competitiva ou medir contra padrões da indústria',
                output: 'Rankings, gaps de performance, oportunidades de melhoria',
                example: 'Comparar eficiência operacional com média da indústria',
                difficulty: 'Intermediário',
                timeToRun: '8-15 minutos',
                benefits: [
                    'Identifica gaps de performance',
                    'Estabelece metas realistas',
                    'Orienta melhorias'
                ],
                limitations: [
                    'Requer dados de benchmark confiáveis',
                    'Contexto pode ser diferente',
                    'Pode desencorajar inovação'
                ]
            },
            
            'geographic': {
                name: 'Análise Geográfica',
                icon: 'fas fa-map-marked-alt',
                category: 'Análise Comparativa',
                description: 'Analisa padrões espaciais e relações geográficas nos dados',
                whatItDoes: 'Identifica padrões baseados em localização e proximidade geográfica',
                whenToUse: 'Para análise de vendas por região, planejamento logístico, análise demográfica',
                output: 'Mapas de calor, clusters geográficos, análise de densidade',
                example: 'Identificar regiões com maior potencial de vendas para expansion',
                difficulty: 'Avançado',
                timeToRun: '10-25 minutos',
                benefits: [
                    'Visualização intuitiva',
                    'Identifica oportunidades regionais',
                    'Suporta decisões de localização'
                ],
                limitations: [
                    'Requer dados de localização',
                    'Pode ser computacionalmente intensivo',
                    'Privacidade pode ser preocupação'
                ]
            }
        };
        
        this.init();
    }
    
    init() {
        this.createExplainerInterface();
        this.setupEventListeners();
    }
    
    createExplainerInterface() {
        // Criar modal para explicações
        const modalHTML = `
            <div id="algorithm-explainer-modal" class="explainer-modal" style="display: none;">
                <div class="modal-overlay" onclick="algorithmExplainer.closeModal()"></div>
                <div class="modal-container">
                    <div class="modal-header">
                        <h2 id="explainer-title">
                            <i id="explainer-icon"></i>
                            <span id="explainer-name"></span>
                        </h2>
                        <div class="modal-meta">
                            <span id="explainer-category" class="category-badge"></span>
                            <span id="explainer-difficulty" class="difficulty-badge"></span>
                            <span id="explainer-time" class="time-badge">
                                <i class="fas fa-clock"></i>
                                <span id="explainer-duration"></span>
                            </span>
                        </div>
                        <button class="modal-close" onclick="algorithmExplainer.closeModal()">
                            <i class="fas fa-times"></i>
                        </button>
                    </div>
                    
                    <div class="modal-body">
                        <div class="explainer-sections">
                            <div class="explainer-section">
                                <h3><i class="fas fa-info-circle"></i> O que é?</h3>
                                <p id="explainer-description"></p>
                            </div>
                            
                            <div class="explainer-section">
                                <h3><i class="fas fa-cogs"></i> Como Funciona?</h3>
                                <p id="explainer-how"></p>
                            </div>
                            
                            <div class="explainer-section">
                                <h3><i class="fas fa-lightbulb"></i> Quando Usar?</h3>
                                <p id="explainer-when"></p>
                            </div>
                            
                            <div class="explainer-section">
                                <h3><i class="fas fa-chart-pie"></i> O que Você Vai Receber?</h3>
                                <p id="explainer-output"></p>
                            </div>
                            
                            <div class="explainer-section">
                                <h3><i class="fas fa-example"></i> Exemplo Prático</h3>
                                <div class="example-box">
                                    <p id="explainer-example"></p>
                                </div>
                            </div>
                            
                            <div class="explainer-pros-cons">
                                <div class="pros-section">
                                    <h3><i class="fas fa-thumbs-up"></i> Vantagens</h3>
                                    <ul id="explainer-benefits"></ul>
                                </div>
                                
                                <div class="cons-section">
                                    <h3><i class="fas fa-exclamation-triangle"></i> Limitações</h3>
                                    <ul id="explainer-limitations"></ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="modal-footer">
                        <button class="btn-secondary" onclick="algorithmExplainer.closeModal()">
                            Entendi
                        </button>
                        <button class="btn-primary" onclick="algorithmExplainer.selectAlgorithm()">
                            <i class="fas fa-check"></i>
                            Usar Este Algoritmo
                        </button>
                    </div>
                </div>
            </div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', modalHTML);
        
        // Adicionar estilos
        this.addStyles();
    }
    
    setupEventListeners() {
        // Adicionar botões de explicação aos checkboxes de análise
        document.addEventListener('DOMContentLoaded', () => {
            setTimeout(() => {
                this.addExplainerButtons();
            }, 1000);
        });
        
        // Escutar mudanças nos checkboxes
        document.addEventListener('change', (e) => {
            if (e.target.name === 'analysis-type') {
                this.updateSelectedAnalyses();
            }
        });
    }
    
    addExplainerButtons() {
        const checkboxes = document.querySelectorAll('input[name="analysis-type"]');
        
        checkboxes.forEach(checkbox => {
            const value = checkbox.value;
            if (this.explanations[value]) {
                const label = checkbox.closest('.tag-checkbox');
                if (label && !label.querySelector('.explainer-button')) {
                    const button = document.createElement('button');
                    button.className = 'explainer-button';
                    button.innerHTML = '<i class="fas fa-question-circle"></i>';
                    button.title = 'Clique para entender este algoritmo';
                    button.onclick = (e) => {
                        e.preventDefault();
                        e.stopPropagation();
                        this.showExplanation(value);
                    };
                    
                    label.appendChild(button);
                }
            }
        });
    }
    
    showExplanation(algorithmKey) {
        const explanation = this.explanations[algorithmKey];
        if (!explanation) return;
        
        // Preencher modal com dados do algoritmo
        document.getElementById('explainer-icon').className = explanation.icon;
        document.getElementById('explainer-name').textContent = explanation.name;
        document.getElementById('explainer-category').textContent = explanation.category;
        document.getElementById('explainer-difficulty').textContent = explanation.difficulty;
        document.getElementById('explainer-difficulty').className = `difficulty-badge ${explanation.difficulty.toLowerCase()}`;
        document.getElementById('explainer-duration').textContent = explanation.timeToRun;
        
        document.getElementById('explainer-description').textContent = explanation.description;
        document.getElementById('explainer-how').textContent = explanation.whatItDoes;
        document.getElementById('explainer-when').textContent = explanation.whenToUse;
        document.getElementById('explainer-output').textContent = explanation.output;
        document.getElementById('explainer-example').textContent = explanation.example;
        
        // Preencher vantagens
        const benefitsList = document.getElementById('explainer-benefits');
        benefitsList.innerHTML = '';
        explanation.benefits.forEach(benefit => {
            const li = document.createElement('li');
            li.textContent = benefit;
            benefitsList.appendChild(li);
        });
        
        // Preencher limitações
        const limitationsList = document.getElementById('explainer-limitations');
        limitationsList.innerHTML = '';
        explanation.limitations.forEach(limitation => {
            const li = document.createElement('li');
            li.textContent = limitation;
            limitationsList.appendChild(li);
        });
        
        // Salvar algoritmo atual
        this.currentAlgorithm = algorithmKey;
        
        // Mostrar modal
        document.getElementById('algorithm-explainer-modal').style.display = 'block';
        document.body.style.overflow = 'hidden';
    }
    
    closeModal() {
        document.getElementById('algorithm-explainer-modal').style.display = 'none';
        document.body.style.overflow = 'auto';
    }
    
    selectAlgorithm() {
        if (this.currentAlgorithm) {
            // Marcar o checkbox correspondente
            const checkbox = document.querySelector(`input[value="${this.currentAlgorithm}"]`);
            if (checkbox) {
                checkbox.checked = true;
                checkbox.dispatchEvent(new Event('change', { bubbles: true }));
            }
            
            this.showNotification(`✅ ${this.explanations[this.currentAlgorithm].name} adicionado à sua análise!`, 'success');
        }
        
        this.closeModal();
    }
    
    updateSelectedAnalyses() {
        const selected = Array.from(document.querySelectorAll('input[name="analysis-type"]:checked'))
            .map(cb => cb.value);
        
        if (selected.length > 0) {
            this.showAnalysisPreview(selected);
        }
    }
    
    showAnalysisPreview(selectedAnalyses) {
        // Criar ou atualizar preview das análises selecionadas
        let previewContainer = document.getElementById('analysis-preview');
        
        if (!previewContainer) {
            previewContainer = document.createElement('div');
            previewContainer.id = 'analysis-preview';
            previewContainer.className = 'analysis-preview';
            
            const tagsPanel = document.getElementById('analysis-tags-panel');
            if (tagsPanel) {
                tagsPanel.appendChild(previewContainer);
            }
        }
        
        if (selectedAnalyses.length === 0) {
            previewContainer.style.display = 'none';
            return;
        }
        
        previewContainer.style.display = 'block';
        
        const totalTime = selectedAnalyses.reduce((total, key) => {
            const explanation = this.explanations[key];
            if (explanation) {
                const timeStr = explanation.timeToRun;
                const maxTime = parseInt(timeStr.split('-')[1] || timeStr.split(' ')[0]);
                return total + maxTime;
            }
            return total;
        }, 0);
        
        const categories = [...new Set(selectedAnalyses.map(key => 
            this.explanations[key]?.category).filter(Boolean))];
        
        previewContainer.innerHTML = `
            <div class="preview-header">
                <h4><i class="fas fa-eye"></i> Preview da Análise</h4>
            </div>
            <div class="preview-stats">
                <div class="stat">
                    <i class="fas fa-list"></i>
                    <span>${selectedAnalyses.length} algoritmos selecionados</span>
                </div>
                <div class="stat">
                    <i class="fas fa-clock"></i>
                    <span>~${totalTime} minutos estimados</span>
                </div>
                <div class="stat">
                    <i class="fas fa-tags"></i>
                    <span>${categories.join(', ')}</span>
                </div>
            </div>
            <div class="preview-algorithms">
                ${selectedAnalyses.map(key => {
                    const explanation = this.explanations[key];
                    return `
                        <div class="preview-algorithm">
                            <i class="${explanation.icon}"></i>
                            <span>${explanation.name}</span>
                            <small>${explanation.difficulty}</small>
                        </div>
                    `;
                }).join('')}
            </div>
            <div class="preview-actions">
                <button class="btn-preview-clear" onclick="algorithmExplainer.clearAllSelections()">
                    <i class="fas fa-times"></i>
                    Limpar Tudo
                </button>
                <button class="btn-preview-recommend" onclick="algorithmExplainer.showRecommendations()">
                    <i class="fas fa-magic"></i>
                    Recomendar Mais
                </button>
            </div>
        `;
    }
    
    clearAllSelections() {
        const checkboxes = document.querySelectorAll('input[name="analysis-type"]');
        checkboxes.forEach(cb => {
            cb.checked = false;
        });
        
        const preview = document.getElementById('analysis-preview');
        if (preview) {
            preview.style.display = 'none';
        }
        
        this.showNotification('Seleções limpas', 'info');
    }
    
    showRecommendations() {
        const selected = Array.from(document.querySelectorAll('input[name="analysis-type"]:checked'))
            .map(cb => cb.value);
        
        // Lógica de recomendação baseada no que já foi selecionado
        const recommendations = this.getRecommendations(selected);
        
        if (recommendations.length === 0) {
            this.showNotification('Você já selecionou uma boa combinação de análises!', 'success');
            return;
        }
        
        // Mostrar modal de recomendações
        this.showRecommendationsModal(recommendations);
    }
    
    getRecommendations(selectedAnalyses) {
        const recommendations = [];
        
        // Se selecionou correlação, recomendar regressão
        if (selectedAnalyses.includes('correlation') && !selectedAnalyses.includes('regression')) {
            recommendations.push('regression');
        }
        
        // Se selecionou análises estatísticas, recomendar clustering
        if (selectedAnalyses.some(a => ['descriptive', 'correlation', 'distribution'].includes(a)) && 
            !selectedAnalyses.includes('clustering')) {
            recommendations.push('clustering');
        }
        
        // Se selecionou dados temporais, recomendar trend
        if (selectedAnalyses.includes('time-series') && !selectedAnalyses.includes('trend')) {
            recommendations.push('trend');
        }
        
        // Se selecionou muitas análises, recomendar detecção de anomalias
        if (selectedAnalyses.length >= 3 && !selectedAnalyses.includes('anomaly')) {
            recommendations.push('anomaly');
        }
        
        return recommendations.filter(rec => this.explanations[rec]);
    }
    
    showRecommendationsModal(recommendations) {
        const modal = document.createElement('div');
        modal.className = 'recommendations-modal';
        modal.innerHTML = `
            <div class="modal-overlay" onclick="this.parentElement.remove()"></div>
            <div class="modal-container">
                <div class="modal-header">
                    <h3><i class="fas fa-magic"></i> Recomendações Inteligentes</h3>
                    <p>Baseado na sua seleção, estas análises podem fornecer insights adicionais:</p>
                </div>
                <div class="recommendations-list">
                    ${recommendations.map(key => {
                        const explanation = this.explanations[key];
                        return `
                            <div class="recommendation-item" data-algorithm="${key}">
                                <div class="rec-icon">
                                    <i class="${explanation.icon}"></i>
                                </div>
                                <div class="rec-info">
                                    <h4>${explanation.name}</h4>
                                    <p>${explanation.description}</p>
                                    <small><strong>Por que:</strong> ${this.getRecommendationReason(key)}</small>
                                </div>
                                <div class="rec-action">
                                    <button class="btn-add-recommendation" onclick="algorithmExplainer.addRecommendation('${key}')">
                                        <i class="fas fa-plus"></i>
                                        Adicionar
                                    </button>
                                </div>
                            </div>
                        `;
                    }).join('')}
                </div>
                <div class="modal-footer">
                    <button class="btn-secondary" onclick="this.closest('.recommendations-modal').remove()">
                        Fechar
                    </button>
                    <button class="btn-primary" onclick="algorithmExplainer.addAllRecommendations(['${recommendations.join("','")}'])">
                        <i class="fas fa-check-double"></i>
                        Adicionar Todas
                    </button>
                </div>
            </div>
        `;
        
        document.body.appendChild(modal);
    }
    
    getRecommendationReason(algorithmKey) {
        const reasons = {
            'regression': 'Complementa a análise de correlação permitindo fazer previsões quantitativas',
            'clustering': 'Revela padrões ocultos que as estatísticas básicas podem não mostrar',
            'trend': 'Complementa a análise temporal identificando direções de mudança',
            'anomaly': 'Com múltiplas análises, é importante identificar dados atípicos que podem afetar resultados',
            'classification': 'Permite categorizar novos dados baseado nos padrões encontrados',
            'comparison': 'Ajuda a validar descobertas comparando diferentes grupos ou períodos'
        };
        
        return reasons[algorithmKey] || 'Fornece insights complementares à sua análise atual';
    }
    
    addRecommendation(algorithmKey) {
        const checkbox = document.querySelector(`input[value="${algorithmKey}"]`);
        if (checkbox) {
            checkbox.checked = true;
            checkbox.dispatchEvent(new Event('change', { bubbles: true }));
            
            this.showNotification(`✅ ${this.explanations[algorithmKey].name} adicionado!`, 'success');
        }
    }
    
    addAllRecommendations(algorithms) {
        let added = 0;
        algorithms.forEach(algorithmKey => {
            const checkbox = document.querySelector(`input[value="${algorithmKey}"]`);
            if (checkbox && !checkbox.checked) {
                checkbox.checked = true;
                added++;
            }
        });
        
        if (added > 0) {
            document.querySelector('input[name="analysis-type"]').dispatchEvent(new Event('change', { bubbles: true }));
            this.showNotification(`✅ ${added} análises adicionadas!`, 'success');
        }
        
        document.querySelector('.recommendations-modal').remove();
    }
    
    addStyles() {
        const styles = `
            <style>
                /* Explainer Button */
                .explainer-button {
                    position: absolute;
                    right: 8px;
                    top: 50%;
                    transform: translateY(-50%);
                    width: 20px;
                    height: 20px;
                    border: none;
                    border-radius: 50%;
                    background: #3b82f6;
                    color: white;
                    font-size: 10px;
                    cursor: pointer;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    transition: all 0.2s ease;
                    z-index: 10;
                }
                
                .explainer-button:hover {
                    background: #2563eb;
                    transform: translateY(-50%) scale(1.1);
                }
                
                .tag-checkbox {
                    position: relative;
                }
                
                /* Modal Styles */
                .explainer-modal {
                    position: fixed;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    z-index: 1000;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 20px;
                }
                
                .modal-overlay {
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background: rgba(0, 0, 0, 0.6);
                    backdrop-filter: blur(4px);
                }
                
                .modal-container {
                    position: relative;
                    background: white;
                    border-radius: 16px;
                    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                    max-width: 800px;
                    width: 100%;
                    max-height: 90vh;
                    overflow-y: auto;
                    animation: modalSlideIn 0.3s ease;
                }
                
                @keyframes modalSlideIn {
                    from {
                        opacity: 0;
                        transform: scale(0.9) translateY(20px);
                    }
                    to {
                        opacity: 1;
                        transform: scale(1) translateY(0);
                    }
                }
                
                .modal-header {
                    padding: 32px 32px 24px;
                    border-bottom: 1px solid #e2e8f0;
                    position: relative;
                }
                
                .modal-header h2 {
                    display: flex;
                    align-items: center;
                    gap: 12px;
                    margin-bottom: 16px;
                    color: #1e293b;
                    font-size: 24px;
                }
                
                .modal-meta {
                    display: flex;
                    gap: 12px;
                    align-items: center;
                    flex-wrap: wrap;
                }
                
                .category-badge,
                .difficulty-badge,
                .time-badge {
                    padding: 4px 12px;
                    border-radius: 12px;
                    font-size: 12px;
                    font-weight: 500;
                    display: flex;
                    align-items: center;
                    gap: 4px;
                }
                
                .category-badge {
                    background: #dbeafe;
                    color: #1d4ed8;
                }
                
                .difficulty-badge.iniciante {
                    background: #dcfce7;
                    color: #166534;
                }
                
                .difficulty-badge.intermediário {
                    background: #fef3c7;
                    color: #92400e;
                }
                
                .difficulty-badge.avançado {
                    background: #fee2e2;
                    color: #991b1b;
                }
                
                .time-badge {
                    background: #f3f4f6;
                    color: #374151;
                }
                
                .modal-close {
                    position: absolute;
                    top: 20px;
                    right: 20px;
                    width: 40px;
                    height: 40px;
                    border: none;
                    border-radius: 8px;
                    background: #f1f5f9;
                    color: #64748b;
                    cursor: pointer;
                    transition: all 0.2s ease;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
                
                .modal-close:hover {
                    background: #e2e8f0;
                    color: #1e293b;
                }
                
                .modal-body {
                    padding: 32px;
                }
                
                .explainer-sections {
                    display: flex;
                    flex-direction: column;
                    gap: 24px;
                }
                
                .explainer-section {
                    padding-bottom: 24px;
                    border-bottom: 1px solid #f1f5f9;
                }
                
                .explainer-section:last-child {
                    border-bottom: none;
                    padding-bottom: 0;
                }
                
                .explainer-section h3 {
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    margin-bottom: 12px;
                    color: #1e293b;
                    font-size: 16px;
                    font-weight: 600;
                }
                
                .explainer-section h3 i {
                    color: #3b82f6;
                }
                
                .explainer-section p {
                    color: #64748b;
                    line-height: 1.6;
                    font-size: 14px;
                }
                
                .example-box {
                    background: #f8fafc;
                    border-left: 4px solid #3b82f6;
                    padding: 16px;
                    border-radius: 0 8px 8px 0;
                    margin-top: 8px;
                }
                
                .example-box p {
                    color: #1e293b;
                    margin: 0;
                    font-style: italic;
                }
                
                .explainer-pros-cons {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 24px;
                    margin-top: 8px;
                }
                
                @media (max-width: 768px) {
                    .explainer-pros-cons {
                        grid-template-columns: 1fr;
                    }
                }
                
                .pros-section h3 {
                    color: #059669;
                }
                
                .cons-section h3 {
                    color: #dc2626;
                }
                
                .pros-section h3 i,
                .cons-section h3 i {
                    color: inherit;
                }
                
                .explainer-pros-cons ul {
                    list-style: none;
                    padding: 0;
                    margin: 0;
                }
                
                .explainer-pros-cons li {
                    padding: 8px 0;
                    color: #64748b;
                    font-size: 14px;
                    line-height: 1.5;
                    position: relative;
                    padding-left: 20px;
                }
                
                .pros-section li::before {
                    content: "✓";
                    position: absolute;
                    left: 0;
                    color: #059669;
                    font-weight: bold;
                }
                
                .cons-section li::before {
                    content: "!";
                    position: absolute;
                    left: 0;
                    color: #dc2626;
                    font-weight: bold;
                }
                
                .modal-footer {
                    padding: 24px 32px;
                    border-top: 1px solid #e2e8f0;
                    display: flex;
                    gap: 12px;
                    justify-content: flex-end;
                }
                
                .btn-secondary,
                .btn-primary {
                    padding: 10px 20px;
                    border-radius: 8px;
                    font-weight: 500;
                    cursor: pointer;
                    transition: all 0.2s ease;
                    display: flex;
                    align-items: center;
                    gap: 8px;
                }
                
                .btn-secondary {
                    border: 1px solid #e2e8f0;
                    background: white;
                    color: #64748b;
                }
                
                .btn-secondary:hover {
                    background: #f8fafc;
                    border-color: #cbd5e1;
                }
                
                .btn-primary {
                    border: none;
                    background: #3b82f6;
                    color: white;
                }
                
                .btn-primary:hover {
                    background: #2563eb;
                }
                
                /* Analysis Preview */
                .analysis-preview {
                    background: #f8fafc;
                    border: 1px solid #e2e8f0;
                    border-radius: 12px;
                    padding: 20px;
                    margin-top: 24px;
                }
                
                .preview-header h4 {
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    margin-bottom: 16px;
                    color: #1e293b;
                }
                
                .preview-stats {
                    display: flex;
                    gap: 16px;
                    margin-bottom: 16px;
                    flex-wrap: wrap;
                }
                
                .preview-stats .stat {
                    display: flex;
                    align-items: center;
                    gap: 6px;
                    color: #64748b;
                    font-size: 14px;
                }
                
                .preview-stats i {
                    color: #3b82f6;
                }
                
                .preview-algorithms {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 8px;
                    margin-bottom: 16px;
                }
                
                .preview-algorithm {
                    display: flex;
                    align-items: center;
                    gap: 6px;
                    background: white;
                    padding: 6px 12px;
                    border-radius: 6px;
                    border: 1px solid #e2e8f0;
                    font-size: 12px;
                }
                
                .preview-algorithm i {
                    color: #3b82f6;
                }
                
                .preview-algorithm small {
                    color: #64748b;
                    margin-left: 4px;
                }
                
                .preview-actions {
                    display: flex;
                    gap: 8px;
                }
                
                .btn-preview-clear,
                .btn-preview-recommend {
                    padding: 8px 16px;
                    border-radius: 6px;
                    font-size: 12px;
                    font-weight: 500;
                    cursor: pointer;
                    transition: all 0.2s ease;
                    display: flex;
                    align-items: center;
                    gap: 6px;
                }
                
                .btn-preview-clear {
                    border: 1px solid #e2e8f0;
                    background: white;
                    color: #64748b;
                }
                
                .btn-preview-clear:hover {
                    background: #f8fafc;
                }
                
                .btn-preview-recommend {
                    border: none;
                    background: #3b82f6;
                    color: white;
                }
                
                .btn-preview-recommend:hover {
                    background: #2563eb;
                }
                
                /* Recommendations Modal */
                .recommendations-modal {
                    position: fixed;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    z-index: 1001;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 20px;
                }
                
                .recommendations-list {
                    display: flex;
                    flex-direction: column;
                    gap: 16px;
                    margin: 24px 0;
                }
                
                .recommendation-item {
                    display: flex;
                    align-items: center;
                    gap: 16px;
                    padding: 16px;
                    background: #f8fafc;
                    border-radius: 12px;
                    border: 1px solid #e2e8f0;
                    transition: all 0.2s ease;
                }
                
                .recommendation-item:hover {
                    border-color: #3b82f6;
                    background: #f0f9ff;
                }
                
                .rec-icon {
                    width: 40px;
                    height: 40px;
                    background: #3b82f6;
                    color: white;
                    border-radius: 8px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    flex-shrink: 0;
                }
                
                .rec-info {
                    flex: 1;
                }
                
                .rec-info h4 {
                    margin-bottom: 4px;
                    color: #1e293b;
                    font-size: 16px;
                }
                
                .rec-info p {
                    color: #64748b;
                    font-size: 14px;
                    margin-bottom: 8px;
                }
                
                .rec-info small {
                    color: #3b82f6;
                    font-size: 12px;
                    font-weight: 500;
                }
                
                .btn-add-recommendation {
                    padding: 8px 16px;
                    border: none;
                    border-radius: 6px;
                    background: #3b82f6;
                    color: white;
                    font-weight: 500;
                    cursor: pointer;
                    transition: all 0.2s ease;
                    display: flex;
                    align-items: center;
                    gap: 6px;
                }
                
                .btn-add-recommendation:hover {
                    background: #2563eb;
                }
            </style>
        `;
        
        document.head.insertAdjacentHTML('beforeend', styles);
    }
    
    showNotification(message, type = 'info') {
        // Usar sistema de notificações existente se disponível
        if (window.dataInsights && typeof window.dataInsights.showNotification === 'function') {
            window.dataInsights.showNotification(message, type);
        } else {
            console.log(`[${type.toUpperCase()}] ${message}`);
        }
    }
}

// Inicializar sistema de explicações
let algorithmExplainer;

document.addEventListener('DOMContentLoaded', () => {
    algorithmExplainer = new AlgorithmExplainerSystem();
});

// Export para uso global
window.AlgorithmExplainerSystem = AlgorithmExplainerSystem;
