# Aula 10: Machine Learning Distribuído com PySpark MLlib

## Objetivos de Aprendizagem

Ao final desta aula, você será capaz de:
- Implementar algoritmos de ML distribuído usando PySpark MLlib
- Construir pipelines completos de machine learning escaláveis
- Aplicar técnicas de detecção de fraudes em grande escala
- Desenvolver sistemas de recomendação distribuídos
- Realizar hyperparameter tuning em ambiente distribuído
- Otimizar performance de modelos ML para big data

## Conteúdo Programático

### 1. Introdução ao Machine Learning Distribuído

#### 1.1 Desafios do ML com Big Data
- **Volume**: Datasets que não cabem em memória
- **Velocidade**: Necessidade de processamento em tempo real
- **Variedade**: Diferentes tipos de dados (estruturados, texto, imagens)
- **Complexidade**: Modelos que requerem poder computacional massivo

#### 1.2 Vantagens do MLlib
- **Escalabilidade**: Processamento distribuído automático
- **Integração**: Seamless com ecossistema Spark
- **Performance**: Otimizações específicas para ML
- **APIs**: Interfaces Python, Scala, Java, R

### 2. Arquitetura MLlib

#### 2.1 Componentes Principais
- **DataFrames**: Estrutura de dados principal
- **Transformers**: Transformações de features
- **Estimators**: Algoritmos de ML
- **Pipelines**: Workflows de ML
- **Evaluators**: Métricas de avaliação

#### 2.2 Feature Engineering Distribuído
- **VectorAssembler**: Combinação de features
- **StringIndexer**: Encoding de variáveis categóricas
- **StandardScaler**: Normalização distribuída
- **PCA**: Redução de dimensionalidade
- **Word2Vec**: Embeddings de texto

### 3. Implementação Prática

#### 3.1 Detecção de Fraudes
```python
# Pipeline completo de detecção de fraudes
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Preparação dos dados
indexer = StringIndexer(inputCol="merchant_category", outputCol="category_idx")
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
scaler = StandardScaler(inputCol="features", outputCol="scaled_features")

# Modelo
rf = RandomForestClassifier(featuresCol="scaled_features", labelCol="is_fraud")

# Pipeline
pipeline = Pipeline(stages=[indexer, assembler, scaler, rf])
model = pipeline.fit(train_data)

# Avaliação
evaluator = BinaryClassificationEvaluator(metricName="areaUnderROC")
auc = evaluator.evaluate(predictions)
```

#### 3.2 Sistema de Recomendação
```python
# Collaborative Filtering com ALS
from pyspark.ml.recommendation import ALS

als = ALS(
    userCol="user_id",
    itemCol="item_id",
    ratingCol="rating",
    maxIter=20,
    regParam=0.1,
    rank=50
)

model = als.fit(ratings_data)
recommendations = model.recommendForAllUsers(10)
```

#### 3.3 Segmentação de Clientes
```python
# Clustering distribuído
from pyspark.ml.clustering import KMeans

kmeans = KMeans(featuresCol="features", k=5)
model = kmeans.fit(customer_data)
predictions = model.transform(customer_data)

# Avaliação
evaluator = ClusteringEvaluator(metricName="silhouette")
silhouette = evaluator.evaluate(predictions)
```

### 4. Técnicas Avançadas

#### 4.1 Hyperparameter Tuning
```python
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

# Grid de parâmetros
paramGrid = ParamGridBuilder() \
    .addGrid(rf.numTrees, [50, 100, 200]) \
    .addGrid(rf.maxDepth, [5, 10, 15]) \
    .build()

# Cross-validation
crossval = CrossValidator(
    estimator=pipeline,
    estimatorParamMaps=paramGrid,
    evaluator=evaluator,
    numFolds=3
)

cv_model = crossval.fit(train_data)
```

#### 4.2 Feature Selection
```python
from pyspark.ml.feature import ChiSqSelector

selector = ChiSqSelector(
    featuresCol="features",
    outputCol="selected_features",
    labelCol="label",
    numTopFeatures=20
)
```

### 5. Casos de Uso Reais

#### 5.1 Detecção de Fraudes Financeiras
- **Dados**: Transações bancárias, histórico de comportamento
- **Features**: Valor, horário, localização, padrões de uso
- **Modelos**: Random Forest, Gradient Boosting
- **Métricas**: Precision, Recall, F1-Score, AUC

#### 5.2 Recomendação de Produtos
- **Dados**: Histórico de compras, avaliações, perfil usuário
- **Algoritmos**: Collaborative Filtering, Matrix Factorization
- **Métricas**: RMSE, MAE, Precision@K, Recall@K

#### 5.3 Previsão de Demanda
- **Dados**: Vendas históricas, sazonalidade, fatores externos
- **Features**: Tendências, sazonalidade, eventos especiais
- **Modelos**: Linear Regression, Random Forest, LSTM

### 6. Otimizações de Performance

#### 6.1 Configurações Spark
```python
spark = SparkSession.builder \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .getOrCreate()
```

#### 6.2 Estratégias de Caching
```python
# Cache datasets frequentemente utilizados
train_data.cache()
test_data.cache()

# Persist com diferentes storage levels
df.persist(StorageLevel.MEMORY_AND_DISK_SER)
```

#### 6.3 Particionamento Inteligente
```python
# Repartition para balanceamento
df = df.repartition(200)

# Coalesce para reduzir partições
df = df.coalesce(50)
```

### 7. Monitoramento e Debugging

#### 7.1 Spark UI
- **Jobs**: Progresso de execução
- **Stages**: Breakdown de tarefas
- **Storage**: Uso de cache
- **Environment**: Configurações

#### 7.2 Métricas de Performance
```python
# Tempo de execução
start_time = time.time()
model = pipeline.fit(train_data)
training_time = time.time() - start_time

# Uso de recursos
spark.sparkContext.statusTracker().getExecutorInfos()
```

### 8. Deployment em Produção

#### 8.1 Modelos Persistentes
```python
# Salvar modelo
model.write().overwrite().save("hdfs://path/to/model")

# Carregar modelo
from pyspark.ml import Pipeline
loaded_model = Pipeline.load("hdfs://path/to/model")
```

#### 8.2 Streaming ML
```python
# ML em tempo real
streaming_query = df.writeStream \
    .foreachBatch(lambda batch_df, batch_id: model.transform(batch_df)) \
    .start()
```

## Exercícios Práticos

### Exercício 1: Detecção de Anomalias
Implemente um sistema de detecção de anomalias usando Isolation Forest distribuído para identificar transações suspeitas.

### Exercício 2: Classificação de Texto
Desenvolva um classificador de sentimentos usando MLlib para analisar reviews de produtos em larga escala.

### Exercício 3: Sistema de Recomendação Híbrido
Combine Collaborative Filtering com Content-based filtering para criar um sistema de recomendação mais robusto.

### Exercício 4: Previsão de Séries Temporais
Use MLlib para prever vendas futuras considerando múltiplas variáveis e sazonalidade.

## Projeto Final

Desenvolva uma plataforma completa de ML que inclua:

1. **Pipeline de ETL** para preparação de dados
2. **Feature Store** distribuído
3. **Treinamento automatizado** de modelos
4. **Avaliação e validação** distribuída
5. **Deployment** em ambiente de produção
6. **Monitoramento** de performance em tempo real

## Recursos Adicionais

### Documentação Oficial
- [Spark MLlib Guide](https://spark.apache.org/docs/latest/ml-guide.html)
- [PySpark ML API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.ml.html)

### Livros Recomendados
- "Learning Spark" - Holden Karau
- "High Performance Spark" - Holden Karau
- "Spark: The Definitive Guide" - Bill Chambers

### Cursos Online
- Databricks Academy
- Coursera: Big Data Analysis with Scala and Spark
- edX: Introduction to Apache Spark

## Próximos Passos

Na próxima aula, exploraremos:
- **Deep Learning Distribuído** com Spark e TensorFlow
- **MLOps** para Machine Learning em escala
- **Streaming Analytics** avançado
- **Graph Analytics** com GraphX
