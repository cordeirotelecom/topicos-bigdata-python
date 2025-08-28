# CAPÍTULO 6: SPARK SQL E DATAFRAMES - ANÁLISE ESTRUTURADA DE DADOS

## 6.1 Introdução ao Spark SQL

O Spark SQL representa uma evolução natural do Apache Spark, introduzindo capacidades de processamento de dados estruturados que combinam a flexibilidade do Spark com a familiaridade e poder expressivo do SQL. Lançado como parte do Spark 1.0 em 2014, o Spark SQL democratizou ainda mais o acesso ao processamento de Big Data, permitindo que analistas e cientistas de dados utilizassem linguagens declarativas familiares.

### 6.1.1 A Evolução para Dados Estruturados

**Contexto Histórico**
Enquanto os RDDs forneciam uma abstração poderosa para processamento distribuído, eles apresentavam algumas limitações importantes:
- API de baixo nível que requeria conhecimento detalhado de programação distribuída
- Falta de otimizações automáticas de consultas
- Ausência de informações de schema que poderiam guiar otimizações
- Dificuldade para analistas de negócio que preferiam SQL

O Spark SQL foi desenvolvido para abordar essas limitações, introduzindo:
- **DataFrames**: Abstração de alto nível para dados estruturados
- **Catalyst Optimizer**: Motor de otimização de consultas baseado em regras
- **Tungsten Engine**: Geração de código e gerenciamento de memória otimizados
- **API SQL**: Interface familiar para usuários de bancos de dados relacionais

### 6.1.2 Vantagens do Processamento Estruturado

**1. Otimização Automática**
O Spark SQL inclui o Catalyst Optimizer, um otimizador de consultas baseado em árvores de expressão que aplica várias otimizações:
- **Predicate Pushdown**: Move filtros para próximo da fonte de dados
- **Projection Pushdown**: Seleciona apenas colunas necessárias
- **Constant Folding**: Avalia expressões constantes em tempo de compilação
- **Join Reordering**: Reordena joins para minimizar dados intermediários

**2. Performance Superior**
Através do projeto Tungsten, o Spark SQL obtém performance próxima ao código nativo:
- **Code Generation**: Gera código Java otimizado para operações específicas
- **Memory Management**: Gerenciamento de memória off-heap para reduzir garbage collection
- **Cache-Aware Computing**: Estruturas de dados otimizadas para hierarquia de cache

**3. Unificação de APIs**
O Spark SQL unifica diferentes interfaces de dados:
- **SQL nativo**: Consultas SQL padrão
- **DataFrame API**: Interface programática estruturada
- **Dataset API**: Interface tipada (Scala/Java)
- **Integração com RDDs**: Interoperabilidade com APIs de baixo nível

### 6.1.3 Casos de Uso Ideais

O Spark SQL é particularmente adequado para:

**Analytics e Business Intelligence**
- Relatórios complexos com agregações múltiplas
- Análises ad-hoc exploratórias
- Data warehousing e OLAP (Online Analytical Processing)
- Dashboards em tempo real

**ETL (Extract, Transform, Load)**
- Transformações complexas de dados
- Limpeza e normalização de datasets
- Integração de múltiplas fontes de dados
- Pipelines de processamento de dados

**Data Science**
- Preparação de dados para machine learning
- Feature engineering em larga escala
- Análise exploratória de dados
- Estatísticas descritivas de datasets massivos

## 6.2 DataFrames - A Nova Abstração

Os DataFrames representam uma abstração fundamental no Spark SQL, oferecendo uma interface de alto nível para trabalhar com dados estruturados. Inspirados nos DataFrames do R e pandas do Python, os DataFrames do Spark estendem esses conceitos para o processamento distribuído.

### 6.2.1 Conceitos Fundamentais

**Definição**
Um DataFrame é uma coleção distribuída de dados organizados em colunas nomeadas, similar a uma tabela em banco de dados relacional ou uma planilha. Cada DataFrame possui:
- **Schema**: Metadados que descrevem a estrutura dos dados
- **Particionamento**: Distribuição física dos dados através do cluster
- **Lineage**: Histórico de transformações para tolerância a falhas
- **Lazy Evaluation**: Execução adiada até que uma ação seja chamada

**Vantagens sobre RDDs**
1. **Schema Awareness**: Conhecimento da estrutura permite otimizações
2. **Type Safety**: Verificação de tipos em tempo de compilação (Datasets)
3. **Catalyst Optimization**: Otimizações automáticas de consultas
4. **Memory Efficiency**: Representação binária compacta
5. **Language Agnostic**: Mesma performance em Scala, Java, Python, R

### 6.2.2 Criação de DataFrames

DataFrames podem ser criados de várias maneiras:

**1. A partir de Fontes de Dados Externas**
```python
# Exemplo conceitual - não executável
# Arquivos Parquet, JSON, CSV, Avro
df = spark.read.parquet("hdfs://data/vendas.parquet")
df = spark.read.json("s3a://bucket/logs.json")
df = spark.read.csv("file:///local/data.csv", header=True, inferSchema=True)

# Bancos de dados relacionais
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost/mydb") \
    .option("dbtable", "vendas") \
    .load()
```

**2. A partir de RDDs**
```python
# Conversão de RDD para DataFrame
rdd = spark.sparkContext.parallelize([(1, "Alice", 25), (2, "Bob", 30)])
df = spark.createDataFrame(rdd, ["id", "name", "age"])
```

**3. A partir de Coleções Locais**
```python
# Criação direta
data = [(1, "Alice", 25), (2, "Bob", 30), (3, "Charlie", 35)]
df = spark.createDataFrame(data, ["id", "name", "age"])
```

### 6.2.3 Schema e Tipos de Dados

**Sistema de Tipos**
O Spark SQL possui um sistema robusto de tipos que mapeia para tipos de dados de diferentes linguagens:

- **Tipos Primitivos**: StringType, IntegerType, LongType, DoubleType, BooleanType
- **Tipos Complexos**: ArrayType, MapType, StructType
- **Tipos Temporais**: DateType, TimestampType
- **Tipos Decimais**: DecimalType para precisão arbitrária

**Schema Definition**
Schemas podem ser definidos explicitamente ou inferidos automaticamente:

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Schema explícito
schema = StructType([
    StructField("id", IntegerType(), False),  # Não nulo
    StructField("name", StringType(), True),  # Anulável
    StructField("age", IntegerType(), True)
])

# Inferência automática (menos eficiente)
df = spark.read.option("inferSchema", "true").csv("data.csv")
```

**Vantagens do Schema Explícito**
- Performance superior (evita passada extra para inferência)
- Validação de dados em tempo de ingestão
- Documentação implícita da estrutura dos dados
- Compatibilidade garantida entre diferentes execuções

### 6.2.4 Operações com DataFrames

**Transformações Fundamentais**

1. **Seleção de Colunas**
```python
# Seleção simples
df.select("name", "age")

# Seleção com expressões
df.select(col("age") + 1)
```

2. **Filtragem**
```python
# Filtros simples
df.filter(col("age") > 25)

# Filtros complexos
df.filter((col("age") > 25) & (col("name").startswith("A")))
```

3. **Agregações**
```python
# Agregações básicas
df.groupBy("department").agg(avg("salary"), count("*"))

# Agregações com janelas
from pyspark.sql.window import Window
window = Window.partitionBy("department").orderBy("salary")
df.withColumn("rank", row_number().over(window))
```

**Operações de Join**
DataFrames suportam vários tipos de joins otimizados:

- **Inner Join**: Retorna apenas registros correspondentes
- **Left/Right Outer Join**: Inclui registros não correspondentes de um lado
- **Full Outer Join**: Inclui todos os registros de ambos os lados
- **Cross Join**: Produto cartesiano (use com cuidado)

```python
# Join simples
vendas.join(produtos, vendas.produto_id == produtos.id)

# Join com múltiplas condições
vendas.join(clientes, 
    (vendas.cliente_id == clientes.id) & 
    (vendas.regiao == clientes.regiao))
```

### 6.2.5 Otimizações de Performance

**1. Predicate Pushdown**
O Catalyst automaticamente move filtros para próximo da fonte:
```python
# Esta consulta será otimizada automaticamente
df.filter(col("year") == 2023).select("sales", "region")
# O filtro será aplicado durante a leitura quando possível
```

**2. Projection Pushdown**
Apenas colunas necessárias são lidas:
```python
# Apenas colunas 'name' e 'age' serão lidas do armazenamento
df.select("name", "age").show()
```

**3. Join Optimization**
- **Broadcast Joins**: Para tabelas pequenas (< 10MB por padrão)
- **Sort-Merge Joins**: Para tabelas grandes com chaves ordenadas
- **Bucketed Joins**: Para tabelas pré-particionadas

**4. Adaptive Query Execution (AQE)**
Introduzido no Spark 3.0, adapta execução baseado em estatísticas runtime:
- Coalescimento dinâmico de partições
- Conversão dinâmica de joins
- Otimização de skew joins

## 6.3 Catalyst Optimizer - O Coração do Spark SQL

O Catalyst Optimizer é um dos componentes mais sofisticados do Apache Spark, responsável por transformar consultas SQL e operações DataFrame em planos de execução otimizados. Sua arquitetura baseada em árvores de expressão permite extensibilidade e aplicação sistemática de regras de otimização.

### 6.3.1 Arquitetura do Catalyst

**Fases de Otimização**
O Catalyst opera em quatro fases principais:

1. **Analysis**: Resolução de referências e validação de tipos
2. **Logical Optimization**: Aplicação de regras baseadas em lógica
3. **Physical Planning**: Seleção de algoritmos físicos
4. **Code Generation**: Geração de código Java otimizado

**Representação em Árvores**
Todas as expressões e consultas são representadas como árvores:
- **Leaf Nodes**: Valores constantes, referências de colunas
- **Internal Nodes**: Operadores como joins, agregações, filtros
- **Tree Transformations**: Regras que transformam árvores em árvores otimizadas

### 6.3.2 Otimizações Principais

**1. Rule-Based Optimization**
Aplicação sistemática de regras de otimização:

- **Constant Folding**: `1 + 2` → `3`
- **Predicate Pushdown**: Move filtros para próximo dos dados
- **Column Pruning**: Remove colunas desnecessárias
- **Boolean Expression Simplification**: `true AND x` → `x`

**2. Cost-Based Optimization (CBO)**
Usa estatísticas de tabelas para decisões de otimização:
- Seleção de algoritmos de join
- Ordem de joins em consultas multi-tabela
- Estimativa de cardinalidade de operações

**3. Join Optimization**
- **Join Reordering**: Reordena joins para minimizar dados intermediários
- **Join Selection**: Escolhe algoritmo ótimo (broadcast, sort-merge, hash)
- **Subquery Optimization**: Reescreve subqueries quando possível

### 6.3.3 Extensibilidade

**Custom Rules**
Desenvolvedores podem adicionar regras personalizadas:
```python
# Exemplo conceitual de regra customizada
class CustomOptimizationRule(Rule[LogicalPlan]):
    def apply(plan):
        # Lógica de otimização customizada
        return optimized_plan
```

**Data Source Optimization**
Fontes de dados podem implementar otimizações específicas:
- Pushdown de predicados para bancos de dados
- Otimizações específicas para formatos colunares
- Índices e estatísticas customizadas

## 6.4 Tungsten Engine - Performance Extrema

O Tungsten Engine, introduzido no Spark 1.4, representa um esforço fundamental para aproximar a performance do Spark ao código nativo. Através de técnicas avançadas de compilação e gerenciamento de memória, o Tungsten transformou o Spark SQL na engine de processamento analítico mais rápida do mercado.

### 6.4.1 Objetivos do Tungsten

**1. Memory Management**
- Reduzir overhead de garbage collection
- Aumentar densidade de dados na memória
- Implementar estruturas de dados cache-friendly

**2. Code Generation**
- Gerar código Java específico para consultas
- Eliminar overhead de interpretação
- Otimizar para arquiteturas de CPU modernas

**3. Cache-Aware Computing**
- Estruturas de dados que aproveitam hierarquia de cache
- Algoritmos que minimizam cache misses
- Processamento vetorizado quando possível

### 6.4.2 Inovações Técnicas

**1. Off-Heap Memory Management**
```
Heap Memory (JVM):        Off-Heap Memory (Tungsten):
[Object][Header][Data] →  [Data][Data][Data][Data]
      ^                           ^
   High overhead            Compact representation
```

Vantagens do off-heap:
- Redução de 2-5x no uso de memória
- Eliminação de garbage collection
- Serialização mais eficiente
- Melhor previsibilidade de performance

**2. Whole-Stage Code Generation**
Tradicional (interpretado):
```
for record in input:
    filtered = filter(record)
    if filtered:
        projected = project(filtered)
        emit(projected)
```

Tungsten (código gerado):
```java
// Código Java gerado automaticamente
public void processNext() {
    if (input.hasNext()) {
        InternalRow row = input.next();
        boolean filter_value = row.getInt(0) > 100;
        if (filter_value) {
            InternalRow project_row = new GenericInternalRow(2);
            project_row.setUTF8String(0, row.getUTF8String(1));
            project_row.setInt(1, row.getInt(2));
            consume(project_row);
        }
    }
}
```

**3. Vectorized Execution**
Para operações compatíveis, processa batches de registros:
- Utiliza instruções SIMD do processador
- Reduz overhead por registro
- Melhora utilização de cache

### 6.4.3 Impacto na Performance

**Benchmarks Comparativos**
O Tungsten obtém speedups significativos:
- **2-3x** mais rápido que Spark sem Tungsten
- **Competitivo** com sistemas nativos como Impala
- **10-100x** mais rápido que MapReduce tradicional

**Casos de Uso Otimizados**
- Agregações complexas
- Joins de tabelas grandes
- Operações com muitas expressões
- Processamento de strings e timestamps

## 6.5 Integração com Fontes de Dados

O Spark SQL se destaca pela capacidade de integrar seamlessly com diversas fontes de dados, desde sistemas de arquivos distribuídos até bancos de dados relacionais e NoSQL.

### 6.5.1 Data Sources API

**Arquitetura Unificada**
A Data Sources API fornece uma interface comum para:
- Leitura e escrita de dados
- Schema discovery
- Predicate pushdown
- Estatísticas de dados

**Implementações Nativas**
- **Parquet**: Formato colunar otimizado para analytics
- **Delta Lake**: Versioning e ACID para data lakes
- **JSON**: Dados semi-estruturados
- **Avro**: Serialização eficiente com schema evolution
- **ORC**: Formato colunar otimizado para Hive

### 6.5.2 Conectores de Bancos de Dados

**JDBC Connector**
Integração com bancos relacionais:
```python
# Exemplo conceitual
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost/database") \
    .option("dbtable", "sales") \
    .option("user", "username") \
    .option("password", "password") \
    .load()
```

**Otimizações para Bancos**
- **Predicate Pushdown**: Filtros executados no banco
- **Column Pruning**: Apenas colunas necessárias são transferidas
- **Partitioned Reads**: Leitura paralela baseada em partições

**Conectores Especializados**
- **Cassandra**: spark-cassandra-connector
- **MongoDB**: mongo-spark-connector
- **Elasticsearch**: elasticsearch-spark
- **Redis**: spark-redis

### 6.5.3 Formatos de Arquivo Otimizados

**Apache Parquet**
Vantagens para analytics:
- **Compressão**: Até 75% menor que formatos row-based
- **Column Pruning**: Lê apenas colunas necessárias
- **Predicate Pushdown**: Filtros aplicados durante leitura
- **Schema Evolution**: Suporte a mudanças de schema

**Delta Lake**
Extensão do Parquet com:
- **ACID Transactions**: Consistência em operações concorrentes
- **Schema Enforcement**: Validação automática de dados
- **Time Travel**: Acesso a versões históricas
- **Merge Operations**: Upserts eficientes

## 6.6 Análise Avançada com Window Functions

Window Functions representam uma das funcionalidades mais poderosas do Spark SQL, permitindo cálculos sofisticados que seriam complexos ou impossíveis com agregações tradicionais.

### 6.6.1 Conceitos de Window Functions

**Definição**
Window Functions operam sobre um conjunto de linhas relacionadas a cada linha, sem colapsar o resultado como GROUP BY:
- Cada linha mantém sua identidade
- Cálculos são feitos sobre uma "janela" de linhas
- Permitem rankings, moving averages, e análises comparativas

**Componentes de uma Window**
1. **PARTITION BY**: Define grupos de linhas
2. **ORDER BY**: Define ordenação dentro da partição
3. **Frame Specification**: Define quais linhas incluir no cálculo

### 6.6.2 Tipos de Window Functions

**1. Ranking Functions**
```sql
-- Exemplo conceitual SQL
SELECT 
    employee_id,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rank,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dense_rank,
    PERCENT_RANK() OVER (PARTITION BY department ORDER BY salary) as percentile
FROM employees
```

**2. Analytical Functions**
```sql
SELECT 
    date,
    sales,
    LAG(sales, 1) OVER (ORDER BY date) as previous_sales,
    LEAD(sales, 1) OVER (ORDER BY date) as next_sales,
    sales - LAG(sales, 1) OVER (ORDER BY date) as growth
FROM daily_sales
```

**3. Aggregate Functions**
```sql
SELECT 
    date,
    sales,
    SUM(sales) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as moving_7day_sum,
    AVG(sales) OVER (PARTITION BY MONTH(date)) as monthly_average
FROM daily_sales
```

### 6.6.3 Frame Specifications

**Tipos de Frames**
- **ROWS**: Baseado em número físico de linhas
- **RANGE**: Baseado em valores lógicos das colunas

**Especificações Comuns**
```sql
-- Todas as linhas da partição
ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING

-- Linha atual e 2 anteriores
ROWS BETWEEN 2 PRECEDING AND CURRENT ROW

-- Moving average de 30 dias
RANGE BETWEEN INTERVAL 30 DAYS PRECEDING AND CURRENT ROW
```

## 6.7 Performance Tuning e Otimização

O Spark SQL oferece múltiplas avenidas para otimização de performance, desde configurações de infraestrutura até técnicas avançadas de modeling de dados.

### 6.7.1 Configurações Críticas

**Memory Management**
```python
# Configurações conceituais
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
```

**Join Optimization**
```python
# Broadcast joins para tabelas pequenas
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "200MB")

# Número de partições para shuffle
spark.conf.set("spark.sql.shuffle.partitions", "400")
```

### 6.7.2 Estratégias de Particionamento

**Partitioning by Columns**
```python
# Particionamento por colunas frequentemente filtradas
df.write \
  .partitionBy("year", "month") \
  .parquet("partitioned_data")
```

**Bucketing**
```python
# Bucketing para otimizar joins
df.write \
  .bucketBy(10, "user_id") \
  .saveAsTable("user_events")
```

### 6.7.3 Caching Strategies

**DataFrame Caching**
```python
# Cache para reutilização
df.cache()  # MEMORY_AND_DISK por padrão
df.persist(StorageLevel.MEMORY_ONLY)  # Apenas memória
```

**SQL Cache**
```sql
-- Cache de tabelas SQL
CACHE TABLE expensive_query AS
SELECT * FROM large_table WHERE complex_condition;
```

## 6.8 Conclusão

O Spark SQL e DataFrames representam uma evolução fundamental no processamento de Big Data, combinando a familiaridade do SQL com a potência do processamento distribuído. Através do Catalyst Optimizer e Tungsten Engine, o Spark SQL oferece performance competitiva com sistemas nativos, mantendo a flexibilidade e facilidade de uso que tornaram o Spark popular.

### 6.8.1 Principais Benefícios

**Democratização do Big Data**
- Interface familiar para analistas de negócio
- Redução da curva de aprendizado
- Integração com ferramentas de BI existentes

**Performance Superior**
- Otimizações automáticas via Catalyst
- Geração de código nativo via Tungsten
- Adaptive Query Execution para otimização runtime

**Flexibilidade Arquitetural**
- Suporte a múltiplas fontes de dados
- Escalabilidade horizontal transparente
- Integração com ecossistema Spark

### 6.8.2 Tendências Futuras

**Machine Learning Integration**
- Feature stores nativos
- AutoML integrado
- Pipelines unificados de dados e ML

**Cloud-Native Optimization**
- Otimizações para storage em nuvem
- Serverless execution
- Kubernetes-native deployment

**Real-Time Analytics**
- Continuous queries
- Streaming SQL
- Delta Live Tables

O Spark SQL estabeleceu-se como o padrão de facto para processamento analítico distribuído, e sua evolução contínua garante relevância para os desafios futuros do Big Data e analytics em escala empresarial.

---

**Próximo Capítulo**: Streaming Analytics com Spark - Processamento em Tempo Real
