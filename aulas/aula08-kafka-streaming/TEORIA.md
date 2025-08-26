# AULA 08: APACHE KAFKA E STREAMING DE DADOS

## 🎯 OBJETIVOS DA AULA
- Compreender os conceitos fundamentais de streaming de dados
- Entender a arquitetura do Apache Kafka
- Aprender sobre produtores, consumidores e tópicos
- Explorar casos de uso reais de streaming

## 📚 CONCEITOS FUNDAMENTAIS

### O que é Streaming de Dados?
**Definição**: Processamento contínuo de dados que chegam em tempo real, ao contrário do processamento em lote (batch).

**Características**:
- **Baixa Latência**: Dados processados em millisegundos
- **Alto Throughput**: Milhões de eventos por segundo
- **Escalabilidade**: Cresce horizontalmente
- **Tolerância a Falhas**: Resistente a quedas de sistema

### Por que Kafka?
**Apache Kafka** é uma plataforma distribuída de streaming que funciona como um "sistema nervoso" para dados em tempo real.

**Vantagens**:
1. **Performance**: Processa milhões de mensagens/segundo
2. **Durabilidade**: Dados persistidos em disco
3. **Escalabilidade**: Clusters com centenas de nós
4. **Ecossistema**: Integração com Spark, Hadoop, etc.

## 🏗️ ARQUITETURA DO KAFKA

### Componentes Principais

#### 1. Producer (Produtor)
**Função**: Publica mensagens em tópicos
**Analogia**: Como um jornalista enviando notícias para um jornal

```
Producer → [Dados] → Kafka Topic
```

#### 2. Consumer (Consumidor)
**Função**: Lê mensagens de tópicos
**Analogia**: Como um leitor assinando um jornal

```
Kafka Topic → [Dados] → Consumer
```

#### 3. Topic (Tópico)
**Função**: Canal nomeado onde mensagens são organizadas
**Analogia**: Como seções de um jornal (esportes, política, etc.)

#### 4. Partition (Partição)
**Função**: Divisão de um tópico para paralelização
**Analogia**: Como múltiplas impressoras produzindo o mesmo jornal

#### 5. Broker
**Função**: Servidor Kafka que armazena dados
**Analogia**: Como uma distribuidora de jornais

#### 6. Cluster
**Função**: Conjunto de brokers trabalhando juntos
**Analogia**: Como uma rede de distribuição nacional

## 🔄 FLUXO DE DADOS NO KAFKA

### Processo Completo
```
1. Producer cria mensagem
2. Kafka determina partição (round-robin ou por chave)
3. Mensagem é replicada entre brokers
4. Consumer lê mensagem do offset atual
5. Consumer confirma processamento (commit)
```

### Garantias de Entrega
1. **At most once**: Mensagem pode ser perdida, nunca duplicada
2. **At least once**: Mensagem nunca perdida, pode ser duplicada
3. **Exactly once**: Mensagem processada exatamente uma vez (ideal)

## 📊 CASOS DE USO REAIS

### 1. E-commerce - Rastreamento de Atividade
**Cenário**: Loja online rastreando cliques de usuários
```
Website → Kafka → Analytics Engine → Dashboard
```
**Benefícios**: Recomendações em tempo real, detecção de fraudes

### 2. Fintech - Processamento de Transações
**Cenário**: Sistema bancário processando pagamentos
```
App Móvel → Kafka → Validador → Banco de Dados
```
**Benefícios**: Processamento instantâneo, auditoria completa

### 3. IoT - Sensores Industriais
**Cenário**: Fábrica monitorando equipamentos
```
Sensores → Kafka → ML Model → Alertas
```
**Benefícios**: Manutenção preditiva, economia de custos

### 4. Media Streaming - Netflix/YouTube
**Cenário**: Plataforma de vídeo coletando métricas
```
Player → Kafka → Analytics → Recomendações
```
**Benefícios**: Melhor experiência do usuário

## ⚙️ CONFIGURAÇÕES IMPORTANTES

### Producer Configurations
- **batch.size**: Tamanho do lote para otimizar throughput
- **linger.ms**: Tempo de espera para formar lotes
- **acks**: Nível de confirmação requerido

### Consumer Configurations
- **auto.offset.reset**: Comportamento quando não há offset
- **enable.auto.commit**: Commit automático de offsets
- **max.poll.records**: Máximo de registros por poll

### Topic Configurations
- **num.partitions**: Número de partições
- **replication.factor**: Fator de replicação
- **retention.ms**: Tempo de retenção de dados

## 🚀 PADRÕES DE DESIGN

### 1. Event Sourcing
**Conceito**: Armazenar mudanças de estado como eventos
**Vantagem**: Histórico completo, possibilidade de replay

### 2. CQRS (Command Query Responsibility Segregation)
**Conceito**: Separar leitura e escrita
**Vantagem**: Otimização independente de cada operação

### 3. Saga Pattern
**Conceito**: Transações distribuídas via eventos
**Vantagem**: Consistência eventual em microserviços

## 📈 MONITORAMENTO E MÉTRICAS

### Métricas Importantes
1. **Throughput**: Mensagens por segundo
2. **Latência**: Tempo entre produção e consumo
3. **Lag**: Atraso do consumer em relação ao producer
4. **Disk Usage**: Uso de disco pelos brokers

### Ferramentas de Monitoramento
- **Kafka Manager**: Interface web para administração
- **Prometheus + Grafana**: Métricas e dashboards
- **Confluent Control Center**: Ferramenta comercial completa

## 🎓 EXERCÍCIOS CONCEITUAIS

### Exercício 1: Design de Sistema
**Problema**: Projetar sistema de chat em tempo real para 1 milhão de usuários
**Considere**: Tópicos, partições, replicação, consumers

### Exercício 2: Análise de Caso
**Problema**: Uber precisa processar 15 milhões de viagens/dia
**Considere**: Latência, throughput, consistency, availability

### Exercício 3: Troubleshooting
**Problema**: Consumers ficando com lag alto
**Investigue**: Partitions, consumer groups, processing time

## 📚 RECURSOS ADICIONAIS

### Documentação
- [Kafka Official Documentation](https://kafka.apache.org/documentation/)
- [Confluent Documentation](https://docs.confluent.io/)

### Livros Recomendados
- "Kafka: The Definitive Guide" - Gwen Shapira
- "Designing Data-Intensive Applications" - Martin Kleppmann

### Cursos Online
- Confluent Kafka Training
- LinkedIn Learning: Apache Kafka
- Udemy: Apache Kafka Series

## 🎯 PRÓXIMOS PASSOS

1. **Instalar Kafka**: Setup local ou uso de serviços cloud
2. **Praticar**: Criar producers e consumers simples
3. **Experimentar**: Diferentes configurações e padrões
4. **Integrar**: Conectar com outras ferramentas (Spark, Elasticsearch)
5. **Monitorar**: Implementar observabilidade completa

---

**Próxima Aula**: Machine Learning em Big Data com Spark MLlib
