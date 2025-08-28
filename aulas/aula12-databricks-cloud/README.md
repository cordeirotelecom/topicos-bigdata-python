# Aula 12: Databricks e Cloud Analytics - Plataforma Unificada de Big Data

## 🎯 Objetivos de Aprendizagem

Ao concluir esta aula, você será capaz de:

- Compreender a arquitetura do Databricks e data lakehouse
- Implementar soluções usando Delta Lake para versionamento de dados
- Desenvolver pipelines de streaming analytics em tempo real
- Utilizar MLflow para MLOps e gestão do ciclo de vida de modelos
- Criar notebooks colaborativos para análise de dados
- Implementar orquestração de workflows e agendamento de jobs
- Monitorar performance e otimizar custos na nuvem
- Integrar com serviços cloud (AWS, Azure, GCP)

## 📚 Conceitos Fundamentais

### 🏗️ Arquitetura Databricks

**Data Lakehouse:**
- Combina benefícios de data lakes e data warehouses
- ACID transactions em data lakes
- Schema enforcement e evolution
- Performance de warehouse com flexibilidade de lake

**Componentes Principais:**
- **Control Plane:** Gerenciamento de workspace e recursos
- **Data Plane:** Processamento de dados nos clusters
- **Unity Catalog:** Governança unificada de dados
- **Delta Lake:** Storage layer com versionamento

**Integração Cloud:**
- **AWS:** S3, IAM, VPC, EC2, RDS
- **Azure:** ADLS, AAD, VNet, VM, SQL Database
- **GCP:** Cloud Storage, IAM, VPC, Compute Engine

### 📊 Delta Lake - Storage Evolutivo

**Características Principais:**
- **ACID Transactions:** Garantia de consistência
- **Time Travel:** Consultas históricas por versão/timestamp
- **Schema Evolution:** Mudanças seguras de schema
- **Upsert Operations:** MERGE para CDC (Change Data Capture)
- **Data Lineage:** Rastreamento de origem dos dados

**Delta Log:**
```json
{
  "version": 0,
  "timestamp": 1640995200000,
  "operation": "WRITE",
  "operationMetrics": {
    "numFiles": 4,
    "numOutputRows": 1000000
  },
  "schema": "struct<id:string,name:string,timestamp:timestamp>"
}
```

### 🌊 Structured Streaming

**Conceitos Fundamentais:**
- **Micro-batching:** Processamento em pequenos lotes
- **Exactly-once Processing:** Garantia de processamento único
- **Checkpointing:** Recuperação de falhas
- **Watermarking:** Tratamento de dados atrasados

**Fontes Suportadas:**
- Apache Kafka
- Amazon Kinesis
- Azure Event Hubs
- File systems (S3, HDFS, etc.)
- TCP sockets

### 🤖 MLflow - MLOps Platform

**Componentes MLflow:**
- **Tracking:** Registro de experimentos e métricas
- **Projects:** Empacotamento de código ML
- **Models:** Gestão de modelos e deployment
- **Registry:** Versionamento e stage de modelos

**Lifecycle do Modelo:**
1. **Experimentation:** Tracking de runs
2. **Staging:** Validação de modelos
3. **Production:** Deploy em produção
4. **Monitoring:** Observabilidade contínua

## 🛠️ Implementação Técnica

### Estrutura da Plataforma

```python
class DatabricksAnalyticsPlatform:
    """
    Simulador completo do ambiente Databricks
    
    Funcionalidades:
    - Delta Lake operations
    - Streaming analytics
    - MLflow integration
    - Notebook management
    - Job scheduling
    - Cost optimization
    """
```

### 📊 Delta Lake Operations

**Criação de Tabela:**
```python
def create_delta_table(self, table_name, schema, partitions=None):
    # Cria tabela Delta com schema definido
    table_info = {
        'name': table_name,
        'schema': schema,
        'partitions': partitions,
        'location': f"{self.delta_path}/{table_name}",
        'format': 'DELTA',
        'version': 0
    }
    
    # Gera dados baseados no schema
    sample_data = self._generate_sample_data(schema, 10000)
    
    return table_info
```

**UPSERT (MERGE) Operations:**
```python
def upsert_delta_table(self, table_name, new_data, merge_condition):
    # Simula operação MERGE
    current_data = self.datasets[table_name]['data']
    
    # Merge baseado na condição
    merged_data = pd.concat([current_data, new_data]).drop_duplicates(
        subset=merge_condition.split('=')[0].strip(), 
        keep='last'
    )
    
    # Incrementa versão
    new_version = current_version + 1
    self._update_version_history(table_name, new_version, 'MERGE')
    
    return merged_data
```

**Time Travel Queries:**
```python
def time_travel_query(self, table_name, version=None, timestamp=None):
    # Consulta versão específica ou por timestamp
    versions = self.datasets[table_name]['versions']
    
    if version is not None:
        target_version = self._find_version(versions, version)
    elif timestamp is not None:
        target_version = self._find_version_by_timestamp(versions, timestamp)
    else:
        target_version = versions[-1]  # Mais recente
    
    return self._get_data_for_version(table_name, target_version)
```

### 🌊 Streaming Analytics

**Configuração de Stream:**
```python
def create_streaming_job(self, job_name, source_config, sink_config, processing_logic):
    job_config = {
        'name': job_name,
        'source': source_config,
        'sink': sink_config,
        'processing': processing_logic,
        'status': 'RUNNING',
        'checkpoints': []
    }
    
    # Conecta à fonte de dados
    if source_config['type'] == 'kafka':
        self._connect_kafka_source(source_config)
    elif source_config['type'] == 'kinesis':
        self._connect_kinesis_source(source_config)
    
    # Inicia processamento
    self._start_stream_processing(job_config)
    
    return job_config
```

**Processamento em Tempo Real:**
```python
def _simulate_stream_processing(self, job_config):
    # Processa batches de dados em tempo real
    for batch in range(5):
        print(f"Processando batch {batch + 1}...")
        
        # Aplica transformações
        if 'aggregation' in job_config['processing']:
            self._apply_aggregations()
        if 'windowing' in job_config['processing']:
            self._apply_windowing()
        if 'filtering' in job_config['processing']:
            self._apply_filters()
        
        # Atualiza checkpoint
        self._update_checkpoint(job_config, batch)
```

### 🤖 MLflow Integration

**Criação de Experimentos:**
```python
def create_ml_experiment(self, experiment_name, model_type, dataset_name, parameters):
    experiment_config = {
        'name': experiment_name,
        'model_type': model_type,
        'dataset': dataset_name,
        'parameters': parameters,
        'runs': []
    }
    
    # Executa treinamento
    run_info = self._simulate_ml_training(experiment_config)
    experiment_config['runs'].append(run_info)
    
    return experiment_config
```

**Treinamento de Modelos:**
```python
def _simulate_ml_training(self, experiment_config):
    model_type = experiment_config['model_type']
    parameters = experiment_config['parameters']
    
    # Simula diferentes algoritmos
    if model_type == 'random_forest':
        accuracy = np.random.uniform(0.85, 0.95)
    elif model_type == 'xgboost':
        accuracy = np.random.uniform(0.88, 0.96)
    elif model_type == 'neural_network':
        accuracy = np.random.uniform(0.82, 0.94)
    
    # Registra métricas
    metrics = {
        'accuracy': accuracy,
        'precision': accuracy + np.random.normal(0, 0.02),
        'recall': accuracy + np.random.normal(0, 0.02),
        'f1_score': accuracy + np.random.normal(0, 0.01)
    }
    
    return {
        'run_id': f"run_{len(experiment_config['runs']) + 1}",
        'parameters': parameters,
        'metrics': metrics,
        'status': 'FINISHED'
    }
```

**Model Deployment:**
```python
def deploy_model(self, experiment_name, run_id, deployment_target="staging"):
    # Configura deployment
    deployment_config = {
        'model_name': f"{experiment_name}_model",
        'version': self._get_next_model_version(experiment_name),
        'target': deployment_target,
        'endpoint_url': f"https://model-serving.databricks.com/{experiment_name}",
        'status': 'ACTIVE'
    }
    
    # Registra no model registry
    self._register_model(experiment_name, deployment_config)
    
    return deployment_config
```

### 📓 Notebook Management

**Criação de Notebooks:**
```python
def create_notebook(self, notebook_name, language="python"):
    notebook_config = {
        'name': notebook_name,
        'language': language,
        'created_at': datetime.now(),
        'cells': self._create_example_cells(language),
        'collaborators': ['user@company.com'],
        'cluster_id': self.databricks.cluster_id
    }
    
    return notebook_config
```

**Células de Exemplo (Python):**
```python
def _create_example_cells(self, language):
    if language == "python":
        return [
            {
                'type': 'markdown',
                'content': f"# {notebook_name}\n\nAnálise de Big Data"
            },
            {
                'type': 'code',
                'content': "import pandas as pd\nimport numpy as np\nfrom pyspark.sql import SparkSession"
            },
            {
                'type': 'code',
                'content': "spark = SparkSession.builder.appName('Analysis').getOrCreate()"
            }
        ]
    elif language == "sql":
        return [
            {
                'type': 'sql',
                'content': "SELECT COUNT(*) FROM my_table"
            }
        ]
```

### ⏰ Job Orchestration

**Agendamento de Jobs:**
```python
def schedule_job(self, job_name, notebook_path, schedule, cluster_config):
    job_config = {
        'name': job_name,
        'notebook_path': notebook_path,
        'schedule': schedule,
        'cluster_config': cluster_config,
        'status': 'ACTIVE',
        'next_run': self._calculate_next_run(schedule)
    }
    
    return job_config
```

**Cálculo de Próxima Execução:**
```python
def _calculate_next_run(self, schedule):
    now = datetime.now()
    
    if schedule == "daily":
        return now + timedelta(days=1)
    elif schedule == "hourly":
        return now + timedelta(hours=1)
    elif schedule.startswith("cron"):
        return self._parse_cron_schedule(schedule)
    
    return now + timedelta(hours=1)
```

### 📈 Monitoring & Observability

**Monitoramento de Cluster:**
```python
def monitor_cluster_performance(self, duration_minutes=5):
    metrics_history = []
    
    for minute in range(duration_minutes):
        # Coleta métricas simuladas
        metrics = {
            'timestamp': datetime.now(),
            'cpu_utilization': np.random.uniform(30, 90),
            'memory_utilization': np.random.uniform(40, 85),
            'disk_io': np.random.uniform(10, 60),
            'active_jobs': np.random.randint(0, 5)
        }
        
        metrics_history.append(metrics)
        self._analyze_performance_metrics(metrics)
    
    return metrics_history
```

**Análise de Performance:**
```python
def _analyze_performance_metrics(self, metrics):
    # Alertas baseados em thresholds
    if metrics['cpu_utilization'] > 80:
        print("⚠️ Alto uso de CPU - considere scaling up")
    if metrics['memory_utilization'] > 80:
        print("⚠️ Alto uso de memória - considere mais RAM")
    if metrics['active_jobs'] > 10:
        print("⚠️ Muitos jobs ativos - possível bottleneck")
```

### 💰 Cost Optimization

**Análise de Custos:**
```python
def optimize_cluster_cost(self, workload_pattern):
    recommendations = []
    
    if workload_pattern == "batch_processing":
        recommendations.extend([
            "Usar Spot instances para reduzir custos",
            "Implementar auto-scaling baseado em carga",
            "Agendar jobs em horários de menor custo"
        ])
    elif workload_pattern == "interactive_analytics":
        recommendations.extend([
            "Usar clusters persistentes durante horário comercial",
            "Implementar auto-termination para períodos ociosos",
            "Considerar instance types otimizadas"
        ])
    
    # Calcula economia potencial
    current_cost = np.random.uniform(1000, 5000)
    potential_savings = np.random.uniform(0.15, 0.40)
    estimated_savings = current_cost * potential_savings
    
    return {
        'current_cost': current_cost,
        'potential_savings_percent': potential_savings * 100,
        'estimated_monthly_savings': estimated_savings,
        'recommendations': recommendations
    }
```

## 📊 Casos de Uso Avançados

### 🛒 E-commerce Real-time Analytics

```python
# Pipeline de análise em tempo real para e-commerce
def ecommerce_realtime_pipeline():
    """
    Pipeline completo para analytics de e-commerce:
    1. Streaming de eventos de navegação
    2. Processamento em tempo real
    3. Recomendações personalizadas
    4. Dashboard em tempo real
    """
    
    # Configuração de streaming
    source_config = {
        'type': 'kafka',
        'brokers': 'localhost:9092',
        'topics': ['page_views', 'purchases', 'cart_events']
    }
    
    # Processamento com janelas temporais
    processing_logic = """
    SELECT 
        user_id,
        product_id,
        COUNT(*) as view_count,
        WINDOW(timestamp, '5 minutes') as window
    FROM page_views 
    GROUP BY user_id, product_id, WINDOW(timestamp, '5 minutes')
    """
    
    # Sink para Delta Lake
    sink_config = {
        'type': 'delta',
        'table': 'user_behavior_analytics',
        'mode': 'append'
    }
```

### 🏥 Healthcare Data Lakehouse

```python
# Sistema de análise para dados de saúde
def healthcare_analytics_platform():
    """
    Plataforma para análise de dados de saúde:
    1. Ingestão segura de dados de pacientes
    2. Processamento HIPAA-compliant
    3. ML para diagnóstico assistido
    4. Dashboards para profissionais de saúde
    """
    
    # Schema para dados de pacientes
    patient_schema = {
        'patient_id': 'string',
        'age': 'integer',
        'gender': 'string',
        'diagnosis_codes': 'array<string>',
        'lab_results': 'map<string,double>',
        'visit_date': 'timestamp'
    }
    
    # Configuração com criptografia
    encryption_config = {
        'key_vault': 'healthcare-keys',
        'encryption_key': 'patient-data-key',
        'access_control': 'rbac'
    }
```

### 🌍 IoT Data Processing

```python
# Processamento de dados IoT em larga escala
def iot_data_platform():
    """
    Plataforma para processamento de dados IoT:
    1. Ingestão de milhões de sensores
    2. Detecção de anomalias em tempo real
    3. Manutenção preditiva
    4. Otimização de energia
    """
    
    # Schema para dados de sensores
    sensor_schema = {
        'device_id': 'string',
        'sensor_type': 'string',
        'timestamp': 'timestamp',
        'value': 'double',
        'unit': 'string',
        'location': 'struct<lat:double,lon:double>',
        'metadata': 'map<string,string>'
    }
    
    # Processamento com detecção de anomalias
    anomaly_detection = """
    SELECT *,
        CASE 
            WHEN ABS(value - AVG(value) OVER (
                PARTITION BY device_id, sensor_type 
                ORDER BY timestamp 
                ROWS BETWEEN 100 PRECEDING AND CURRENT ROW
            )) > 3 * STDDEV(value) OVER (
                PARTITION BY device_id, sensor_type 
                ORDER BY timestamp 
                ROWS BETWEEN 100 PRECEDING AND CURRENT ROW
            ) THEN 'ANOMALY'
            ELSE 'NORMAL'
        END as status
    FROM sensor_data
    """
```

## 🎯 Exercícios Práticos

### Exercício 1: Data Lakehouse para Varejo
```python
# Implemente um data lakehouse completo para varejo
def retail_lakehouse_project():
    """
    Objetivos:
    1. Criar tabelas Delta para vendas, produtos, clientes
    2. Implementar CDC para sincronização de dados
    3. Criar pipeline de streaming para eventos em tempo real
    4. Desenvolver modelos de ML para previsão de vendas
    5. Criar dashboard executivo
    """
    
    # Tabelas principais
    tables = {
        'sales': ['transaction_id', 'customer_id', 'product_id', 'amount', 'timestamp'],
        'products': ['product_id', 'name', 'category', 'price', 'inventory'],
        'customers': ['customer_id', 'name', 'segment', 'location', 'signup_date']
    }
    
    # Pipeline de ML
    ml_pipeline = {
        'demand_forecasting': 'time_series_model',
        'customer_segmentation': 'clustering_model',
        'price_optimization': 'regression_model'
    }
```

### Exercício 2: Plataforma de Streaming Media
```python
# Desenvolva analytics para plataforma de streaming
def streaming_media_analytics():
    """
    Objetivos:
    1. Processar eventos de visualização em tempo real
    2. Sistema de recomendação baseado em comportamento
    3. Análise de engajamento e churn
    4. A/B testing para interface
    5. Otimização de conteúdo
    """
    
    # Eventos de streaming
    events = [
        'video_start', 'video_pause', 'video_stop', 
        'video_complete', 'search', 'like', 'share'
    ]
    
    # Métricas em tempo real
    realtime_metrics = [
        'concurrent_viewers', 'popular_content', 
        'engagement_rate', 'buffering_events'
    ]
```

### Exercício 3: Fintech Data Platform
```python
# Construa plataforma de dados para fintech
def fintech_data_platform():
    """
    Objetivos:
    1. Processamento de transações em tempo real
    2. Detecção de fraudes com ML
    3. Análise de risco de crédito
    4. Compliance e auditoria
    5. Análise de performance de portfólio
    """
    
    # Compliance requirements
    compliance = {
        'data_retention': '7_years',
        'encryption': 'AES_256',
        'audit_trail': 'immutable',
        'access_control': 'zero_trust'
    }
    
    # Modelos de risco
    risk_models = {
        'fraud_detection': 'gradient_boosting',
        'credit_scoring': 'neural_network',
        'market_risk': 'monte_carlo'
    }
```

## 🚀 Projeto Final: Plataforma Unificada de Analytics

### Especificações Completas

**Objetivo:** Desenvolver uma plataforma completa de analytics usando conceitos do Databricks

**Componentes Obrigatórios:**

1. **Data Lakehouse Architecture**
   - Delta Lake com múltiplas tabelas
   - Schema evolution e time travel
   - Data lineage e cataloging
   - Governance e access control

2. **Real-time Processing**
   - Streaming analytics com Kafka/Kinesis
   - Complex event processing
   - Real-time dashboards
   - Alert system

3. **MLOps Pipeline**
   - Automated model training
   - A/B testing framework
   - Model monitoring
   - Automated deployment

4. **Collaborative Environment**
   - Multi-language notebooks
   - Version control integration
   - Code review process
   - Documentation system

5. **Operations & Monitoring**
   - Cost optimization
   - Performance monitoring
   - SLA tracking
   - Incident management

**Critérios de Avaliação:**
- Arquitetura e design (25%)
- Implementação técnica (25%)
- MLOps e automation (20%)
- Monitoring e observability (15%)
- Documentação e apresentação (15%)

## 📊 Comparação com Outras Plataformas

### Databricks vs. Alternativas

| Característica | Databricks | Snowflake | AWS EMR | Azure Synapse |
|----------------|------------|-----------|---------|---------------|
| **Unified Analytics** | ✅ | ⚠️ | ⚠️ | ✅ |
| **Delta Lake** | ✅ | ❌ | ⚠️ | ⚠️ |
| **MLflow Integration** | ✅ | ❌ | ❌ | ⚠️ |
| **Collaborative Notebooks** | ✅ | ⚠️ | ❌ | ✅ |
| **Auto-scaling** | ✅ | ✅ | ✅ | ✅ |
| **Multi-cloud** | ✅ | ✅ | ❌ | ❌ |

### Quando Usar Databricks

**Ideal Para:**
- Data science e ML workflows
- Streaming analytics complexo
- Data lakehouse architecture
- Collaborative analytics
- Multi-cloud deployment

**Não Ideal Para:**
- Simple data warehousing
- Transactional workloads
- Real-time OLTP
- Very small datasets

## 🔗 Recursos Adicionais

### Certificações Databricks
- **Databricks Certified Data Engineer Associate**
- **Databricks Certified Data Scientist Associate**
- **Databricks Certified Machine Learning Professional**

### Laboratórios Práticos
```python
# Setup ambiente de laboratório
def setup_databricks_lab():
    # Community Edition (gratuita)
    community_url = "https://community.cloud.databricks.com"
    
    # Datasets de exemplo
    sample_datasets = [
        "retail_sales", "web_logs", "sensor_data", 
        "financial_transactions", "social_media"
    ]
    
    # Notebooks de exemplo
    example_notebooks = [
        "Delta_Lake_Intro", "Streaming_Analytics", 
        "MLflow_Tutorial", "Cost_Optimization"
    ]
```

### Integrações Cloud

**AWS Integration:**
```python
# Configuração AWS
aws_config = {
    'instance_profile': 'databricks-instance-profile',
    's3_bucket': 'my-data-lake',
    'vpc_id': 'vpc-12345678',
    'subnet_ids': ['subnet-12345678', 'subnet-87654321']
}
```

**Azure Integration:**
```python
# Configuração Azure
azure_config = {
    'service_principal': 'databricks-sp',
    'storage_account': 'mydatalake',
    'vnet_id': '/subscriptions/.../virtualNetworks/my-vnet',
    'subnet_name': 'databricks-private-subnet'
}
```

**GCP Integration:**
```python
# Configuração GCP
gcp_config = {
    'service_account': 'databricks-sa@project.iam.gserviceaccount.com',
    'storage_bucket': 'my-data-lake',
    'vpc_network': 'projects/my-project/global/networks/my-vpc',
    'subnet': 'projects/my-project/regions/us-central1/subnetworks/my-subnet'
}
```

## 🎉 Conclusão

O Databricks representa uma evolução significativa na área de Big Data Analytics, oferecendo:

**Principais Benefícios:**
- **Unificação:** Analytics, ML e BI em uma plataforma
- **Colaboração:** Notebooks compartilhados e versionados
- **Escalabilidade:** Auto-scaling baseado em demanda
- **Governança:** Unity Catalog para gestão unificada
- **Performance:** Otimizações automáticas do Spark

**Tendências Futuras:**
- **Lakehouse 2.0:** Ainda mais integração
- **AutoML Avançado:** Automação completa do ML
- **Real-time Everything:** Streaming como padrão
- **Serverless Computing:** Zero-ops infrastructure
- **AI-Driven Optimization:** IA para otimização automática

O futuro do Big Data está na simplificação e democratização das ferramentas avançadas, e o Databricks está na vanguarda dessa transformação.

---

**Professor:** Vagner Cordeiro  
**Disciplina:** Tópicos de Big Data em Python  
**Instituição:** Universidade do Estado de Santa Catarina (UDESC)
