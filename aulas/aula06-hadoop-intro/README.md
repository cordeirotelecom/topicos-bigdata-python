# 🐘 Aula 06 - Hadoop Ecosystem Completo

## 🎯 Objetivos da Aula
- Compreender profundamente a arquitetura do Hadoop
- Realizar instalação completa em diferentes ambientes
- Configurar e operar cluster Hadoop local
- Implementar jobs MapReduce práticos
- Analisar casos de uso reais de empresas

## 📋 Conteúdo Programático

### 1. 📚 Fundamentos do Hadoop
- **Histórico e evolução**: De Yahoo! para Apache Foundation
- **Arquitetura distribuída**: Master/Slave, tolerância a falhas
- **Componentes principais**: HDFS, YARN, MapReduce
- **Ecossistema**: Hive, HBase, Spark, Kafka integration

### 2. 💾 HDFS (Hadoop Distributed File System)
- **Arquitetura NameNode/DataNode**: Metadados vs dados reais
- **Replicação e tolerância a falhas**: Factor de replicação
- **Comandos básicos**: put, get, ls, cat, rm
- **Block size optimization**: 128MB default, quando ajustar

### 3. 🔧 YARN (Yet Another Resource Negotiator)
- **ResourceManager**: Alocação global de recursos
- **NodeManager**: Execução local de containers
- **ApplicationMaster**: Gerenciamento de aplicações
- **Container**: Unidade de execução

### 4. 🗺️ MapReduce Framework
- **Map phase**: Processamento paralelo
- **Shuffle & Sort**: Organização de dados intermediários
- **Reduce phase**: Agregação de resultados
- **Combiner**: Otimização de rede

## 🛠️ Laboratório Prático Avançado

### � Acesse o Laboratório Completo
**[🚀 Abrir Laboratório Interativo](./laboratorio-hadoop.html)**

O laboratório inclui:
- ✅ **Instalação guiada** para Windows, Linux e Docker
- ✅ **Configuração passo a passo** com todos os arquivos XML
- ✅ **Exemplos práticos** de MapReduce em Python
- ✅ **Análise de logs** de servidores web
- ✅ **Casos de uso reais** de empresas como Facebook, Uber
- ✅ **Scripts de download** automatizados
- ✅ **Interface web** para monitoramento

## 🏢 Empresas que Utilizam Hadoop

### 🌐 Casos de Uso Reais
- **Meta (Facebook)**: 300+ PB de dados de usuários
- **Twitter**: Análise de tweets em tempo real
- **LinkedIn**: Matching de perfis profissionais
- **Spotify**: Sistema de recomendação musical
- **Uber**: Otimização de rotas e preços dinâmicos
- **Airbnb**: Análise de mercado imobiliário
- **Amazon**: Sistema de recomendações (29% aumento vendas)

### 💼 Setores Principais
- **Financeiro**: Detecção de fraudes, análise de risco
- **Saúde**: Pesquisa genômica, análise de prontuários
- **Varejo**: Comportamento do cliente, gestão de estoque
- **Telecomunicações**: Otimização de rede, análise de tráfego
- **Governo**: Inteligência, segurança nacional
- **Mídia**: Recomendações de conteúdo, análise de audiência

## 📊 Quando Utilizar Hadoop?

### ✅ Ideal para:
- **Volume**: Datasets > 1TB
- **Variedade**: Dados estruturados, semi-estruturados, não estruturados
- **Velocidade**: Processamento batch de grandes volumes
- **Custo**: Hardware commodity vs sistemas proprietários
- **Escalabilidade**: Crescimento horizontal linear

### ❌ Não recomendado para:
- Dados pequenos (< 100GB)
- Processamento em tempo real crítico
- Transações ACID complexas
- Consultas interativas frequentes

## 🔧 Arquitetura Detalhada

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Client        │    │   NameNode      │    │  ResourceManager│
│                 │───▶│   (Metadata)    │    │   (YARN)        │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │                        │
                              ▼                        ▼
                    ┌─────────────────┐    ┌─────────────────┐
                    │   DataNode 1    │    │  NodeManager 1  │
                    │   (Data Blocks) │    │  (Containers)   │
                    └─────────────────┘    └─────────────────┘
                    
                    ┌─────────────────┐    ┌─────────────────┐
                    │   DataNode 2    │    │  NodeManager 2  │
                    │   (Data Blocks) │    │  (Containers)   │
                    └─────────────────┘    └─────────────────┘
```

## 🚀 Scripts de Instalação

### Windows PowerShell
```powershell
# Download script automático
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/apache/hadoop/trunk/dev-support/bin/install-hadoop-windows.ps1" -OutFile "install-hadoop.ps1"
.\install-hadoop.ps1
```

### Linux/Ubuntu
```bash
# Script de instalação completa
curl -fsSL https://raw.githubusercontent.com/apache/hadoop/trunk/dev-support/bin/install-hadoop-linux.sh | bash
```

### Docker Compose
```yaml
# Cluster Hadoop completo em containers
version: '3.8'
services:
  namenode:
    image: apache/hadoop:3.3.6
    ports: ["9870:9870", "9000:9000"]
  datanode:
    image: apache/hadoop:3.3.6
  resourcemanager:
    image: apache/hadoop:3.3.6
    ports: ["8088:8088"]
```

## 📈 Performance e Otimização

### 🔧 Configurações Importantes
```xml
<!-- hdfs-site.xml -->
<property>
  <name>dfs.block.size</name>
  <value>268435456</value> <!-- 256MB para datasets grandes -->
</property>

<!-- mapred-site.xml -->
<property>
  <name>mapreduce.job.maps</name>
  <value>10</value> <!-- Ajustar conforme CPU cores -->
</property>
```

### 📊 Monitoramento
- **NameNode Web UI**: http://localhost:9870
- **ResourceManager UI**: http://localhost:8088
- **Job History Server**: http://localhost:19888
- **DataNode Status**: http://localhost:9864

## 🎓 Exercícios Práticos

### 1. WordCount Avançado
Implemente WordCount que:
- Ignora stop words
- Conta apenas palavras > 3 caracteres
- Ordena resultado por frequência

### 2. Análise de Logs
Processe logs de servidor web para:
- Top 10 IPs mais frequentes
- Análise de status codes
- Detecção de padrões de ataque

### 3. ETL Pipeline
Crie pipeline que:
- Lê dados de múltiplas fontes
- Aplica transformações
- Salva em formato otimizado (Parquet)

## 📚 Recursos Adicionais

- 📖 **Documentação Oficial**: https://hadoop.apache.org/docs/
- 🎥 **Hadoop Summit Videos**: https://hadoop.apache.org/summit/
- 📊 **Benchmarks**: https://hadoop.apache.org/benchmarks/
- 🛠️ **Ecosystem Tools**: https://hadoop.apache.org/ecosystem/

## 🎯 Próxima Aula: Apache Spark
Evolução natural do Hadoop para processamento em memória e tempo real.

### 3. YARN (Yet Another Resource Negotiator)
- Resource Manager
- Node Manager
- Container management

### 4. MapReduce Framework
- Paradigma Map-Reduce
- Job execution flow
- Optimization techniques

## 🛠️ Atividades Práticas

### Exercício 1: Setup Hadoop Cluster
- Configuração pseudo-distribuída
- Inicialização dos serviços
- Verificação do cluster

### Exercício 2: HDFS Operations
- Upload/download de arquivos
- Operações de diretório
- Monitoramento de espaço

### Exercício 3: MapReduce Jobs
- Word Count clássico
- Data aggregation
- Custom reducers

## 📊 Projeto Prático
Implementação de um pipeline de análise de logs de servidor usando MapReduce para identificar:
- IPs mais ativos
- Páginas mais acessadas
- Padrões de erro

## 📚 Material de Apoio
- [Documentação oficial Hadoop](https://hadoop.apache.org/docs/)
- [Guia de instalação](../INSTALACAO.md)
- [Scripts de configuração](./scripts/)

## 🎯 Próxima Aula
Aula 07 - Apache Spark Fundamentals
