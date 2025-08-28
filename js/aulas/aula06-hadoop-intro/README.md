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

## 🎯 Próxima Aula
Aula 07 - Apache Spark Fundamentals
