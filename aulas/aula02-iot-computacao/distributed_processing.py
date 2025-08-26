# AULA 02: IoT e Computacao Distribuida - Processamento Distribuido
# Professor: Vagner Cordeiro
# Curso: Topicos de Big Data em Python

# PROCESSAMENTO DISTRIBUIDO EM IoT E BIG DATA
# ============================================================
# Professor: Vagner Cordeiro

# 1. FUNDAMENTOS DE COMPUTACAO DISTRIBUIDA
# --------------------------------------------------
# DEFINICAO:
#    - Sistema composto por multiplos computadores independentes
#    - Comunicacao atraves de rede para alcançar objetivo comum
#    - Compartilhamento de recursos e coordenacao de atividades
#    - Transparencia para o usuario final

# CARACTERISTICAS PRINCIPAIS:
#    - Concorrencia: Multiplos processos executando simultaneamente
#    - Ausencia de relogio global: Cada no tem seu proprio tempo
#    - Falhas independentes: Nos podem falhar independentemente
#    - Heterogeneidade: Diferentes hardware, software e redes

# VANTAGENS:
#    - Escalabilidade: Adicionar recursos conforme necessidade
#    - Tolerancia a falhas: Sistema continua funcionando com falhas parciais
#    - Compartilhamento de recursos: Utilizacao eficiente de recursos
#    - Performance: Paralelismo aumenta velocidade de processamento

# DESAFIOS:
#    - Complexidade: Projeto e implementacao mais complexos
#    - Comunicacao: Latencia e falhas de rede
#    - Sincronizacao: Coordenacao entre processos distribuidos
#    - Seguranca: Protecao contra ataques em ambiente distribuido

# 2. ARQUITETURAS DE SISTEMAS DISTRIBUIDOS
# --------------------------------------------------
# CLIENTE-SERVIDOR:
#    - Modelo tradicional com servidores centralizados
#    - Clientes fazem requisicoes, servidores processam respostas
#    - Vantagens: Simplicidade, controle centralizado
#    - Desvantagens: Ponto unico de falha, gargalo de performance

# PEER-TO-PEER (P2P):
#    - Todos os nos sao equivalentes em funcionalidade
#    - Cada no pode ser cliente e servidor simultaneamente
#    - Exemplos: BitTorrent, Blockchain, Gnutella
#    - Vantagens: Descentralizacao, escalabilidade
#    - Desvantagens: Complexidade de coordenacao

# MICROSERVICOS:
#    - Aplicacao dividida em servicos pequenos e independentes
#    - Cada servico tem responsabilidade especifica
#    - Comunicacao atraves de APIs REST ou mensagens
#    - Vantagens: Flexibilidade, escalabilidade independente
#    - Desvantagens: Complexidade de rede, latencia

# SERVICE-ORIENTED ARCHITECTURE (SOA):
#    - Servicos como componentes reutilizaveis
#    - Interface bem definida e padronizada
#    - Descoberta dinamica de servicos
#    - Composicao de servicos para criar aplicacoes

# 3. MODELOS DE CONSISTENCIA
# --------------------------------------------------
# CONSISTENCIA FORTE:
#    - Todas as replicas tem mesmos dados simultaneamente
#    - Garante consistencia mas pode reduzir disponibilidade
#    - Adequado para sistemas bancarios e financeiros
#    - Implementado com protocolos como 2PC, Paxos

# CONSISTENCIA EVENTUAL:
#    - Sistema convergira para estado consistente eventualmente
#    - Permite alta disponibilidade e tolerancia a particoes
#    - Adequado para redes sociais, catalogo de produtos
#    - Implementado em sistemas como DynamoDB, Cassandra

# CONSISTENCIA FRACA:
#    - Nenhuma garantia sobre quando dados serao consistentes
#    - Melhor performance mas menos garantias
#    - Adequado para sistemas de cache, analytics

# TEOREMA CAP:
#    - Consistency, Availability, Partition Tolerance
#    - Sistema distribuido pode garantir apenas 2 dos 3
#    - CP: Consistency + Partition Tolerance (MongoDB, Redis)
#    - AP: Availability + Partition Tolerance (Cassandra, DynamoDB)
#    - CA: Consistency + Availability (sistemas tradicionais)

# 4. ALGORITMOS DE CONSENSO
# --------------------------------------------------
# PAXOS:
#    - Algoritmo para consenso em sistemas distribuidos
#    - Garante acordo mesmo com falhas de nos
#    - Complexo de implementar corretamente
#    - Base para muitos sistemas de banco de dados

# RAFT:
#    - Alternativa mais simples ao Paxos
#    - Eleicao de lider e replicacao de log
#    - Usado em etcd, Consul, CockroachDB
#    - Mais facil de entender e implementar

# PBFT (Practical Byzantine Fault Tolerance):
#    - Tolerancia a falhas bizantinas (nos maliciosos)
#    - Usado em blockchain e sistemas criticos
#    - Requer 3f+1 nos para tolerar f nos bizantinos
#    - Alto overhead de comunicacao

# BLOCKCHAIN CONSENSUS:
#    - Proof of Work (Bitcoin): Consenso baseado em poder computacional
#    - Proof of Stake (Ethereum 2.0): Consenso baseado em stake economico
#    - Delegated Proof of Stake: Delegacao de poder de voto

# 5. PADROES DE COMUNICACAO
# --------------------------------------------------
# REQUEST-RESPONSE:
#    - Cliente envia requisicao e aguarda resposta
#    - Sincrono e bloqueante
#    - Simples mas pode gerar latencia
#    - Adequado para operacoes CRUD

# MESSAGE PASSING:
#    - Comunicacao atraves de troca de mensagens
#    - Pode ser sincrono ou assincrono
#    - Desacoplamento temporal entre componentes
#    - Implementado com message queues

# PUBLISH-SUBSCRIBE:
#    - Produtores publicam mensagens em topicos
#    - Consumidores se inscrevem em topicos de interesse
#    - Desacoplamento entre produtores e consumidores
#    - Escalabilidade e flexibilidade

# EVENT SOURCING:
#    - Estado derivado de sequencia de eventos
#    - Eventos sao imutaveis e ordenados
#    - Permite auditoria completa e replay
#    - Complexidade adicional de implementacao

# 6. TECNOLOGIAS PARA PROCESSAMENTO DISTRIBUIDO
# --------------------------------------------------
# APACHE HADOOP:
#    - Framework para processamento distribuido
#    - HDFS para armazenamento distribuido
#    - MapReduce para processamento batch
#    - Ecossistema rico com Hive, Pig, HBase

# APACHE SPARK:
#    - Engine de processamento em memoria
#    - APIs em Scala, Java, Python, R
#    - Suporte a batch, streaming, ML, grafos
#    - Mais rapido que MapReduce para muitas cargas

# APACHE KAFKA:
#    - Plataforma de streaming distribuida
#    - Alta vazao e baixa latencia
#    - Persistencia duravel de mensagens
#    - Usado para pipelines de dados em tempo real

# APACHE FLINK:
#    - Engine de processamento de stream
#    - Baixa latencia e alta vazao
#    - Processamento event-time nativo
#    - Tolerancia a falhas com checkpoints

# KUBERNETES:
#    - Orquestrador de containers
#    - Gerenciamento automatico de aplicacoes
#    - Escalabilidade automatica
#    - Service discovery e load balancing

# 7. IoT E EDGE COMPUTING
# --------------------------------------------------
# EDGE COMPUTING DISTRIBUIDO:
#    - Processamento proximo aos dispositivos IoT
#    - Reduz latencia e uso de largura de banda
#    - Permite operacao offline
#    - Hierarquia: Device -> Edge -> Fog -> Cloud

# FOG COMPUTING:
#    - Camada intermediaria entre edge e cloud
#    - Agregacao e pre-processamento de dados
#    - Filtragem e analise em tempo real
#    - Balanceamento de carga entre edge e cloud

# MESH NETWORKS:
#    - Dispositivos IoT formam rede mesh
#    - Comunicacao peer-to-peer entre dispositivos
#    - Redundancia e tolerancia a falhas
#    - Protocolos: Zigbee, Thread, WiFi Mesh

# SWARM INTELLIGENCE:
#    - Comportamento coletivo emergente
#    - Inspirado em sistemas biologicos
#    - Aplicacao em robotica e IoT
#    - Algoritmos: Particle Swarm, Ant Colony

# 8. PADROES DE TOLERANCIA A FALHAS
# --------------------------------------------------
# CIRCUIT BREAKER:
#    - Previne cascata de falhas
#    - Estados: Closed, Open, Half-Open
#    - Falha rapida quando servico indisponivel
#    - Implementacao: Hystrix, Resilience4j

# BULKHEAD:
#    - Isolamento de recursos
#    - Falha em um componente nao afeta outros
#    - Pools separados de threads/conexoes
#    - Inspirado em compartimentos de navios

# TIMEOUT E RETRY:
#    - Timeout previne bloqueio indefinido
#    - Retry com backoff exponencial
#    - Jitter para evitar thundering herd
#    - Circuit breaker para evitar retry desnecessario

# REPLICACAO:
#    - Multiplas copias dos dados/servicos
#    - Master-Slave: Uma replica primaria
#    - Master-Master: Multiplas replicas ativas
#    - Quorum: Maioria das replicas deve concordar

# 9. MONITORAMENTO E OBSERVABILIDADE
# --------------------------------------------------
# METRICAS:
#    - Contadores, gauges, histogramas
#    - Agregacao temporal e espacial
#    - Alertas baseados em thresholds
#    - Ferramentas: Prometheus, Grafana

# LOGGING DISTRIBUIDO:
#    - Correlacao de logs entre servicos
#    - Trace IDs para rastreamento de requisicoes
#    - Centralizacao com ELK Stack
#    - Estruturacao de logs para analytics

# TRACING DISTRIBUIDO:
#    - Rastreamento de requisicoes entre servicos
#    - Identificacao de gargalos e latencia
#    - Ferramentas: Jaeger, Zipkin, OpenTelemetry
#    - Sampling para reduzir overhead

# HEALTH CHECKS:
#    - Verificacao automatica de saude de servicos
#    - Liveness e readiness probes
#    - Dependency checks para servicos externos
#    - Failover automatico baseado em health

# 10. CASOS DE USO EM IoT
# --------------------------------------------------
# SMART CITIES:
#    - Rede distribuida de sensores urbanos
#    - Processamento edge para resposta rapida
#    - Agregacao de dados para analytics
#    - Coordenacao entre multiplos sistemas

# INDUSTRIA 4.0:
#    - Sensores em equipamentos industriais
#    - Processamento local para controle
#    - Comunicacao machine-to-machine
#    - Otimizacao distribuida de processos

# VEICULOS AUTONOMOS:
#    - Sensores distribuidos no veiculo
#    - Comunicacao vehicle-to-vehicle (V2V)
#    - Processamento em tempo real
#    - Coordenacao com infraestrutura

# AGRICULTURA INTELIGENTE:
#    - Sensores distribuidos em fazendas
#    - Irrigacao automatizada coordenada
#    - Monitoramento ambiental distribuido
#    - Otimizacao de recursos agricolas

# ============================================================
# PROXIMOS PASSOS:
# - Estudar implementacoes especificas de algoritmos de consenso
# - Praticar com ferramentas como Kubernetes e Docker
# - Implementar padroes de tolerancia a falhas
# - Explorar casos de uso em IoT e edge computing
# - Aprofundar conhecimento em monitoramento distribuido
    