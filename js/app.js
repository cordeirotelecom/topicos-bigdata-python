// Initialize application when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('DataScience Pro - Initializing application...');
    
    // Initialize main features
    initializeNavigation();
    initializeReferences();
    
    // Initialize analysis tool specifically
    initializeAnalysisTool();
    
    // Show welcome message
    setTimeout(() => {
        Utils.showNotification('Bem-vindo ao DataScience Pro! Explore nossos guias e ferramentas.', 'success');
    }, 1000);
    
    console.log('Application initialized successfully!');
});

// Initialize references search functionality
function initializeReferences() {
    const searchInput = document.getElementById('ref-search');
    const categoryFilter = document.getElementById('category-filter');
    const referencesList = document.getElementById('references-list');
    
    if (!searchInput || !categoryFilter || !referencesList) return;
    
    // Load references
    const references = getReferenceData();
    displayReferences(references, referencesList);
    
    // Search functionality
    function performSearch() {
        const searchTerm = searchInput.value.toLowerCase();
        const selectedCategory = categoryFilter.value;
        
        const filteredRefs = references.filter(ref => {
            const matchesSearch = !searchTerm || 
                ref.title.toLowerCase().includes(searchTerm) ||
                ref.description.toLowerCase().includes(searchTerm) ||
                ref.authors.some(author => author.toLowerCase().includes(searchTerm));
            
            const matchesCategory = !selectedCategory || ref.category === selectedCategory;
            
            return matchesSearch && matchesCategory;
        });
        
        displayReferences(filteredRefs, referencesList);
    }
    
    searchInput.addEventListener('input', performSearch);
    categoryFilter.addEventListener('change', performSearch);
}

// Get reference data
function getReferenceData() {
    return [
        {
            title: "Python for Data Science Handbook",
            authors: ["Jake VanderPlas"],
            year: 2023,
            category: "livros",
            description: "Guia essencial para análise de dados científicos com Python, pandas, NumPy e matplotlib.",
            url: "https://jakevdp.github.io/PythonDataScienceHandbook/",
            type: "book",
            access: "gratuito"
        },
        {
            title: "Scikit-learn: Machine Learning in Python",
            authors: ["Fabian Pedregosa", "Gaël Varoquaux", "Alexandre Gramfort"],
            year: 2011,
            category: "artigos",
            description: "Artigo seminal sobre a biblioteca scikit-learn para machine learning em Python.",
            url: "http://jmlr.org/papers/v12/pedregosa11a.html",
            type: "article",
            access: "gratuito"
        },
        {
            title: "Pandas Documentation",
            authors: ["Pandas Development Team"],
            year: 2024,
            category: "documentacao",
            description: "Documentação oficial da biblioteca pandas para manipulação e análise de dados.",
            url: "https://pandas.pydata.org/docs/",
            type: "documentation",
            access: "gratuito"
        },
        {
            title: "NumPy: The Fundamental Package for Scientific Computing",
            authors: ["Stefan van der Walt", "S. Chris Colbert", "Gaël Varoquaux"],
            year: 2011,
            category: "artigos",
            description: "Artigo sobre o NumPy, biblioteca fundamental para computação científica em Python.",
            url: "https://numpy.org/citing-numpy/",
            type: "article",
            access: "gratuito"
        },
        {
            title: "Matplotlib: A 2D Graphics Environment",
            authors: ["John D. Hunter"],
            year: 2007,
            category: "artigos",
            description: "Artigo original sobre matplotlib, biblioteca principal para visualização em Python.",
            url: "https://ieeexplore.ieee.org/document/4160265",
            type: "article",
            access: "pago"
        },
        {
            title: "Seaborn: Statistical Data Visualization",
            authors: ["Michael Waskom"],
            year: 2021,
            category: "documentacao",
            description: "Documentação do seaborn para visualização estatística de dados.",
            url: "https://seaborn.pydata.org/",
            type: "documentation",
            access: "gratuito"
        },
        {
            title: "The Elements of Statistical Learning",
            authors: ["Trevor Hastie", "Robert Tibshirani", "Jerome Friedman"],
            year: 2017,
            category: "livros",
            description: "Livro clássico sobre aprendizado estatístico e métodos de machine learning.",
            url: "https://web.stanford.edu/~hastie/ElemStatLearn/",
            type: "book",
            access: "gratuito"
        },
        {
            title: "Jupyter Notebook Documentation",
            authors: ["Project Jupyter"],
            year: 2024,
            category: "documentacao",
            description: "Documentação oficial do Jupyter Notebook para análise interativa de dados.",
            url: "https://jupyter-notebook.readthedocs.io/",
            type: "documentation",
            access: "gratuito"
        },
        {
            title: "Data Science from Scratch",
            authors: ["Joel Grus"],
            year: 2019,
            category: "livros",
            description: "Introdução prática à ciência de dados implementando algoritmos do zero.",
            url: "https://www.oreilly.com/library/view/data-science-from/9781492041122/",
            type: "book",
            access: "pago"
        },
        {
            title: "Plotly Python Documentation",
            authors: ["Plotly Technologies"],
            year: 2024,
            category: "documentacao",
            description: "Documentação para criação de visualizações interativas com Plotly.",
            url: "https://plotly.com/python/",
            type: "documentation",
            access: "gratuito"
        },
        {
            title: "Statistical Thinking for the 21st Century",
            authors: ["Russell A. Poldrack"],
            year: 2023,
            category: "livros",
            description: "Livro moderno sobre pensamento estatístico aplicado à análise de dados.",
            url: "https://statsthinking21.github.io/statsthinking21-core-site/",
            type: "book",
            access: "gratuito"
        },
        {
            title: "SciPy Documentation",
            authors: ["SciPy Developers"],
            year: 2024,
            category: "documentacao",
            description: "Documentação da biblioteca SciPy para computação científica.",
            url: "https://docs.scipy.org/",
            type: "documentation",
            access: "gratuito"
        },
        {
            title: "An Introduction to Statistical Learning",
            authors: ["Gareth James", "Daniela Witten", "Trevor Hastie", "Robert Tibshirani"],
            year: 2021,
            category: "livros",
            description: "Introdução acessível ao aprendizado estatístico com aplicações em R e Python.",
            url: "https://www.statlearning.com/",
            type: "book",
            access: "gratuito"
        },
        {
            title: "TensorFlow Documentation",
            authors: ["TensorFlow Team"],
            year: 2024,
            category: "documentacao",
            description: "Documentação oficial do TensorFlow para machine learning e deep learning.",
            url: "https://www.tensorflow.org/api_docs",
            type: "documentation",
            access: "gratuito"
        },
        {
            title: "Deep Learning",
            authors: ["Ian Goodfellow", "Yoshua Bengio", "Aaron Courville"],
            year: 2016,
            category: "livros",
            description: "Livro abrangente sobre deep learning e redes neurais artificiais.",
            url: "https://www.deeplearningbook.org/",
            type: "book",
            access: "gratuito"
        },
        {
            title: "Pattern Recognition and Machine Learning",
            authors: ["Christopher M. Bishop"],
            year: 2006,
            category: "livros",
            description: "Texto clássico sobre reconhecimento de padrões e machine learning.",
            url: "https://www.microsoft.com/en-us/research/people/cmbishop/prml-book/",
            type: "book",
            access: "pago"
        },
        {
            title: "Apache Spark Documentation",
            authors: ["Apache Software Foundation"],
            year: 2024,
            category: "documentacao",
            description: "Documentação oficial do Apache Spark para processamento de big data.",
            url: "https://spark.apache.org/docs/latest/",
            type: "documentation",
            access: "gratuito"
        },
        {
            title: "Kaggle Learn",
            authors: ["Kaggle Team"],
            year: 2024,
            category: "cursos",
            description: "Cursos gratuitos sobre data science, machine learning e análise de dados.",
            url: "https://www.kaggle.com/learn",
            type: "course",
            access: "gratuito"
        },
        {
            title: "R for Data Science",
            authors: ["Hadley Wickham", "Garrett Grolemund"],
            year: 2017,
            category: "livros",
            description: "Guia prático para análise de dados usando a linguagem R.",
            url: "https://r4ds.had.co.nz/",
            type: "book",
            access: "gratuito"
        },
        {
            title: "OpenAI GPT Research Papers",
            authors: ["OpenAI Research Team"],
            year: 2024,
            category: "artigos",
            description: "Coleção de artigos de pesquisa sobre modelos de linguagem GPT.",
            url: "https://openai.com/research",
            type: "article",
            access: "gratuito"
        },
        {
            title: "Google Colab",
            authors: ["Google Research"],
            year: 2024,
            category: "ferramentas",
            description: "Ambiente gratuito baseado em Jupyter para machine learning e análise de dados.",
            url: "https://colab.research.google.com/",
            type: "tool",
            access: "gratuito"
        },
        {
            title: "Anaconda Documentation",
            authors: ["Anaconda Inc."],
            year: 2024,
            category: "documentacao",
            description: "Documentação da distribuição Anaconda para ciência de dados em Python.",
            url: "https://docs.anaconda.com/",
            type: "documentation",
            access: "gratuito"
        },
        {
            title: "Coursera Data Science Specialization",
            authors: ["Johns Hopkins University"],
            year: 2024,
            category: "cursos",
            description: "Especialização em ciência de dados oferecida pela Johns Hopkins University.",
            url: "https://www.coursera.org/specializations/jhu-data-science",
            type: "course",
            access: "pago"
        },
        {
            title: "MIT Introduction to Computational Thinking",
            authors: ["MIT"],
            year: 2024,
            category: "cursos",
            description: "Curso do MIT sobre pensamento computacional aplicado à ciência de dados.",
            url: "https://computationalthinking.mit.edu/",
            type: "course",
            access: "gratuito"
        },
        {
            title: "Nature Methods - Computational Biology",
            authors: ["Nature Publishing Group"],
            year: 2024,
            category: "artigos",
            description: "Artigos científicos sobre métodos computacionais em biologia.",
            url: "https://www.nature.com/nmeth/",
            type: "journal",
            access: "pago"
        },
        {
            title: "arXiv.org - Statistics and Machine Learning",
            authors: ["Cornell University"],
            year: 2024,
            category: "artigos",
            description: "Repositório de artigos científicos sobre estatística e machine learning.",
            url: "https://arxiv.org/list/stat.ML/recent",
            type: "repository",
            access: "gratuito"
        },
        {
            title: "Towards Data Science (Medium)",
            authors: ["Various Authors"],
            year: 2024,
            category: "artigos",
            description: "Publicação no Medium com artigos sobre ciência de dados e machine learning.",
            url: "https://towardsdatascience.com/",
            type: "blog",
            access: "freemium"
        },
        {
            title: "KDnuggets",
            authors: ["KDnuggets Team"],
            year: 2024,
            category: "artigos",
            description: "Portal com notícias, tutoriais e recursos sobre data science e machine learning.",
            url: "https://www.kdnuggets.com/",
            type: "portal",
            access: "gratuito"
        },
        {
            title: "GitHub - Awesome Data Science",
            authors: ["Open Source Community"],
            year: 2024,
            category: "ferramentas",
            description: "Lista curada de recursos, ferramentas e bibliotecas para ciência de dados.",
            url: "https://github.com/academic/awesome-datascience",
            type: "repository",
            access: "gratuito"
        },
        {
            title: "Fast.ai Practical Deep Learning",
            authors: ["Jeremy Howard", "Sylvain Gugger"],
            year: 2024,
            category: "cursos",
            description: "Curso prático de deep learning com abordagem top-down.",
            url: "https://course.fast.ai/",
            type: "course",
            access: "gratuito"
        }
    ];
}

// Display references
function displayReferences(references, container) {
    if (references.length === 0) {
        container.innerHTML = `
            <div class="no-results">
                <i class="fas fa-search"></i>
                <p>Nenhuma referência encontrada com os critérios de busca.</p>
            </div>
        `;
        return;
    }
    
    container.innerHTML = references.map(ref => `
        <div class="reference-card" data-category="${ref.category}">
            <div class="reference-header">
                <h4 class="reference-title">
                    <a href="${ref.url}" target="_blank" rel="noopener noreferrer">
                        ${ref.title}
                        <i class="fas fa-external-link-alt"></i>
                    </a>
                </h4>
                <div class="reference-meta">
                    <span class="reference-badge ${ref.access}">${ref.access}</span>
                    <span class="reference-badge category">${getCategoryName(ref.category)}</span>
                    <span class="reference-year">${ref.year}</span>
                </div>
            </div>
            <div class="reference-authors">
                <i class="fas fa-user-graduate"></i>
                ${ref.authors.join(', ')}
            </div>
            <div class="reference-description">
                ${ref.description}
            </div>
            <div class="reference-actions">
                <button class="btn-secondary" onclick="copyReference('${encodeURIComponent(JSON.stringify(ref))}')">
                    <i class="fas fa-copy"></i> Copiar Citação
                </button>
                <a href="${ref.url}" target="_blank" rel="noopener noreferrer" class="btn-primary">
                    <i class="fas fa-external-link-alt"></i> Acessar
                </a>
            </div>
        </div>
    `).join('');
}

// Get category display name
function getCategoryName(category) {
    const categoryNames = {
        'livros': 'Livros',
        'artigos': 'Artigos',
        'documentacao': 'Documentação',
        'cursos': 'Cursos',
        'ferramentas': 'Ferramentas'
    };
    return categoryNames[category] || category;
}

// Copy reference citation
function copyReference(encodedRef) {
    try {
        const ref = JSON.parse(decodeURIComponent(encodedRef));
        
        let citation = `${ref.authors.join(', ')}. (${ref.year}). `;
        citation += `${ref.title}. `;
        
        if (ref.type === 'book') {
            citation += 'Livro. ';
        } else if (ref.type === 'article') {
            citation += 'Artigo científico. ';
        } else if (ref.type === 'documentation') {
            citation += 'Documentação técnica. ';
        } else if (ref.type === 'course') {
            citation += 'Curso online. ';
        }
        
        citation += `Disponível em: ${ref.url}`;
        
        if (navigator.clipboard && window.isSecureContext) {
            navigator.clipboard.writeText(citation).then(() => {
                Utils.showNotification('Citação copiada para a área de transferência!', 'success');
            }).catch(() => {
                fallbackCopyTextToClipboard(citation);
            });
        } else {
            fallbackCopyTextToClipboard(citation);
        }
    } catch (error) {
        console.error('Error copying reference:', error);
        Utils.showNotification('Erro ao copiar citação.', 'error');
    }
}

// Fallback copy function
function fallbackCopyTextToClipboard(text) {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.top = "0";
    textArea.style.left = "0";
    textArea.style.position = "fixed";
    
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    
    try {
        const successful = document.execCommand('copy');
        if (successful) {
            Utils.showNotification('Citação copiada para a área de transferência!', 'success');
        } else {
            Utils.showNotification('Falha ao copiar citação.', 'error');
        }
    } catch (error) {
        console.error('Fallback copy failed:', error);
        Utils.showNotification('Erro ao copiar citação.', 'error');
    }
    
    document.body.removeChild(textArea);
}

// Make functions available globally
window.copyReference = copyReference;
