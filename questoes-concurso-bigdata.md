# Questões de Concurso Público - Big Data Analytics

**Banco de questões baseadas em concursos públicos brasileiros reais**  
Fonte: CESPE, FCC, VUNESP, FGV, CONSULPLAN e outras bancas  
Área: Tecnologia da Informação, Análise de Sistemas e Gestão Pública  
Atualizado: Setembro 2025

---

## **QUESTÃO 1** (Adaptada - CESPE/CEBRASPE 2024)

**No contexto de Big Data, os "5 Vs" representam as principais características que definem esta área. Sobre essas características, analise as assertivas abaixo:**

**I.** Volume refere-se à quantidade massiva de dados que excede a capacidade de processamento de sistemas tradicionais.  
**II.** Velocidade (Velocity) está relacionada tanto à rapidez da geração dos dados quanto à necessidade de processamento em tempo real.  
**III.** Variedade (Variety) indica a diversidade de tipos e formatos de dados, incluindo estruturados, semi-estruturados e não-estruturados.  
**IV.** Veracidade (Veracity) diz respeito à qualidade, precisão e confiabilidade dos dados coletados.  
**V.** Valor (Value) representa a capacidade de extrair insights úteis e significativos dos dados processados.

**Alternativas:**
- A) Apenas as assertivas I, II e III estão corretas
- B) Apenas as assertivas I, III e V estão corretas  
- C) Apenas as assertivas II, IV e V estão corretas
- D) Todas as assertivas estão corretas
- E) Apenas as assertivas I, II e IV estão corretas

---

### **RESPOSTA: D**

**Explicação:** Todas as assertivas estão corretas. Os 5 Vs do Big Data são: Volume (quantidade massiva), Velocity (velocidade de geração e processamento), Variety (variedade de formatos), Veracity (veracidade/qualidade dos dados) e Value (valor/insights extraídos). Esta é uma evolução do conceito original dos 3 Vs (Volume, Velocity, Variety) proposto pela IBM, posteriormente expandido para incluir Veracity e Value.

---

## **QUESTÃO 2** (Adaptada - FCC 2023)

**O Apache Hadoop é um framework de código aberto para armazenamento distribuído e processamento de grandes conjuntos de dados. Sobre os componentes principais do ecossistema Hadoop, é CORRETO afirmar:**

**Alternativas:**
- A) O HDFS (Hadoop Distributed File System) utiliza o princípio write-once, read-many e replica os dados em um único nó para garantir a integridade
- B) O MapReduce é adequado apenas para processamento de dados estruturados em formato relacional
- C) O YARN (Yet Another Resource Negotiator) é responsável pelo gerenciamento de recursos e escalonamento de jobs no cluster Hadoop
- D) O NameNode armazena fisicamente todos os blocos de dados do sistema de arquivos distribuído
- E) O Hadoop funciona exclusivamente em sistemas operacionais proprietários como Windows Server

---

### **RESPOSTA: C**

**Explicação:** O YARN (Yet Another Resource Negotiator) é o gerenciador de recursos do Hadoop 2.0+, responsável pelo escalonamento de jobs e gerenciamento de recursos do cluster. A alternativa A está incorreta pois o HDFS replica dados em múltiplos nós (fator de replicação padrão = 3). A alternativa B está incorreta pois MapReduce processa dados estruturados e não-estruturados. A alternativa D está incorreta pois o NameNode armazena metadados, não os blocos físicos. A alternativa E está incorreta pois Hadoop é multiplataforma (Linux, Windows, etc.).

---

## **QUESTÃO 3** (Adaptada - VUNESP 2024)

**Apache Spark é um framework de processamento distribuído que oferece vantagens significativas em relação ao MapReduce tradicional. Sobre o Apache Spark, analise as afirmações:**

**I.** Spark utiliza processamento in-memory (na memória RAM) para operações iterativas, proporcionando performance superior ao MapReduce baseado em disco.  
**II.** Spark SQL permite consultas SQL sobre dados estruturados e semi-estruturados usando DataFrames e Datasets.  
**III.** MLlib é a biblioteca de machine learning distribuído do Spark que oferece algoritmos escaláveis.  
**IV.** Spark Streaming processa dados em tempo real usando o conceito de micro-batches.  
**V.** GraphX é o componente do Spark para processamento de grafos e análise de redes.

**Estão corretas:**
- A) Apenas I, II e III
- B) Apenas II, IV e V  
- C) Apenas I, III e IV
- D) Apenas I, II, III e IV
- E) Todas as afirmações

---

### **RESPOSTA: E**

**Explicação:** Todas as afirmações estão corretas. O Apache Spark oferece: (I) processamento in-memory para operações iterativas até 100x mais rápido que MapReduce; (II) Spark SQL com suporte a DataFrames/Datasets para consultas SQL; (III) MLlib com algoritmos de ML distribuídos; (IV) Spark Streaming para processamento em tempo real via micro-batches; (V) GraphX para análise de grafos e algoritmos de rede como PageRank.

---

## **QUESTÃO 4** (Adaptada - FGV 2023)

**No contexto de arquiteturas de dados modernos, a Arquitetura Lambda é uma abordagem híbrida que combina processamento batch e stream. Sobre esta arquitetura, é CORRETO afirmar:**

**Alternativas:**
- A) A camada batch processa apenas dados históricos enquanto a camada speed processa dados em tempo real, sendo que ambas são consultadas separadamente
- B) A arquitetura Lambda elimina completamente a necessidade de processamento batch, focando apenas em streaming
- C) A serving layer combina resultados das camadas batch e speed para fornecer uma visão unificada dos dados processados
- D) Lambda é adequada apenas para dados estruturados em formato relacional
- E) A arquitetura Lambda requer obrigatoriamente o uso de Apache Hadoop como única tecnologia de processamento

---

### **RESPOSTA: C**

**Explicação:** A Arquitetura Lambda possui três camadas: Batch Layer (processa grandes volumes de dados históricos), Speed Layer (processa dados em tempo real/near real-time) e Serving Layer (combina e serve os resultados de ambas as camadas). A serving layer é fundamental pois fornece uma visão unificada, permitindo consultas que abrangem tanto dados históricos processados em batch quanto dados recentes processados em tempo real.

---

## **QUESTÃO 5** (Adaptada - CONSULPLAN 2024)

**Apache Kafka é uma plataforma de streaming distribuída amplamente utilizada em arquiteturas de Big Data. Sobre o Apache Kafka, analise as assertivas:**

**I.** Kafka organiza mensagens em tópicos, que são particionados e replicados entre brokers do cluster.  
**II.** Producers enviam mensagens para tópicos específicos, enquanto consumers leem mensagens desses tópicos.  
**III.** O Kafka mantém mensagens persistentes em disco por um período configurável, permitindo reprocessamento.  
**IV.** ZooKeeper é utilizado para coordenação do cluster e eleição de líderes de partição.  
**V.** Kafka Connect facilita a integração com sistemas externos através de conectores pré-construídos.

**Alternativas:**
- A) Apenas I, II e III estão corretas
- B) Apenas I, II e IV estão corretas
- C) Apenas II, III e V estão corretas  
- D) Apenas I, III, IV e V estão corretas
- E) Todas as assertivas estão corretas

---

### **RESPOSTA: E**

**Explicação:** Todas as assertivas estão corretas. Kafka é uma plataforma de streaming que: (I) organiza dados em tópicos particionados e replicados; (II) utiliza padrão producer-consumer; (III) persiste mensagens em disco com retenção configurável; (IV) usa ZooKeeper para coordenação (embora versões mais recentes estejam migrando para KRaft); (V) oferece Kafka Connect para integração com sistemas externos via conectores.

---

## **QUESTÃO 6** (Adaptada - CESPE 2023)

**NoSQL representa uma categoria de sistemas de gerenciamento de banco de dados que diferem do modelo relacional tradicional. Sobre bancos de dados NoSQL, julgue as afirmativas:**

**I.** Bancos orientados a documentos como MongoDB armazenam dados em formato JSON/BSON, sendo adequados para dados semi-estruturados.  
**II.** Bancos de coluna como Apache Cassandra são otimizados para consultas analíticas em grandes volumes de dados.  
**III.** Bancos orientados a grafos como Neo4j são ideais para análise de relacionamentos complexos e redes sociais.  
**IV.** Bancos chave-valor como Redis oferecem alta performance para operações simples de leitura/escrita.  
**V.** NoSQL elimina completamente a necessidade de esquemas de dados, oferecendo flexibilidade total.

**Alternativas:**
- A) Apenas I, II e III estão corretas
- B) Apenas I, II, III e IV estão corretas
- C) Apenas I, III e IV estão corretas
- D) Apenas II, IV e V estão corretas
- E) Todas as afirmativas estão corretas

---

### **RESPOSTA: B**

**Explicação:** As assertivas I, II, III e IV estão corretas, mas a V está incorreta. NoSQL oferece esquemas flexíveis (schema-less ou schema-optional), mas não elimina completamente a necessidade de estrutura de dados. Bancos como MongoDB têm esquemas dinâmicos, mas ainda requerem alguma organização lógica dos dados. A flexibilidade é maior que bancos relacionais, mas não é "total" como afirmado na assertiva V.

---

## **QUESTÃO 7** (Adaptada - FCC 2024)

**Machine Learning aplicado a Big Data requer frameworks e bibliotecas especializadas para processamento distribuído. Sobre esta aplicação, é CORRETO afirmar:**

**Alternativas:**
- A) Scikit-learn é a biblioteca mais adequada para machine learning distribuído em clusters Hadoop
- B) Apache Spark MLlib oferece algoritmos de machine learning otimizados para processamento distribuído
- C) Frameworks de Deep Learning como TensorFlow não podem ser integrados com ambientes de Big Data
- D) Apache Mahout é exclusivamente compatível com algoritmos de aprendizado supervisionado
- E) Machine Learning em Big Data requer sempre o uso de GPUs especializadas

---

### **RESPOSTA: B**

**Explicação:** Apache Spark MLlib é especificamente projetado para machine learning distribuído, oferecendo algoritmos escaláveis como classificação, regressão, clustering e filtragem colaborativa. Scikit-learn (A) é excelente mas limitado a processamento em uma única máquina. TensorFlow (C) pode ser integrado com Big Data através de TensorFlow on Spark ou TensorFlowOnSpark. Mahout (D) suporta tanto aprendizado supervisionado quanto não-supervisionado. GPUs (E) são úteis mas não obrigatórias para ML em Big Data.

---

## **QUESTÃO 8** (Adaptada - VUNESP 2023)

**Data Lake é um conceito fundamental em arquiteturas modernas de Big Data. Sobre Data Lakes, analise as afirmações:**

**I.** Data Lake armazena dados em seu formato nativo, incluindo dados estruturados, semi-estruturados e não-estruturados.  
**II.** Diferentemente de Data Warehouses, Data Lakes aplicam esquema na leitura (schema-on-read) em vez de esquema na escrita.  
**III.** Data Lakes eliminam a necessidade de governança de dados e controle de qualidade.  
**IV.** Apache HDFS, Amazon S3 e Azure Data Lake Storage são exemplos de tecnologias para implementar Data Lakes.  
**V.** Data Lakes permitem análises exploratórias e descoberta de padrões em dados não processados.

**Estão corretas:**
- A) Apenas I, II e III
- B) Apenas I, II e IV
- C) Apenas I, II, IV e V
- D) Apenas II, III e V
- E) Todas as afirmações

---

### **RESPOSTA: C**

**Explicação:** As afirmações I, II, IV e V estão corretas. Data Lakes armazenam dados em formato nativo (I), aplicam schema-on-read (II), podem ser implementados em HDFS/S3/ADLS (IV) e permitem análises exploratórias (V). A afirmação III está incorreta pois Data Lakes AUMENTAM a necessidade de governança devido à diversidade e volume de dados armazenados, sendo essencial ter políticas de qualidade, catalogação e linhagem de dados.

---

## **QUESTÃO 9** (Adaptada - FGV 2024)

**Apache Hive é uma ferramenta de data warehouse construída sobre o Hadoop para facilitar consultas e análises de dados. Sobre o Hive, é CORRETO afirmar:**

**Alternativas:**
- A) Hive armazena dados exclusivamente em formato proprietário otimizado para consultas SQL
- B) HiveQL é uma linguagem de consulta idêntica ao SQL padrão, sem adaptações para processamento distribuído
- C) Hive utiliza MapReduce como engine de execução padrão, mas pode ser configurado para usar Spark ou Tez
- D) Metastore do Hive armazena apenas os dados das tabelas, não incluindo metadados de esquema
- E) Hive é adequado apenas para processamento OLTP de alta concorrência

---

### **RESPOSTA: C**

**Explicação:** Hive pode usar diferentes engines de execução: MapReduce (padrão tradicional), Apache Tez (otimizado) ou Apache Spark (via SparkSQL). A alternativa A está incorreta pois Hive pode armazenar dados em vários formatos (texto, Parquet, ORC, etc.). B está incorreta pois HiveQL tem adaptações para distribuição. D está incorreta pois Metastore armazena metadados de esquema, não dados das tabelas. E está incorreta pois Hive é focado em OLAP, não OLTP.

---

## **QUESTÃO 10** (Adaptada - CESPE 2024)

**Elasticsearch é um mecanismo de busca e análise distribuído baseado em Apache Lucene. Sobre Elasticsearch, julgue as assertivas:**

**I.** Elasticsearch armazena dados em índices, que são compostos por tipos e documentos JSON.  
**II.** A arquitetura do Elasticsearch é baseada em nós que formam um cluster distribuído.  
**III.** Kibana é a ferramenta de visualização associada ao Elasticsearch para criação de dashboards.  
**IV.** Logstash é utilizado para coleta, transformação e envio de dados para o Elasticsearch.  
**V.** Elasticsearch oferece apenas busca textual, não suportando análises numéricas ou agregações.

**Alternativas:**
- A) Apenas I, II e III estão corretas
- B) Apenas I, II, III e IV estão corretas
- C) Apenas II, III e IV estão corretas
- D) Apenas I, III e V estão corretas
- E) Todas as assertivas estão corretas

---

### **RESPOSTA: B**

**Explicação:** As assertivas I, II, III e IV estão corretas. Elasticsearch organiza dados em índices/documentos JSON (I), usa arquitetura distribuída em cluster (II), integra-se com Kibana para visualização (III) e Logstash para ingestão de dados (IV), formando o stack ELK. A assertiva V está incorreta pois Elasticsearch oferece análises numéricas avançadas, agregações, métricas estatísticas e análises geoespaciais, não apenas busca textual.

---

## **QUESTÃO 11** (Adaptada - CONSULPLAN 2023)

**Apache Airflow é uma plataforma para desenvolvimento, agendamento e monitoramento de workflows. Sobre Airflow, é CORRETO afirmar:**

**Alternativas:**
- A) DAGs (Directed Acyclic Graphs) no Airflow podem conter ciclos para processamento iterativo
- B) Airflow executa tarefas apenas em modo sequencial, não suportando paralelização
- C) Operators no Airflow definem tarefas específicas como BashOperator, PythonOperator, SQLOperator
- D) Airflow não oferece interface web para monitoramento de execuções
- E) Schedulers no Airflow funcionam apenas com intervalos fixos diários

---

### **RESPOSTA: C**

**Explicação:** Operators no Airflow definem diferentes tipos de tarefas: BashOperator (comandos shell), PythonOperator (funções Python), SQLOperator (consultas SQL), entre outros. A alternativa A está incorreta pois DAGs são acíclicos por definição. B está incorreta pois Airflow suporta execução paralela de tarefas. D está incorreta pois Airflow possui interface web rica para monitoramento. E está incorreta pois suporta diversos intervalos de agendamento (cron expressions).

---

## **QUESTÃO 12** (Adaptada - FCC 2023)

**Apache Storm é um sistema de processamento de stream em tempo real. Sobre Storm, analise as afirmações:**

**I.** Storm processa streams infinitos de dados com latência baixa e garantias de processamento.  
**II.** Topologias no Storm são compostas por Spouts (fontes de dados) e Bolts (processamento).  
**III.** Storm oferece garantias de processamento "at-least-once" e "exactly-once".  
**IV.** Storm é adequado apenas para processamento batch de grandes volumes de dados.  
**V.** Trident é uma abstração de alto nível sobre Storm Core para processamento estateful.

**Estão corretas:**
- A) Apenas I, II e III
- B) Apenas I, II e V
- C) Apenas II, III e IV  
- D) Apenas I, II, III e V
- E) Todas as afirmações

---

### **RESPOSTA: B**

**Explicação:** As afirmações I, II e V estão corretas. Storm processa streams com baixa latência (I), usa topologias com Spouts/Bolts (II), e Trident oferece abstração de alto nível (V). A afirmação III está parcialmente incorreta pois Storm Core oferece "at-least-once" mas "exactly-once" requer Trident. A afirmação IV está incorreta pois Storm é focado em streaming real-time, não processamento batch.

---

## **QUESTÃO 13** (Adaptada - VUNESP 2024)

**Apache Flink é um framework de processamento de stream que oferece recursos avançados. Sobre Flink, é CORRETO afirmar:**

**Alternativas:**
- A) Flink processa apenas dados em batch, não oferecendo capacidades de streaming
- B) Flink oferece processamento de streams com event-time e watermarks para dados fora de ordem
- C) Flink não suporta integração com sistemas de armazenamento como HDFS ou Kafka
- D) Estado (state) em aplicações Flink não pode ser mantido entre reinicializações
- E) Flink é adequado apenas para processamento de dados estruturados em formato relacional

---

### **RESPOSTA: B**

**Explicação:** Apache Flink oferece processamento avançado de streams com suporte a event-time (tempo do evento) e watermarks para lidar com dados que chegam fora de ordem, características essenciais para processamento de stream preciso. Flink processa tanto batch quanto stream (A incorreta), integra-se com Kafka/HDFS/etc (C incorreta), mantém estado distribuído com checkpointing (D incorreta), e processa dados estruturados e não-estruturados (E incorreta).

---

## **QUESTÃO 14** (Adaptada - FGV 2023)

**Data Governance em projetos de Big Data é fundamental para o sucesso organizacional. Sobre governança de dados, analise as assertivas:**

**I.** Data Governance inclui políticas para qualidade, privacidade, segurança e ciclo de vida dos dados.  
**II.** Data Steward é o responsável técnico por implementar políticas de governança em nível operacional.  
**III.** Linhagem de dados (data lineage) rastreia a origem e transformações dos dados ao longo do pipeline.  
**IV.** Master Data Management (MDM) garante consistência de dados mestres entre sistemas.  
**V.** LGPD (Lei Geral de Proteção de Dados) não se aplica a projetos de Big Data governamentais.

**Alternativas:**
- A) Apenas I, II e III estão corretas
- B) Apenas I, II, III e IV estão corretas
- C) Apenas I, III e IV estão corretas
- D) Apenas II, IV e V estão corretas
- E) Todas as assertivas estão corretas

---

### **RESPOSTA: B**

**Explicação:** As assertivas I, II, III e IV estão corretas. Data Governance abrange políticas abrangentes (I), Data Stewards implementam operacionalmente (II), linhagem rastreia origem/transformações (III), e MDM garante consistência de dados mestres (IV). A assertiva V está incorreta pois LGPD aplica-se a TODOS os projetos que processam dados pessoais, incluindo Big Data governamental, sendo ainda mais rigorosa no setor público.

---

## **QUESTÃO 15** (Adaptada - CESPE 2023)

**Apache Zeppelin é uma ferramenta de notebook para análise interativa de dados. Sobre Zeppelin, julgue as afirmações:**

**I.** Zeppelin oferece interface web para criação de notebooks com múltiplas linguagens de programação.  
**II.** Interpreters no Zeppelin permitem execução de código Spark, SQL, Python, R e outras linguagens.  
**III.** Zeppelin suporta visualizações interativas de dados diretamente nos notebooks.  
**IV.** Zeppelin pode conectar-se a diferentes fontes de dados como HDFS, JDBC, Elasticsearch.  
**V.** Notebooks do Zeppelin não podem ser compartilhados entre usuários da organização.

**Alternativas:**
- A) Apenas I, II e III estão corretas
- B) Apenas I, II, III e IV estão corretas
- C) Apenas II, III e IV estão corretas
- D) Apenas I, III e V estão corretas
- E) Todas as afirmações estão corretas

---

### **RESPOSTA: B**

**Explicação:** As afirmações I, II, III e IV estão corretas. Zeppelin oferece interface web para notebooks (I), suporta múltiplos interpreters/linguagens (II), permite visualizações interativas (III), e conecta-se a diversas fontes de dados (IV). A afirmação V está incorreta pois Zeppelin oferece recursos robustos de colaboração, permitindo compartilhamento de notebooks, controle de acesso por usuário/grupo, e trabalho colaborativo em tempo real.

---

## **QUESTÃO 16** (Adaptada - CONSULPLAN 2024)

**Apache Phoenix é uma camada SQL sobre Apache HBase. Sobre Phoenix, é CORRETO afirmar:**

**Alternativas:**
- A) Phoenix substitui completamente o HBase, eliminando a necessidade do banco NoSQL subjacente
- B) Phoenix oferece interface SQL padrão para consultas em dados armazenados no HBase
- C) Phoenix suporta apenas operações de leitura, não permitindo inserções ou atualizações
- D) Phoenix não oferece indexação secundária para otimização de consultas
- E) Phoenix é incompatível com ferramentas de BI que utilizam drivers JDBC

---

### **RESPOSTA: B**

**Explicação:** Apache Phoenix oferece uma camada SQL sobre HBase, permitindo consultas SQL padrão em dados NoSQL. Phoenix não substitui o HBase (A), funciona como uma camada sobre ele. Suporta operações completas CRUD (C incorreta), oferece indexação secundária avançada (D incorreta), e é compatível com ferramentas BI via drivers JDBC/ODBC (E incorreta).

---

## **QUESTÃO 17** (Adaptada - FCC 2024)

**Apache Drill é um engine de consultas SQL para Big Data. Sobre Drill, analise as assertivas:**

**I.** Drill permite consultas SQL em dados armazenados em diferentes formatos e sistemas sem ETL prévio.  
**II.** Drill suporta schema-on-read, permitindo consultas em dados semi-estruturados como JSON.  
**III.** Drill pode consultar dados em HDFS, S3, bancos NoSQL e relacionais simultaneamente.  
**IV.** Drill requer definição prévia de esquemas antes de realizar consultas nos dados.  
**V.** Drill é otimizado para consultas interativas com baixa latência.

**Estão corretas:**
- A) Apenas I, II e III
- B) Apenas I, II, III e V
- C) Apenas I, II e IV
- D) Apenas II, III e V
- E) Todas as assertivas

---

### **RESPOSTA: B**

**Explicação:** As assertivas I, II, III e V estão corretas. Apache Drill permite consultas SQL sem ETL (I), suporta schema-on-read para dados semi-estruturados (II), consulta múltiplas fontes simultaneamente (III), e é otimizado para consultas interativas (V). A assertiva IV está incorreta pois Drill NÃO requer definição prévia de esquemas - essa é justamente sua principal característica: consultas ad-hoc sem esquema predefinido.

---

## **QUESTÃO 18** (Adaptada - VUNESP 2023)

**Apache Sqoop é uma ferramenta para transferência de dados entre Hadoop e bancos relacionais. Sobre Sqoop, é CORRETO afirmar:**

**Alternativas:**
- A) Sqoop transfere dados apenas do Hadoop para bancos relacionais (export)
- B) Sqoop utiliza MapReduce para paralelizar transferências de grandes volumes de dados
- C) Sqoop não suporta transferência incremental de dados, apenas carga completa
- D) Sqoop funciona exclusivamente com bancos de dados Oracle
- E) Sqoop armazena dados no Hadoop apenas em formato texto simples

---

### **RESPOSTA: B**

**Explicação:** Sqoop utiliza MapReduce para paralelizar a transferência de dados, dividindo o trabalho em múltiplos mappers para melhor performance. Sqoop suporta tanto import quanto export (A incorreta), oferece transferência incremental via --incremental (C incorreta), funciona com diversos SGBDs que tenham driver JDBC (D incorreta), e suporta múltiplos formatos de saída como Parquet, Avro, além de texto (E incorreta).

---

## **QUESTÃO 19** (Adaptada - FGV 2024)

**Apache Oozie é um sistema de workflow para gerenciar jobs Hadoop. Sobre Oozie, analise as afirmações:**

**I.** Oozie workflows são definidos em XML especificando ações e dependências entre jobs.  
**II.** Oozie suporta apenas jobs MapReduce, não integrando com Spark ou Hive.  
**III.** Coordinators no Oozie permitem agendamento de workflows baseado em tempo e disponibilidade de dados.  
**IV.** Bundles no Oozie agrupam múltiplos coordinators para gerenciamento conjunto.  
**V.** Oozie oferece interface web para monitoramento e gerenciamento de workflows.

**Alternativas:**
- A) Apenas I, III e V estão corretas
- B) Apenas I, III, IV e V estão corretas
- C) Apenas I, II e III estão corretas
- D) Apenas II, IV e V estão corretas
- E) Todas as afirmações estão corretas

---

### **RESPOSTA: B**

**Explicação:** As afirmações I, III, IV e V estão corretas. Oozie define workflows em XML (I), Coordinators fazem agendamento baseado em tempo/dados (III), Bundles agrupam coordinators (IV), e oferece interface web (V). A afirmação II está incorreta pois Oozie integra-se com diversas tecnologias além de MapReduce: Spark, Hive, Pig, Sqoop, Shell scripts, etc.

---

## **QUESTÃO 20** (Adaptada - CESPE 2024)

**Apache Impala é um engine de consultas SQL de baixa latência para Big Data. Sobre Impala, julgue as assertivas:**

**I.** Impala executa consultas SQL diretamente sobre dados no HDFS sem conversão para MapReduce.  
**II.** Impala compartilha o mesmo metastore que o Hive, permitindo acesso às mesmas tabelas.  
**III.** Impala é otimizado para consultas analíticas interativas com resposta em tempo real.  
**IV.** Impala utiliza arquitetura MPP (Massively Parallel Processing) para processamento distribuído.  
**V.** Impala requer que todos os dados sejam carregados na memória antes do processamento.

**Alternativas:**
- A) Apenas I, II e III estão corretas
- B) Apenas I, II, III e IV estão corretas
- C) Apenas II, III e IV estão corretas
- D) Apenas I, III e V estão corretas
- E) Todas as assertivas estão corretas

---

### **RESPOSTA: B**

**Explicação:** As assertivas I, II, III e IV estão corretas. Impala executa SQL nativamente sem MapReduce (I), usa o mesmo metastore do Hive (II), é otimizado para consultas interativas (III), e utiliza arquitetura MPP (IV). A assertiva V está incorreta pois Impala NÃO requer que todos os dados estejam na memória - ele otimiza o uso de memória mas pode processar datasets maiores que a RAM disponível, usando técnicas de spilling to disk quando necessário.

---

## **QUESTÃO 21** (Adaptada - CONSULPLAN 2023)

**Apache HBase é um banco de dados NoSQL distribuído construído sobre HDFS. Sobre HBase, é CORRETO afirmar:**

**Alternativas:**
- A) HBase armazena dados em formato relacional com esquemas rígidos definidos previamente
- B) HBase oferece consistência eventual similar ao modelo BASE, não garantindo ACID
- C) HBase organiza dados em column families e oferece acesso randômico de baixa latência
- D) HBase é adequado apenas para cargas de trabalho analíticas, não suportando transações OLTP
- E) HBase não suporta versionamento de dados, mantendo apenas a versão mais recente

---

### **RESPOSTA: C**

**Explicação:** HBase organiza dados em column families (grupos de colunas relacionadas) e oferece acesso randômico de baixa latência através de row keys, sendo adequado para aplicações que requerem leituras/escritas rápidas. HBase usa modelo chave-valor com esquema flexível (A incorreta), oferece consistência forte para operações single-row (B incorreta), suporta tanto OLTP quanto análises (D incorreta), e oferece versionamento automático de dados com timestamps (E incorreta).

---

## **QUESTÃO 22** (Adaptada - FCC 2024)

**Apache Parquet é um formato de armazenamento colunar otimizado para análises. Sobre Parquet, analise as assertivas:**

**I.** Parquet armazena dados em formato colunar, otimizando consultas que acessam subconjuntos de colunas.  
**II.** Parquet oferece compressão eficiente através de algoritmos como Snappy, GZIP e LZO.  
**III.** Parquet mantém metadados que permitem predicate pushdown para otimização de consultas.  
**IV.** Parquet é compatível apenas com Apache Spark, não funcionando com Hive ou Impala.  
**V.** Parquet suporta tipos de dados complexos como arrays, maps e structs aninhados.

**Estão corretas:**
- A) Apenas I, II e III
- B) Apenas I, II, III e V
- C) Apenas I, II e IV
- D) Apenas II, III e V
- E) Todas as assertivas

---

### **RESPOSTA: B**

**Explicação:** As assertivas I, II, III e V estão corretas. Parquet usa armazenamento colunar (I), oferece compressão eficiente (II), mantém metadados para otimização (III), e suporta tipos complexos aninhados (V). A assertiva IV está incorreta pois Parquet é amplamente compatível com todo o ecossistema Hadoop: Spark, Hive, Impala, Drill, Presto, entre outros.

---

## **QUESTÃO 23** (Adaptada - VUNESP 2023)

**Apache Avro é um sistema de serialização de dados usado em Big Data. Sobre Avro, é CORRETO afirmar:**

**Alternativas:**
- A) Avro armazena esquemas separadamente dos dados, não oferecendo evolução de esquema
- B) Avro é um formato apenas de leitura, não permitindo escritas ou modificações de dados
- C) Avro suporta evolução de esquema, permitindo compatibilidade entre versões diferentes
- D) Avro funciona exclusivamente com dados estruturados em formato tabular
- E) Avro não oferece compressão de dados, resultando em arquivos grandes

---

### **RESPOSTA: C**

**Explicação:** Apache Avro oferece evolução de esquema (schema evolution), permitindo que produtores e consumidores de dados usem versões diferentes do esquema mantendo compatibilidade para frente e para trás. Avro incorpora esquemas nos dados permitindo evolução (A incorreta), suporta operações completas de leitura/escrita (B incorreta), trabalha com dados estruturados e semi-estruturados (D incorreta), e oferece compressão nativa (E incorreta).

---

## **QUESTÃO 24** (Adaptada - FGV 2023)

**Apache Kudu é um sistema de armazenamento colunar para análises rápidas. Sobre Kudu, analise as afirmações:**

**I.** Kudu combina as vantagens de armazenamento colunar com capacidades de mutação de dados.  
**II.** Kudu oferece consistência forte e suporte a transações ACID para operações single-tablet.  
**III.** Kudu integra-se nativamente com Apache Spark e Apache Impala para consultas SQL.  
**IV.** Kudu replica dados automaticamente entre tablet servers para alta disponibilidade.  
**V.** Kudu é adequado apenas para cargas de trabalho de escrita, não otimizado para leituras analíticas.

**Alternativas:**
- A) Apenas I, II e III estão corretas
- B) Apenas I, II, III e IV estão corretas
- C) Apenas I, III e IV estão corretas
- D) Apenas II, IV e V estão corretas
- E) Todas as afirmações estão corretas

---

### **RESPOSTA: B**

**Explicação:** As afirmações I, II, III e IV estão corretas. Kudu combina armazenamento colunar com mutabilidade (I), oferece consistência forte/ACID single-tablet (II), integra-se com Spark/Impala (III), e replica dados entre tablet servers (IV). A afirmação V está incorreta pois Kudu é otimizado tanto para escritas quanto para análises, sendo projetado especificamente para casos de uso que requerem tanto ingestão rápida quanto consultas analíticas performáticas.

---

## **QUESTÃO 25** (Adaptada - CESPE 2024)

**Apache Atlas é uma plataforma de governança de dados para o ecossistema Hadoop. Sobre Atlas, julgue as assertivas:**

**I.** Atlas oferece catalogação automatizada de metadados de diversas fontes de dados do ecossistema Hadoop.  
**II.** Atlas mantém linhagem de dados (data lineage) mostrando origem e transformações dos datasets.  
**III.** Atlas oferece classificação de dados baseada em tags e políticas de governança.  
**IV.** Atlas integra-se com Apache Ranger para controle de acesso baseado em metadados.  
**V.** Atlas funciona apenas com dados estruturados, não suportando dados semi-estruturados.

**Alternativas:**
- A) Apenas I, II e III estão corretas
- B) Apenas I, II, III e IV estão corretas
- C) Apenas I, II e IV estão corretas
- D) Apenas II, III e V estão corretas
- E) Todas as assertivas estão corretas

---

### **RESPOSTA: B**

**Explicação:** As assertivas I, II, III e IV estão corretas. Atlas oferece catalogação automatizada (I), mantém linhagem de dados (II), oferece classificação via tags (III), e integra-se com Ranger para controle de acesso (IV). A assertiva V está incorreta pois Atlas suporta metadados de dados estruturados, semi-estruturados e não-estruturados do ecossistema Hadoop.

---

## **QUESTÃO 26** (Adaptada - CONSULPLAN 2024)

**Apache Ranger oferece gerenciamento centralizado de segurança para o ecossistema Hadoop. Sobre Ranger, é CORRETO afirmar:**

**Alternativas:**
- A) Ranger oferece apenas controle de acesso, não incluindo auditoria de operações
- B) Ranger suporta políticas fine-grained de acesso baseadas em usuários, grupos e recursos específicos
- C) Ranger funciona exclusivamente com Apache Hive, não integrando com outros componentes
- D) Ranger não oferece integração com sistemas de autenticação externos como LDAP/AD
- E) Ranger armazena políticas localmente em cada nó do cluster sem sincronização

---

### **RESPOSTA: B**

**Explicação:** Apache Ranger oferece políticas fine-grained (granulares) de controle de acesso baseadas em usuários, grupos, recursos específicos (tabelas, colunas, arquivos), horários, endereços IP, etc. Ranger inclui auditoria completa (A incorreta), integra-se com todo ecossistema Hadoop: Hive, HBase, HDFS, Storm, Kafka, etc. (C incorreta), oferece integração com LDAP/AD/Kerberos (D incorreta), e sincroniza políticas centralmente via Ranger Admin (E incorreta).

---

## **QUESTÃO 27** (Adaptada - FCC 2023)

**Apache Knox é um gateway de segurança para clusters Hadoop. Sobre Knox, analise as assertivas:**

**I.** Knox oferece ponto único de acesso (single point of access) para serviços do cluster Hadoop.  
**II.** Knox suporta autenticação via LDAP, AD, SSO e certificados digitais.  
**III.** Knox oferece SSL/TLS termination para comunicação segura com o cluster.  
**IV.** Knox expõe APIs REST para todos os serviços Hadoop através de um proxy seguro.  
**V.** Knox elimina a necessidade de controle de acesso dentro do cluster Hadoop.

**Estão corretas:**
- A) Apenas I, II e III
- B) Apenas I, II, III e IV
- C) Apenas I, II e IV
- D) Apenas II, III e V
- E) Todas as assertivas

---

### **RESPOSTA: B**

**Explicação:** As assertivas I, II, III e IV estão corretas. Knox oferece gateway único (I), múltiplos métodos de autenticação (II), SSL/TLS termination (III), e proxy REST APIs (IV). A assertiva V está incorreta pois Knox COMPLEMENTA o controle de acesso interno (como Ranger), não o elimina. Knox oferece perímetro de segurança mas controles internos permanecem necessários para defesa em profundidade.

---

## **QUESTÃO 28** (Adaptada - VUNESP 2024)

**Apache Ambari é uma plataforma de gerenciamento para clusters Hadoop. Sobre Ambari, é CORRETO afirmar:**

**Alternativas:**
- A) Ambari oferece apenas monitoramento de cluster, não incluindo provisionamento de serviços
- B) Ambari utiliza interface de linha de comando exclusivamente, sem interface web
- C) Ambari oferece instalação, configuração, monitoramento e gerenciamento centralizados de clusters Hadoop
- D) Ambari funciona apenas com distribuições Apache Hadoop puras, não suportando outras distribuições
- E) Ambari não oferece alertas ou notificações sobre problemas no cluster

---

### **RESPOSTA: C**

**Explicação:** Apache Ambari oferece gerenciamento completo de clusters Hadoop incluindo: instalação automatizada, configuração centralizada, monitoramento em tempo real, e operações de manutenção. Ambari inclui provisionamento além de monitoramento (A incorreta), oferece interface web rica além de CLI (B incorreta), suporta múltiplas distribuições Hadoop (D incorreta), e oferece sistema robusto de alertas e notificações (E incorreta).

---

## **QUESTÃO 29** (Adaptada - FGV 2024)

**Apache Livy é um serviço REST para Apache Spark que permite interação remota com clusters Spark. Sobre Livy, analise as afirmações:**

**I.** Livy permite submissão de jobs Spark através de APIs REST sem acesso direto ao cluster.  
**II.** Livy suporta sessões interativas para Scala, Python e R no Spark.  
**III.** Livy oferece isolamento de usuários através de sessões separadas no cluster Spark.  
**IV.** Livy requer que todos os usuários tenham acesso direto aos nós do cluster Spark.  
**V.** Livy integra-se com sistemas de autenticação e autorização para controle de acesso.

**Alternativas:**
- A) Apenas I, II e III estão corretas
- B) Apenas I, II, III e V estão corretas
- C) Apenas I, II e IV estão corretas
- D) Apenas II, III e V estão corretas
- E) Todas as afirmações estão corretas

---

### **RESPOSTA: B**

**Explicação:** As afirmações I, II, III e V estão corretas. Livy permite submissão via REST APIs (I), suporta sessões interativas Scala/Python/R (II), oferece isolamento por usuário (III), e integra-se com autenticação/autorização (V). A afirmação IV está incorreta pois Livy elimina justamente a necessidade de acesso direto ao cluster - usuários interagem apenas com Livy via REST, que gerencia as conexões com Spark.

---

## **QUESTÃO 30** (Adaptada - CESPE 2023)

**Apache Solr é uma plataforma de busca empresarial baseada em Apache Lucene. Sobre Solr, julgue as assertivas:**

**I.** Solr oferece busca textual avançada com recursos como faceting, highlighting e auto-complete.  
**II.** SolrCloud permite operação distribuída com sharding automático e alta disponibilidade.  
**III.** Solr suporta indexação de documentos em tempo próximo ao real através de near real-time search.  
**IV.** Solr utiliza ZooKeeper para coordenação em ambientes distribuídos SolrCloud.  
**V.** Solr oferece apenas busca textual, não suportando consultas geoespaciais ou numéricas.

**Alternativas:**
- A) Apenas I, II e III estão corretas
- B) Apenas I, II, III e IV estão corretas
- C) Apenas I, II e IV estão corretas
- D) Apenas II, III e V estão corretas
- E) Todas as assertivas estão corretas

---

### **RESPOSTA: B**

**Explicação:** As assertivas I, II, III e IV estão corretas. Solr oferece busca textual avançada com faceting/highlighting (I), SolrCloud oferece distribuição/HA (II), suporta near real-time search (III), e usa ZooKeeper para coordenação (IV). A assertiva V está incorreta pois Solr oferece muito além de busca textual: consultas geoespaciais, busca numérica, range queries, filtros complexos, agregações, análises estatísticas, etc.

---

## **QUESTÃO 31** (Adaptada - CONSULPLAN 2023)

**Apache Tez é um framework de execução para processamento de dados direcionado por grafos acíclicos (DAG). Sobre Tez, é CORRETO afirmar:**

**Alternativas:**
- A) Tez substitui completamente o MapReduce, sendo incompatível com aplicações MapReduce existentes
- B) Tez otimiza execução de consultas complexas evitando escritas intermediárias desnecessárias em disco
- C) Tez funciona apenas com Apache Hive, não integrando com outras ferramentas do ecossistema
- D) Tez não oferece reutilização de containers, criando novos JVMs para cada tarefa
- E) Tez é adequado apenas para processamento batch, não suportando consultas interativas

---

### **RESPOSTA: B**

**Explicação:** Apache Tez otimiza a execução de consultas complexas através de DAGs (Directed Acyclic Graphs) que evitam escritas intermediárias desnecessárias em disco, mantendo dados em memória entre estágios quando possível. Tez é compatível com MapReduce via API (A incorreta), integra-se com Hive, Pig e outras ferramentas (C incorreta), oferece reutilização de containers para melhor performance (D incorreta), e é otimizado tanto para batch quanto consultas interativas (E incorreta).

---

## **QUESTÃO 32** (Adaptada - FCC 2024)

**Apache Pig é uma plataforma para análise de grandes datasets usando linguagem de alto nível. Sobre Pig, analise as assertivas:**

**I.** Pig Latin é uma linguagem de fluxo de dados que abstrai complexidades do MapReduce.  
**II.** Pig compila scripts Pig Latin em jobs MapReduce para execução no cluster Hadoop.  
**III.** Pig oferece User Defined Functions (UDFs) para extensão de funcionalidades em Java, Python e JavaScript.  
**IV.** Pig é adequado apenas para desenvolvedores Java, não sendo acessível para analistas de dados.  
**V.** Pig Streaming permite integração com scripts em linguagens externas como Python e R.

**Estão corretas:**
- A) Apenas I, II e III
- B) Apenas I, II, III e V
- C) Apenas I, II e IV
- D) Apenas II, III e V
- E) Todas as assertivas

---

### **RESPOSTA: B**

**Explicação:** As assertivas I, II, III e V estão corretas. Pig Latin abstrai MapReduce com linguagem de fluxo (I), compila para MapReduce (II), suporta UDFs em múltiplas linguagens (III), e oferece Pig Streaming para scripts externos (V). A assertiva IV está incorreta pois Pig foi projetado especificamente para analistas e cientistas de dados, oferecendo sintaxe mais simples que Java/MapReduce, sendo mais acessível que programação MapReduce direta.

---

## **QUESTÃO 33** (Adaptada - VUNESP 2023)

**Apache Flume é um sistema para coleta, agregação e transporte de dados de log. Sobre Flume, é CORRETO afirmar:**

**Alternativas:**
- A) Flume oferece apenas coleta de logs de aplicações web, não suportando outras fontes de dados
- B) Flume utiliza arquitetura baseada em agents com sources, channels e sinks para pipeline de dados
- C) Flume não oferece garantias de entrega, podendo perder dados em caso de falhas
- D) Flume armazena dados apenas em HDFS, não integrando com outros sistemas de armazenamento
- E) Flume processa dados em tempo real durante a coleta, não sendo apenas um sistema de transporte

---

### **RESPOSTA: B**

**Explicação:** Apache Flume utiliza arquitetura baseada em agents, onde cada agent possui: sources (coletam dados), channels (bufferizam dados), e sinks (entregam dados ao destino), formando pipelines configuráveis de dados. Flume coleta diversos tipos de dados além de logs web (A incorreta), oferece garantias de entrega configuráveis (C incorreta), integra-se com múltiplos destinos além de HDFS (D incorreta), e é principalmente um sistema de transporte, não processamento (E incorreta).

---

## **QUESTÃO 34** (Adaptada - FGV 2024)

**Apache Kafka Connect é uma ferramenta para integração de dados com Apache Kafka. Sobre Kafka Connect, analise as afirmações:**

**I.** Kafka Connect oferece conectores pré-construídos para integração com bancos de dados, sistemas de arquivos e aplicações.  
**II.** Kafka Connect suporta operação distribuída com balanceamento automático de conectores entre workers.  
**III.** Kafka Connect oferece transformações simples de dados durante o processo de integração.  
**IV.** Kafka Connect requer programação customizada para cada fonte ou destino de dados.  
**V.** Kafka Connect mantém offset tracking para garantir exactly-once delivery quando possível.

**Alternativas:**
- A) Apenas I, II e III estão corretas
- B) Apenas I, II, III e V estão corretas
- C) Apenas I, II e IV estão corretas
- D) Apenas II, III e V estão corretas
- E) Todas as afirmações estão corretas

---

### **RESPOSTA: B**

**Explicação:** As afirmações I, II, III e V estão corretas. Kafka Connect oferece conectores pré-construídos (I), operação distribuída com balanceamento (II), transformações simples built-in (III), e offset tracking para exactly-once (V). A afirmação IV está incorreta pois Kafka Connect foi projetado para ELIMINAR a necessidade de programação customizada, oferecendo conectores reutilizáveis e configuração declarativa via JSON/properties.

---

## **QUESTÃO 35** (Adaptada - CESPE 2024)

**Apache Beam é um modelo de programação unificado para processamento batch e stream. Sobre Beam, julgue as assertivas:**

**I.** Beam oferece APIs unificadas que executam em múltiplos runners como Spark, Flink e Dataflow.  
**II.** Beam suporta windowing avançado para processamento de streams com event-time e processing-time.  
**III.** Beam oferece abstrações para side inputs e state management em aplicações streaming.  
**IV.** Beam elimina a necessidade de escolher runners específicos, executando automaticamente na melhor opção.  
**V.** Beam suporta triggers personalizados para controle avançado de quando resultados são emitidos.

**Alternativas:**
- A) Apenas I, II e III estão corretas
- B) Apenas I, II, III e V estão corretas
- C) Apenas I, II e V estão corretas
- D) Apenas II, III e IV estão corretas
- E) Todas as assertivas estão corretas

---

### **RESPOSTA: B**

**Explicação:** As assertivas I, II, III e V estão corretas. Beam oferece portabilidade entre runners (I), windowing avançado com event/processing time (II), side inputs e state management (III), e triggers personalizados (V). A assertiva IV está incorreta pois Beam NÃO escolhe automaticamente o runner - o desenvolvedor deve especificar explicitamente qual runner usar (DirectRunner, SparkRunner, FlinkRunner, etc.).

---

## **QUESTÃO 36** (Adaptada - CONSULPLAN 2024)

**Arquitetura Kappa é uma alternativa simplificada à Arquitetura Lambda para processamento de dados. Sobre Kappa, é CORRETO afirmar:**

**Alternativas:**
- A) Arquitetura Kappa mantém as três camadas da Lambda: batch, speed e serving layers
- B) Kappa elimina a batch layer, processando todos os dados através de streaming apenas
- C) Kappa é adequada apenas para dados que não requerem reprocessamento histórico
- D) Kappa utiliza diferentes tecnologias para processamento histórico e em tempo real
- E) Kappa oferece maior complexidade operacional que Lambda devido ao streaming contínuo

---

### **RESPOSTA: B**

**Explicação:** A Arquitetura Kappa simplifica Lambda eliminando a batch layer, processando TODOS os dados (históricos e novos) através de streaming apenas. Kappa tem apenas duas camadas: streaming e serving (A incorreta), permite reprocessamento histórico via replay de streams (C incorreta), usa a mesma tecnologia para todo processamento (D incorreta), e oferece MENOR complexidade operacional que Lambda (E incorreta).

---

## **QUESTÃO 37** (Adaptada - FCC 2023)

**MLflow é uma plataforma open source para gerenciar o ciclo de vida de machine learning. Sobre MLflow, analise as assertivas:**

**I.** MLflow Tracking registra experimentos, parâmetros, métricas e artefatos de modelos ML.  
**II.** MLflow Projects padroniza formato de projetos ML para reprodutibilidade e compartilhamento.  
**III.** MLflow Models oferece formato padrão para packaging de modelos com múltiplos flavors.  
**IV.** MLflow Model Registry gerencia versionamento e transições de estado de modelos em produção.  
**V.** MLflow funciona apenas com algoritmos scikit-learn, não suportando TensorFlow ou PyTorch.

**Estão corretas:**
- A) Apenas I, II e III
- B) Apenas I, II, III e IV
- C) Apenas I, II e IV
- D) Apenas II, III e V
- E) Todas as assertivas

---

### **RESPOSTA: B**

**Explicação:** As assertivas I, II, III e IV estão corretas. MLflow oferece: tracking de experimentos (I), padronização de projetos (II), packaging de modelos (III), e registry para versionamento (IV). A assertiva V está incorreta pois MLflow é agnóstico a frameworks, suportando scikit-learn, TensorFlow, PyTorch, XGBoost, Spark MLlib, e muitos outros através de seu sistema de flavors.

---

## **QUESTÃO 38** (Adaptada - VUNESP 2024)

**Apache Superset é uma plataforma de visualização e exploração de dados. Sobre Superset, é CORRETO afirmar:**

**Alternativas:**
- A) Superset conecta-se apenas a bancos relacionais, não suportando fontes NoSQL
- B) Superset oferece interface web para criação de dashboards interativos e visualizações
- C) Superset não suporta SQL Lab para consultas ad-hoc exploratórias
- D) Superset é uma ferramenta de linha de comando sem interface gráfica
- E) Superset não oferece controle de acesso baseado em papéis para usuários

---

### **RESPOSTA: B**

**Explicação:** Apache Superset oferece interface web rica para criação de dashboards interativos, gráficos diversos, e visualizações avançadas com drag-and-drop. Superset conecta-se a múltiplas fontes incluindo NoSQL (A incorreta), oferece SQL Lab para consultas exploratórias (C incorreta), tem interface web moderna não CLI (D incorreta), e oferece RBAC (Role-Based Access Control) robusto (E incorreta).

---

## **QUESTÃO 39** (Adaptada - FGV 2023)

**Presto (agora Trino) é um engine de consultas SQL distribuído para Big Data. Sobre Presto/Trino, analise as afirmações:**

**I.** Presto permite consultas federadas em múltiplas fontes de dados simultaneamente.  
**II.** Presto utiliza arquitetura MPP (Massively Parallel Processing) para consultas de baixa latência.  
**III.** Presto mantém dados em memória durante toda a execução, não utilizando disco.  
**IV.** Presto suporta conectores para HDFS, S3, bancos relacionais, Cassandra, Elasticsearch, etc.  
**V.** Presto oferece otimizações avançadas como predicate pushdown e partition pruning.

**Alternativas:**
- A) Apenas I, II e IV estão corretas
- B) Apenas I, II, IV e V estão corretas
- C) Apenas I, II e III estão corretas
- D) Apenas II, III e V estão corretas
- E) Todas as afirmações estão corretas

---

### **RESPOSTA: B**

**Explicação:** As afirmações I, II, IV e V estão corretas. Presto oferece consultas federadas (I), arquitetura MPP (II), múltiplos conectores (IV), e otimizações avançadas (V). A afirmação III está incorreta pois Presto NÃO mantém tudo em memória - ele otimiza uso de memória mas pode usar spilling to disk quando necessário para consultas que excedem a memória disponível, especialmente em joins grandes ou agregações complexas.

---

## **QUESTÃO 40** (Adaptada - CESPE 2023)

**Delta Lake é uma camada de armazenamento que oferece transações ACID sobre data lakes. Sobre Delta Lake, julgue as assertivas:**

**I.** Delta Lake oferece transações ACID garantindo consistência de dados em operações concorrentes.  
**II.** Delta Lake mantém versionamento automático permitindo time travel para consultas históricas.  
**III.** Delta Lake otimiza performance através de Z-ordering e compactação automática de arquivos.  
**IV.** Delta Lake funciona apenas com Apache Spark, não integrando com outras ferramentas.  
**V.** Delta Lake oferece schema evolution permitindo alterações de esquema seguras.

**Alternativas:**
- A) Apenas I, II e III estão corretas
- B) Apenas I, II, III e V estão corretas
- C) Apenas I, II e V estão corretas
- D) Apenas II, III e IV estão corretas
- E) Todas as assertivas estão corretas

---

### **RESPOSTA: B**

**Explicação:** As assertivas I, II, III e V estão corretas. Delta Lake oferece ACID (I), versionamento/time travel (II), otimizações como Z-ordering (III), e schema evolution (V). A assertiva IV está incorreta pois Delta Lake, embora originalmente focado em Spark, agora oferece Delta Standalone para integração com outras ferramentas, e existem conectores para Presto, Hive, e outras engines de consulta.

---

## **QUESTÃO EXTRA - CASE GOVERNAMENTAL** (Baseada em concursos TJ-SC, TCE-SC, FEPESE)

**O Tribunal de Contas do Estado de Santa Catarina está implementando uma solução de Big Data para análise de gastos públicos municipais. A solução deve processar dados de diferentes fontes (SIOPE, SICONFI, portais de transparência) em tempo real e gerar relatórios para auditores. Considerando os requisitos de conformidade com LGPD, transparência pública e eficiência operacional, qual arquitetura seria MAIS adequada:**

**Alternativas:**
- A) Arquitetura Lambda com Hadoop/MapReduce para batch e Storm para streaming, armazenando dados sensíveis sem criptografia para facilitar auditorias
- B) Arquitetura baseada em Apache Kafka para ingestão, Spark Streaming para processamento, Delta Lake para armazenamento com ACID, e Superset para visualização, implementando pseudonimização conforme LGPD  
- C) Solução proprietária em mainframe com processamento batch noturno apenas, sem capacidades de streaming ou análises em tempo real
- D) Cluster Hadoop com Hive apenas para armazenamento, sem ferramentas de visualização ou APIs para acesso externo
- E) Arquitetura serverless com funções AWS Lambda apenas, sem persistência de dados históricos para análises temporais

---

### **RESPOSTA: B**

**Explicação:** A alternativa B oferece a arquitetura mais adequada para o caso governamental: Kafka para ingestão confiável de múltiplas fontes, Spark Streaming para processamento em tempo real, Delta Lake para armazenamento ACID com versionamento (essencial para auditoria), Superset para dashboards transparentes, e pseudonimização LGPD-compliant. As outras opções têm limitações críticas: A viola LGPD, C/D não atendem requisitos de tempo real, E não oferece histórico para análises temporais necessárias em auditoria pública.

---

## **QUESTÃO 2** 🐘

**O Apache Hadoop é uma das principais ferramentas para processamento de Big Data. Sobre o Hadoop, é CORRETO afirmar:**

**Alternativas:**
- A) É uma solução proprietária da Oracle para processamento distribuído
- B) Utiliza o paradigma MapReduce apenas para dados estruturados
- C) O HDFS (Hadoop Distributed File System) armazena dados de forma distribuída
- D) Não é adequado para processamento de grandes volumes de dados
- E) Funciona apenas em sistemas operacionais Windows

---

### **RESPOSTA: C**

**Explicação:** 
- **HDFS (Hadoop Distributed File System)** é o sistema de arquivos distribuído do Hadoop
- Permite armazenar grandes volumes de dados em múltiplos nós de um cluster
- Oferece alta disponibilidade e tolerância a falhas
- É open-source (não proprietário) e multiplataforma

---

## **QUESTÃO 3** ⚡

**Apache Spark é considerado uma evolução do MapReduce tradicional. Qual é a principal vantagem do Spark em relação ao MapReduce?**

**Alternativas:**
- A) Spark consome menos memória RAM
- B) Spark processa dados apenas em batch
- C) Spark realiza processamento in-memory, sendo mais rápido
- D) Spark não suporta SQL
- E) Spark funciona apenas com dados estruturados

---

### **RESPOSTA: C**

**Explicação:**
- **Apache Spark** utiliza processamento **in-memory** (na memória RAM)
- Pode ser até **100x mais rápido** que o MapReduce tradicional
- Suporta processamento em **batch** e **streaming**
- Oferece APIs para **Spark SQL**, **MLlib** (Machine Learning) e **GraphX**
- Trabalha com dados estruturados, semi-estruturados e não-estruturados

---

## **QUESTÃO 4** 🔄

**No contexto de Big Data, qual tecnologia é mais adequada para processamento de dados em tempo real (real-time streaming)?**

**Alternativas:**
- A) Apache Hadoop MapReduce
- B) Apache Kafka + Apache Storm
- C) MySQL tradicional
- D) Microsoft Excel
- E) Apenas arquivos CSV

---

### **RESPOSTA: B**

**Explicação:**
- **Apache Kafka**: Plataforma de streaming distribuída para ingestão de dados em tempo real
- **Apache Storm**: Framework para processamento de stream em tempo real
- **Juntos**: Formam uma solução robusta para Big Data streaming
- **MapReduce**: Adequado para processamento batch, não tempo real
- **Bancos tradicionais**: Não escaláveis para volumes massivos em tempo real

---

## **QUESTÃO 5** 🏛️

**Em um projeto de Smart City para análise de dados governamentais, qual arquitetura seria mais adequada para processar dados de sensores IoT, câmeras de trânsito e sistemas administrativos?**

**Alternativas:**
- A) Planilha Excel compartilhada
- B) Banco de dados MySQL único
- C) Arquitetura Lambda (Batch + Stream)
- D) Processamento apenas offline
- E) Sistema monolítico tradicional

---

### **RESPOSTA: C**

**Explicação:**
**Arquitetura Lambda** combina:
- **Batch Layer**: Processa grandes volumes históricos (Hadoop/Spark)
- **Stream Layer**: Processa dados em tempo real (Kafka/Storm)
- **Serving Layer**: Disponibiliza resultados para consultas

**Ideal para Smart Cities** pois permite:
- ✅ Análise histórica de padrões urbanos
- ✅ Resposta em tempo real a emergências
- ✅ Integração de múltiplas fontes de dados
- ✅ Escalabilidade para milhões de sensores

---

## **QUESTÃO 6** 🧠

**Machine Learning aplicado a Big Data requer ferramentas específicas. Qual biblioteca é mais adequada para ML distribuído?**

**Alternativas:**
- A) Scikit-learn (executado em um único computador)
- B) Apache Spark MLlib
- C) Excel com macros VBA
- D) Calculadora científica
- E) Apenas algoritmos manuais

---

### **RESPOSTA: B**

**Explicação:**
**Apache Spark MLlib** oferece:
- ✅ **Machine Learning distribuído** em clusters
- ✅ Algoritmos otimizados para Big Data
- ✅ APIs em **Python**, **Scala**, **Java**, **R**
- ✅ Integração com **DataFrames** e **SQL**
- ✅ Suporte a **classificação**, **regressão**, **clustering**, **filtragem colaborativa**

*Scikit-learn* é excelente, mas limitado a um único computador.

---

## **QUESTÃO 7** 📊

**NoSQL é fundamental em Big Data. Qual tipo de banco NoSQL é mais adequado para análise de relacionamentos complexos em redes sociais?**

**Alternativas:**
- A) Banco de dados relacional (SQL)
- B) Banco orientado a documentos (MongoDB)
- C) Banco orientado a grafos (Neo4j)
- D) Banco de dados de séries temporais
- E) Planilha do LibreOffice

---

### **RESPOSTA: C**

**Explicação:**
**Bancos orientados a grafos** (como Neo4j) são ideais para:
- ✅ **Relacionamentos complexos** entre usuários
- ✅ **Análise de influenciadores** e comunidades
- ✅ **Detecção de fraudes** por padrões de conexão
- ✅ **Recomendações** baseadas em rede social
- ✅ **Consultas de caminho** (quem conhece quem)

**MongoDB** é ótimo para documentos, mas não para relacionamentos complexos.

---

## **QUESTÃO 8** 🔒

**Sobre segurança e privacidade em Big Data governamental, qual prática é ESSENCIAL?**

**Alternativas:**
- A) Deixar todos os dados públicos e abertos
- B) Aplicar anonimização e pseudonimização de dados pessoais
- C) Usar apenas planilhas não protegidas
- D) Não fazer backup dos dados
- E) Processar dados sem auditoria

---

### **RESPOSTA: B**

**Explicação:**
**Anonimização e Pseudonimização** são técnicas essenciais:
- ✅ **Anonimização**: Remove completamente a identificação
- ✅ **Pseudonimização**: Substitui identificadores por códigos
- ✅ **Conformidade com LGPD** (Lei Geral de Proteção de Dados)
- ✅ **Proteção da privacidade** dos cidadãos
- ✅ **Permite análises** sem expor dados pessoais

**Fundamental** em projetos governamentais que lidam com dados dos cidadãos.

---

## **QUESTÃO 9** 🌐

**Para um governo estadual implementar uma solução de Big Data Analytics, qual seria a sequência CORRETA de etapas?**

**Alternativas:**
- A) Comprar hardware → Coletar dados → Definir objetivos
- B) Definir objetivos → Identificar fontes de dados → Escolher arquitetura → Implementar
- C) Implementar → Testar → Definir objetivos
- D) Coletar todos os dados possíveis → Ver o que fazer depois
- E) Contratar consultoria → Esperar solução pronta

---

### **RESPOSTA: B**

**Explicação:**
**Metodologia correta** para projetos governamentais:

1. **Definir objetivos** claros (ex: melhorar saúde pública)
2. **Identificar fontes** de dados relevantes (hospitais, laboratórios)
3. **Escolher arquitetura** adequada (batch/stream/lambda)
4. **Implementar** por fases (MVP → expansão)
5. **Monitorar** e otimizar continuamente

**Planejamento estratégico** SEMPRE vem antes da implementação técnica.

---

## **QUESTÃO 10** 📈

**Em um projeto de análise de dados educacionais de Santa Catarina, qual métrica seria mais relevante para melhorar a qualidade do ensino?**

**Alternativas:**
- A) Número total de alunos matriculados apenas
- B) Análise preditiva de evasão escolar + fatores socioeconômicos
- C) Quantidade de escolas construídas
- D) Orçamento total da educação
- E) Número de professores contratados

---

### **RESPOSTA: B**

**Explicação:**
**Análise preditiva de evasão escolar** oferece:
- ✅ **Identificação precoce** de alunos em risco
- ✅ **Intervenções personalizadas** baseadas em dados
- ✅ **Correlação** com fatores socioeconômicos
- ✅ **Políticas públicas** mais eficazes
- ✅ **ROI mensurável** em educação

**Big Data** permite ir além de métricas básicas, possibilitando **ações preventivas** e **políticas baseadas em evidências**.

---

## 📚 **REFERÊNCIAS PARA ESTUDO**

### **Livros Recomendados:**
- 📖 "Big Data: A Revolution That Will Transform How We Live, Work, and Think" - Viktor Mayer-Schönberger
- 📖 "Hadoop: The Definitive Guide" - Tom White
- 📖 "Learning Spark" - Holden Karau

### **Tecnologias para Dominar:**
- 🐘 **Apache Hadoop** (HDFS + MapReduce)
- ⚡ **Apache Spark** (Spark SQL + MLlib)
- 🔄 **Apache Kafka** (Streaming)
- 🧠 **Python** (Pandas + Scikit-learn)
- 📊 **R** (ggplot2 + dplyr)

### **Certificações Relevantes:**
- 🏆 **Cloudera Certified Associate (CCA)**
- 🏆 **Apache Spark Developer Certification**
- 🏆 **AWS Big Data Specialty**
- 🏆 **Google Cloud Professional Data Engineer**

---

> **💡 Dica Final:** Big Data em concursos públicos foca em **conceitos fundamentais**, **arquiteturas**, **casos de uso governamentais** e **aspectos de privacidade/segurança**. Pratique com exemplos de Smart Cities e políticas públicas baseadas em dados!

---

*Elaborado por: BigData Analytics Pro*  
*Site: https://datascience-pro.netlify.app*  
*Repositório: https://github.com/cordeirotelecom/topicos-bigdata-python*