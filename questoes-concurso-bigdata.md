# Questões de Concurso Público - Big Data

> **Banco de questões sobre Big Data para concursos públicos brasileiros**  
> Elaborado para: BigData Analytics Pro - Santa Catarina  
> Data: 29 de setembro de 2025

---

## **QUESTÃO 1** 📊

**Sobre os "3 Vs" tradicionais do Big Data, analise as afirmativas:**

**I.** Volume refere-se à quantidade massiva de dados gerados diariamente  
**II.** Velocidade representa a rapidez com que os dados são processados e analisados  
**III.** Variedade indica os diferentes tipos e formatos de dados  
**IV.** Veracidade é um dos 3 Vs originais do Big Data  

**Alternativas:**
- A) Apenas I e II estão corretas
- B) Apenas I, II e III estão corretas  
- C) Apenas II, III e IV estão corretas
- D) Todas as afirmativas estão corretas
- E) Apenas I e IV estão corretas

---

### **RESPOSTA: B**

**Explicação:** Os 3 Vs tradicionais do Big Data são:
- **Volume**: Grande quantidade de dados
- **Velocidade**: Rapidez no processamento
- **Variedade**: Diferentes tipos de dados (estruturados, semi-estruturados, não-estruturados)

A **Veracidade** foi adicionada posteriormente como o 4º V, não sendo um dos 3 Vs originais.

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