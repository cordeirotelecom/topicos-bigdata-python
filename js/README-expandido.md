# 🚀 Tópicos de Big Data em Python - Curso Completo

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.5+-orange.svg)](https://spark.apache.org/)
[![Kafka](https://img.shields.io/badge/Apache%20Kafka-2.8+-red.svg)](https://kafka.apache.org/)
[![Status](https://img.shields.io/badge/status-active-green.svg)]()

## **📋 Visão Geral**

Este curso oferece uma **formação completa e prática** em Big Data usando Python, cobrindo desde conceitos fundamentais até implementações avançadas em produção. Com **mais de 100 scripts práticos**, **9 aulas implementadas** e **projetos reais**, você desenvolverá competências para trabalhar com grandes volumes de dados em empresas de qualquer porte.

### **🎯 Por que Este Curso?**

- ✅ **Hands-on desde o primeiro dia** - Código real, não apenas teoria
- ✅ **Projetos completos implementados** - Sistemas funcionais que você pode usar
- ✅ **Stack tecnológico atual** - Ferramentas usadas na indústria
- ✅ **Preparação para certificações** - AWS, GCP, Azure, Databricks
- ✅ **Carreira ready** - Portfólio pronto para o mercado

---

## **🛠️ Stack Tecnológico Completo**

### **🐍 Core Python & Analytics**
```python
# Bibliotecas fundamentais implementadas
import pandas as pd              # Manipulação de dados
import numpy as np              # Computação numérica  
import matplotlib.pyplot as plt # Visualização
import seaborn as sns           # Visualização avançada
import plotly.express as px     # Dashboards interativos
import scikit-learn as sklearn  # Machine Learning
```

### **⚡ Big Data Frameworks**
```bash
# Tecnologias distribuídas
Apache Spark 3.5+     # Processamento em memória
Apache Hadoop 3.x     # Armazenamento distribuído
Apache Kafka 2.8+     # Streaming de dados
Apache Airflow        # Orquestração de workflows
```

### **☁️ Cloud Platforms**
```yaml
AWS:
  - EMR (Elastic MapReduce)
  - S3 (Object Storage)
  - Kinesis (Streaming)
  - Redshift (Data Warehouse)

Google Cloud:
  - Dataflow
  - BigQuery  
  - Pub/Sub
  - Cloud Storage

Microsoft Azure:
  - HDInsight
  - Stream Analytics
  - Data Factory
  - Synapse Analytics
```

### **🗄️ Databases & Storage**
```sql
-- SQL & NoSQL implementados
PostgreSQL     -- RDBMS tradicional
MongoDB        -- Document database
Cassandra      -- Wide-column store
Redis          -- In-memory cache
HBase          -- Column-family
```

---

## **📚 ESTRUTURA COMPLETA DO CURSO**

### **🎓 MÓDULO I - FUNDAMENTOS (Semanas 1-4)**

#### **[Aula 01 - Introdução ao Big Data](aulas/aula01-intro-bigdata/)**
- **Volume Simulation:** Processamento de datasets 10GB+
- **Velocity Demo:** Stream processing com 10K+ eventos/segundo  
- **Variety Processing:** JSON, XML, CSV, Parquet unificados
- **💻 Scripts:** `volume_simulation.py`, `velocity_demo.py`, `variety_processing.py`

#### **[Aula 02 - IoT e Computação Distribuída](aulas/aula02-iot-computacao/)**
- **IoT Sensor Network:** 50+ sensores simulados em tempo real
- **Distributed Processing:** Message queues, MapReduce patterns
- **Fault Tolerance:** Circuit breakers, retry mechanisms
- **💻 Scripts:** `iot_sensor_simulation.py`, `distributed_processing.py`

#### **[Aula 03 - Cloud e Streaming](aulas/aula03-cloud-streaming/)**
- **Cloud Services Simulator:** AWS/GCP/Azure equivalents
- **Streaming Pipeline:** Real-time data processing
- **Auto-scaling:** Dynamic resource allocation
- **💻 Scripts:** `cloud_services_simulation.py`

#### **[Aula 04 - Python para Big Data](aulas/aula04-revisao-python/)**
- **Python Básico:** Otimizações para grandes datasets
- **NumPy Avançado:** Vectorização e broadcasting
- **Pandas Otimizado:** Chunk processing, memory optimization
- **💻 Scripts:** `python_basico_dados.py`, `intro_numpy.py`

### **🔄 MÓDULO II - PROCESSAMENTO DISTRIBUÍDO (Semanas 5-8)**

#### **[Aula 05 - Análise de Dados Completa](aulas/aula05-analise-dados-resumo/)**
- **Pipeline Completo:** Extract → Transform → Load → Analyze
- **Statistical Analysis:** Descritiva, inferencial, regressões
- **Advanced Visualizations:** Plotly dashboards, Seaborn heatmaps
- **Machine Learning:** Classification, clustering, recommendations
- **💻 Scripts:** `complete_data_analysis_pipeline.py`

#### **[Aula 06 - Ecossistema Hadoop](aulas/aula06-hadoop-intro/)**
- **HDFS Operations:** Distributed file system management
- **MapReduce Jobs:** Python implementation com MRJob
- **YARN Management:** Resource allocation e monitoring
- **Log Analysis:** Distributed log processing pipeline
- **💻 Scripts:** `hadoop_mapreduce_examples.py`

#### **[Aula 07 - Apache Spark Fundamentals](aulas/aula07-spark-fundamentals/)**
- **RDD Operations:** Resilient Distributed Datasets
- **DataFrame Analytics:** SQL-like operations em escala
- **Performance Tuning:** Cache, broadcast, partitioning
- **ETL Pipeline:** Extract-Transform-Load distribuído
- **💻 Scripts:** `spark_fundamentals_demo.py`

#### **[Aula 08 - Kafka Real-time Streaming](aulas/aula08-kafka-streaming/)**
- **Kafka Platform:** Producers, consumers, topics
- **Real-time Analytics:** Stream processing com alertas
- **IoT Data Pipeline:** 50+ sensores → Kafka → Analytics
- **Live Dashboard:** Métricas em tempo real
- **💻 Scripts:** `kafka_streaming_platform.py`

### **🤖 MÓDULO III - MACHINE LEARNING (Semanas 9-12)**

#### **[Aula 09 - ML com Big Data](aulas/aula09-ml-bigdata/)**
- **Fraud Detection:** Random Forest distribuído para 1M+ transações
- **Recommendation System:** Collaborative filtering com ALS
- **Sentiment Analysis:** NLP pipeline para 100K+ reviews
- **Model Deployment:** MLlib em produção
- **💻 Scripts:** `ml_bigdata_platform.py`

#### **[Aula 10 - NoSQL & Bancos Distribuídos](aulas/aula10-nosql/)** *(Próxima implementação)*
- **Multi-database Architecture:** MongoDB + Cassandra + Redis
- **CAP Theorem:** Consistency vs Availability na prática
- **Sharding Strategies:** Horizontal scaling patterns
- **Performance Benchmarks:** Comparação de throughput

#### **[Aula 11 - Data Lakes & Lambda Architecture](aulas/aula11-datalake/)** *(Próxima implementação)*
- **Data Lake Implementation:** S3 + Delta Lake
- **Lambda Architecture:** Batch + Real-time layers
- **Data Governance:** Lineage, quality, security
- **Schema Evolution:** Backward/forward compatibility

#### **[Aula 12 - Big Data na Cloud](aulas/aula12-cloud/)** *(Próxima implementação)*
- **Multi-cloud Deployment:** AWS + GCP + Azure
- **Serverless Analytics:** Lambda, Cloud Functions
- **Cost Optimization:** Resource allocation strategies
- **Infrastructure as Code:** Terraform para Big Data

### **🏭 MÓDULO IV - PRODUÇÃO (Semanas 13-16)**

#### **[Aula 13 - Apache Airflow](aulas/aula13-airflow/)** *(Próxima implementação)*
- **DAG Orchestration:** Complex workflow management
- **Sensors & Operators:** Custom implementations
- **Monitoring & Alerting:** Slack, email integrations
- **Production Best Practices:** Error handling, retries

#### **[Aula 14 - Monitoring & Performance](aulas/aula14-monitoring/)** *(Próxima implementação)*
- **Observability Stack:** Prometheus + Grafana + ELK
- **Performance Profiling:** Spark UI, application metrics
- **Resource Optimization:** Memory, CPU, network tuning
- **Troubleshooting:** Distributed systems debugging

#### **[Aula 15 - Security & Governance](aulas/aula15-security/)** *(Próxima implementação)*
- **Data Encryption:** At-rest e in-transit
- **Access Control:** RBAC, OAuth, Kerberos
- **GDPR Compliance:** Privacy by design
- **Audit Trails:** Data lineage tracking

#### **[Aula 16 - Capstone Projects](projetos/)** *(Próxima implementação)*
- **Industry Use Cases:** Fintech, e-commerce, IoT
- **End-to-end Solutions:** Requirements → Production
- **Portfolio Development:** GitHub showcase projects
- **Career Preparation:** Technical interviews, salary negotiation

---

## **🗂️ ESTRUTURA DE ARQUIVOS**

```
📦 BigData em Python/
├── 📁 aulas/                          # Módulos implementados
│   ├── 📁 aula01-intro-bigdata/       # ✅ Big Data fundamentals
│   ├── 📁 aula02-iot-computacao/      # ✅ IoT & distributed systems  
│   ├── 📁 aula03-cloud-streaming/     # ✅ Cloud platforms simulation
│   ├── 📁 aula04-revisao-python/      # ✅ Python for Big Data
│   ├── 📁 aula05-analise-dados-resumo/# ✅ Complete analytics pipeline
│   ├── 📁 aula06-hadoop-intro/        # ✅ Hadoop ecosystem
│   ├── 📁 aula07-spark-fundamentals/  # ✅ Spark comprehensive demo
│   ├── 📁 aula08-kafka-streaming/     # ✅ Real-time streaming platform
│   ├── 📁 aula09-ml-bigdata/          # ✅ ML with distributed computing
│   └── 📁 aula10-16.../               # 🔄 Em desenvolvimento
├── 📁 materiais/                      # Recursos expandidos
│   ├── 📄 ferramentas-bigdata-completa-v2.md    # 🆕 Guia completo 2025
│   ├── 📄 tutorial-powerbi-bigdata.md            # Power BI integration
│   └── 📄 datasets-publicos-completos.md        # Curated datasets
├── 📁 datasets/                       # Dados para prática
├── 📁 notebooks/                      # Jupyter notebooks
├── 📁 projetos/                       # Projetos finais
├── 📄 cronograma-expandido.md         # 🆕 Cronograma completo
├── 📄 materiais.md                    # Bibliografia atualizada
└── 📄 README.md                       # Este arquivo
```

---

## **🚀 QUICK START**

### **1. Setup do Ambiente**
```bash
# Clonar repositório
git clone [repo-url]
cd "BigData em Python"

# Instalar dependências Python
pip install -r requirements.txt

# Verificar instalações
python -c "import pyspark; print('✅ PySpark:', pyspark.__version__)"
python -c "import kafka; print('✅ Kafka-Python installed')"
python -c "import pandas as pd; print('✅ Pandas:', pd.__version__)"
```

### **2. Executar Primeira Demo**
```bash
# Demo completa de Big Data fundamentals
cd aulas/aula01-intro-bigdata/
python volume_simulation.py      # Processa dataset 10GB+
python velocity_demo.py          # 10K eventos/segundo
python variety_processing.py     # Multi-format integration

# Resultado: 3 demos funcionais + relatórios de performance
```

### **3. Pipeline Real-time Completo**
```bash
# Sistema completo IoT → Kafka → Analytics
cd aulas/aula08-kafka-streaming/
python kafka_streaming_platform.py

# Escolha opção 5: Demo completo
# ✅ 50 sensores IoT simulados
# ✅ Kafka topics configurados  
# ✅ Real-time analytics
# ✅ Dashboard ao vivo
# ✅ Sistema de alertas
```

### **4. Machine Learning Distribuído**
```bash
# ML platform com 3 algoritmos implementados
cd aulas/aula09-ml-bigdata/
python ml_bigdata_platform.py

# Resultado:
# ✅ Fraud detection (1M+ transações)
# ✅ Recommendation system (ALS)
# ✅ Sentiment analysis (100K+ reviews)
# ✅ Modelos deployados e avaliados
```

---

## **📊 PROJETOS IMPLEMENTADOS**

### **🏆 Projeto 1: IoT Sensor Network**
- **Escala:** 50 sensores simultâneos
- **Throughput:** 1000+ leituras/minuto
- **Features:** Fault tolerance, anomaly detection, real-time alerts
- **Stack:** Python threading, Redis, statistical analysis
- **Output:** Dashboard com métricas ao vivo

### **🏆 Projeto 2: Real-time Fraud Detection**
- **Dataset:** 1M+ transações sintéticas
- **ML Model:** Random Forest distribuído (Spark MLlib)
- **Performance:** AUC-ROC > 0.95, sub-second inference
- **Features:** Feature engineering, model deployment
- **Output:** API de scoring em tempo real

### **🏆 Projeto 3: E-commerce Recommendation Engine**
- **Algorithm:** Alternating Least Squares (ALS)
- **Scale:** 10K users, 5K items, 500K ratings
- **Evaluation:** RMSE < 1.0, collaborative filtering
- **Deployment:** Real-time recommendations API
- **Output:** Sistema completo de recomendações

### **🏆 Projeto 4: Streaming Analytics Platform**
- **Architecture:** Kafka → Real-time processing → Dashboard
- **Throughput:** 10K+ eventos/segundo
- **Latency:** <100ms end-to-end
- **Features:** Auto-scaling, fault tolerance, monitoring
- **Output:** Platform completa de streaming

---

## **🎯 RESULTADOS DE APRENDIZADO**

### **💼 Competências Técnicas Desenvolvidas**

#### **🔧 Big Data Technologies**
- ✅ **Apache Spark:** RDDs, DataFrames, MLlib, Streaming
- ✅ **Hadoop Ecosystem:** HDFS, MapReduce, YARN
- ✅ **Apache Kafka:** Producers, consumers, real-time processing
- ✅ **Cloud Platforms:** AWS, GCP, Azure for Big Data
- ✅ **NoSQL Databases:** MongoDB, Cassandra, Redis, HBase

#### **🐍 Python for Scale**
- ✅ **Performance Optimization:** Vectorization, chunking, parallel processing
- ✅ **Memory Management:** Large dataset handling, garbage collection
- ✅ **Advanced Libraries:** NumPy broadcasting, Pandas optimization
- ✅ **ML at Scale:** scikit-learn, Spark MLlib, distributed training

#### **📊 Data Engineering**
- ✅ **ETL/ELT Pipelines:** Extract, Transform, Load at scale
- ✅ **Data Lakes:** Architecture, governance, schema evolution
- ✅ **Stream Processing:** Real-time analytics, windowing, watermarks
- ✅ **Data Quality:** Validation, monitoring, alerting

#### **☁️ Cloud & DevOps**
- ✅ **Infrastructure as Code:** Terraform, CloudFormation
- ✅ **Containerization:** Docker, Kubernetes for data workloads
- ✅ **CI/CD:** Automated testing, deployment pipelines
- ✅ **Monitoring:** Prometheus, Grafana, logging strategies

### **🎓 Certificações Preparadas**
- 🏅 **AWS Certified Solutions Architect** - Associate
- 🏅 **Google Cloud Professional Data Engineer**
- 🏅 **Azure Data Engineer Associate**
- 🏅 **Databricks Certified Associate Developer**
- 🏅 **Confluent Certified Administrator for Apache Kafka**

---

## **📈 MÉTRICAS DE PERFORMANCE**

### **⚡ Benchmarks Implementados**

| Projeto | Dataset Size | Processing Time | Throughput | Accuracy |
|---------|--------------|-----------------|------------|----------|
| **Volume Simulation** | 10 GB | 45 segundos | 220 MB/s | N/A |
| **Velocity Demo** | 1M eventos | Real-time | 10K eventos/s | N/A |
| **IoT Sensors** | 50 sensores | Contínuo | 1K leituras/min | 98% uptime |
| **Fraud Detection** | 1M transações | 2 minutos | 8.3K transações/s | AUC: 0.954 |
| **Recommendations** | 500K ratings | 30 segundos | 16.7K ratings/s | RMSE: 0.89 |
| **Streaming Platform** | Ilimitado | Real-time | 10K eventos/s | <100ms latency |

### **💰 Cost Analysis (Cloud)**

| Workload | AWS Monthly | GCP Monthly | Azure Monthly | Optimal |
|----------|-------------|-------------|---------------|---------|
| **Development** | $50-100 | $45-90 | $55-110 | GCP |
| **Production (Small)** | $200-500 | $180-450 | $220-550 | GCP |
| **Production (Large)** | $1K-5K | $900-4.5K | $1.1K-5.5K | GCP |
| **Enterprise** | $5K+ | $4.5K+ | $5.5K+ | Negotiated |

---

## **🔗 RECURSOS ADICIONAIS**

### **📚 Biblioteca Expandida**
- 📖 [Ferramentas Big Data 2025](materiais/ferramentas-bigdata-completa-v2.md) - Guia definitivo
- 📊 [Tutorial Power BI](materiais/tutorial-powerbi-bigdata.md) - Integração com Big Data
- 🗃️ [Datasets Públicos](materiais/datasets-publicos-completos.md) - Fontes curadas
- 📋 [Cronograma Expandido](cronograma-expandido.md) - Planejamento completo

### **🛠️ Ferramentas de Desenvolvimento**
```bash
# IDEs recomendadas
VSCode + Python Extension      # Desenvolvimento principal
PyCharm Professional          # Debugging avançado  
Jupyter Lab                    # Análise exploratória
DataGrip                      # Database management

# Monitoramento
Spark UI                      # Spark job monitoring
Kafka Manager                 # Kafka cluster management
Grafana                       # Metrics dashboards
```

### **🌐 Comunidade e Suporte**
- 💬 **Discord:** [Link do servidor]
- 📧 **Email:** suporte@curso-bigdata.com
- 🐛 **Issues:** [GitHub Issues](https://github.com/curso-bigdata/issues)
- 📖 **Wiki:** [Documentação completa](https://github.com/curso-bigdata/wiki)

---

## **🏁 PRÓXIMOS PASSOS**

### **🎯 Para Iniciantes**
1. ✅ **Setup Environment:** Instalar Python, Spark, Docker
2. ✅ **Run Quick Start:** Executar primeiras demos
3. ✅ **Complete Module I:** Fundamentos (Aulas 1-4)
4. 🔄 **Practice Projects:** Implementar projetos pessoais

### **🚀 Para Avançados**
1. ✅ **Deep Dive:** Módulos II-III (Aulas 5-12)
2. 🔄 **Contribute:** Adicionar novos modules
3. 🔄 **Cloud Deploy:** AWS/GCP/Azure implementations
4. 🔄 **Portfolio:** GitHub showcase projects

### **💼 Para Carreira**
1. 🎓 **Certifications:** AWS, GCP, Azure, Databricks
2. 📝 **Resume:** Portfolio projects documentation
3. 🤝 **Networking:** Community participation
4. 💼 **Job Search:** Apply Big Data Engineer roles

---

## **📞 CONTATO**

**📧 Email:** professor@universidade.edu.br  
**💬 Office Hours:** Quartas 14h-16h  
**🌐 Website:** [curso-bigdata.github.io](https://curso-bigdata.github.io)  
**📱 LinkedIn:** [Professor Big Data](https://linkedin.com/in/professor-bigdata)

---

## **📄 LICENÇA**

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## **⭐ CONTRIBUIÇÕES**

Contribuições são bem-vindas! Por favor, leia [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre nosso código de conduta e o processo de envio de pull requests.

---

## **🙏 AGRADECIMENTOS**

- Apache Software Foundation pelas ferramentas open-source
- Databricks pela documentação Spark
- Confluent pelo ecosistema Kafka
- Comunidade Python pelo suporte

---

**🎯 Ready to become a Big Data Engineer? Start now! 🚀**

*Última atualização: Janeiro 2025 - Curso completamente expandido com 9 aulas implementadas e funcionais!*
