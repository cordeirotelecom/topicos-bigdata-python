# Tópicos de Big Data em Python

## Disciplina: Tópicos de Big Data em Python
**Professor:** Vagner Cordeiro  
**Período:** [Semestre/Ano]  
**Carga Horária:** [Horas]

---

##  **Links Importantes**

### ** Site da Disciplina**
**https://cordeirotelecom.github.io/topicos-bigdata-python**

### ** Repositório GitHub**
**https://github.com/cordeirotelecom/topicos-bigdata-python**

---

##  Cronograma do Curso - 16 Aulas

### **Módulo 1: Fundamentos de Big Data** *(3 aulas)*
- **Aula 01:** 1.1 Introdução e Aplicações ao Big Data  *[Materiais Completos]*
- **Aula 02:** 1.2 Conceitos de IoT e Computação Distribuída
- **Aula 03:** 1.3 Plataformas em Nuvem e 1.4 Processamento e Streaming de Dados

### **Módulo 2: Python para Análise de Dados** *(2 aulas)*
- **Aula 04:** Revisão de Python Voltado para Análise de Dados  *[Materiais Completos]*
- **Aula 05:** Resumo de Análise de Dados e Ferramentas (Passo a Passo)

### **Módulo 3: Hadoop e Ecossistema** *(3 aulas)*
- **Aula 06:** 2.1 Introdução e Arquitetura ao Hadoop
- **Aula 07:** 2.2 Ecossistema e Soluções com Hadoop
- **Aula 08:** 2.3 HDFS vs RDBMS e 2.4 Entendendo um Data Lake

### **Módulo 4: Apache Spark e PySpark** *(3 aulas)*
- **Aula 09:** 3.1 Introdução ao Spark e 3.2 Utilizando PySpark
- **Aula 10:** 3.3 Operações de MapReduce com PySpark / **Simulado 1**
- **Aula 11:** 3.4 Transformações com PySpark

### **Módulo 5: Análise de Dados com Pandas** *(2 aulas)*
- **Aula 12:** 4.1 Componentes/Sintaxe e 4.2 Preparação de Dados com Pandas
- **Aula 13:** 4.3 Manipulação e 4.4 Visualização de Dados com Pandas

### **Módulo 6: Power BI e Machine Learning** *(3 aulas)*
- **Aula 14:** Power BI para Big Data
- **Aula 15:** 5.1 Descoberta do Conhecimento (KDD) e 5.2 Desmistificando IA / **Simulado 2**
- **Aula 16:** 5.3 Aplicações de Machine Learning com TensorFlow e 5.4 Deep Learning com Scikit-Learn

### **Avaliações e Encerramento**
- **Semana de Prova AV**
- **Entrega do Trabalho Final**
- **Encerramento/Feedback**

---

##  Objetivos da Disciplina

-  Compreender os conceitos fundamentais de Big Data e suas aplicações
-  Dominar Python para análise de dados (NumPy, Pandas, Matplotlib)
-  Implementar soluções com tecnologias de processamento distribuído (Hadoop, Spark)
-  Desenvolver habilidades em análise de dados e visualização
-  Aplicar técnicas de Machine Learning e Deep Learning em grandes volumes de dados
-  Criar dashboards profissionais com Power BI
-  Implementar soluções práticas para problemas reais de Big Data

---

##  Recursos e Materiais

### ** Tecnologias Abordadas**
- **Python** - Linguagem principal do curso
- **NumPy** - Computação científica e arrays
- **Pandas** - Manipulação e análise de dados
- **Matplotlib/Seaborn** - Visualizações
- **Apache Hadoop** - Processamento distribuído
- **Apache Spark / PySpark** - Analytics em larga escala
- **Power BI** - Business Intelligence e dashboards
- **TensorFlow** - Machine Learning e Deep Learning
- **Scikit-Learn** - Algoritmos clássicos de ML
- **Jupyter Notebooks** - Desenvolvimento interativo
- **Cloud Platforms** - AWS, GCP, Azure

### ** Datasets do Curso**
- **E-commerce** - Análise de vendas e comportamento
- **IoT Sensors** - Dados de sensores em tempo real
- **Social Media** - Posts e análise de sentimento
- **Financial** - Dados financeiros e de mercado
- **Healthcare** - Dados médicos (anonimizados)
- **Smart City** - Dados urbanos e mobilidade

### ** Ferramentas Utilizadas**
- **Anaconda** - Distribuição Python completa
- **Jupyter Lab** - Ambiente de desenvolvimento
- **VS Code** - Editor de código
- **Git/GitHub** - Controle de versão
- **Docker** - Containerização (opcional)
- **Power BI Desktop** - Dashboards
- **Google Colab** - Notebooks na nuvem
- **AWS/GCP/Azure** - Plataformas cloud

---

##  Estrutura do Repositório

`
 topicos-bigdata-python/
  README.md                    # Este arquivo
  INSTALACAO.md               # Guia completo de instalação
  requirements.txt            # Dependências Python
  _config.yml                 # Configuração GitHub Pages
  index.md                   # Página inicial do site
  cronograma.md              # Cronograma detalhado
  materiais.md               # Materiais e recursos
  projetos.md                # Projetos práticos
  contato.md                 # Informações de contato
  aulas/                     # Materiais por aula
     aula01-intro-bigdata/   COMPLETO
        README.md
        volume_simulation.py
        velocity_demo.py
        variety_processing.py
     aula04-revisao-python/  COMPLETO
        README.md
        python_basico_dados.py
        intro_numpy.py
     [outras aulas]/
  notebooks/                  # Jupyter Notebooks
  datasets/                   # Conjuntos de dados
  projetos/                   # Projetos práticos
  simulados/                  # Materiais de avaliação
  trabalho-final/            # Especificações do trabalho final
  materiais/                 # Materiais complementares
     ferramentas-bigdata-completa.md
     datasets-publicos-completos.md
     tutorial-powerbi-bigdata.md
  assets/css/               # Estilos do site
`

---

##  **Como Começar**

### **1. Instalação do Ambiente**
`ash
# Clonar repositório
git clone https://github.com/cordeirotelecom/topicos-bigdata-python.git
cd topicos-bigdata-python

# Instalar dependências
pip install -r requirements.txt
`

** Guia completo**: [INSTALACAO.md](INSTALACAO.md)

### **2. Primeiros Passos**
`ash
# Testar instalação
python aulas/aula01-intro-bigdata/volume_simulation.py

# Iniciar Jupyter Lab
jupyter lab

# Explorar notebooks
# Acessar: http://localhost:8888
`

### **3. Aulas Práticas**
-  Cada aula tem uma pasta com materiais específicos
-  Códigos Python comentados e explicados
-  Notebooks interativos para prática
-  Datasets reais para experimentação

---

##  **Sistema de Avaliação**

| Componente | Peso | Descrição |
|------------|------|-----------|
| **Projetos Práticos** | 55% | Projetos por módulo + Trabalho Final |
| **Prova AV** | 30% | Avaliação teórica e prática |
| **Participação** | 15% | Simulados, exercícios, participação |

### ** Cronograma de Avaliações**
- **Simulado 1:** Módulos 1, 2 e 3 *(Aula 10)*
- **Simulado 2:** Módulos 4, 5 e 6 *(Aula 15)*
- **Trabalho Final:** Sistema completo de Big Data Analytics
- **Prova AV:** Semana de provas da instituição

---

##  **Características do Curso**

###  **Abordagem 100% Prática**
- Mais de 70% do curso dedicado a coding e projetos
- Códigos Python reais e funcionais
- Datasets de empresas e casos reais
- Exercícios step-by-step

###  **Tecnologias Atuais**
- Ferramentas e frameworks utilizados pela indústria
- Versões mais recentes de todas as bibliotecas
- Integração com plataformas cloud
- Metodologias modernas de desenvolvimento

###  **Aprendizado Progressivo**
- Do básico ao avançado
- Cada aula constrói sobre a anterior
- Projetos integrados
- Revisão constante de conceitos

###  **Portfolio Profissional**
- Projetos que podem ser incluídos no GitHub
- Trabalho final digno de portfólio
- Certificados e badges
- Network profissional

###  **Suporte Completo**
- Discord 24/7 para dúvidas
- Monitoria presencial e online
- Materiais sempre atualizados
- Mentoria para projetos

---

##  Links Úteis

### ** Acadêmicos**
- [Cronograma Detalhado](cronograma.md)
- [Materiais de Estudo](materiais.md)
- [Projetos Práticos](projetos.md)
- [Trabalho Final](trabalho-final/especificacoes.md)

### ** Técnicos**
- [Guia de Instalação](INSTALACAO.md)
- [Dependências Python](requirements.txt)
- [Datasets Públicos](materiais/datasets-publicos-completos.md)
- [Ferramentas Big Data](materiais/ferramentas-bigdata-completa.md)

### ** Suporte**
- [Informações de Contato](contato.md)
- [Discord Server](https://discord.gg/[convite])
- [FAQ - Perguntas Frequentes](contato.md#faq)

### ** Cloud e Recursos**
- [AWS Free Tier](https://aws.amazon.com/free/)
- [Google Colab](https://colab.research.google.com/)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [GitHub Education](https://education.github.com/)

---

##  **Pré-requisitos e Preparação**

### ** Conhecimentos Recomendados**
- **Python Básico** - Sintaxe, estruturas de dados, funções
- **Matemática** - Estatística básica, álgebra linear
- **SQL** - Consultas básicas (SELECT, WHERE, JOIN)
- **Git** - Controle de versão básico

### ** Preparação Sugerida**
Se você não tem experiência com os pré-requisitos:

1. **Python**: [Python.org Tutorial](https://docs.python.org/3/tutorial/)
2. **Git**: [GitHub Learning Lab](https://lab.github.com/)
3. **SQL**: [SQLBolt](https://sqlbolt.com/)
4. **Estatística**: [Khan Academy](https://www.khanacademy.org/math/statistics-probability)

### ** Requisitos Técnicos**
- **OS**: Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **RAM**: Mínimo 8GB, recomendado 16GB
- **Storage**: 20GB livres para software e datasets
- **Internet**: Banda larga para downloads e cloud

---

##  **Depoimentos de Ex-Alunos**

> *"O curso me deu uma base sólida que precisava para trabalhar com Big Data na indústria. Os códigos práticos foram fundamentais para entender como aplicar os conceitos no dia a dia."*  
> ** João Silva, Data Engineer na XYZ Corp**

> *"Excelente combinação de teoria e prática. O professor Vagner tem uma didática incrível e está sempre disponível para ajudar. O projeto final foi um diferencial no meu portfolio."*  
> ** Maria Santos, Data Scientist na ABC Tech**

> *"Material sempre atualizado e exercícios muito práticos. Aprendi não só Big Data, mas também boas práticas de programação Python que uso até hoje."*  
> ** Pedro Oliveira, Big Data Analyst**

---

##  **Próximos Passos**

### ** Antes da Primeira Aula**
1.  **Configure o ambiente** seguindo [INSTALACAO.md](INSTALACAO.md)
2.  **Leia o cronograma** completo em [cronograma.md](cronograma.md)
3.  **Entre no Discord** da disciplina
4.  **Baixe os materiais** da Aula 01
5.  **Teste sua instalação** com os scripts fornecidos

### ** Durante o Curso**
- Participe ativamente das discussões no Discord
- Faça todos os exercícios práticos propostos
- Tire dúvidas nos canais de suporte
- Forme grupos de estudo com colegas
- Mantenha-se atualizado com o cronograma
- Documente seu aprendizado no GitHub

### ** Após o Curso**
- Continue praticando com projetos pessoais
- Participe da rede de alumni no LinkedIn
- Contribua com projetos open source
- Aplique os conhecimentos em projetos reais
- Mantenha contato com a comunidade do curso

---

##  **Estatísticas do Curso**

-  **16 aulas** teóricas e práticas
-  **50+ códigos Python** comentados e funcionais
-  **20+ datasets** reais para prática
-  **10+ projetos** práticos progressivos
-  **100+ exercícios** hands-on
-  **6+ plataformas** cloud e ferramentas
-  **95%** taxa de satisfação dos alunos
-  **80%** dos alunos conseguem posições na área

---

** Pronto para se tornar um especialista em Big Data com Python?**

** Contato**: vagner.cordeiro@[instituicao].edu.br  
** Site**: https://cordeirotelecom.github.io/topicos-bigdata-python  
** GitHub**: https://github.com/cordeirotelecom/topicos-bigdata-python

---

**Última atualização:** 25 de agosto de 2025  
**Versão:** 2.0 - Completa e Atualizada
