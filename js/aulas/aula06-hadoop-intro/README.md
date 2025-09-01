# Aula 06 - Introdução ao Hadoop Ecosystem

## 🎯 Objetivos da Aula
- Compreender a arquitetura do Hadoop
- Configurar um cluster Hadoop local
- Trabalhar com HDFS, YARN e MapReduce
- Implementar jobs MapReduce em Python

## 📋 Conteúdo Programático

### 1. Fundamentos do Hadoop
- Histórico e evolução
- Arquitetura distribuída
- Componentes principais

### 2. HDFS (Hadoop Distributed File System)
- Arquitetura NameNode/DataNode
- Replicação e tolerância a falhas
- Comandos básicos

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

# ROTEIRO DE LABORATÓRIO HADOOP
## Tutorial Completo: Introdução, Instalação e Prática com Apache Hadoop

---

## ÍNDICE

1. [Introdução ao Big Data e Hadoop](#1-introdução-ao-big-data-e-hadoop)
   - 1.1 O que é Big Data?
   - 1.2 Os 5Vs do Big Data
   - 1.3 O que é Apache Hadoop?
   - 1.4 Por que o Hadoop é Importante?
   - 1.5 Casos de Uso Reais

2. [Arquitetura do Hadoop](#2-arquitetura-do-hadoop)
   - 2.1 Visão Geral da Arquitetura
   - 2.2 HDFS (Hadoop Distributed File System)
   - 2.3 MapReduce
   - 2.4 YARN (Yet Another Resource Negotiator)
   - 2.5 Ecossistema Hadoop

3. [Pré-requisitos e Preparação do Ambiente](#3-pré-requisitos-e-preparação-do-ambiente)
   - 3.1 Requisitos de Sistema
   - 3.2 Conhecimentos Prévios Necessários
   - 3.3 Ferramentas Auxiliares

4. [Instalação do Hadoop](#4-instalação-do-hadoop)
   - 4.1 Métodos de Instalação
   - 4.2 Instalação Automatizada com Scripts
   - 4.3 Verificação da Instalação
   - 4.4 Troubleshooting Comum

5. [Exercícios Práticos](#5-exercícios-práticos)
   - 5.1 Exercício 1: Grep (Busca de Padrões)
   - 5.2 Exercício 2: WordCount (Contagem de Palavras)
   - 5.3 Exercício 3: Análise de Logs (Novo)
   - 5.4 Exercício 4: Processamento de Dados CSV (Novo)

6. [Monitoramento e Interface Web](#6-monitoramento-e-interface-web)
   - 6.1 Interface Web do Hadoop
   - 6.2 Monitoramento de Jobs
   - 6.3 Análise de Performance

7. [Integração com Python](#7-integração-com-python)
   - 7.1 Bibliotecas Python para Hadoop
   - 7.2 Exemplos Práticos com Python
   - 7.3 Desenvolvimento de Jobs MapReduce em Python

8. [Troubleshooting e FAQ](#8-troubleshooting-e-faq)
   - 8.1 Problemas Comuns
   - 8.2 Soluções e Workarounds
   - 8.3 Perguntas Frequentes

9. [Recursos Adicionais](#9-recursos-adicionais)
   - 9.1 Documentação Oficial
   - 9.2 Tutoriais Complementares
   - 9.3 Comunidade e Suporte

10. [Referências](#10-referências)

---



## 1. INTRODUÇÃO AO BIG DATA E HADOOP

### 1.1 O que é Big Data?

Big Data refere-se a conjuntos de dados extremamente grandes, complexos e diversos que crescem exponencialmente ao longo do tempo. Esses dados são tão volumosos, variados e gerados em alta velocidade que as ferramentas tradicionais de processamento de dados e sistemas de gerenciamento de banco de dados não conseguem capturar, armazenar, gerenciar e analisar eficientemente [1].

O conceito de Big Data emergiu da necessidade de lidar com a explosão de dados digitais que começou no final dos anos 1990 e se acelerou dramaticamente com o advento das redes sociais, dispositivos móveis, Internet das Coisas (IoT) e computação em nuvem. Segundo estimativas recentes, o volume global de dados deve atingir 180 zettabytes até 2025, representando um crescimento exponencial que desafia os métodos tradicionais de processamento [2].

### 1.2 Os 5Vs do Big Data

![Diagrama dos 5Vs do Big Data](https://private-us-east-1.manuscdn.com/sessionFile/Kv3nXRCXCLHmEa8ubHl8P8/sandbox/WewAvHF1P8YRJu9LP7jPJa-images_1756742930678_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0xETEE4b1BHR2xZSA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvS3YzblhSQ1hDTEhtRWE4dWJIbDhQOC9zYW5kYm94L1dld0F2SEYxUDhZUkp1OUxQN2pQSmEtaW1hZ2VzXzE3NTY3NDI5MzA2NzhfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMHhFVEVFNGIxQkhSMnhaU0EucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=WYiYrv9bngYPA1MY9e39JT19u3IafkF1BcV7Kj4Rx-Bty0HHnFk6M4-p6g~1bnXxyWUv3ixGwybEy8g~CGWoOkr0ptZP822O1ncIzRDvwKDp7pks9Zfo9D0TdDRTFsUnO3TwyHTrURW1L-sd3C1Yt3sPZUV1kbErXbDDICgZtzVoK9WqPMIuwWu5do53TpeXBXGMfqJ4cXgGkXX8sELSV8y8B8mUayNrID49UlmIFEKAH7hN3TVBAEaBhawML-DWmspJsyrJO9-VgmgzGdEJMS0agjS55Fi84Y7ooZAQjcTTkMa2ZETlUeRrskza8XpmJfUgucDVP13NtBGbh3Ze9Q__)

Em 2025, o Big Data é caracterizado pelos **5Vs fundamentais**, uma evolução do modelo original de 3Vs que agora inclui duas dimensões críticas adicionais [3]:

#### **1. Volume (Escala dos Dados)**
O Volume refere-se à quantidade massiva de dados gerados e coletados. Em 2025, estamos lidando com:
- **Petabytes e Exabytes** de dados corporativos
- **2.5 quintilhões de bytes** de dados criados diariamente
- **Crescimento de 40% ao ano** no volume global de dados

**Exemplos práticos em 2025:**
- Netflix processa mais de 15 petabytes de dados diariamente para recomendações
- Google processa mais de 20 petabytes de dados por dia
- Walmart coleta mais de 2.5 petabytes de dados de transações de clientes por hora

#### **2. Velocity (Velocidade dos Dados)**
A Velocity representa a velocidade com que os dados são gerados, processados e analisados. Em 2025, isso inclui:
- **Processamento em tempo real** (real-time)
- **Streaming de dados** contínuo
- **Análise instantânea** para tomada de decisões

**Exemplos práticos em 2025:**
- Sistemas de detecção de fraude bancária processam transações em milissegundos
- Plataformas de trading algorítmico executam milhões de operações por segundo
- Sistemas de IoT em carros autônomos processam dados de sensores em tempo real

#### **3. Variety (Variedade dos Dados)**
A Variety abrange os diferentes tipos e formatos de dados. Em 2025, isso inclui:
- **Dados estruturados** (bancos de dados relacionais)
- **Dados semi-estruturados** (XML, JSON)
- **Dados não estruturados** (textos, imagens, vídeos, áudios)

**Exemplos práticos em 2025:**
- Análise de sentimentos combinando texto, emojis e imagens de redes sociais
- Sistemas de saúde integrando exames médicos, histórico clínico e dados de wearables
- Plataformas de e-commerce analisando comportamento de navegação, reviews e dados demográficos

#### **4. Veracity (Veracidade dos Dados)**
A Veracity refere-se à qualidade, precisão e confiabilidade dos dados. Em 2025, isso é crucial devido a:
- **Dados incompletos ou inconsistentes**
- **Informações falsas** (fake news, deepfakes)
- **Ruído nos dados** de sensores IoT

**Exemplos práticos em 2025:**
- Algoritmos de verificação de fatos em plataformas de mídia social
- Sistemas de validação de dados médicos para diagnósticos por IA
- Filtros de qualidade em dados de sensores industriais

#### **5. Value (Valor dos Dados)**
O Value representa o benefício e insights acionáveis extraídos dos dados. Em 2025, o foco está em:
- **ROI mensurável** de iniciativas de Big Data
- **Insights acionáveis** para decisões estratégicas
- **Monetização de dados** como ativo empresarial

**Exemplos práticos em 2025:**
- Modelos preditivos que reduzem custos operacionais em 20-30%
- Personalização que aumenta conversões de vendas em até 50%
- Otimização de supply chain que reduz desperdícios em 25%

### 1.3 O que é Apache Hadoop?

Apache Hadoop é uma estrutura de software de código aberto projetada especificamente para armazenar e processar grandes volumes de dados de forma distribuída em clusters de computadores comuns (commodity hardware). Desenvolvido originalmente pelo Yahoo! em 2006, baseado nos papers do Google sobre MapReduce e Google File System, o Hadoop se tornou o padrão de facto para processamento de Big Data [4].

O nome "Hadoop" vem do elefante de brinquedo amarelo do filho de Doug Cutting, um dos criadores do projeto. Esta origem lúdica contrasta com a robustez e seriedade da plataforma, que hoje processa exabytes de dados em organizações ao redor do mundo.

**Características fundamentais do Hadoop:**

- **Escalabilidade horizontal**: Capacidade de adicionar mais nós ao cluster para aumentar a capacidade de processamento e armazenamento
- **Tolerância a falhas**: Replicação automática de dados em múltiplos nós para garantir disponibilidade
- **Processamento distribuído**: Divisão de tarefas complexas em subtarefas menores executadas em paralelo
- **Custo-efetivo**: Utilização de hardware comum ao invés de servidores especializados caros
- **Flexibilidade**: Capacidade de processar dados estruturados e não estruturados

### 1.4 Por que o Hadoop é Importante em 2025?

Em 2025, o Hadoop continua sendo uma tecnologia fundamental para Big Data, especialmente quando integrado com tecnologias modernas de IA e machine learning. Sua importância se manifesta em várias dimensões [5]:

#### **Escalabilidade Massiva**
O Hadoop pode processar desde gigabytes até exabytes de dados, escalando horizontalmente conforme a necessidade. Empresas como Facebook e LinkedIn operam clusters Hadoop com milhares de nós, processando petabytes de dados diariamente.

#### **Economia de Custos**
Comparado a soluções proprietárias tradicionais, o Hadoop oferece uma redução de custos de 10x a 100x para armazenamento e processamento de Big Data. Isso democratiza o acesso a análises avançadas para empresas de todos os tamanhos.

#### **Integração com IA e Machine Learning**
Em 2025, o Hadoop serve como base para pipelines de machine learning, fornecendo dados limpos e processados para algoritmos de IA. Ferramentas como Apache Spark e TensorFlow se integram nativamente com o ecossistema Hadoop.

#### **Processamento de Dados Não Estruturados**
Com 80% dos dados corporativos sendo não estruturados (textos, imagens, vídeos), o Hadoop oferece a flexibilidade necessária para processar esses formatos diversos, algo que bancos de dados relacionais tradicionais não conseguem fazer eficientemente.

### 1.5 Casos de Uso Reais em 2025

#### **1. Saúde Digital e Medicina Personalizada**
Hospitais e sistemas de saúde utilizam Hadoop para:
- Processar imagens médicas (raios-X, ressonâncias) para diagnósticos assistidos por IA
- Analisar dados genômicos para medicina personalizada
- Monitorar dados de dispositivos wearables para prevenção de doenças
- Otimizar operações hospitalares e reduzir custos

**Exemplo:** O Hospital Johns Hopkins utiliza Hadoop para processar mais de 50TB de dados médicos diários, melhorando diagnósticos em 30% e reduzindo tempo de análise de semanas para horas.

#### **2. Cidades Inteligentes (Smart Cities)**
Governos municipais implementam Hadoop para:
- Otimizar tráfego urbano com dados de sensores e câmeras
- Gerenciar consumo de energia e recursos hídricos
- Melhorar segurança pública com análise preditiva
- Otimizar coleta de lixo e serviços urbanos

**Exemplo:** A cidade de Barcelona processa dados de mais de 20.000 sensores IoT usando Hadoop, reduzindo congestionamentos em 25% e economizando 30% no consumo de água.

#### **3. Fintech e Detecção de Fraudes**
Instituições financeiras usam Hadoop para:
- Detectar fraudes em tempo real analisando padrões de transação
- Avaliar riscos de crédito com dados alternativos
- Personalizar produtos financeiros baseados em comportamento
- Cumprir regulamentações de compliance automaticamente

**Exemplo:** O Banco Santander processa mais de 100 milhões de transações diárias usando Hadoop, detectando fraudes com 99.5% de precisão e reduzindo falsos positivos em 60%.

#### **4. E-commerce e Personalização**
Plataformas de comércio eletrônico utilizam Hadoop para:
- Sistemas de recomendação em tempo real
- Otimização de preços dinâmica
- Análise de sentimentos de reviews e redes sociais
- Previsão de demanda e gestão de estoque

**Exemplo:** A Amazon processa mais de 15 petabytes de dados de clientes diariamente com Hadoop, gerando 35% de suas receitas através de recomendações personalizadas.

#### **5. Agricultura de Precisão**
O agronegócio moderno emprega Hadoop para:
- Análise de dados de satélites e drones para monitoramento de culturas
- Otimização de irrigação baseada em dados climáticos
- Previsão de safras e detecção precoce de pragas
- Rastreabilidade completa da cadeia alimentar

**Exemplo:** A John Deere utiliza Hadoop para processar dados de mais de 500.000 máquinas agrícolas conectadas, aumentando produtividade em 20% e reduzindo uso de pesticidas em 15%.

---



## 2. ARQUITETURA DO HADOOP

### 2.1 Visão Geral da Arquitetura

![Arquitetura Hadoop](https://private-us-east-1.manuscdn.com/sessionFile/Kv3nXRCXCLHmEa8ubHl8P8/sandbox/WewAvHF1P8YRJu9LP7jPJa-images_1756742930681_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL05EaHBwUVlMZVFvWg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvS3YzblhSQ1hDTEhtRWE4dWJIbDhQOC9zYW5kYm94L1dld0F2SEYxUDhZUkp1OUxQN2pQSmEtaW1hZ2VzXzE3NTY3NDI5MzA2ODFfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMDVFYUhCd1VWbE1aVkZ2V2cucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=M75niLEpXOvOFcAUMr9T9xiCl5dHILticMwNWByH44znmjZt~X-h6lgfZ-mfFQlLeetzF13qy4XaIZGD9ImvCLDsa~iOEaCiGit9fcn2SInWgKEdux6Cj6syTcYPKfWl6W~4kCFXz2AOML34wACXD3gFTgSJ8E0s5qN4RceBabxFLEScyt4SIPTaj4dVTNMlrJaC5aMIHsK23DS4k2ij~yj382Q6QdsKpciJ7Rx7igRCSDjqh4c4lfIuBlsMsRoSF8ZP2h0~~FSPAa1LFLaNa2ozKCv99UKkMNd1EopiVyznIeFMBqRXBFX~ET-R3-VjtXI5Aa4WJ5KDlN2FPn6cUg__)

A arquitetura do Apache Hadoop é baseada em um design distribuído que permite o processamento paralelo de grandes volumes de dados em clusters de computadores comuns. A arquitetura é composta por quatro componentes principais que trabalham em conjunto para fornecer uma plataforma robusta e escalável [6]:

1. **Hadoop Common**: Bibliotecas e utilitários comuns necessários para outros módulos Hadoop
2. **HDFS (Hadoop Distributed File System)**: Sistema de arquivos distribuído para armazenamento
3. **YARN (Yet Another Resource Negotiator)**: Gerenciador de recursos e agendador de tarefas
4. **MapReduce**: Framework de programação para processamento distribuído

Esta arquitetura modular permite que cada componente seja otimizado independentemente, mantendo a interoperabilidade e facilitando a manutenção e evolução do sistema.

### 2.2 HDFS (Hadoop Distributed File System)

![Arquitetura HDFS](https://private-us-east-1.manuscdn.com/sessionFile/Kv3nXRCXCLHmEa8ubHl8P8/sandbox/WewAvHF1P8YRJu9LP7jPJa-images_1756742930682_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL05WWm91YnlEam43cg.gif?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvS3YzblhSQ1hDTEhtRWE4dWJIbDhQOC9zYW5kYm94L1dld0F2SEYxUDhZUkp1OUxQN2pQSmEtaW1hZ2VzXzE3NTY3NDI5MzA2ODJfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMDVXV205MVlubEVhbTQzY2cuZ2lmIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=J44lviJNPRibDx0KNt1wy3PJ0N6f~Y5taSiCsySbgLiO24R3g~RCLAyddhrNfMQXB5lCAYoOjq7rF2KMXGsypXZr9tzVnpyBt3zMKZnNb1h6ll0tgK6LCi59C5u53PyDFgnpvszwTXwaNee4sRaf~miKXsQssK77sYZPyKdVJYI8dXxnExC6b-kr7CQjLQgH3yDPBcnGCng1Es5UFOjXeQUY9zi1Ig3Un7i85aT26Ma6jZkQXsaQWCrmza1BOkzpUNOG00plNHaD6sFLdbc-8w-P1qdufr0fy1LoFS0TP20n9U1xtHX5rDN0mi-JcceGwMbw4wHOedHRsfsVTOY~Uw__)

O HDFS é o sistema de arquivos distribuído do Hadoop, projetado para armazenar grandes arquivos de dados em clusters de máquinas comuns de forma confiável e eficiente. Baseado no Google File System (GFS), o HDFS é otimizado para throughput alto ao invés de baixa latência [7].

#### **Componentes Principais do HDFS:**

**NameNode (Nó Mestre)**
O NameNode é o componente central do HDFS que gerencia o namespace do sistema de arquivos e regula o acesso aos arquivos pelos clientes. Suas responsabilidades incluem:

- **Metadados**: Armazena informações sobre a estrutura de diretórios, permissões de arquivos e localização dos blocos
- **Mapeamento de blocos**: Mantém o mapeamento de quais DataNodes contêm quais blocos de dados
- **Operações de namespace**: Executa operações como abrir, fechar, renomear arquivos e diretórios
- **Replicação**: Determina a estratégia de replicação de blocos para garantir disponibilidade

**DataNodes (Nós Escravos)**
Os DataNodes são responsáveis pelo armazenamento real dos dados e executam operações de leitura e escrita conforme solicitado pelos clientes. Suas funções incluem:

- **Armazenamento de blocos**: Cada arquivo é dividido em blocos (padrão de 128MB) armazenados nos DataNodes
- **Replicação**: Mantém múltiplas cópias de cada bloco (padrão de 3 réplicas)
- **Heartbeat**: Envia sinais periódicos ao NameNode para confirmar que está operacional
- **Relatórios de blocos**: Informa ao NameNode sobre os blocos que possui

#### **Características Técnicas do HDFS:**

**Tolerância a Falhas**
O HDFS implementa tolerância a falhas através de múltiplas estratégias:
- **Replicação de dados**: Cada bloco é replicado em múltiplos DataNodes (padrão: 3 réplicas)
- **Detecção de falhas**: Monitoramento contínuo da saúde dos nós através de heartbeats
- **Recuperação automática**: Re-replicação automática quando um nó falha
- **Checksums**: Verificação de integridade dos dados para detectar corrupção

**Escalabilidade**
O HDFS escala horizontalmente adicionando mais DataNodes ao cluster:
- **Capacidade linear**: Cada novo DataNode adiciona capacidade de armazenamento e throughput
- **Balanceamento automático**: Redistribuição automática de dados para otimizar utilização
- **Suporte a milhares de nós**: Clusters com mais de 4.000 nós em produção

### 2.3 MapReduce

![MapReduce Workflow](https://private-us-east-1.manuscdn.com/sessionFile/Kv3nXRCXCLHmEa8ubHl8P8/sandbox/WewAvHF1P8YRJu9LP7jPJa-images_1756742930683_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL2UzdXAyUlA3NWExMw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvS3YzblhSQ1hDTEhtRWE4dWJIbDhQOC9zYW5kYm94L1dld0F2SEYxUDhZUkp1OUxQN2pQSmEtaW1hZ2VzXzE3NTY3NDI5MzA2ODNfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMlV6ZFhBeVVsQTNOV0V4TXcucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=MCDSkODfXG5S-aWLWOOFCpuiQIaL8wMNB23P9mYLKlbFnxR8K8IC6jj-fYfACh~doQWnfLkyekHdylyUGn2Ae0ZLuJO0R3jid79mo73XFWzfvgB53Eq1uNIMFLFTFLJmJSzgTQKAk~OK7Nkisoit2t8F3AqdB3Rw4oEtAKXHNpTmXBXkXKXW23oNB8nCfFZb4MH-pTq6RBm4yQcy5RrSAukYW8g-YwU038RvEt58prK7fZXyldvCoMWh-DikSuUYvVWwKLchTNJikZbodZJXclajAvpGuJW8KxKMOeBxNhan1VSFadtAK2-cw47K4tH643lQhD5XOUHUpc2Op3wp1A__)

MapReduce é um modelo de programação e uma implementação associada para processar e gerar grandes conjuntos de dados de forma distribuída. Inspirado nas funções map e reduce da programação funcional, o MapReduce divide o processamento em duas fases principais [8].

#### **Fases do MapReduce:**

**Fase Map**
A fase Map processa dados de entrada em paralelo, aplicando uma função definida pelo usuário a cada registro:

```
Map(chave1, valor1) → lista(chave2, valor2)
```

- **Paralelização**: Cada mapper processa uma porção dos dados de entrada independentemente
- **Transformação**: Converte dados de entrada em pares chave-valor intermediários
- **Localidade de dados**: Mappers são executados preferencialmente nos nós que contêm os dados

**Fase Shuffle e Sort**
Entre as fases Map e Reduce, o sistema executa shuffle e sort:
- **Shuffle**: Redistribui dados intermediários baseado nas chaves
- **Sort**: Ordena dados por chave para otimizar o processamento Reduce
- **Particionamento**: Determina qual Reducer processará cada chave

**Fase Reduce**
A fase Reduce agrega os valores intermediários por chave:

```
Reduce(chave2, lista(valor2)) → lista(chave3, valor3)
```

- **Agregação**: Combina todos os valores associados a uma chave específica
- **Paralelização**: Múltiplos reducers processam diferentes chaves simultaneamente
- **Saída final**: Produz o resultado final do processamento

#### **Exemplo Prático: WordCount**

O WordCount é o "Hello World" do MapReduce, demonstrando como contar palavras em documentos:

**Entrada:**
```
"Hello World"
"Hello Hadoop"
```

**Fase Map:**
```
Mapper 1: "Hello World" → [("Hello", 1), ("World", 1)]
Mapper 2: "Hello Hadoop" → [("Hello", 1), ("Hadoop", 1)]
```

**Fase Shuffle:**
```
"Hello" → [1, 1]
"World" → [1]
"Hadoop" → [1]
```

**Fase Reduce:**
```
Reducer 1: ("Hello", [1, 1]) → ("Hello", 2)
Reducer 2: ("World", [1]) → ("World", 1)
Reducer 3: ("Hadoop", [1]) → ("Hadoop", 1)
```

### 2.4 YARN (Yet Another Resource Negotiator)

YARN é o sistema de gerenciamento de recursos do Hadoop 2.x que separa as funções de gerenciamento de recursos e agendamento de jobs da lógica de processamento de dados. Esta separação permite que o Hadoop suporte múltiplos frameworks de processamento além do MapReduce [9].

#### **Componentes do YARN:**

**ResourceManager (RM)**
O ResourceManager é o componente central que gerencia recursos em todo o cluster:
- **Agendamento global**: Aloca recursos para aplicações baseado em políticas configuradas
- **Monitoramento**: Rastreia recursos disponíveis e utilizados em cada nó
- **Gerenciamento de aplicações**: Coordena o ciclo de vida das aplicações

**NodeManager (NM)**
Cada nó do cluster executa um NodeManager que gerencia recursos locais:
- **Monitoramento local**: Monitora uso de CPU, memória e disco no nó
- **Execução de containers**: Inicia e monitora containers de aplicações
- **Relatórios**: Envia informações de status para o ResourceManager

**ApplicationMaster (AM)**
Cada aplicação tem seu próprio ApplicationMaster que coordena sua execução:
- **Negociação de recursos**: Solicita recursos necessários ao ResourceManager
- **Coordenação de tarefas**: Gerencia a execução de tarefas da aplicação
- **Monitoramento**: Monitora progresso e trata falhas de tarefas

#### **Vantagens do YARN:**

**Utilização Eficiente de Recursos**
- **Compartilhamento dinâmico**: Recursos são alocados dinamicamente baseado na demanda
- **Múltiplos frameworks**: Suporte simultâneo a MapReduce, Spark, Storm, etc.
- **Isolamento**: Aplicações são isoladas em containers para evitar interferência

**Escalabilidade Melhorada**
- **Descentralização**: ApplicationMasters distribuem a carga de gerenciamento
- **Suporte a clusters maiores**: Clusters com mais de 10.000 nós
- **Melhor throughput**: Redução de gargalos de comunicação

### 2.5 Ecossistema Hadoop

![Ecossistema Hadoop](https://private-us-east-1.manuscdn.com/sessionFile/Kv3nXRCXCLHmEa8ubHl8P8/sandbox/WewAvHF1P8YRJu9LP7jPJa-images_1756742930684_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL1pMTVRtRzg0UlBMdg.jpg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvS3YzblhSQ1hDTEhtRWE4dWJIbDhQOC9zYW5kYm94L1dld0F2SEYxUDhZUkp1OUxQN2pQSmEtaW1hZ2VzXzE3NTY3NDI5MzA2ODRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMXBNVFZSdFJ6ZzBVbEJNZGcuanBnIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=rBHRWpMlEdQs2u6~29OMvGO0Lqa3~l6-awIb7nEsf5J19Fajo7L1Nu1d~Qoj98gODPCGR8VQwchhb4IK1ogeoz-2V-R3e840Fc4wodWsGa3X13jCRkfziQ~~-sBoEqLhSbawH622RixNHvMGylKbpFwyext4kYr5rqmRXOeVyIipi3l~4Qcwh437Tz7NuG~VCFzHyTojqNWR9aqtZwnniOgYjecWp7UapHZCiTV5jeeV2K1UBqAXd~A~ftE-Or8ovwXuPj9A9auUP04qfC3r0SQ9sB4m7oZFqH3f-GdNo-qK0VVmVlpsuFKTt8si5816-~xAzrpk7ftH~9kfena3xg__)

O ecossistema Hadoop é uma coleção de ferramentas e frameworks que estendem as capacidades básicas do Hadoop para diferentes casos de uso. Em 2025, este ecossistema inclui mais de 100 projetos ativos [10].

#### **Componentes Principais do Ecossistema:**

**Armazenamento e Gestão de Dados**
- **HBase**: Banco de dados NoSQL distribuído para acesso aleatório em tempo real
- **Cassandra**: Banco de dados distribuído para alta disponibilidade
- **MongoDB**: Banco de dados de documentos para dados semi-estruturados

**Processamento de Dados**
- **Apache Spark**: Engine de processamento unificado para batch e streaming
- **Apache Storm**: Processamento de streams em tempo real
- **Apache Flink**: Processamento de streams com baixa latência

**Análise e Consulta**
- **Apache Hive**: Data warehouse para consultas SQL em dados Hadoop
- **Apache Pig**: Linguagem de alto nível para análise de dados
- **Presto**: Engine de consulta SQL distribuída para análise interativa

**Ingestão de Dados**
- **Apache Flume**: Coleta e agregação de dados de logs
- **Apache Sqoop**: Transferência de dados entre Hadoop e bancos relacionais
- **Apache Kafka**: Plataforma de streaming distribuída

**Coordenação e Workflow**
- **Apache Zookeeper**: Serviço de coordenação para aplicações distribuídas
- **Apache Oozie**: Sistema de workflow para jobs Hadoop
- **Apache Airflow**: Plataforma para desenvolvimento e agendamento de workflows

#### **Integração com Tecnologias Modernas (2025)**

**Inteligência Artificial e Machine Learning**
- **TensorFlow on Hadoop**: Treinamento distribuído de modelos de deep learning
- **MLlib (Spark)**: Biblioteca de machine learning escalável
- **H2O.ai**: Plataforma de machine learning em memória

**Cloud Computing**
- **Amazon EMR**: Hadoop gerenciado na AWS
- **Google Cloud Dataproc**: Hadoop e Spark gerenciados no Google Cloud
- **Azure HDInsight**: Hadoop gerenciado no Microsoft Azure

**Containers e Orquestração**
- **Kubernetes**: Orquestração de containers para aplicações Hadoop
- **Docker**: Containerização de componentes do ecossistema
- **Apache Mesos**: Gerenciamento de recursos para datacenters

---


## 3. PRÉ-REQUISITOS E PREPARAÇÃO DO AMBIENTE

### 3.1 Requisitos de Sistema

Antes de iniciar a instalação do Hadoop, é fundamental verificar se o sistema atende aos requisitos mínimos e recomendados para uma operação eficiente.

#### **Requisitos de Hardware**

**Configuração Mínima (Ambiente de Desenvolvimento/Teste):**
- **CPU**: 2 cores, 2.0 GHz
- **RAM**: 4 GB (mínimo), 8 GB (recomendado)
- **Armazenamento**: 20 GB de espaço livre
- **Rede**: Conexão de internet estável

**Configuração Recomendada (Ambiente de Produção):**
- **CPU**: 8+ cores, 2.4+ GHz
- **RAM**: 32+ GB
- **Armazenamento**: 1+ TB SSD/NVMe para logs, 10+ TB HDD para dados
- **Rede**: Gigabit Ethernet ou superior

#### **Requisitos de Software**

**Sistema Operacional Suportado:**
- **Linux**: Ubuntu 18.04+, CentOS 7+, Red Hat Enterprise Linux 7+
- **Windows**: Windows 10/11 (com WSL2 recomendado)
- **macOS**: macOS 10.14+ (para desenvolvimento apenas)

**Dependências Obrigatórias:**
- **Java**: OpenJDK 8 ou Oracle JDK 8/11 (Java 17+ suportado no Hadoop 3.3+)
- **SSH**: OpenSSH para comunicação entre nós
- **Python**: Python 3.7+ para scripts e ferramentas auxiliares

### 3.2 Conhecimentos Prévios Necessários

Para aproveitar ao máximo este laboratório, é recomendável ter conhecimento básico em:

#### **Conceitos Fundamentais**
- **Sistemas distribuídos**: Compreensão básica de como sistemas distribuídos funcionam
- **Linha de comando Linux**: Navegação, manipulação de arquivos, permissões
- **Redes de computadores**: Conceitos básicos de TCP/IP, portas, firewalls
- **Programação**: Conhecimento básico em Java ou Python é útil

#### **Conceitos de Big Data**
- **Processamento batch vs. streaming**: Diferenças entre processamento em lote e tempo real
- **Dados estruturados vs. não estruturados**: Tipos de dados e suas características
- **Escalabilidade horizontal vs. vertical**: Estratégias de crescimento de sistemas

### 3.3 Ferramentas Auxiliares

#### **Editores de Texto Recomendados**
- **nano**: Editor simples para configurações rápidas
- **vim/vi**: Editor avançado para usuários experientes
- **Visual Studio Code**: IDE com extensões para Big Data

#### **Ferramentas de Monitoramento**
- **htop**: Monitor de processos e recursos do sistema
- **iotop**: Monitor de I/O de disco
- **netstat**: Monitor de conexões de rede

## 4. INSTALAÇÃO DO HADOOP

### 4.1 Métodos de Instalação

Existem várias abordagens para instalar o Hadoop, cada uma adequada para diferentes cenários e níveis de experiência.

#### **Métodos Disponíveis:**

**1. Instalação Manual**
- **Vantagens**: Controle total sobre configuração, aprendizado profundo
- **Desvantagens**: Complexa, propensa a erros, demorada
- **Recomendado para**: Usuários avançados, ambientes de produção customizados

**2. Distribuições Comerciais**
- **Cloudera**: Cloudera Data Platform (CDP)
- **Hortonworks**: Hortonworks Data Platform (HDP) - agora parte da Cloudera
- **MapR**: MapR Data Platform - descontinuado em 2019
- **Vantagens**: Suporte comercial, ferramentas de gerenciamento, integração facilitada
- **Desvantagens**: Custo, dependência de fornecedor

**3. Instalação com Scripts Automatizados**
- **Vantagens**: Rápida, reduz erros, reproduzível
- **Desvantagens**: Menos flexibilidade, pode ocultar detalhes importantes
- **Recomendado para**: Ambientes de aprendizado, prototipagem rápida

**4. Containers e Cloud**
- **Docker**: Containers pré-configurados
- **Kubernetes**: Orquestração de clusters Hadoop
- **Cloud Services**: EMR (AWS), Dataproc (GCP), HDInsight (Azure)

### 4.2 Instalação Automatizada com Scripts

Para este laboratório, utilizaremos os scripts desenvolvidos pelo Professor Vagner Cordeiro, que automatizam o processo de instalação e configuração do Hadoop em modo pseudo-distribuído. Esta abordagem é ideal para aprendizado e desenvolvimento.

> **⚠️ ATENÇÃO IMPORTANTE:**
> A instalação manual do Hadoop pode ser extremamente complexa devido às múltiplas dependências, configurações específicas de sistema operacional e versões de software que mudam constantemente. Os scripts automatizados eliminam a maioria desses problemas, permitindo foco no aprendizado dos conceitos fundamentais.

#### **Visão Geral dos Scripts**

O Professor Vagner Cordeiro desenvolveu três scripts que automatizam todo o processo de instalação:

**1. script_hadoop1.sh (prepare_hadoop.sh)**
- **Função**: Preparação do ambiente e download do Hadoop
- **Ações executadas**:
  - Limpeza de instalações anteriores
  - Verificação de conectividade com internet
  - Checagem de recursos do sistema (memória e espaço em disco)
  - Instalação de dependências (Java 8, SSH)
  - Download do Hadoop 3.4.1 (versão otimizada)
  - Verificação de integridade do arquivo baixado

**2. script_hadoop2.sh**
- **Função**: Instalação e configuração do Hadoop
- **Ações executadas**:
  - Descompactação do arquivo Hadoop
  - Configuração do SSH para acesso sem senha (passwordless)
  - Configuração dos arquivos de configuração do Hadoop
  - Formatação do NameNode
  - Inicialização dos serviços Hadoop
  - Verificação da instalação

**3. setup_exercises.sh**
- **Função**: Configuração dos exercícios práticos
- **Ações executadas**:
  - Criação de diretórios para exercícios
  - Cópia de arquivos de configuração para o HDFS
  - Preparação de dados de exemplo
  - Configuração de exercícios de MapReduce

#### **Passo a Passo da Instalação**

**ETAPA 1: Download dos Scripts**

Acesse o link fornecido pelo professor para baixar os três scripts necessários:

```
https://drive.google.com/drive/folders/1C7hRMz7N1OJrYxk7vIA-E9qyiw5ZLEpu?usp=sharing
```

Os arquivos que você deve baixar são:
- `script_hadoop1.sh` (ou `prepare_hadoop.sh`)
- `script_hadoop2.sh`
- `setup_exercises.sh`

**ETAPA 2: Configuração de Permissões**

Após o download, é necessário dar permissões de execução aos scripts:

```bash
# Navegue até o diretório onde os scripts foram baixados
cd ~/Downloads

# Conceda permissões de execução
chmod +x script_hadoop1.sh
chmod +x script_hadoop2.sh
chmod +x setup_exercises.sh

# Verificar permissões (opcional)
ls -la *.sh
```

**ETAPA 3: Execução do Primeiro Script**

Execute o script de preparação do ambiente:

```bash
# Execute o primeiro script
sudo ./script_hadoop1.sh
```

**O que acontece durante a execução:**
- O script verifica se há instalações anteriores do Hadoop e as remove
- Testa a conectividade com a internet
- Verifica se há memória suficiente (mínimo 2GB) e espaço em disco (mínimo 10GB)
- Instala o Java 8 (OpenJDK) se não estiver presente
- Configura as variáveis de ambiente JAVA_HOME
- Instala e configura o SSH
- Baixa o Hadoop 3.4.1 do repositório oficial Apache
- Verifica a integridade do arquivo baixado usando checksums

**Indicadores de sucesso:**
- Mensagem "Hadoop download completed successfully"
- Arquivo `/tmp/hadoop.tar.gz` criado
- Nenhuma mensagem de erro durante a execução

**ETAPA 4: Execução do Segundo Script**

Execute o script de instalação e configuração:

```bash
# Execute o segundo script
sudo ./script_hadoop2.sh
```

**O que acontece durante a execução:**
- Descompactação do Hadoop em `/usr/local/hadoop`
- Configuração do usuário hadoop (se necessário)
- Geração de chaves SSH para comunicação sem senha
- Configuração dos arquivos principais do Hadoop:
  - `core-site.xml`: Configurações centrais do Hadoop
  - `hdfs-site.xml`: Configurações específicas do HDFS
  - `mapred-site.xml`: Configurações do MapReduce
  - `yarn-site.xml`: Configurações do YARN
- Formatação do sistema de arquivos HDFS
- Inicialização dos serviços:
  - NameNode
  - DataNode
  - ResourceManager
  - NodeManager

**Indicadores de sucesso:**
- Mensagem "Hadoop installation completed successfully"
- Serviços Hadoop rodando (verificável com `jps`)
- Interface web acessível em `http://localhost:9870`

### 4.3 Verificação da Instalação

Após a execução dos scripts, é importante verificar se a instalação foi bem-sucedida.

#### **Verificação dos Processos Java**

Use o comando `jps` para verificar se os processos Hadoop estão rodando:

```bash
jps
```

**Saída esperada:**
```
12345 NameNode
12346 DataNode
12347 ResourceManager
12348 NodeManager
12349 Jps
```

#### **Verificação dos Arquivos de Configuração**

Verifique o conteúdo do arquivo `core-site.xml`:

```bash
cat /usr/local/hadoop/etc/hadoop/core-site.xml
```

**Conteúdo esperado:**
```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

#### **Verificação da Interface Web**

Acesse a interface web do Hadoop através do navegador:
- **NameNode**: http://localhost:9870
- **ResourceManager**: http://localhost:8088

A interface deve mostrar informações sobre o cluster, incluindo:
- Status dos nós
- Capacidade de armazenamento
- Jobs em execução
- Métricas de performance

#### **Teste Básico do HDFS**

Execute comandos básicos para testar o HDFS:

```bash
# Criar diretório no HDFS
/usr/local/hadoop/bin/hdfs dfs -mkdir /test

# Listar conteúdo do diretório raiz
/usr/local/hadoop/bin/hdfs dfs -ls /

# Verificar status do sistema de arquivos
/usr/local/hadoop/bin/hdfs dfsadmin -report
```

### 4.4 Troubleshooting Comum

#### **Problema: Java não encontrado**

**Sintomas:**
- Erro "JAVA_HOME is not set"
- Comandos Hadoop falham com erro de Java

**Solução:**
```bash
# Verificar se Java está instalado
java -version

# Se não estiver instalado
sudo apt update
sudo apt install openjdk-8-jdk

# Configurar JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64' >> ~/.bashrc
```

#### **Problema: SSH não configurado**

**Sintomas:**
- Erro "Permission denied (publickey)"
- Falha na inicialização dos serviços

**Solução:**
```bash
# Gerar chaves SSH
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa

# Adicionar chave pública ao authorized_keys
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# Configurar permissões
chmod 0600 ~/.ssh/authorized_keys

# Testar conexão SSH
ssh localhost
```

#### **Problema: Portas em uso**

**Sintomas:**
- Erro "Address already in use"
- Serviços não inicializam

**Solução:**
```bash
# Verificar portas em uso
netstat -tulpn | grep :9000
netstat -tulpn | grep :9870

# Matar processos usando as portas (se necessário)
sudo kill -9 <PID>

# Reiniciar serviços Hadoop
/usr/local/hadoop/sbin/stop-all.sh
/usr/local/hadoop/sbin/start-all.sh
```

#### **Problema: Espaço em disco insuficiente**

**Sintomas:**
- Erro "No space left on device"
- HDFS reporta 0% de espaço disponível

**Solução:**
```bash
# Verificar espaço em disco
df -h

# Limpar logs antigos
sudo rm -rf /usr/local/hadoop/logs/*

# Limpar arquivos temporários
sudo rm -rf /tmp/hadoop-*

# Verificar configuração de espaço reservado no HDFS
/usr/local/hadoop/bin/hdfs dfsadmin -report
```

---


## 5. EXERCÍCIOS PRÁTICOS

### 5.1 Preparação dos Exercícios

Antes de iniciar os exercícios práticos, execute o script de configuração dos exercícios:

```bash
# Execute o terceiro script
sudo ./setup_exercises.sh
```

**O que o script faz:**
- Cria a estrutura de diretórios para os exercícios
- Configura arquivos de entrada no HDFS
- Prepara dados de exemplo para os exercícios
- Cria o diretório `/exercicios_alunos/vagner_cordeiro`

**Navegação para o diretório de exercícios:**
```bash
cd exercicios_alunos/vagner_cordeiro
```

### 5.2 Exercício 1: Grep (Busca de Padrões)

#### **Objetivo do Exercício**
O exercício Grep demonstra como usar o MapReduce para buscar padrões específicos em arquivos de texto. Este é um exemplo fundamental que ilustra como o MapReduce pode ser usado para filtrar e processar dados baseado em critérios específicos.

#### **Conceitos Aprendidos**
- **Processamento de texto**: Como o MapReduce processa arquivos de texto linha por linha
- **Expressões regulares**: Uso de regex para busca de padrões complexos
- **Filtragem distribuída**: Como filtros são aplicados em paralelo em um cluster
- **Agregação de resultados**: Como resultados de múltiplos mappers são combinados

#### **Cenário Prático**
Imagine que você trabalha em uma empresa de telecomunicações e precisa analisar logs de configuração de equipamentos de rede para encontrar todas as configurações relacionadas ao sistema de arquivos distribuído (DFS). Este tipo de análise é comum em:
- **Auditoria de sistemas**: Verificação de configurações de segurança
- **Troubleshooting**: Identificação de problemas em configurações
- **Compliance**: Verificação de conformidade com políticas corporativas

#### **Execução do Exercício**

**Comando:**
```bash
/usr/local/hadoop/bin/hadoop jar \
/usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.4.1.jar \
grep /user/root/input /user/root/output 'dfs[a-z.]+'
```

**Explicação detalhada do comando:**
- `hadoop jar`: Executa um arquivo JAR no Hadoop
- `hadoop-mapreduce-examples-3.4.1.jar`: Arquivo contendo exemplos pré-compilados
- `grep`: Nome da classe/programa a ser executado
- `/user/root/input`: Diretório de entrada no HDFS contendo os arquivos a serem processados
- `/user/root/output`: Diretório de saída onde os resultados serão armazenados
- `'dfs[a-z.]+'`: Expressão regular que busca palavras começando com "dfs" seguidas de letras minúsculas ou pontos

**O que acontece internamente:**

**Fase Map:**
```java
// Pseudocódigo do Mapper
for each line in input_file:
    if line.matches(".*dfs[a-z.]+.*"):
        for each word in line:
            if word.matches("dfs[a-z.]+"):
                emit(word, 1)
```

**Fase Reduce:**
```java
// Pseudocódigo do Reducer
for each unique_word:
    total_count = sum(all_counts_for_word)
    emit(unique_word, total_count)
```

#### **Visualização dos Resultados**

**Comando para ver resultados:**
```bash
/usr/local/hadoop/bin/hdfs dfs -cat /user/root/output/*
```

**Exemplo de saída esperada:**
```
dfs.blocksize	1
dfs.namenode.http-address	1
dfs.namenode.name.dir	1
dfs.replication	1
dfs.datanode.data.dir	1
```

**Interpretação dos resultados:**
- Cada linha mostra uma configuração DFS encontrada e quantas vezes apareceu
- `dfs.replication 1`: A configuração de replicação apareceu uma vez
- `dfs.namenode.http-address 1`: O endereço HTTP do NameNode apareceu uma vez

#### **Cópia para Sistema Local (Opcional)**
```bash
# Copiar resultados para o sistema de arquivos local
/usr/local/hadoop/bin/hdfs dfs -get /user/root/output output_grep

# Visualizar resultados localmente
cat output_grep/*
```

### 5.3 Exercício 2: WordCount (Contagem de Palavras)

#### **Objetivo do Exercício**
O WordCount é o exemplo mais clássico de MapReduce, demonstrando como contar a frequência de palavras em documentos. Este exercício é fundamental para entender os conceitos de Map e Reduce.

#### **Conceitos Aprendidos**
- **Tokenização**: Como texto é dividido em palavras individuais
- **Agregação distribuída**: Como contagens são somadas em paralelo
- **Particionamento**: Como dados são distribuídos entre reducers
- **Combiners**: Otimização que reduz tráfego de rede

#### **Cenário Prático**
Este tipo de processamento é usado em:
- **Análise de sentimentos**: Contagem de palavras positivas/negativas em reviews
- **SEO e marketing**: Análise de frequência de palavras-chave em conteúdo
- **Pesquisa acadêmica**: Análise de frequência de termos em literatura científica
- **Detecção de spam**: Identificação de palavras comuns em emails spam

#### **Execução do Exercício**

**Comando:**
```bash
/usr/local/hadoop/bin/hadoop jar \
/usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.4.1.jar \
wordcount /user/root/input/input.txt /user/root/output_wordcount
```

**Explicação detalhada:**
- `wordcount`: Programa que conta frequência de palavras
- `/user/root/input/input.txt`: Arquivo específico de entrada
- `/user/root/output_wordcount`: Diretório de saída para este exercício

**Processo detalhado do WordCount:**

**Entrada de exemplo:**
```
O Hadoop facilita o processamento de grandes volumes de dados.
O Hadoop é uma ferramenta poderosa para Big Data.
```

**Fase Map:**
```
Mapper 1: "O Hadoop facilita o processamento..."
→ [("O", 1), ("Hadoop", 1), ("facilita", 1), ("o", 1), ("processamento", 1), ...]

Mapper 2: "O Hadoop é uma ferramenta..."
→ [("O", 1), ("Hadoop", 1), ("é", 1), ("uma", 1), ("ferramenta", 1), ...]
```

**Fase Shuffle e Sort:**
```
"O" → [1, 1]
"Hadoop" → [1, 1]
"o" → [1]
"processamento" → [1]
"é" → [1]
"uma" → [1]
...
```

**Fase Reduce:**
```
Reducer 1: ("O", [1, 1]) → ("O", 2)
Reducer 2: ("Hadoop", [1, 1]) → ("Hadoop", 2)
Reducer 3: ("o", [1]) → ("o", 1)
...
```

#### **Visualização dos Resultados**

**Comando:**
```bash
/usr/local/hadoop/bin/hdfs dfs -cat /user/root/output_wordcount/*
```

**Exemplo de saída:**
```
Big	1
Data	1
Hadoop	2
O	2
de	1
dados	1
é	1
facilita	1
ferramenta	1
grandes	1
o	1
para	1
poderosa	1
processamento	1
uma	1
volumes	1
```

**Análise dos resultados:**
- Palavras são ordenadas alfabeticamente
- "Hadoop" e "O" aparecem 2 vezes cada
- Outras palavras aparecem 1 vez cada
- Case-sensitive: "O" e "o" são contados separadamente

#### **Cópia para Sistema Local**
```bash
/usr/local/hadoop/bin/hdfs dfs -get /user/root/output_wordcount output_wordcount_local
cat output_wordcount_local/*
```

### 5.4 Exercício 3: Análise de Logs (Novo)

#### **Objetivo do Exercício**
Este exercício avançado demonstra como processar logs de servidor web para extrair estatísticas úteis, simulando um cenário real de análise de Big Data.

#### **Preparação dos Dados**

Primeiro, vamos criar um arquivo de log simulado:

```bash
# Criar arquivo de log de exemplo
cat > webserver.log << 'EOF'
192.168.1.100 - - [10/Jan/2025:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326
192.168.1.101 - - [10/Jan/2025:13:55:37 +0000] "GET /about.html HTTP/1.1" 200 1024
192.168.1.102 - - [10/Jan/2025:13:55:38 +0000] "POST /login HTTP/1.1" 404 512
192.168.1.100 - - [10/Jan/2025:13:55:39 +0000] "GET /products.html HTTP/1.1" 200 4096
192.168.1.103 - - [10/Jan/2025:13:55:40 +0000] "GET /index.html HTTP/1.1" 200 2326
192.168.1.101 - - [10/Jan/2025:13:55:41 +0000] "GET /contact.html HTTP/1.1" 500 256
EOF

# Copiar para HDFS
/usr/local/hadoop/bin/hdfs dfs -put webserver.log /user/root/input/
```

#### **Análise de Códigos de Status HTTP**

Vamos criar um programa MapReduce personalizado para contar códigos de status HTTP:

```bash
# Usar grep para extrair códigos de status
/usr/local/hadoop/bin/hadoop jar \
/usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.4.1.jar \
grep /user/root/input/webserver.log /user/root/output_status_codes '[0-9]{3}'
```

**Visualizar resultados:**
```bash
/usr/local/hadoop/bin/hdfs dfs -cat /user/root/output_status_codes/*
```

#### **Análise de IPs Mais Frequentes**

```bash
# Extrair IPs usando grep
/usr/local/hadoop/bin/hadoop jar \
/usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.4.1.jar \
grep /user/root/input/webserver.log /user/root/output_ips '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
```

### 5.5 Exercício 4: Processamento de Dados CSV (Novo)

#### **Objetivo do Exercício**
Demonstrar como processar dados estruturados em formato CSV, um caso comum em análise de dados empresariais.

#### **Preparação dos Dados**

Criar arquivo CSV de vendas:

```bash
cat > sales_data.csv << 'EOF'
produto,categoria,preco,quantidade,data
Notebook,Eletrônicos,2500.00,2,2025-01-10
Mouse,Eletrônicos,50.00,10,2025-01-10
Teclado,Eletrônicos,150.00,5,2025-01-10
Cadeira,Móveis,800.00,3,2025-01-10
Mesa,Móveis,1200.00,1,2025-01-10
Notebook,Eletrônicos,2500.00,1,2025-01-11
Mouse,Eletrônicos,50.00,15,2025-01-11
EOF

# Copiar para HDFS
/usr/local/hadoop/bin/hdfs dfs -put sales_data.csv /user/root/input/
```

#### **Análise de Produtos Mais Vendidos**

```bash
# Contar frequência de produtos
/usr/local/hadoop/bin/hadoop jar \
/usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.4.1.jar \
wordcount /user/root/input/sales_data.csv /user/root/output_products
```

#### **Análise de Categorias**

```bash
# Extrair categorias usando grep
/usr/local/hadoop/bin/hadoop jar \
/usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.4.1.jar \
grep /user/root/input/sales_data.csv /user/root/output_categories 'Eletrônicos|Móveis'
```

### 5.6 Limpeza e Preparação para Novos Exercícios

#### **Limpeza de Diretórios de Saída**

Antes de executar novos exercícios, é necessário limpar os diretórios de saída anteriores:

```bash
# Remover diretórios de saída anteriores
/usr/local/hadoop/bin/hdfs dfs -rm -r /user/root/output
/usr/local/hadoop/bin/hdfs dfs -rm -r /user/root/output_wordcount
/usr/local/hadoop/bin/hdfs dfs -rm -r /user/root/output_status_codes
/usr/local/hadoop/bin/hdfs dfs -rm -r /user/root/output_ips
/usr/local/hadoop/bin/hdfs dfs -rm -r /user/root/output_products
/usr/local/hadoop/bin/hdfs dfs -rm -r /user/root/output_categories
```

#### **Verificação do Espaço no HDFS**

```bash
# Verificar uso do espaço no HDFS
/usr/local/hadoop/bin/hdfs dfs -du -h /user/root/

# Relatório detalhado do HDFS
/usr/local/hadoop/bin/hdfs dfsadmin -report
```

### 5.7 Exercícios Desafio (Opcionais)

#### **Desafio 1: Análise de Temperatura**

Crie um arquivo com dados de temperatura e use MapReduce para encontrar a temperatura máxima por cidade:

```bash
cat > temperature_data.txt << 'EOF'
São Paulo,25.5,2025-01-10
Rio de Janeiro,32.1,2025-01-10
Brasília,28.3,2025-01-10
São Paulo,26.2,2025-01-11
Rio de Janeiro,33.5,2025-01-11
Brasília,29.1,2025-01-11
EOF

/usr/local/hadoop/bin/hdfs dfs -put temperature_data.txt /user/root/input/
```

#### **Desafio 2: Análise de Redes Sociais**

Simule dados de interações em redes sociais:

```bash
cat > social_media.txt << 'EOF'
user1 likes post123
user2 shares post123
user1 comments post456
user3 likes post123
user2 likes post789
user1 shares post456
EOF

/usr/local/hadoop/bin/hdfs dfs -put social_media.txt /user/root/input/
```

Use WordCount para analisar as ações mais comuns (likes, shares, comments).

---


## 6. MONITORAMENTO E INTERFACE WEB

### 6.1 Interface Web do Hadoop

O Hadoop fornece interfaces web intuitivas para monitoramento e gerenciamento do cluster. Essas interfaces são essenciais para administradores e desenvolvedores acompanharem o desempenho e status do sistema.

#### **NameNode Web UI (Porto 9870)**

Acesse: `http://localhost:9870`

**Funcionalidades principais:**
- **Overview**: Status geral do cluster, capacidade de armazenamento, número de arquivos
- **Datanodes**: Lista de DataNodes ativos, capacidade individual, status de saúde
- **Browse File System**: Navegador web para o HDFS, permite visualizar arquivos e diretórios
- **Logs**: Logs detalhados do NameNode para troubleshooting

**Métricas importantes:**
- **Configured Capacity**: Capacidade total configurada do cluster
- **DFS Used**: Espaço utilizado no HDFS
- **Non DFS Used**: Espaço usado por arquivos não-HDFS
- **DFS Remaining**: Espaço disponível no HDFS
- **Block Pool Used**: Espaço usado pelos metadados dos blocos

#### **ResourceManager Web UI (Porto 8088)**

Acesse: `http://localhost:8088`

**Funcionalidades principais:**
- **Applications**: Lista de aplicações em execução, concluídas e falhas
- **Cluster**: Métricas do cluster, nós ativos, recursos disponíveis
- **Scheduler**: Informações sobre agendamento de recursos
- **Tools**: Ferramentas de configuração e logs

**Métricas importantes:**
- **Memory Total**: Memória total disponível no cluster
- **Memory Used**: Memória atualmente em uso
- **VCores Total**: Número total de cores virtuais
- **Active Nodes**: Número de nós ativos no cluster

### 6.2 Monitoramento de Jobs

#### **Acompanhamento de Jobs MapReduce**

Quando você executa um job MapReduce, pode acompanhar seu progresso através da interface web:

1. **Acesse o ResourceManager** (`http://localhost:8088`)
2. **Clique em "Applications"** para ver jobs em execução
3. **Clique no Application ID** para detalhes específicos do job
4. **Monitore as fases**: Map, Shuffle, Reduce

**Informações detalhadas do job:**
- **Progress**: Porcentagem de conclusão de cada fase
- **Elapsed Time**: Tempo decorrido desde o início
- **Maps/Reduces**: Número de tasks map e reduce
- **Pending/Running/Complete**: Status das tasks

#### **Logs de Aplicações**

Para acessar logs detalhados de um job:

```bash
# Listar aplicações recentes
/usr/local/hadoop/bin/yarn application -list

# Ver logs de uma aplicação específica
/usr/local/hadoop/bin/yarn logs -applicationId application_1234567890123_0001
```

### 6.3 Análise de Performance

#### **Métricas de Performance do HDFS**

```bash
# Relatório detalhado do HDFS
/usr/local/hadoop/bin/hdfs dfsadmin -report

# Verificar saúde do sistema de arquivos
/usr/local/hadoop/bin/hdfs fsck /

# Estatísticas de uso por diretório
/usr/local/hadoop/bin/hdfs dfs -du -h /user/root/
```

#### **Métricas de Performance do YARN**

```bash
# Status dos nós do cluster
/usr/local/hadoop/bin/yarn node -list

# Informações sobre filas de recursos
/usr/local/hadoop/bin/yarn queue -status default
```

#### **Comandos de Monitoramento do Sistema**

```bash
# Monitorar processos Java do Hadoop
jps -v

# Monitorar uso de recursos
htop

# Monitorar I/O de disco
iotop

# Monitorar conexões de rede
netstat -tulpn | grep java
```

## 7. INTEGRAÇÃO COM PYTHON

### 7.1 Bibliotecas Python para Hadoop

O Python oferece várias bibliotecas para interagir com o ecossistema Hadoop, facilitando o desenvolvimento de aplicações de Big Data.

#### **PyHDFS - Interação com HDFS**

Instalação e uso básico:

```bash
# Instalar PyHDFS
pip3 install hdfs

# Exemplo de uso
python3 << 'EOF'
from hdfs import InsecureClient

# Conectar ao HDFS
client = InsecureClient('http://localhost:9870', user='root')

# Listar arquivos
print("Arquivos no HDFS:")
print(client.list('/user/root/'))

# Ler arquivo
try:
    with client.read('/user/root/input/input.txt') as reader:
        content = reader.read()
        print("Conteúdo do arquivo:")
        print(content.decode('utf-8'))
except Exception as e:
    print(f"Erro ao ler arquivo: {e}")
EOF
```

#### **MRJob - MapReduce em Python**

Instalação:
```bash
pip3 install mrjob
```

Exemplo de WordCount em Python:

```python
# Criar arquivo word_count.py
cat > word_count.py << 'EOF'
from mrjob.job import MRJob
import re

class WordCount(MRJob):
    
    def mapper(self, _, line):
        # Dividir linha em palavras e emitir cada palavra com contagem 1
        words = re.findall(r'\w+', line.lower())
        for word in words:
            yield word, 1
    
    def reducer(self, word, counts):
        # Somar todas as contagens para cada palavra
        yield word, sum(counts)

if __name__ == '__main__':
    WordCount.run()
EOF

# Executar localmente
python3 word_count.py input.txt

# Executar no Hadoop
python3 word_count.py -r hadoop hdfs:///user/root/input/input.txt
```

### 7.2 Exemplos Práticos com Python

#### **Exemplo 1: Análise de Logs com Python**

```python
cat > log_analyzer.py << 'EOF'
from mrjob.job import MRJob
import re

class LogAnalyzer(MRJob):
    
    def mapper(self, _, line):
        # Extrair código de status HTTP usando regex
        status_match = re.search(r'" (\d{3}) ', line)
        if status_match:
            status_code = status_match.group(1)
            yield status_code, 1
    
    def reducer(self, status_code, counts):
        yield status_code, sum(counts)

if __name__ == '__main__':
    LogAnalyzer.run()
EOF
```

#### **Exemplo 2: Processamento de CSV com Python**

```python
cat > csv_processor.py << 'EOF'
from mrjob.job import MRJob
import csv
from io import StringIO

class CSVProcessor(MRJob):
    
    def mapper(self, _, line):
        # Pular cabeçalho
        if line.startswith('produto,'):
            return
        
        try:
            # Processar linha CSV
            reader = csv.reader(StringIO(line))
            row = next(reader)
            produto, categoria, preco, quantidade, data = row
            
            # Emitir categoria com quantidade vendida
            yield categoria, int(quantidade)
            
        except Exception as e:
            # Ignorar linhas malformadas
            pass
    
    def reducer(self, categoria, quantidades):
        total = sum(quantidades)
        yield categoria, total

if __name__ == '__main__':
    CSVProcessor.run()
EOF
```

### 7.3 Desenvolvimento de Jobs MapReduce em Python

#### **Estrutura Básica de um Job MRJob**

```python
from mrjob.job import MRJob
from mrjob.step import MRStep

class MultiStepJob(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper_step1,
                   reducer=self.reducer_step1),
            MRStep(mapper=self.mapper_step2,
                   reducer=self.reducer_step2)
        ]
    
    def mapper_step1(self, _, line):
        # Primeiro passo de mapeamento
        pass
    
    def reducer_step1(self, key, values):
        # Primeiro passo de redução
        pass
    
    def mapper_step2(self, key, value):
        # Segundo passo de mapeamento
        pass
    
    def reducer_step2(self, key, values):
        # Segundo passo de redução
        pass
```

#### **Configuração para Hadoop**

Criar arquivo de configuração `.mrjob.conf`:

```yaml
runners:
  hadoop:
    hadoop_home: /usr/local/hadoop
    hadoop_streaming_jar: /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar
    jobconf:
      mapreduce.job.maps: 2
      mapreduce.job.reduces: 1
```

## 8. TROUBLESHOOTING E FAQ

### 8.1 Problemas Comuns

#### **Problema: "Safe mode is ON"**

**Sintomas:**
- Erro ao tentar escrever no HDFS
- Mensagem "Name node is in safe mode"

**Causa:**
O NameNode entra em safe mode durante a inicialização ou quando detecta problemas no sistema de arquivos.

**Solução:**
```bash
# Verificar status do safe mode
/usr/local/hadoop/bin/hdfs dfsadmin -safemode get

# Sair do safe mode (use com cuidado)
/usr/local/hadoop/bin/hdfs dfsadmin -safemode leave

# Aguardar saída automática do safe mode
/usr/local/hadoop/bin/hdfs dfsadmin -safemode wait
```

#### **Problema: DataNode não inicia**

**Sintomas:**
- DataNode não aparece no `jps`
- Interface web mostra 0 DataNodes

**Possíveis causas e soluções:**

1. **Conflito de cluster ID:**
```bash
# Verificar logs do DataNode
tail -f /usr/local/hadoop/logs/hadoop-*-datanode-*.log

# Se houver conflito de cluster ID, reformatar
/usr/local/hadoop/bin/hdfs namenode -format -force
```

2. **Permissões incorretas:**
```bash
# Corrigir permissões
sudo chown -R $USER:$USER /usr/local/hadoop
sudo chmod -R 755 /usr/local/hadoop
```

3. **Portas em uso:**
```bash
# Verificar portas
netstat -tulpn | grep :9000
netstat -tulpn | grep :9864

# Reiniciar serviços
/usr/local/hadoop/sbin/stop-dfs.sh
/usr/local/hadoop/sbin/start-dfs.sh
```

#### **Problema: Job falha com "Container killed"**

**Sintomas:**
- Jobs MapReduce falham durante execução
- Logs mostram "Container killed by ResourceManager"

**Causa:**
Geralmente relacionado a limitações de memória.

**Solução:**
```bash
# Verificar configurações de memória
grep -r "yarn.nodemanager.resource.memory-mb" /usr/local/hadoop/etc/hadoop/
grep -r "yarn.scheduler.maximum-allocation-mb" /usr/local/hadoop/etc/hadoop/

# Ajustar configurações se necessário
# Editar yarn-site.xml para aumentar limites de memória
```

### 8.2 Soluções e Workarounds

#### **Otimização de Performance**

**Para jobs pequenos:**
```bash
# Reduzir overhead de inicialização
export HADOOP_OPTS="$HADOOP_OPTS -Djava.net.preferIPv4Stack=true"
export HADOOP_CLIENT_OPTS="$HADOOP_CLIENT_OPTS -Xmx512m"
```

**Para processamento de arquivos pequenos:**
```bash
# Usar CombineFileInputFormat para arquivos pequenos
-D mapreduce.input.fileinputformat.split.maxsize=134217728
```

#### **Monitoramento Avançado**

```bash
# Script de monitoramento contínuo
cat > monitor_hadoop.sh << 'EOF'
#!/bin/bash
while true; do
    echo "=== $(date) ==="
    echo "HDFS Status:"
    /usr/local/hadoop/bin/hdfs dfsadmin -report | grep -E "(Live datanodes|DFS Used|DFS Remaining)"
    echo ""
    echo "YARN Status:"
    /usr/local/hadoop/bin/yarn node -list | grep RUNNING
    echo ""
    echo "Running Applications:"
    /usr/local/hadoop/bin/yarn application -list | grep RUNNING
    echo "========================"
    sleep 30
done
EOF

chmod +x monitor_hadoop.sh
```

### 8.3 Perguntas Frequentes

**Q: Posso executar múltiplos jobs simultaneamente?**
A: Sim, o YARN gerencia recursos automaticamente e pode executar múltiplos jobs em paralelo, dependendo dos recursos disponíveis.

**Q: Como aumentar o número de mappers/reducers?**
A: O número de mappers é determinado pelo tamanho dos dados de entrada e configuração de split. O número de reducers pode ser configurado com `-D mapreduce.job.reduces=N`.

**Q: É possível usar Hadoop com dados em tempo real?**
A: O Hadoop tradicional é otimizado para processamento batch. Para dados em tempo real, considere Apache Storm, Apache Spark Streaming ou Apache Flink.

**Q: Como fazer backup dos dados do HDFS?**
A: Use `hdfs dfs -cp` para cópia dentro do HDFS ou `hdfs dfs -get` para exportar para sistema local. Para clusters de produção, considere DistCp.

**Q: Hadoop funciona bem em máquinas virtuais?**
A: Sim, mas com limitações de performance. Para produção, hardware dedicado é recomendado.

## 9. RECURSOS ADICIONAIS

### 9.1 Documentação Oficial

- **Apache Hadoop**: https://hadoop.apache.org/docs/stable/
- **HDFS Architecture**: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html
- **MapReduce Tutorial**: https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html
- **YARN Architecture**: https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/YARN.html

### 9.2 Tutoriais Complementares

- **Cloudera Tutorials**: https://www.cloudera.com/tutorials.html
- **Hortonworks Sandbox**: https://www.cloudera.com/downloads/hortonworks-sandbox.html
- **Hadoop Ecosystem**: https://data-flair.training/blogs/hadoop-ecosystem-components/

### 9.3 Comunidade e Suporte

- **Stack Overflow**: Tag "hadoop" para perguntas técnicas
- **Apache Hadoop Mailing Lists**: https://hadoop.apache.org/mailing_lists.html
- **Hadoop User Groups**: Grupos locais de usuários Hadoop
- **Conferences**: Strata Data Conference, Hadoop Summit

### 9.4 Ferramentas de Desenvolvimento

- **IDEs Recomendadas**:
  - IntelliJ IDEA com plugin Hadoop
  - Eclipse com plugin Hadoop Development Tools
  - Visual Studio Code com extensões Big Data

- **Ferramentas de Linha de Comando**:
  - `hdfs dfs`: Comandos do sistema de arquivos HDFS
  - `yarn`: Comandos de gerenciamento YARN
  - `mapred`: Comandos específicos do MapReduce

### 9.5 Próximos Passos

Após dominar os conceitos básicos deste laboratório, considere explorar:

1. **Apache Spark**: Framework mais moderno para processamento de Big Data
2. **Apache Hive**: Data warehouse para consultas SQL em dados Hadoop
3. **Apache HBase**: Banco de dados NoSQL para acesso aleatório
4. **Apache Kafka**: Plataforma de streaming para dados em tempo real
5. **Machine Learning**: Integração com TensorFlow, Scikit-learn, MLlib

## 10. REFERÊNCIAS

[1] Teradata. "What are the 5 V's of Big Data?" Acessado em janeiro 2025. https://www.teradata.com/glossary/what-are-the-5-v-s-of-big-data

[2] Twilio. "Understanding the 5 V's of Big Data." Julho 2025. https://www.twilio.com/en-us/resource-center/big-data-characteristics

[3] GeeksforGeeks. "6V's of Big Data." Junho 2025. https://www.geeksforgeeks.org/data-science/5-vs-of-big-data/

[4] Apache Software Foundation. "Apache Hadoop Documentation." https://hadoop.apache.org/docs/stable/

[5] DataCamp. "Big Data Technologies: Tools, Solutions, and Trends for 2025." Agosto 2025. https://www.datacamp.com/blog/big-data-technologies

[6] TechVidvan. "Apache Hadoop Architecture - HDFS, YARN & MapReduce." Abril 2020. https://techvidvan.com/tutorials/hadoop-architecture/

[7] Apache Software Foundation. "HDFS Architecture Guide." https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html

[8] Apache Software Foundation. "MapReduce Tutorial." https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html

[9] Apache Software Foundation. "Apache Hadoop YARN." https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/YARN.html

[10] Data Flair. "Hadoop Ecosystem Components - A Complete Tutorial." https://data-flair.training/blogs/hadoop-ecosystem-components/



