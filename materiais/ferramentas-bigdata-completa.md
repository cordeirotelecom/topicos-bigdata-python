# 🛠️ Ferramentas de Big Data - Guia Completo

## **Categorias de Ferramentas**

### **🗄️ Armazenamento e Sistemas de Arquivos**

#### **Apache Hadoop HDFS**
**Descrição:** Sistema de arquivos distribuído para armazenamento de grandes volumes  
**Quando usar:** Dados estruturados e não estruturados em larga escala  
**Prós:** Tolerância a falhas, escalabilidade horizontal  
**Contras:** Latência alta para consultas em tempo real  

**Instalação Passo a Passo:**
```bash
# 1. Download do Hadoop
wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz

# 2. Extração
tar -xzf hadoop-3.3.4.tar.gz
sudo mv hadoop-3.3.4 /opt/hadoop

# 3. Configuração de variáveis
export HADOOP_HOME=/opt/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# 4. Configuração básica
# Editar core-site.xml, hdfs-site.xml, yarn-site.xml
```

**Caso Prático:** Armazenamento de logs de aplicações web de uma empresa de e-commerce

---

#### **Amazon S3**
**Descrição:** Serviço de armazenamento em nuvem escalável  
**Quando usar:** Data Lakes, backup, arquivamento  
**Prós:** Durabilidade 99.999999999%, integração com AWS  
**Contras:** Custos podem escalar rapidamente  

**Configuração:**
```python
import boto3

# Configuração do cliente S3
s3_client = boto3.client('s3',
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-east-1'
)

# Upload de arquivo
s3_client.upload_file('local_file.csv', 'bucket-name', 'path/file.csv')
```

---

### **⚡ Processamento de Dados**

#### **Apache Spark**
**Descrição:** Engine de processamento distribuído para Big Data  
**Quando usar:** Processamento batch e streaming, ML  
**Prós:** Velocidade, versatilidade, APIs múltiplas  
**Contras:** Uso intensivo de memória  

**Instalação e Configuração:**
```bash
# Instalação via pip
pip install pyspark

# Ou via conda
conda install pyspark

# Download standalone
wget https://archive.apache.org/dist/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz
tar -xzf spark-3.4.1-bin-hadoop3.tgz
```

**Exemplo Prático:**
```python
from pyspark.sql import SparkSession

# Criação da sessão Spark
spark = SparkSession.builder \
    .appName("BigDataAnalysis") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()

# Leitura de dados
df = spark.read.csv("hdfs://path/to/large_dataset.csv", header=True)

# Processamento
result = df.groupBy("category").agg({"sales": "sum"}).orderBy("category")
result.show()
```

**Caso Real:** Análise de transações bancárias para detecção de fraude

---

#### **Apache Kafka**
**Descrição:** Plataforma de streaming distribuída  
**Quando usar:** Streaming de dados em tempo real  
**Prós:** Baixa latência, alta throughput  
**Contras:** Complexidade de configuração  

**Instalação:**
```bash
# Download
wget https://downloads.apache.org/kafka/2.8.2/kafka_2.13-2.8.2.tgz
tar -xzf kafka_2.13-2.8.2.tgz

# Iniciar Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Iniciar Kafka
bin/kafka-server-start.sh config/server.properties
```

**Exemplo Python:**
```python
from kafka import KafkaProducer, KafkaConsumer
import json

# Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Envio de dados
producer.send('bigdata-topic', {'sensor_id': 1, 'temperature': 25.6})

# Consumer
consumer = KafkaConsumer(
    'bigdata-topic',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    print(f"Received: {message.value}")
```

---

### **🔍 Processamento de Consultas**

#### **Apache Hive**
**Descrição:** Data warehouse software para consultas SQL em Hadoop  
**Quando usar:** Análises batch em dados estruturados  
**Prós:** Interface SQL familiar, integração com Hadoop  
**Contras:** Latência alta  

**Instalação:**
```bash
# Download Hive
wget https://downloads.apache.org/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz
tar -xzf apache-hive-3.1.3-bin.tar.gz

# Configuração
export HIVE_HOME=/opt/hive
export PATH=$PATH:$HIVE_HOME/bin
```

**Exemplo de Uso:**
```sql
-- Criação de tabela externa
CREATE EXTERNAL TABLE sales_data (
    id INT,
    product_name STRING,
    price DOUBLE,
    quantity INT,
    sale_date STRING
)
STORED AS TEXTFILE
LOCATION '/user/data/sales/';

-- Query de análise
SELECT product_name, SUM(price * quantity) as revenue
FROM sales_data
WHERE sale_date >= '2023-01-01'
GROUP BY product_name
ORDER BY revenue DESC;
```

---

#### **Apache Drill**
**Descrição:** Engine SQL para exploração de dados  
**Quando usar:** Consultas ad-hoc em dados semi-estruturados  
**Prós:** Schema-free, múltiplas fontes de dados  
**Contras:** Limitações em joins complexos  

---

### **🏗️ Orquestração e Workflow**

#### **Apache Airflow**
**Descrição:** Plataforma para orquestração de workflows  
**Quando usar:** ETL complexos, pipelines de dados  
**Prós:** Interface visual, extensibilidade  
**Contras:** Curva de aprendizado íngreme  

**Instalação:**
```bash
# Instalação via pip
pip install apache-airflow

# Inicialização
airflow db init
airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com

# Iniciar webserver
airflow webserver --port 8080

# Iniciar scheduler
airflow scheduler
```

**Exemplo de DAG:**
```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def extract_data():
    # Lógica de extração
    pass

def transform_data():
    # Lógica de transformação
    pass

def load_data():
    # Lógica de carga
    pass

dag = DAG(
    'bigdata_etl_pipeline',
    default_args={
        'owner': 'data-team',
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    description='Pipeline ETL para Big Data',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False
)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag
)

extract_task >> transform_task >> load_task
```

---

### **📊 Bancos NoSQL**

#### **MongoDB**
**Descrição:** Banco de dados orientado a documentos  
**Quando usar:** Dados semi-estruturados, desenvolvimento ágil  
**Prós:** Flexibilidade de schema, escalabilidade horizontal  
**Contras:** Consistência eventual  

**Instalação:**
```bash
# Ubuntu/Debian
sudo apt-get install mongodb

# Usando Docker
docker run --name mongodb -p 27017:27017 -d mongo:latest
```

**Exemplo Python:**
```python
from pymongo import MongoClient
import pandas as pd

# Conexão
client = MongoClient('mongodb://localhost:27017/')
db = client['bigdata_db']
collection = db['sensor_data']

# Inserção de dados
sensor_data = {
    'sensor_id': 'TEMP001',
    'timestamp': datetime.now(),
    'temperature': 25.6,
    'humidity': 60.2,
    'location': {'lat': -23.5505, 'lng': -46.6333}
}
collection.insert_one(sensor_data)

# Consulta e conversão para DataFrame
cursor = collection.find({'sensor_id': 'TEMP001'})
df = pd.DataFrame(list(cursor))
```

---

#### **Apache Cassandra**
**Descrição:** Banco NoSQL distribuído  
**Quando usar:** Alta disponibilidade, write-heavy workloads  
**Prós:** Performance linear com escala  
**Contras:** Modelo de dados limitado  

---

### **☁️ Ferramentas Cloud**

#### **Amazon EMR**
**Descrição:** Plataforma Big Data gerenciada na AWS  
**Quando usar:** Processamento Spark/Hadoop sem gerenciar infraestrutura  
**Prós:** Configuração automática, integração AWS  
**Contras:** Vendor lock-in, custos  

**Configuração via CLI:**
```bash
# Criar cluster EMR
aws emr create-cluster \
    --name "BigData-Cluster" \
    --release-label emr-6.4.0 \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m5.xlarge \
                      InstanceGroupType=CORE,InstanceCount=2,InstanceType=m5.xlarge \
    --applications Name=Spark Name=Hadoop Name=Hive \
    --ec2-attributes KeyName=my-key-pair \
    --use-default-roles
```

---

#### **Google BigQuery**
**Descrição:** Data warehouse serverless  
**Quando usar:** Analytics em petabytes de dados  
**Prós:** Sem infraestrutura, SQL padrão  
**Contras:** Custos por consulta  

**Exemplo Python:**
```python
from google.cloud import bigquery
import pandas as pd

# Cliente BigQuery
client = bigquery.Client()

# Query
query = """
    SELECT product_category, SUM(sales_amount) as total_sales
    FROM `project.dataset.sales_table`
    WHERE sale_date >= '2023-01-01'
    GROUP BY product_category
    ORDER BY total_sales DESC
"""

# Executar e converter para DataFrame
df = client.query(query).to_dataframe()
```

---

### **🔧 Ferramentas de Desenvolvimento**

#### **Jupyter Notebooks**
**Descrição:** Ambiente interativo para análise de dados  
**Quando usar:** Exploração de dados, prototipagem  
**Prós:** Interatividade, visualizações inline  
**Contras:** Não adequado para produção  

**Configuração para Big Data:**
```bash
# Instalação com extensões
pip install jupyter jupyterlab
pip install pyspark findspark

# Configuração para Spark
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
```

---

#### **Apache Zeppelin**
**Descrição:** Notebook para analytics interativo  
**Quando usar:** Colaboração em análises Big Data  
**Prós:** Múltiplas linguagens, integração Spark  
**Contras:** Interface menos polida que Jupyter  

---

### **📈 Monitoramento e Visualização**

#### **Grafana**
**Descrição:** Plataforma de monitoramento e observabilidade  
**Quando usar:** Dashboards em tempo real  
**Prós:** Múltiplas fontes de dados, alertas  
**Contras:** Requer configuração de datasources  

#### **Apache Superset**
**Descrição:** Plataforma de visualização de dados  
**Quando usar:** Dashboards empresariais  
**Prós:** Interface web moderna, SQL Lab  
**Contras:** Curva de aprendizado  

---

## **🏗️ Arquiteturas de Referência**

### **Lambda Architecture**
```
Data Sources → [Batch Layer] → [Master Dataset] → [Batch Views]
             → [Speed Layer] → [Real-time Views]  → [Serving Layer]
```

### **Kappa Architecture**
```
Data Sources → [Stream Processing] → [Serving Layer]
```

### **Modern Data Stack**
```
Sources → [Ingestion] → [Storage] → [Transformation] → [Analytics] → [Activation]
```

---

## **📋 Guia de Seleção de Ferramentas**

### **Por Volume de Dados**
- **< 1GB:** Pandas, SQLite
- **1GB - 100GB:** PostgreSQL, MySQL
- **100GB - 10TB:** Spark, Clickhouse
- **> 10TB:** Hadoop, Cloud Data Warehouses

### **Por Velocidade de Processamento**
- **Batch (horas/dias):** Hadoop MapReduce
- **Near Real-time (minutos):** Spark Structured Streaming
- **Real-time (segundos):** Kafka Streams, Apache Flink

### **Por Tipo de Dados**
- **Estruturados:** Hive, BigQuery, Redshift
- **Semi-estruturados:** MongoDB, Elasticsearch
- **Não estruturados:** HDFS, S3, Azure Blob

---

## **🎯 Cases de Uso por Indústria**

### **E-commerce**
- **Recomendações:** Spark MLlib + Redis
- **Análise de clickstream:** Kafka + Elasticsearch
- **Fraud detection:** Spark Streaming + ML models

### **Fintech**
- **Risk assessment:** Hadoop + Hive + R/Python
- **Real-time trading:** Kafka + Apache Flink
- **Compliance reporting:** Airflow + Spark + BigQuery

### **IoT/Manufacturing**
- **Sensor data:** InfluxDB + Grafana
- **Predictive maintenance:** Spark + TensorFlow
- **Edge processing:** Apache NiFi + Edge computing

---

*Este guia é atualizado regularmente com as últimas versões e melhores práticas.*
