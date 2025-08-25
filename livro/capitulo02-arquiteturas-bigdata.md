# Capítulo 2: Arquiteturas de Big Data - Fundamentos Tecnológicos

**Autor:** Prof. Vagner Cordeiro  
**Disciplina:** Tópicos de Big Data em Python

---

## 2.1 Evolução das Arquiteturas de Dados

### Arquiteturas Tradicionais vs. Big Data

#### Limitações dos Sistemas Monolíticos
As arquiteturas tradicionais de dados, baseadas em sistemas centralizados, enfrentam limitações fundamentais quando confrontadas com os desafios do Big Data:

##### Escalabilidade Vertical (Scale-Up)
- **Conceito**: Aumento de capacidade através de hardware mais potente
- **Limitações físicas**: Lei de Moore em desaceleração, limites térmicos
- **Custos exponenciais**: Relação não-linear entre performance e investimento
- **Pontos únicos de falha**: Vulnerabilidade a falhas catastróficas

##### Gargalos de I/O
- **Largura de banda de disco**: Velocidade de acesso limitada
- **Latência de rede**: Comunicação entre componentes
- **Contenção de recursos**: Competição por recursos compartilhados

#### Paradigma Distribuído
A transição para arquiteturas distribuídas fundamenta-se em princípios científicos sólidos:

##### Escalabilidade Horizontal (Scale-Out)
- **Paralelização**: Divisão de trabalho entre múltiplas máquinas
- **Elasticidade**: Adição/remoção dinâmica de recursos
- **Economia linear**: Custos proporcionais à capacidade
- **Tolerância a falhas**: Redundância inerente

##### Princípio da Localidade
- **Localidade temporal**: Dados recentemente acessados tendem a ser acessados novamente
- **Localidade espacial**: Dados próximos tendem a ser acessados conjuntamente
- **Localidade geográfica**: Processamento próximo aos dados

## 2.2 Sistemas de Armazenamento Distribuído

### Google File System (GFS) - Marco Conceitual

#### Premissas de Design
O GFS revolucionou o pensamento sobre sistemas de arquivos através de premissas inovadoras:

1. **Falhas como norma**: Hardware commodity falha frequentemente
2. **Arquivos grandes**: Otimização para arquivos de gigabytes/terabytes
3. **Workloads específicos**: Escritas append-only, leituras sequenciais
4. **Bandwidth mais importante que latência**: Throughput prioritário

#### Arquitetura Fundamental
- **Master único**: Metadados centralizados, simplicidade operacional
- **Chunkservers múltiplos**: Armazenamento distribuído de dados
- **Chunks de 64MB**: Redução de overhead de metadados
- **Replicação tripla**: Tolerância a falhas por redundância

### Hadoop Distributed File System (HDFS)

#### Evolução Open-Source
HDFS representa implementação open-source dos conceitos GFS:

##### NameNode (Master)
- **Namespace management**: Hierarquia de diretórios e arquivos
- **Block placement**: Decisões de localização de dados
- **Replication management**: Manutenção de fatores de replicação
- **Ponto crítico**: Single point of failure (mitigado por High Availability)

##### DataNodes (Workers)
- **Block storage**: Armazenamento físico de blocos de dados
- **Heartbeats**: Comunicação periódica com NameNode
- **Block reports**: Inventário de blocos armazenados
- **Pipeline replication**: Replicação em cadeia para eficiência

#### Características Técnicas

##### Tamanho de Bloco
- **Padrão**: 128MB (Hadoop 2.x+), anteriormente 64MB
- **Justificativa**: Minimização de overhead de metadados
- **Trade-off**: Latência vs. throughput

##### Estratégias de Replicação
- **Rack awareness**: Consciência de topologia de rede
- **Primeira réplica**: Mesmo nó do cliente (se possível)
- **Segunda réplica**: Rack diferente
- **Terceira réplica**: Mesmo rack da segunda, nó diferente

### Sistemas NoSQL para Big Data

#### Taxonomia NoSQL
Classificação baseada em modelos de dados e características:

##### Key-Value Stores
- **Modelo**: Associações simples chave-valor
- **Características**: Alta performance, escalabilidade horizontal
- **Exemplos**: Amazon DynamoDB, Redis, Riak
- **Aplicações**: Caching, sessões web, configurações

##### Document Stores
- **Modelo**: Documentos semi-estruturados (JSON, BSON)
- **Características**: Flexibilidade de schema, consultas complexas
- **Exemplos**: MongoDB, CouchDB, Amazon DocumentDB
- **Aplicações**: Content management, catálogos de produtos

##### Column-Family
- **Modelo**: Famílias de colunas esparsas
- **Características**: Compressão eficiente, consultas analíticas
- **Exemplos**: Cassandra, HBase, Google Bigtable
- **Aplicações**: Time series, logs, dados de sensores

##### Graph Databases
- **Modelo**: Nós e relacionamentos
- **Características**: Traversal eficiente, consultas de grafos
- **Exemplos**: Neo4j, Amazon Neptune, ArangoDB
- **Aplicações**: Redes sociais, detecção de fraudes, recomendações

## 2.3 Frameworks de Processamento Distribuído

### MapReduce - Paradigma Fundamental

#### Modelo de Programação
MapReduce abstrai complexidade de programação distribuída:

##### Fase Map
- **Input**: Pares chave-valor de entrada
- **Processamento**: Transformação local e independente
- **Output**: Pares chave-valor intermediários
- **Paralelização**: Múltiplos mappers executam simultaneamente

##### Fase Shuffle
- **Particionamento**: Distribuição baseada em chaves
- **Ordenação**: Agrupamento de chaves idênticas
- **Transferência**: Movimento de dados entre nós
- **Gargalo**: Operação intensiva de I/O e rede

##### Fase Reduce
- **Input**: Chaves agrupadas com valores associados
- **Processamento**: Agregação ou síntese
- **Output**: Resultado final
- **Paralelização**: Múltiplos reducers por partições

#### Vantagens e Limitações

##### Vantagens
- **Simplicidade**: Abstração de alto nível
- **Tolerância a falhas**: Recuperação automática
- **Escalabilidade**: Linear em muitos casos
- **Portabilidade**: Independência de dados específicos

##### Limitações
- **Latência alta**: Overhead de inicialização
- **I/O intensivo**: Escritas intermediárias em disco
- **Inadequado para iterações**: Múltiplos jobs para algoritmos iterativos
- **Modelo restritivo**: Nem todos problemas se adequam

### Apache Spark - Evolução do Paradigma

#### Inovações Fundamentais

##### Resilient Distributed Datasets (RDDs)
- **Conceito**: Abstração de coleções distribuídas imutáveis
- **Lineage**: Grafo de dependências para recuperação
- **Lazy evaluation**: Execução adiada para otimizações
- **Caching**: Persistência em memória para reutilização

##### Unified Engine
- **Batch processing**: Processamento tradicional em lotes
- **Stream processing**: Processamento de fluxos contínuos
- **Machine learning**: MLlib para aprendizado de máquina
- **Graph processing**: GraphX para análise de grafos

#### Arquitetura Spark

##### Driver Program
- **SparkContext**: Ponto de entrada principal
- **DAG Scheduler**: Construção de grafo de execução
- **Task Scheduler**: Distribuição de tarefas
- **Cluster Manager**: Interface com gerenciadores de cluster

##### Executors
- **JVM processes**: Processos Java isolados
- **Task execution**: Execução de tarefas distribuídas
- **Data caching**: Armazenamento de dados em cache
- **Shuffle service**: Gerenciamento de dados intermediários

#### Otimizações Avançadas

##### Catalyst Optimizer
- **Rule-based optimization**: Regras predefinidas de otimização
- **Cost-based optimization**: Decisões baseadas em estatísticas
- **Code generation**: Geração de código Java otimizado
- **Predicate pushdown**: Filtragem próxima aos dados

##### Tungsten Execution Engine
- **Memory management**: Gerenciamento explícito de memória
- **Binary processing**: Processamento direto em formato binário
- **Vectorization**: SIMD para operações vetoriais
- **Whole-stage code generation**: Fusão de operações

## 2.4 Arquiteturas de Streaming

### Fundamentos de Stream Processing

#### Características de Streams
Fluxos de dados contínuos apresentam desafios únicos:

##### Infinitude
- **Streams ilimitados**: Dados chegam continuamente
- **Memory constraints**: Impossibilidade de armazenar tudo
- **Windowing**: Necessidade de janelas temporais
- **Approximation**: Algoritmos aproximados para eficiência

##### Ordem temporal
- **Event time**: Timestamp de ocorrência do evento
- **Processing time**: Timestamp de processamento
- **Watermarks**: Mecanismo para lidar com atrasos
- **Out-of-order events**: Eventos fora de ordem temporal

#### Semânticas de Processamento

##### At-least-once
- **Garantia**: Cada evento processado pelo menos uma vez
- **Implementação**: Acknowledgments e retries
- **Problemas**: Duplicação de eventos
- **Aplicações**: Sistemas tolerantes a duplicação

##### At-most-once
- **Garantia**: Cada evento processado no máximo uma vez
- **Implementação**: Sem retries após falhas
- **Problemas**: Perda de eventos
- **Aplicações**: Sistemas tolerantes a perda

##### Exactly-once
- **Garantia**: Cada evento processado exatamente uma vez
- **Complexidade**: Implementação sofisticada
- **Técnicas**: Idempotência, transações distribuídas
- **Estado da arte**: Ainda em evolução

### Apache Kafka - Plataforma de Streaming

#### Modelo de Dados

##### Topics e Partitions
- **Topics**: Categorias de mensagens
- **Partitions**: Subdivisões para paralelização
- **Ordering**: Ordem garantida dentro de partições
- **Scaling**: Adição de partições para escalabilidade

##### Producers e Consumers
- **Producers**: Publicadores de mensagens
- **Consumers**: Subscritores de mensagens
- **Consumer Groups**: Paralelização de consumo
- **Offset management**: Controle de posição de leitura

#### Arquitetura Distribuída

##### Brokers
- **Cluster**: Conjunto de servidores Kafka
- **Replication**: Redundância entre brokers
- **Leader/Follower**: Padrão de replicação
- **Fault tolerance**: Tolerância a falhas de brokers

##### ZooKeeper (Kafka < 2.8)
- **Coordination**: Coordenação de cluster
- **Metadata**: Armazenamento de metadados
- **Leader election**: Eleição de líderes
- **KRaft**: Substituto interno (Kafka 2.8+)

## 2.5 Arquiteturas Lambda e Kappa

### Lambda Architecture

#### Motivação
Necessidade de combinar processamento batch e streaming:

##### Desafios Híbridos
- **Completude vs. Latência**: Trade-off fundamental
- **Correção vs. Velocidade**: Precisão versus rapidez
- **Complexidade**: Manutenção de dois sistemas

#### Componentes

##### Batch Layer
- **Função**: Processamento completo e preciso
- **Características**: Alto throughput, alta latência
- **Tecnologias**: Hadoop MapReduce, Spark Batch
- **Output**: Batch views (visões pré-computadas)

##### Speed Layer
- **Função**: Processamento rápido e aproximado
- **Características**: Baixa latência, throughput limitado
- **Tecnologias**: Storm, Spark Streaming, Flink
- **Output**: Real-time views (visões em tempo real)

##### Serving Layer
- **Função**: Unificação de resultados
- **Características**: Consultas eficientes
- **Tecnologias**: ElasticSearch, Cassandra, HBase
- **Output**: Merged views (visões unificadas)

### Kappa Architecture

#### Filosofia Simplificada
Eliminação da complexidade de sistemas duplos:

##### Stream-only
- **Paradigma**: Tudo é stream
- **Reprocessing**: Replay de streams históricos
- **Consistência**: Única lógica de processamento
- **Simplificação**: Redução de complexidade operacional

#### Implementação

##### Event Sourcing
- **Conceito**: Armazenamento de eventos, não estado
- **Immutability**: Eventos imutáveis
- **Replay**: Reconstrução de estado via replay
- **Auditability**: Trilha completa de eventos

##### Stream Reprocessing
- **Versioning**: Múltiplas versões de processors
- **Migration**: Migração gradual entre versões
- **Testing**: Validação em streams de desenvolvimento
- **Rollback**: Reversão para versões anteriores

## 2.6 Arquiteturas Cloud-Native

### Contêineres e Orquestração

#### Docker para Big Data
Contêineres revolucionam deployment de aplicações big data:

##### Benefícios
- **Portabilidade**: Consistência entre ambientes
- **Isolamento**: Dependências encapsuladas
- **Eficiência**: Overhead menor que VMs
- **DevOps**: Integração com pipelines CI/CD

##### Desafios
- **Persistent storage**: Dados que sobrevivem ao contêiner
- **Networking**: Comunicação entre serviços
- **Resource management**: Alocação de CPU/memória
- **Security**: Isolamento e vulnerabilidades

#### Kubernetes para Big Data

##### Primitivas Fundamentais
- **Pods**: Unidades básicas de deployment
- **Services**: Abstração de rede
- **Volumes**: Armazenamento persistente
- **ConfigMaps/Secrets**: Configuração e credenciais

##### Operadores Especializados
- **Spark Operator**: Kubernetes-native Spark
- **Kafka Operator**: Gestão automatizada de Kafka
- **Hadoop Operator**: HDFS e YARN em Kubernetes
- **ML Operators**: TensorFlow, PyTorch operators

### Serverless para Big Data

#### Function-as-a-Service (FaaS)
Execução de código sem gerenciamento de infraestrutura:

##### Características
- **Event-driven**: Execução baseada em eventos
- **Stateless**: Funções sem estado persistente
- **Auto-scaling**: Escalabilidade automática
- **Pay-per-use**: Cobrança por execução

##### Limitações para Big Data
- **Execution time limits**: Timeouts para funções
- **Memory constraints**: Limites de memória
- **State management**: Dificuldade com estado persistente
- **Cold starts**: Latência de inicialização

#### Managed Services
Serviços gerenciados abstraem complexidade operacional:

##### AWS Big Data Services
- **EMR**: Managed Hadoop/Spark clusters
- **Kinesis**: Streaming platform
- **Redshift**: Data warehouse
- **Athena**: Serverless query engine

##### Google Cloud Platform
- **Dataproc**: Managed Spark/Hadoop
- **Dataflow**: Stream/batch processing
- **BigQuery**: Serverless data warehouse
- **Pub/Sub**: Messaging service

##### Microsoft Azure
- **HDInsight**: Managed analytics clusters
- **Stream Analytics**: Real-time processing
- **Synapse**: Unified analytics platform
- **Event Hubs**: Event streaming platform

## 2.7 Tendências Arquiteturais Emergentes

### Data Mesh
Paradigma descentralizado para arquiteturas de dados:

#### Princípios Fundamentais

##### Domain-oriented Data Ownership
- **Descentralização**: Ownership por domínios de negócio
- **Autonomia**: Times autônomos para seus dados
- **Especialização**: Expertise específica de domínio
- **Responsabilidade**: Accountability pelos dados

##### Data as a Product
- **Product thinking**: Dados como produtos internos
- **SLAs**: Service Level Agreements para dados
- **Discoverability**: Facilitação de descoberta
- **Quality**: Garantias de qualidade

##### Self-serve Data Platform
- **Infrastructure as code**: Automação de infraestrutura
- **Developer experience**: Ferramentas acessíveis
- **Standardization**: Padrões técnicos comuns
- **Monitoring**: Observabilidade built-in

### Lakehouse Architecture
Convergência de data lakes e data warehouses:

#### Evolução Natural
- **Data Lakes**: Flexibilidade sem performance
- **Data Warehouses**: Performance sem flexibilidade
- **Lakehouses**: Melhor dos dois mundos

#### Tecnologias Habilitadoras

##### Delta Lake
- **ACID transactions**: Transações em data lakes
- **Schema evolution**: Evolução de esquemas
- **Time travel**: Versionamento de dados
- **Upserts/Deletes**: Operações de modificação

##### Apache Iceberg
- **Table format**: Formato de tabela universal
- **Partition evolution**: Evolução de particionamento
- **Hidden partitioning**: Particionamento transparente
- **Schema evolution**: Mudanças de esquema seguras

### Edge Computing
Processamento próximo à origem dos dados:

#### Motivações
- **Latency**: Redução de latência de rede
- **Bandwidth**: Economia de largura de banda
- **Privacy**: Processamento local de dados sensíveis
- **Reliability**: Funcionamento offline

#### Desafios
- **Resource constraints**: Limitações de hardware
- **Management**: Gerenciamento distribuído
- **Consistency**: Sincronização entre edge e cloud
- **Security**: Segurança em ambientes desprotegidos

## 2.8 Conclusão

As arquiteturas de Big Data evoluíram significativamente desde os primeiros sistemas monolíticos. A progressão de MapReduce para Spark, de batch para streaming, e de on-premises para cloud-native reflete a maturação do campo.

### Insights Principais

1. **Não existe arquitetura única**: Diferentes problemas requerem diferentes soluções
2. **Trade-offs são inevitáveis**: Performance vs. flexibilidade, consistência vs. disponibilidade
3. **Simplicidade é valiosa**: Arquiteturas complexas são difíceis de manter
4. **Evolução contínua**: Novas tecnologias emergem constantemente

### Diretrizes de Design

1. **Comece simples**: Adicione complexidade apenas quando necessário
2. **Pense em escala**: Considere crescimento futuro
3. **Priorize confiabilidade**: Falhas são inevitáveis
4. **Meça tudo**: Monitoramento é essencial
5. **Automatize operações**: Reduzir erro humano

O próximo capítulo explorará as ferramentas específicas que implementam estas arquiteturas, fornecendo perspectiva prática sobre os conceitos teóricos apresentados.

---

**Referências Técnicas**

1. Ghemawat, S., Gobioff, H., & Leung, S. T. (2003). The Google file system. ACM SIGOPS.
2. Dean, J., & Ghemawat, S. (2008). MapReduce: Simplified data processing on large clusters.
3. Zaharia, M., et al. (2012). Resilient distributed datasets: A fault-tolerant abstraction for in-memory cluster computing.
4. Marz, N., & Warren, J. (2015). Big Data: Principles and best practices of scalable realtime data systems.
5. Dehghani, Z. (2021). Data Mesh: Delivering Data-Driven Value at Scale.
