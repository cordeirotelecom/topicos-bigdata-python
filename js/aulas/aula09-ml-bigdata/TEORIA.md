# AULA 09: MACHINE LEARNING EM BIG DATA

## 🎯 OBJETIVOS DA AULA
- Compreender os desafios de ML em grandes volumes de dados
- Entender algoritmos distribuídos de Machine Learning
- Explorar Apache Spark MLlib
- Aprender sobre feature engineering em escala
- Conhecer casos de uso reais de ML em Big Data

## 📚 CONCEITOS FUNDAMENTAIS

### O que é Machine Learning em Big Data?
**Definição**: Aplicação de algoritmos de aprendizado de máquina em datasets que são grandes demais para processamento em uma única máquina.

**Desafios Únicos**:
- **Volume**: Datasets de terabytes ou petabytes
- **Velocidade**: Processamento em tempo real
- **Variedade**: Dados estruturados e não-estruturados
- **Veracidade**: Qualidade e confiabilidade dos dados

### Por que ML Distribuído?
**Necessidade**: Datasets modernos excedem capacidade de uma máquina

**Benefícios**:
1. **Escalabilidade**: Processa datasets "infinitos"
2. **Performance**: Paralelização reduz tempo de treinamento
3. **Recursos**: Utiliza clusters de centenas de máquinas
4. **Custo**: Mais econômico que supercomputadores

## 🏗️ ARQUITETURAS DE ML DISTRIBUÍDO

### 1. Data Parallelism (Paralelismo de Dados)
**Conceito**: Mesmo modelo treinado em diferentes partições dos dados

```
Dataset → Partição 1 → Modelo 1 ↘
       → Partição 2 → Modelo 2 → Agregação → Modelo Final
       → Partição 3 → Modelo 3 ↗
```

**Vantagens**:
- Simples de implementar
- Escala bem com dados
- Funciona com algoritmos existentes

### 2. Model Parallelism (Paralelismo de Modelo)
**Conceito**: Modelo dividido entre diferentes máquinas

```
Dados → Parte A do Modelo (Máquina 1) → Parte B do Modelo (Máquina 2) → Resultado
```

**Vantagens**:
- Permite modelos muito grandes
- Útil para deep learning
- Otimiza uso de memória

### 3. Parameter Server Architecture
**Conceito**: Servidores dedicados mantêm parâmetros do modelo

```
Workers → Gradientes → Parameter Server → Parâmetros Atualizados → Workers
```

**Vantagens**:
- Sincronização eficiente
- Tolerância a falhas
- Escalabilidade horizontal

## 🚀 APACHE SPARK MLLIB

### Visão Geral
**MLlib** é a biblioteca de Machine Learning distribuído do Apache Spark, projetada para simplificar ML em grande escala.

**Características**:
- **APIs de Alto Nível**: DataFrame-based API
- **Algoritmos Distribuídos**: Implementações escaláveis
- **Pipeline ML**: Workflows reproduzíveis
- **Integração**: Funciona com ecossistema Spark

### Algoritmos Disponíveis

#### Classificação
1. **Logistic Regression**: Para problemas de classificação binária/multiclasse
2. **Random Forest**: Ensemble de árvores de decisão
3. **Gradient Boosting**: Algoritmo de boosting
4. **SVM**: Support Vector Machines
5. **Naive Bayes**: Classificador probabilístico

#### Regressão
1. **Linear Regression**: Regressão linear clássica
2. **Ridge/Lasso**: Regressão com regularização
3. **Random Forest Regression**: Ensemble para regressão
4. **Gradient Boosting Regression**: Boosting para regressão

#### Clustering
1. **K-Means**: Clustering baseado em centróides
2. **Gaussian Mixture Models**: Clustering probabilístico
3. **LDA**: Latent Dirichlet Allocation para topic modeling

#### Sistemas de Recomendação
1. **ALS**: Alternating Least Squares
2. **Matrix Factorization**: Decomposição de matrizes

### Pipeline de ML no Spark

#### Conceitos Principais
1. **Transformer**: Transforma dados (ex: normalização)
2. **Estimator**: Treina modelo a partir de dados
3. **Pipeline**: Sequência de transformers e estimators

#### Exemplo de Pipeline
```
Dados Brutos → Preprocessamento → Feature Engineering → Treinamento → Modelo
```

**Etapas Detalhadas**:
1. **Data Loading**: Carregar dados de fontes diversas
2. **Data Cleaning**: Tratar valores nulos e outliers
3. **Feature Engineering**: Criar e selecionar features
4. **Model Training**: Treinar algoritmo escolhido
5. **Model Evaluation**: Avaliar performance
6. **Model Deployment**: Colocar em produção

## 🛠️ FEATURE ENGINEERING EM ESCALA

### Transformações Comuns

#### Para Dados Numéricos
1. **Normalização**: Escalar valores para [0,1]
2. **Padronização**: Média 0, desvio padrão 1
3. **Binning**: Converter numérico em categórico
4. **Polynomial Features**: Criar features polinomiais

#### Para Dados Categóricos
1. **String Indexer**: Converter strings em índices
2. **One-Hot Encoding**: Criar variáveis dummy
3. **Feature Hashing**: Hash de features categóricas

#### Para Dados de Texto
1. **Tokenização**: Dividir texto em palavras
2. **TF-IDF**: Term Frequency-Inverse Document Frequency
3. **Word2Vec**: Embeddings de palavras
4. **N-grams**: Sequências de palavras

### Seleção de Features
1. **Filter Methods**: Baseados em estatísticas
2. **Wrapper Methods**: Baseados em performance do modelo
3. **Embedded Methods**: Seleção durante treinamento

## 📊 CASOS DE USO REAIS

### 1. Netflix - Sistema de Recomendação
**Desafio**: Recomendar filmes para 200+ milhões de usuários
**Solução**: Collaborative Filtering com ALS
**Escala**: Trilhões de interações, milhões de títulos
**Resultado**: 80% do conteúdo assistido vem de recomendações

### 2. Uber - Previsão de Demanda
**Desafio**: Prever demanda por corridas em tempo real
**Solução**: Time Series Forecasting + ML
**Escala**: Milhões de viagens/dia, centenas de cidades
**Resultado**: Melhor alocação de motoristas, menor tempo de espera

### 3. Spotify - Descoberta Musical
**Desafio**: Personalizar playlists para 400+ milhões usuários
**Solução**: Deep Learning + Collaborative Filtering
**Escala**: Bilhões de streams, milhões de músicas
**Resultado**: Aumento de 30% no engagement

### 4. Fraud Detection (Bancos)
**Desafio**: Detectar fraudes em transações em tempo real
**Solução**: Ensemble Methods + Real-time Scoring
**Escala**: Milhões de transações/dia
**Resultado**: Redução de 60% em fraudes

## ⚙️ OTIMIZAÇÃO E TUNING

### Hyperparameter Tuning
1. **Grid Search**: Busca exaustiva em grid de parâmetros
2. **Random Search**: Busca aleatória mais eficiente
3. **Bayesian Optimization**: Busca inteligente baseada em probabilidade

### Cross-Validation Distribuído
**Problema**: Validação em datasets grandes é custosa
**Solução**: Paralelizar folds de cross-validation
**Benefício**: Reduz tempo de validação significativamente

### Caching e Persistência
**Estratégias**:
- Cache de datasets intermediários
- Persistência de modelos treinados
- Checkpoint para training longo

## 📈 AVALIAÇÃO DE MODELOS

### Métricas para Classificação
1. **Accuracy**: Porcentagem de predições corretas
2. **Precision/Recall**: Para datasets desbalanceados
3. **F1-Score**: Média harmônica de precision e recall
4. **AUC-ROC**: Área sob a curva ROC

### Métricas para Regressão
1. **RMSE**: Root Mean Square Error
2. **MAE**: Mean Absolute Error
3. **R²**: Coeficiente de determinação

### Métricas para Clustering
1. **Silhouette Score**: Qualidade dos clusters
2. **Inertia**: Soma das distâncias aos centróides

## 🚀 TENDÊNCIAS E FUTURO

### AutoML (Automated Machine Learning)
**Conceito**: Automatização do pipeline completo de ML
**Ferramentas**: H2O.ai, DataRobot, Google AutoML
**Benefício**: Democratiza ML para não-especialistas

### MLOps (Machine Learning Operations)
**Conceito**: DevOps aplicado a Machine Learning
**Inclui**: Versionamento, CI/CD, monitoramento
**Ferramentas**: MLflow, Kubeflow, TensorFlow Serving

### Federated Learning
**Conceito**: Treinar modelos sem centralizar dados
**Benefício**: Privacidade e compliance
**Aplicações**: Mobile AI, healthcare, finance

### Edge ML
**Conceito**: Executar ML em dispositivos edge
**Benefício**: Baixa latência, privacidade
**Desafios**: Recursos limitados, otimização

## 🎓 EXERCÍCIOS CONCEITUAIS

### Exercício 1: Design de Sistema
**Problema**: Sistema de recomendação para e-commerce com 10 milhões de usuários
**Considere**: Algoritmos, escalabilidade, latência, cold start

### Exercício 2: Feature Engineering
**Problema**: Prever preços de imóveis usando dados públicos
**Considere**: Features geográficas, temporais, econômicas

### Exercício 3: Otimização
**Problema**: Reduzir tempo de treinamento de 8 horas para 1 hora
**Considere**: Paralelização, sampling, feature selection

## 📚 RECURSOS ADICIONAIS

### Livros Recomendados
- "Hands-On Machine Learning" - Aurélien Géron
- "The Elements of Statistical Learning" - Hastie, Tibshirani, Friedman
- "Pattern Recognition and Machine Learning" - Christopher Bishop

### Cursos Online
- Coursera: Machine Learning Course (Andrew Ng)
- edX: MIT Introduction to Machine Learning
- Udacity: Machine Learning Engineer Nanodegree

### Frameworks e Ferramentas
- **Apache Spark MLlib**: ML distribuído
- **TensorFlow**: Deep learning em escala
- **PyTorch**: Research e produção
- **H2O.ai**: AutoML platform
- **MLflow**: ML lifecycle management

## 🎯 PRÓXIMOS PASSOS

1. **Praticar**: Implementar algoritmos simples
2. **Experimentar**: Usar Spark MLlib em datasets reais
3. **Especializar**: Focar em domain específico (NLP, Computer Vision, etc.)
4. **Produzir**: Colocar modelos em produção
5. **Continuar**: Acompanhar research e novas técnicas

---

**Próxima Aula**: Deep Learning Distribuído e Redes Neurais em Escala
