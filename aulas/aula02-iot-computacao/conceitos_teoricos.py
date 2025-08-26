# AULA 02: IoT e Computacao Distribuida - Conceitos Teoricos Avancados
# Professor: Vagner Cordeiro
# Curso: Topicos de Big Data em Python

# IoT E COMPUTACAO DISTRIBUIDA - FUNDAMENTOS TEORICOS
# ============================================================
# Professor: Vagner Cordeiro

# 1. INTRODUCAO AO INTERNET OF THINGS (IoT)
# --------------------------------------------------
# DEFINICAO TECNICA:
#    - Rede de dispositivos fisicos interconectados
#    - Capacidade de coleta, processamento e transmissao de dados
#    - Integracao com sistemas de informacao empresariais
#    - Automacao e tomada de decisao baseada em dados

# ARQUITETURA IoT EM CAMADAS:
#    - Camada de Percepcao (Sensors/Actuators):
#      * Sensores: Temperatura, umidade, pressao, movimento
#      * Atuadores: Motores, valvulas, LEDs, alto-falantes
#      * Microcontroladores: Arduino, Raspberry Pi, ESP32
#    
#    - Camada de Conectividade (Network):
#      * Protocolos de baixo nivel: I2C, SPI, UART
#      * Conectividade local: WiFi, Bluetooth, Zigbee
#      * Conectividade WAN: 4G/5G, LoRaWAN, NB-IoT
#    
#    - Camada de Processamento (Edge/Fog):
#      * Edge Computing: Processamento local nos dispositivos
#      * Fog Computing: Processamento intermediario (gateways)
#      * Pre-processamento e filtragem de dados
#    
#    - Camada de Aplicacao (Cloud/Services):
#      * Armazenamento em nuvem (databases, data lakes)
#      * Analytics e machine learning
#      * Dashboards e interfaces de usuario
#      * APIs e integracao com sistemas existentes

# PROTOCOLOS DE COMUNICACAO IoT:
#    - Application Layer:
#      * MQTT (Message Queuing Telemetry Transport):
#        - Protocolo publish/subscribe
#        - Baixo overhead, ideal para redes limitadas
#        - QoS levels: 0 (at most once), 1 (at least once), 2 (exactly once)
#      
#      * CoAP (Constrained Application Protocol):
#        - Similar ao HTTP mas otimizado para dispositivos limitados
#        - Suporte a multicast e discovery
#        - Confirmacao automatica de mensagens
#      
#      * HTTP/HTTPS:
#        - Protocolo web tradicional
#        - REST APIs para integracao
#        - Maior overhead mas amplamente suportado
#    
#    - Network Layer:
#      * IPv6: Enderecamento suficiente para bilhoes de dispositivos
#      * 6LoWPAN: IPv6 over Low-Power Wireless Personal Area Networks
#      * RPL: Routing Protocol for Low-Power and Lossy Networks

# 2. SENSORES E ATUADORES - CLASSIFICACAO TECNICA
# --------------------------------------------------
# SENSORES ANALOGICOS VS DIGITAIS:
#    - Analogicos:
#      * Saida continua proporcional ao fenomeno medido
#      * Requer ADC (Analog-to-Digital Converter)
#      * Exemplos: Termistores, fotoresistores, potenciometros
#    
#    - Digitais:
#      * Saida em formato digital direto
#      * Comunicacao via protocolos como I2C, SPI
#      * Exemplos: DHT22 (temp/umidade), BME280 (pressao)

# SENSORES POR CATEGORIA FISICA:
#    - Mecanicos:
#      * Acelerometros: Medicao de aceleracao em 3 eixos
#      * Giroscopios: Medicao de velocidade angular
#      * Magnetometros: Medicao de campo magnetico
#      * Encoders: Medicao de posicao/rotacao
#    
#    - Termicos:
#      * Termopares: Ampla faixa de temperatura
#      * RTDs: Resistive Temperature Detectors
#      * Termistores: NTC (Negative) e PTC (Positive)
#      * Sensores infravermelhos: Medicao sem contato
#    
#    - Opticos:
#      * Fotodiodos: Conversao luz-corrente
#      * Fototransistores: Amplificacao do sinal luminoso
#      * LDRs: Light Dependent Resistors
#      * Cameras: Imagem digital para computer vision
#    
#    - Quimicos:
#      * Sensores de gas: CO, CO2, NOx, SOx
#      * pH meters: Acidez/alcalinidade
#      * Sensores de umidade do solo
#      * Sensores de qualidade do ar (PM2.5, PM10)

# 3. EDGE COMPUTING - PARADIGMA DISTRIBUIDO
# --------------------------------------------------
# DEFINICAO E MOTIVACAO:
#    - Processamento de dados proximo a fonte de geracao
#    - Reducao de latencia para aplicacoes criticas
#    - Diminuicao do trafego para data centers centralizados
#    - Maior privacidade e seguranca dos dados

# ARQUITETURAS EDGE:
#    - Device Edge:
#      * Processamento diretamente no dispositivo IoT
#      * Microprocessadores com capacidade limitada
#      * Ideal para decisoes simples e rapidas
#    
#    - Local Edge:
#      * Gateways e servidores locais
#      * Agregacao de multiplos dispositivos
#      * Processamento de complexidade media
#    
#    - Regional Edge:
#      * Data centers regionais distribuidos
#      * Processamento de alta complexidade
#      * Servicos para multiplas localidades

# TECNOLOGIAS EDGE:
#    - Hardware:
#      * NVIDIA Jetson: GPUs para AI no edge
#      * Intel NUC: Computadores compactos
#      * Google Coral: TPUs para machine learning
#      * AWS Snowball Edge: Storage e compute portatil
#    
#    - Software:
#      * Docker: Containerizacao de aplicacoes
#      * Kubernetes: Orquestracao de containers
#      * Apache NiFi: Fluxo de dados automatizado
#      * Apache Kafka: Streaming de dados

# 4. FOG COMPUTING - CAMADA INTERMEDIARIA
# --------------------------------------------------
# CONCEITO E POSICIONAMENTO:
#    - Extensao da computacao em nuvem para o edge
#    - Camada intermediaria entre dispositivos e cloud
#    - Maior capacidade computacional que edge puro
#    - Menor latencia que cloud computing tradicional

# CARACTERISTICAS DO FOG:
#    - Baixa Latencia: Processamento proximo aos usuarios
#    - Localizacao Geografica: Distribuido geograficamente
#    - Mobilidade: Suporte a dispositivos moveis
#    - Heterogeneidade: Diferentes tipos de hardware

# CASOS DE USO FOG:
#    - Veiculos Conectados:
#      * Processamento de dados de sensores veiculares
#      * Comunicacao vehicle-to-infrastructure (V2I)
#      * Decisoes de roteamento em tempo real
#    
#    - Smart Grids:
#      * Monitoramento distribuido da rede eletrica
#      * Balanceamento automatico de carga
#      * Deteccao e isolamento de falhas
#    
#    - Augmented Reality:
#      * Renderizacao distribuida de conteudo
#      * Reducao de latencia para experiencia fluida
#      * Processamento de computer vision

# 5. PROTOCOLOS DE REDE PARA IoT
# --------------------------------------------------
# REDES DE AREA PESSOAL (PAN):
#    - Bluetooth Low Energy (BLE):
#      * Consumo energetico ultra-baixo
#      * Alcance tipico: 10-50 metros
#      * Topologia star com central e perifericos
#      * Adequado para wearables e beacons
#    
#    - Zigbee:
#      * Baseado no IEEE 802.15.4
#      * Topologia mesh auto-organizavel
#      * Baixo consumo e longo alcance
#      * Adequado para automacao residencial

# REDES DE LONGA DISTANCIA (LPWAN):
#    - LoRaWAN (Long Range WAN):
#      * Longo alcance: 2-15 km em area urbana
#      * Baixo consumo energetico
#      * Topologia star-of-stars com gateways
#      * Classes A, B, C para diferentes use cases
#    
#    - NB-IoT (Narrowband IoT):
#      * Tecnologia celular otimizada para IoT
#      * Cobertura indoor melhorada
#      * Suporte a grandes numeros de dispositivos
#      * Integrada a redes LTE existentes
#    
#    - Sigfox:
#      * Rede proprietaria de baixo consumo
#      * Mensagens pequenas (12 bytes uplink)
#      * Cobertura nacional em muitos paises
#      * Modelo de negocios baseado em conectividade

# 6. SEGURANCA EM IoT - ABORDAGEM MULTICAMADA
# --------------------------------------------------
# DESAFIOS DE SEGURANCA:
#    - Recursos Limitados: CPU, memoria, energia restritos
#    - Atualizacao Dificil: Dispositivos em campo remoto
#    - Autenticacao Fraca: Senhas padrao, credenciais fracas
#    - Criptografia Inadequada: Algoritmos fracos ou ausentes

# FRAMEWORK DE SEGURANCA:
#    - Camada de Dispositivo:
#      * Hardware Security Module (HSM)
#      * Trusted Platform Module (TPM)
#      * Secure Boot e firmware signing
#      * Physical Unclonable Functions (PUF)
#    
#    - Camada de Comunicacao:
#      * TLS/DTLS para criptografia em transito
#      * Certificados X.509 para autenticacao
#      * VPNs para tunelamento seguro
#      * Message Authentication Codes (MAC)
#    
#    - Camada de Aplicacao:
#      * OAuth 2.0 para autorizacao
#      * JWT (JSON Web Tokens) para sessoes
#      * Role-Based Access Control (RBAC)
#      * API rate limiting e throttling

# PADROES DE SEGURANCA IoT:
#    - NIST Cybersecurity Framework
#    - IEC 62443 para sistemas industriais
#    - ISO/IEC 27001 para gestao de seguranca
#    - OWASP IoT Top 10 vulnerabilidades

# 7. BIG DATA EM IoT - VOLUME, VELOCIDADE, VARIEDADE
# --------------------------------------------------
# CARACTERISTICAS DOS DADOS IoT:
#    - Volume Massivo:
#      * Bilhoes de dispositivos gerando dados continuamente
#      * Crescimento exponencial de dados
#      * Necessidade de armazenamento escalavel
#    
#    - Alta Velocidade:
#      * Dados gerados em tempo real
#      * Necessidade de processamento em tempo real
#      * Stream processing para analise instantanea
#    
#    - Variedade de Formatos:
#      * Dados estruturados: Sensores numericos
#      * Dados semi-estruturados: JSON, XML
#      * Dados nao-estruturados: Imagens, audio, video

# PIPELINE DE DADOS IoT:
#    - Ingestion (Ingestao):
#      * Apache Kafka para streaming
#      * Apache Pulsar para mensageria
#      * Amazon Kinesis para AWS
#      * Google Pub/Sub para GCP
#    
#    - Processing (Processamento):
#      * Apache Spark para batch e streaming
#      * Apache Flink para low-latency streaming
#      * Apache Storm para real-time processing
#      * Apache Beam para programming model unificado
#    
#    - Storage (Armazenamento):
#      * Time-Series Databases: InfluxDB, TimescaleDB
#      * NoSQL: MongoDB, Cassandra, DynamoDB
#      * Data Lakes: Hadoop HDFS, Amazon S3
#      * Graph Databases: Neo4j, Amazon Neptune

# 8. MACHINE LEARNING EM IoT
# --------------------------------------------------
# PARADIGMAS ML IoT:
#    - Cloud ML:
#      * Treinamento em cloud com poder computacional
#      * Inferencia enviando dados para cloud
#      * Maior latencia mas maior precisao
#    
#    - Edge ML:
#      * Modelos pre-treinados executados no edge
#      * Inferencia local com baixa latencia
#      * Modelos menores e mais eficientes
#    
#    - Federated Learning:
#      * Treinamento distribuido nos dispositivos
#      * Preservacao de privacidade dos dados
#      * Agregacao de modelos sem compartilhar dados

# TECNICAS ML PARA IoT:
#    - Anomaly Detection:
#      * Deteccao de comportamentos anormais
#      * Algoritmos: Isolation Forest, One-Class SVM
#      * Aplicacao: Manutencao preditiva, seguranca
#    
#    - Time Series Forecasting:
#      * Predicao de valores futuros
#      * Algoritmos: ARIMA, LSTM, Prophet
#      * Aplicacao: Previsao de demanda, otimizacao
#    
#    - Classification:
#      * Categorizacao de eventos ou objetos
#      * Algoritmos: Random Forest, SVM, Neural Networks
#      * Aplicacao: Reconhecimento de padroes, diagnostico

# 9. CASOS DE USO INDUSTRIAIS
# --------------------------------------------------
# SMART MANUFACTURING (INDUSTRIA 4.0):
#    - Monitoramento de Equipamentos:
#      * Sensores de vibracao, temperatura, pressao
#      * Deteccao precoce de falhas
#      * Otimizacao de cronogramas de manutencao
#    
#    - Controle de Qualidade:
#      * Computer vision para inspecao
#      * Deteccao automatica de defeitos
#      * Rastreabilidade de produtos
#    
#    - Otimizacao de Processos:
#      * Sensores de fluxo e nivel
#      * Controle automatico de parametros
#      * Reducao de desperdicios e energia

# SMART CITIES:
#    - Gestao de Trafego:
#      * Sensores de trafego e cameras
#      * Otimizacao de semaforos em tempo real
#      * Sistemas de transporte inteligente
#    
#    - Gestao de Residuos:
#      * Sensores de nivel em lixeiras
#      * Otimizacao de rotas de coleta
#      * Reducao de custos operacionais
#    
#    - Iluminacao Inteligente:
#      * Sensores de presenca e luminosidade
#      * Ajuste automatico de intensidade
#      * Economia de energia significativa

# AGRICULTURA INTELIGENTE:
#    - Monitoramento do Solo:
#      * Sensores de umidade, pH, nutrientes
#      * Irrigacao automatizada e precisao
#      * Otimizacao do uso de fertilizantes
#    
#    - Monitoramento Climatico:
#      * Estacoes meteorologicas distribuidas
#      * Previsao de condicoes adversas
#      * Protecao de culturas
#    
#    - Pecuaria Inteligente:
#      * Monitoramento de saude animal
#      * Rastreamento de localizacao
#      * Otimizacao de alimentacao

# 10. TENDENCIAS FUTURAS
# --------------------------------------------------
# 5G E IoT:
#    - Ultra-Low Latency: < 1ms para aplicacoes criticas
#    - Massive IoT: Suporte a milhoes de dispositivos por km²
#    - Network Slicing: Redes virtuais dedicadas
#    - Edge Computing Nativo: Computacao integrada a rede

# ARTIFICIAL INTELLIGENCE OF THINGS (AIoT):
#    - Integracao nativa de AI em dispositivos IoT
#    - Chips especializados para AI (NPUs, TPUs)
#    - AutoML para otimizacao automatica de modelos
#    - Explainable AI para transparencia

# QUANTUM IoT:
#    - Quantum Key Distribution para seguranca
#    - Quantum sensors para precisao extrema
#    - Quantum computing para otimizacao complexa
#    - Quantum internet para comunicacao segura

# DIGITAL TWINS:
#    - Replicas digitais de sistemas fisicos
#    - Simulacao e otimizacao em tempo real
#    - Manutencao preditiva avancada
#    - Design e teste de novos produtos

# ============================================================
# EXERCICIOS PRATICOS SUGERIDOS:
# 1. Projetar arquitetura IoT para smart home
# 2. Comparar protocolos MQTT vs CoAP
# 3. Calcular latencia edge vs cloud processing
# 4. Analisar trade-offs de seguranca vs performance
# 5. Dimensionar pipeline de dados para 1M sensores

def explicar_iot():
    """Explica conceitos fundamentais de IoT"""
    print("🌐 INTERNET DAS COISAS (IoT)")
    print("=" * 50)
    print()
    print("📖 DEFINIÇÃO:")
    print("   IoT é uma rede de dispositivos físicos conectados à internet")
    print("   que coletam e compartilham dados automaticamente.")
    print()
    print("🔧 COMPONENTES PRINCIPAIS:")
    print("   1. SENSORES - Coletam dados do ambiente")
    print("   2. CONECTIVIDADE - WiFi, Bluetooth, 4G/5G")
    print("   3. PROCESSAMENTO - Análise local ou na nuvem")
    print("   4. INTERFACE - Apps, dashboards, alertas")
    print()
    print("📊 EXEMPLOS PRÁTICOS:")
    print("   • Casa inteligente: termostatos, lâmpadas")
    print("   • Agricultura: sensores de umidade do solo")
    print("   • Saúde: monitores cardíacos")
    print("   • Indústria: sensores de temperatura em máquinas")
    print()

def explicar_computacao_distribuida():
    """Explica conceitos de computação distribuída"""
    print("⚡ COMPUTAÇÃO DISTRIBUÍDA")
    print("=" * 50)
    print()
    print("📖 DEFINIÇÃO:")
    print("   Sistema onde o processamento é dividido entre")
    print("   múltiplos computadores trabalhando juntos.")
    print()
    print("🎯 VANTAGENS:")
    print("   ✅ ESCALABILIDADE - Adiciona mais máquinas conforme necessário")
    print("   ✅ TOLERÂNCIA A FALHAS - Se uma máquina falha, outras continuam")
    print("   ✅ PERFORMANCE - Processamento paralelo mais rápido")
    print("   ✅ ECONOMIA - Usa hardware commodity")
    print()
    print("⚠️ DESAFIOS:")
    print("   ❌ COMPLEXIDADE - Coordenação entre máquinas")
    print("   ❌ LATÊNCIA DE REDE - Comunicação entre nós")
    print("   ❌ CONSISTÊNCIA - Manter dados sincronizados")
    print("   ❌ DEBUGGING - Difícil rastrear problemas")
    print()

def explicar_message_queues():
    """Explica sistemas de filas de mensagens"""
    print("📬 SISTEMAS DE FILAS DE MENSAGENS")
    print("=" * 50)
    print()
    print("📖 CONCEITO:")
    print("   Sistemas que permitem comunicação assíncrona")
    print("   entre diferentes partes de uma aplicação.")
    print()
    print("🔄 PADRÕES PRINCIPAIS:")
    print()
    print("   1. PRODUCER-CONSUMER:")
    print("      • Producer: Envia mensagens")
    print("      • Queue: Armazena mensagens")
    print("      • Consumer: Processa mensagens")
    print()
    print("   2. PUBLISH-SUBSCRIBE:")
    print("      • Publisher: Publica em tópicos")
    print("      • Broker: Gerencia tópicos")
    print("      • Subscriber: Recebe mensagens do tópico")
    print()
    print("📊 BENEFÍCIOS:")
    print("   ✅ DESACOPLAMENTO - Sistemas independentes")
    print("   ✅ ESCALABILIDADE - Adiciona consumidores facilmente")
    print("   ✅ CONFIABILIDADE - Mensagens não se perdem")
    print("   ✅ BALANCEAMENTO - Distribui carga automaticamente")
    print()

def explicar_mapreduce():
    """Explica conceitos de MapReduce"""
    print("🗺️ MAPREDUCE - PARADIGMA DE PROCESSAMENTO")
    print("=" * 50)
    print()
    print("📖 CONCEITO:")
    print("   Modelo de programação para processar grandes")
    print("   volumes de dados de forma distribuída.")
    print()
    print("🔄 FASES DO MAPREDUCE:")
    print()
    print("   1. MAP (Mapeamento):")
    print("      • Recebe dados de entrada")
    print("      • Aplica função de transformação")
    print("      • Produz pares chave-valor")
    print()
    print("   2. SHUFFLE (Embaralhamento):")
    print("      • Agrupa dados por chave")
    print("      • Distribui para reducers")
    print("      • Ordena dados")
    print()
    print("   3. REDUCE (Redução):")
    print("      • Recebe dados agrupados")
    print("      • Aplica função de agregação")
    print("      • Produz resultado final")
    print()
    print("💡 EXEMPLO CONCEITUAL - CONTAGEM DE PALAVRAS:")
    print("   INPUT: 'hello world hello'")
    print("   MAP: [(hello,1), (world,1), (hello,1)]")
    print("   SHUFFLE: {hello: [1,1], world: [1]}")
    print("   REDUCE: {hello: 2, world: 1}")
    print()

def explicar_big_data_iot():
    """Explica a relação entre IoT e Big Data"""
    print("🔗 IoT + BIG DATA")
    print("=" * 50)
    print()
    print("📊 CARACTERÍSTICAS DOS DADOS IoT:")
    print()
    print("   VOLUME:")
    print("   • Milhões de dispositivos gerando dados 24/7")
    print("   • Sensores coletam dados continuamente")
    print("   • Crescimento exponencial de dados")
    print()
    print("   VELOCIDADE:")
    print("   • Dados gerados em tempo real")
    print("   • Necessidade de processamento imediato")
    print("   • Streaming de dados contínuo")
    print()
    print("   VARIEDADE:")
    print("   • Dados estruturados: temperaturas, pressão")
    print("   • Dados semi-estruturados: logs JSON")
    print("   • Dados não-estruturados: imagens, áudio")
    print()
    print("🎯 CASOS DE USO:")
    print("   • SMART CITIES: Semáforos inteligentes")
    print("   • INDÚSTRIA 4.0: Manutenção preditiva")
    print("   • AGRICULTURA: Irrigação automatizada")
    print("   • SAÚDE: Monitoramento remoto")
    print()

def explicar_ferramentas():
    """Explica ferramentas para IoT e Big Data"""
    print("🛠️ FERRAMENTAS E TECNOLOGIAS")
    print("=" * 50)
    print()
    print("📡 PROTOCOLOS IoT:")
    print("   • MQTT - Messaging para IoT")
    print("   • CoAP - Web protocol para dispositivos limitados")
    print("   • LoRaWAN - Comunicação de longo alcance")
    print("   • HTTP/HTTPS - Protocolo web tradicional")
    print()
    print("☁️ PLATAFORMAS IoT:")
    print("   • AWS IoT Core - Amazon")
    print("   • Azure IoT Hub - Microsoft")
    print("   • Google Cloud IoT - Google")
    print("   • IBM Watson IoT - IBM")
    print()
    print("📊 PROCESSAMENTO DE DADOS:")
    print("   • Apache Kafka - Streaming de dados")
    print("   • Apache Storm - Processamento em tempo real")
    print("   • Apache Spark - Analytics distribuído")
    print("   • Apache Flink - Stream processing")
    print()
    print("💾 ARMAZENAMENTO:")
    print("   • Time-series databases: InfluxDB, TimescaleDB")
    print("   • NoSQL: MongoDB, Cassandra")
    print("   • Data Lakes: HDFS, S3")
    print()

def main():
    """Função principal que demonstra todos os conceitos"""
    print("🎓 AULA 02: IoT E COMPUTAÇÃO DISTRIBUÍDA")
    print("👨‍🏫 Professor: Vagner Cordeiro")
    print("=" * 60)
    print()
    
    explicar_iot()
    print("\n" + "="*60 + "\n")
    
    explicar_computacao_distribuida()
    print("\n" + "="*60 + "\n")
    
    explicar_message_queues()
    print("\n" + "="*60 + "\n")
    
    explicar_mapreduce()
    print("\n" + "="*60 + "\n")
    
    explicar_big_data_iot()
    print("\n" + "="*60 + "\n")
    
    explicar_ferramentas()
    print("\n" + "="*60 + "\n")
    
    print("📚 RESUMO DA AULA:")
    print("✅ IoT conecta dispositivos físicos à internet")
    print("✅ Computação distribuída divide processamento")
    print("✅ Message queues facilitam comunicação assíncrona")
    print("✅ MapReduce processa dados em grande escala")
    print("✅ IoT + Big Data = insights em tempo real")
    print()
    print("💡 PRÓXIMA AULA: Cloud Computing e Streaming")
    print("📖 ESTUDO: Pesquise sobre Apache Kafka e MQTT")

if __name__ == "__main__":
    main()
