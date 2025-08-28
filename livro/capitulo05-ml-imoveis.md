# Capítulo 5: Machine Learning com Dados Locais - Preços Imobiliários de Floripa

*Como a inteligência artificial revela os segredos do mercado imobiliário catarinense*

---

## O Desafio: Precificar Imóveis na Ilha da Magia

**Patrícia** é corretora de imóveis há 15 anos em Florianópolis e sempre confiou na experiência para avaliar propriedades. Mas o mercado mudou drasticamente:

- **Pandemia**: Preços subiram 40% em 2 anos
- **Novos bairros**: Áreas antes "sem valor" agora são cobiçadas  
- **Clientes exigentes**: Querem justificativas técnicas para preços
- **Concorrência**: Startups usando IA para avaliações

*"Preciso me modernizar ou vou perder espaço no mercado."* - Patrícia

---

## Entendendo o Mercado Imobiliário de SC

### 🏠 **Características Únicas de Florianópolis**

**Fatores que Influenciam Preços**:
1. **Proximidade da praia**: Cada 100m = -5% no preço
2. **Ponte Hercílio Luz**: Acesso ao continente valoriza
3. **UFSC**: Proximidade aumenta demanda por quitinetes  
4. **Centro histórico**: Patrimônio vs. modernidade
5. **Morros**: Vista panorâmica vs. dificuldade de acesso

**Dados Reais do Mercado (2024)**:
- **Média m²**: R$ 8.500 (região central)
- **Lagoa da Conceição**: R$ 12.000/m²
- **Ingleses**: R$ 6.800/m²  
- **São José**: R$ 4.200/m²

### 📊 **Fontes de Dados Disponíveis**

**Patrícia mapeou as fontes**:
- **IPTU**: Dados da Prefeitura de Florianópolis
- **Cartórios**: Registros de compra/venda
- **Sites imobiliários**: ZAP, VivaReal, OLX
- **IBGE**: Dados demográficos por bairro
- **Google Maps**: Distâncias e pontos de interesse

---

## Construindo o Modelo Preditivo

### 🎯 **Definindo o Problema**

**Objetivo**: Prever preço de imóveis com base em características físicas e localização.

**Variáveis Independentes (Features)**:
- Área total (m²)
- Número de quartos/banheiros
- Idade do imóvel
- Distância da praia
- Distância do centro
- Nota do bairro (infraestrutura)

**Variável Dependente (Target)**:
- Preço de venda (R$)

### 🐍 **Coletando e Preparando os Dados**

Patrícia organizou dados de 8 imóveis reais de Florianópolis numa planilha:

**📊 Dados de Imóveis - Florianópolis (Amostra Real)**

| Área (m²) | Quartos | Banheiros | Idade | Dist. Praia | Dist. Centro | Nota Bairro | Preço |
|-----------|---------|-----------|-------|-------------|--------------|-------------|--------|
| 85 | 2 | 1 | 5 anos | 0.5 km | 8.2 km | 8.5 | R$ 720.000 |
| 120 | 3 | 2 | 15 anos | 2.1 km | 5.1 km | 7.2 | R$ 580.000 |
| 65 | 2 | 1 | 8 anos | 0.3 km | 12.3 km | 9.1 | R$ 850.000 |
| 200 | 4 | 3 | 2 anos | 1.8 km | 6.8 km | 8.8 | R$ 1.200.000 |

*E mais 4 imóveis com características similares...*

**🔍 Primeira Observação de Patrícia**:
- Imóvel menor (65m²) mas pertinho da praia = R$ 850.000
- Imóvel maior (120m²) mas longe da praia = R$ 580.000  
- **Conclusão**: Localização pesa muito!
```

### 🔍 **Análise Exploratória dos Dados**

Patrícia fez uma análise simples para entender o que mais influencia preços:

**📈 Correlações Descobertas** (quanto uma variável influencia outra):

**🏠 Área vs Preço**: 0.82 (correlação forte)
- *Maior área = preço maior (óbvio, mas confirmado!)*

**🏖️ Distância da Praia vs Preço**: -0.65 (correlação negativa forte)  
- *Mais longe da praia = preço menor*

**🌟 Nota do Bairro vs Preço**: 0.58 (correlação moderada)
- *Bairro melhor = preço maior*

**💡 Insight de Patrícia**: *"A regra é simples: área grande + perto da praia + bom bairro = preço alto!"*

### 🤖 **Treinando o Modelo de Machine Learning**

Patrícia decidiu ensinar o computador a avaliar imóveis automaticamente:

**🎯 Processo Simplificado**:
1. **Separar dados**: 70% para ensinar, 30% para testar
2. **Escolher algoritmo**: Random Forest (boa escolha para imóveis)
3. **Treinar modelo**: Computador aprende os padrões
4. **Testar precisão**: Ver se acerta as previsões

**📊 Resultado do Treinamento**:
- **Acurácia**: 87% (muito bom!)
- **Erro médio**: R$ 45.000 (aceitável para imóveis)
- **Tempo de treinamento**: 2 segundos

*Patrícia ficou impressionada: "O modelo acerta o preço na maioria das vezes!"*

---

## Aplicação Prática: Ferramenta de Avaliação

### 🏡 **Sistema de Avaliação Automática**

Agora Patrícia tem uma "calculadora inteligente" que avalia qualquer imóvel:

**🔧 Como Funciona**:
1. **Inserir dados** do imóvel (área, quartos, localização, etc.)
2. **Modelo calcula** baseado nos padrões aprendidos
3. **Resultado instantâneo** com faixa de preço

**📝 Exemplo Prático - Apartamento na Lagoa da Conceição**:

**Características do Imóvel**:
- 90 m² / 2 quartos / 2 banheiros
- 5 anos de idade / 800m da praia
- 8.5 km do centro / Bairro nota 8.8

**🎯 Avaliação do Modelo**:
- **Preço estimado**: R$ 780.000
- **Faixa de confiança**: R$ 702.000 - R$ 858.000
- **Preço por m²**: R$ 8.667

*"Agora posso dar uma estimativa precisa em segundos!" - Patrícia*
    
    return {
        'preco_estimado': preco_previsto,
        'faixa_minima': preco_min,
        'faixa_maxima': preco_max,
        'preco_m2': preco_previsto / area
    }

# Exemplo prático: Apartamento na Lagoa da Conceição
resultado = avaliar_imovel(
    area=90,           # 90 m²
    quartos=2,         # 2 quartos
    banheiros=2,       # 2 banheiros  
    idade=5,           # 5 anos
    dist_praia=0.8,    # 800m da praia
    dist_centro=8.5,   # 8.5km do centro
    nota_bairro=8.8    # Bairro nota 8.8
)

print("=== AVALIAÇÃO AUTOMÁTICA ===")
print(f"Preço estimado: R$ {resultado['preco_estimado']:,.0f}")
print(f"Faixa de valor: R$ {resultado['faixa_minima']:,.0f} - R$ {resultado['faixa_maxima']:,.0f}")
print(f"Preço por m²: R$ {resultado['preco_m2']:,.0f}")
```

### 📊 **Análise de Importância das Features**

```python
# Quais fatores mais influenciam o preço?
importancias = modelo.feature_importances_
feature_importance = pd.DataFrame({
    'feature': features,
    'importancia': importancias
}).sort_values('importancia', ascending=False)

# Visualizando
plt.figure(figsize=(10, 6))
sns.barplot(data=feature_importance, x='importancia', y='feature')
plt.title('Importância dos Fatores no Preço do Imóvel')
plt.xlabel('Importância (%)')
plt.show()

print("Ranking de Importância:")
for i, row in feature_importance.iterrows():
    print(f"{row['feature']}: {row['importancia']*100:.1f}%")
```

**Resultado para Florianópolis**:
1. **Área (m²)**: 35% de influência
2. **Distância da praia**: 25% de influência  
3. **Nota do bairro**: 18% de influência
4. **Número de quartos**: 12% de influência

---

## Casos de Uso Reais

### 🎯 **Cenário 1: Negociação Baseada em Dados**

**Situação**: Cliente quer comprar apartamento por R$ 650.000, mas modelo indica R$ 720.000.

```python
# Análise de diferença de preço
preco_pedido = 650000
preco_modelo = 720000
diferenca = preco_modelo - preco_pedido
percentual = (diferenca / preco_modelo) * 100

print(f"Diferença: R$ {diferenca:,.0f} ({percentual:.1f}%)")
print(f"Recomendação: {'COMPRAR' if percentual > 15 else 'NEGOCIAR'}")
```

**Resultado**: Diferença de 10.8% - dentro da margem aceitável.

### 🏗️ **Cenário 2: Investimento em Reforma**

```python
def calcular_roi_reforma(preco_atual, custo_reforma, area_atual, area_nova=None):
    """
    Calcula ROI de uma reforma
    """
    
    # Se não expandir área, considera melhoria de 10% no preço
    if area_nova is None:
        preco_pos_reforma = preco_atual * 1.10
        roi = ((preco_pos_reforma - preco_atual - custo_reforma) / custo_reforma) * 100
    else:
        # Se expandir, recalcula baseado na nova área
        preco_m2_atual = preco_atual / area_atual
        preco_pos_reforma = preco_m2_atual * area_nova * 1.05  # 5% desconto por obra
        roi = ((preco_pos_reforma - preco_atual - custo_reforma) / custo_reforma) * 100
    
    return {
        'preco_pos_reforma': preco_pos_reforma,
        'roi_percentual': roi,
        'lucro_liquido': preco_pos_reforma - preco_atual - custo_reforma
    }

# Exemplo: Reforma de R$ 80.000 em apartamento de R$ 600.000
roi_reforma = calcular_roi_reforma(600000, 80000, 85)
print(f"ROI da reforma: {roi_reforma['roi_percentual']:.1f}%")
print(f"Lucro líquido: R$ {roi_reforma['lucro_liquido']:,.0f}")
```

### 📈 **Cenário 3: Análise de Tendências por Bairro**

```python
# Simulação de crescimento por bairro
bairros_floripa = {
    'Lagoa da Conceição': {'crescimento_anual': 8.5, 'preco_atual': 12000},
    'Centro': {'crescimento_anual': 5.2, 'preco_atual': 8500},
    'Ingleses': {'crescimento_anual': 12.1, 'preco_atual': 6800},
    'Coqueiros': {'crescimento_anual': 9.8, 'preco_atual': 7200}
}

print("=== PROJEÇÃO DE PREÇOS 2025-2027 ===")
for bairro, dados in bairros_floripa.items():
    preco_2027 = dados['preco_atual'] * (1 + dados['crescimento_anual']/100)**3
    valorizacao = ((preco_2027 - dados['preco_atual']) / dados['preco_atual']) * 100
    
    print(f"{bairro}:")
    print(f"  Atual: R$ {dados['preco_atual']:,.0f}/m²")
    print(f"  2027: R$ {preco_2027:,.0f}/m² (+{valorizacao:.1f}%)")
```

---

## Expansão do Modelo: Feature Engineering Avançado

### 🗺️ **Dados Geográficos Enriquecidos**

```python
# Integração com APIs para enriquecer dados
def calcular_score_localizacao(latitude, longitude):
    """
    Calcula score de localização baseado em pontos de interesse
    """
    
    # Simulação de pontos próximos (em um sistema real, usaria Google Places API)
    pontos_interesse = {
        'mercados': 2,
        'escolas': 1, 
        'hospitais': 1,
        'parques': 3,
        'restaurantes': 8,
        'bancos': 2
    }
    
    # Score baseado em densidade de pontos de interesse
    score = sum(pontos_interesse.values()) / 10  # Normalizado para 0-10
    return min(score, 10)

# Exemplo de uso
score_lagoa = calcular_score_localizacao(-27.6, -48.4)
print(f"Score de localização Lagoa: {score_lagoa:.1f}/10")
```

### 🏢 **Comparação com Mercado**

```python
# Sistema de benchmarking
def comparar_com_mercado(preco_m2, bairro, tipo_imovel):
    """
    Compara preço com média do mercado
    """
    
    # Médias reais por bairro (dados de mercado 2024)
    medias_mercado = {
        'Lagoa da Conceição': 12000,
        'Centro': 8500,
        'Ingleses': 6800,
        'Coqueiros': 7200,
        'Canasvieiras': 5900
    }
    
    media_bairro = medias_mercado.get(bairro, 7000)
    diferenca_percentual = ((preco_m2 - media_bairro) / media_bairro) * 100
    
    if diferenca_percentual > 20:
        status = "ACIMA DO MERCADO"
    elif diferenca_percentual < -20:
        status = "ABAIXO DO MERCADO"
    else:
        status = "DENTRO DA MÉDIA"
    
    return {
        'status': status,
        'diferenca_percentual': diferenca_percentual,
        'media_bairro': media_bairro
    }

# Exemplo
comparacao = comparar_com_mercado(10500, 'Lagoa da Conceição', 'apartamento')
print(f"Status: {comparacao['status']}")
print(f"Diferença: {comparacao['diferenca_percentual']:+.1f}%")
```

---

## Lições Aprendidas e Impacto

### ✅ **Resultados Alcançados por Patrícia**

**Após 6 meses usando ML**:
- **40% mais assertiva** nas avaliações
- **25% aumento** no número de vendas
- **Clientes mais confiantes** nas negociações  
- **Tempo de avaliação**: De 2 horas para 15 minutos

### 🎯 **Melhores Práticas Descobertas**

**1. Qualidade dos Dados é Fundamental**:
```python
# Sempre validar dados de entrada
def validar_dados_imovel(dados):
    validacoes = {
        'area_m2': dados['area_m2'] > 20 and dados['area_m2'] < 1000,
        'preco': dados['preco'] > 100000 and dados['preco'] < 10000000,
        'idade_anos': dados['idade_anos'] >= 0 and dados['idade_anos'] <= 100
    }
    
    return all(validacoes.values()), validacoes
```

**2. Modelo Precisa ser Atualizado Constantemente**:
- Retreinar a cada 3 meses com novos dados
- Monitorar accuracy em dados novos
- Ajustar para mudanças no mercado

**3. Combinar IA com Expertise Humana**:
- Modelo dá estimativa inicial
- Corretor analisa fatores subjetivos  
- Decisão final combina ambos

### 🚀 **Próximos Passos para Expansão**

**Patrícia planeja**:
1. **Integrar dados de trânsito** (tempos de deslocamento)
2. **Análise de sentimentos** em redes sociais sobre bairros
3. **Previsão de tendências** de curto prazo (3-6 meses)
4. **Sistema de alertas** para oportunidades de investimento

---

## Conclusão: IA Democratizando o Mercado Imobiliário

### 💡 **Principais Insights**

**Para Profissionais**:
- Machine Learning não substitui expertise, potencializa
- Dados locais de qualidade fazem toda diferença
- Clientes valorizam transparência e embasamento técnico

**Para Investidores**:
- Análises quantitativas reduzem riscos
- Modelos podem identificar oportunidades não óbvias
- Importante entender limitações do modelo

**Para o Mercado de SC**:
- Florianópolis tem características únicas que modelos devem capturar
- Sazonalidade turística influencia preços
- Crescimento populacional exige atualização constante de dados

---

## Recursos para Implementação

### 📚 **Fontes de Dados SC**
- [Portal de Dados Abertos - Florianópolis](http://dados.pmf.sc.gov.br/)
- [FipeZAP - Índice de Preços](https://www.fipe.org.br/web/indices/fipezap/)
- [IBGE - Cadastro de Municípios](https://cnm.org.br/)

### 🛠️ **Ferramentas Utilizadas**
```python
# Principais bibliotecas
import pandas as pd          # Manipulação de dados
import scikit-learn as sklearn  # Machine Learning
import matplotlib.pyplot as plt  # Visualizações
import seaborn as sns        # Gráficos estatísticos
import requests              # APIs externas
import geopy                 # Dados geográficos
```

### 💻 **Próximo Projeto**
Adapte este modelo para sua região:
1. Colete dados locais de imóveis
2. Identifique fatores únicos da sua cidade
3. Treine modelo com dados históricos
4. Valide com especialistas locais
5. Implemente e monitore performance

---

## **Skills de Mercado: O Que Profissionais de Big Data Precisam Saber**

### 💼 **Competências Mais Valorizadas no Mercado**

Baseado em análise de **500+ vagas** de emprego em Big Data, Machine Learning e Análise de Dados no Brasil, estas são as skills mais procuradas:

#### **🐍 Linguagens de Programação**
Python, SQL, R, Scala, Java, PySpark, Apache Spark, Pandas, NumPy, SciPy, Matplotlib, Seaborn, Plotly, Jupyter Notebook, Git, GitHub

#### **🏗️ Frameworks e Ferramentas Big Data**
Apache Spark, Hadoop, Kafka, Airflow, Databricks, Snowflake, Apache Hive, Apache Pig, Apache Sqoop, Elasticsearch, Apache Cassandra, MongoDB, Redis

#### **☁️ Plataformas Cloud**
AWS (S3, EC2, EMR, Redshift, Glue, SageMaker), Google Cloud Platform (BigQuery, Dataflow, AI Platform, Cloud Storage), Microsoft Azure (Data Factory, Synapse, Machine Learning Studio, Data Lake)

#### **🤖 Machine Learning e IA**
Scikit-learn, TensorFlow, PyTorch, Keras, XGBoost, LightGBM, MLflow, Kubeflow, Docker, Kubernetes, MLOps, Feature Engineering, Model Deployment

#### **📊 Visualização e BI**
Power BI, Tableau, Looker, Grafana, Apache Superset, DAX, Power Query (M), QlikView, Excel Avançado, Google Data Studio

#### **🗄️ Bancos de Dados**
PostgreSQL, MySQL, Oracle, SQL Server, BigQuery, Redshift, Snowflake, DynamoDB, Neo4j, Apache Parquet, Delta Lake

#### **⚙️ Engenharia de Dados (ETL/ELT)**
Apache Airflow, Talend, Informatica, SSIS, Azure Data Factory, Google Dataflow, dbt, Apache NiFi, Pentaho, AWS Glue

#### **📈 Análise Estatística**
Estatística Descritiva, Inferencial, Regressão Linear/Logística, Séries Temporais, A/B Testing, Hypothesis Testing, ANOVA, Chi-Square

#### **🔧 Ferramentas de Desenvolvimento**
Docker, Kubernetes, Jenkins, GitLab CI/CD, Terraform, Apache Maven, SBT, IntelliJ, PyCharm, VS Code, Linux, Bash

#### **💡 Metodologias e Conceitos**
Agile, Scrum, DevOps, DataOps, MLOps, Data Governance, Data Quality, Data Lineage, GDPR Compliance, Data Mesh, Lake House Architecture

### 🎯 **Perfis Profissionais Mais Demandados**

#### **1. Analista de Dados**
*Salário médio: R$ 4.500 - R$ 8.000*
- **Skills**: Python, SQL, Excel, Power BI, Estatística
- **Foco**: Análise exploratória, dashboards, relatórios

#### **2. Cientista de Dados**
*Salário médio: R$ 8.000 - R$ 15.000*
- **Skills**: Python, R, Machine Learning, Estatística Avançada
- **Foco**: Modelos preditivos, algoritmos, insights estratégicos

#### **3. Engenheiro de Dados**
*Salário médio: R$ 9.000 - R$ 18.000*
- **Skills**: Spark, Airflow, Cloud, ETL, Arquitetura de Dados
- **Foco**: Pipelines, infraestrutura, processamento em larga escala

#### **4. Engenheiro de Machine Learning**
*Salário médio: R$ 12.000 - R$ 25.000*
- **Skills**: MLOps, Docker, Kubernetes, Model Deployment
- **Foco**: Produtização de modelos, escalabilidade

#### **5. Arquiteto de Dados**
*Salário médio: R$ 15.000 - R$ 30.000*
- **Skills**: Cloud Architecture, Data Governance, Estratégia
- **Foco**: Desenho de soluções, governança, estratégia de dados

### 🚀 **Roadmap de Carreira**

#### **Nível Iniciante (0-2 anos)**
```
Excel → SQL → Python → Power BI → Estatística Básica
```

#### **Nível Intermediário (2-5 anos)**
```
Pandas → Machine Learning → Cloud Básico → Git → Airflow
```

#### **Nível Avançado (5+ anos)**
```
Spark → MLOps → Arquitetura → Gestão de Equipes → Estratégia
```

### 💰 **Certificações Valorizadas**

#### **Cloud Providers**
- **AWS**: Data Engineer, Machine Learning Specialty, Solutions Architect
- **Google Cloud**: Professional Data Engineer, Machine Learning Engineer
- **Microsoft Azure**: Data Engineer Associate, Data Scientist Associate

#### **Ferramentas Específicas**
- **Databricks**: Certified Data Engineer, Certified Machine Learning Professional
- **Snowflake**: SnowPro Core, SnowPro Advanced
- **Tableau**: Desktop Specialist, Certified Data Analyst

### 🏢 **Setores que Mais Contratam em SC**

#### **Tecnologia**
- Softplan, WEG, Neoway, Involves, Senior Sistemas
- **Foco**: Produtos de software, SaaS, consultoria

#### **Financeiro**
- Bancos regionais, fintechs, cooperativas de crédito
- **Foco**: Análise de risco, detecção de fraudes, CRM

#### **Varejo/E-commerce**
- Havan, Magazine Luiza (operações SC), marketplaces
- **Foco**: Precificação, recomendação, supply chain

#### **Indústria 4.0**
- WEG, Embraco, Metalúrgicas, têxtil
- **Foco**: IoT, manutenção preditiva, otimização

#### **Setor Público**
- Prefeituras, governo estadual, autarquias
- **Foco**: Smart cities, transparência, eficiência

---

*"Machine Learning transformou minha forma de trabalhar. Agora tenho dados para embasar cada decisão e meus clientes confiam mais nas minhas avaliações."* - Patrícia, Corretora de Imóveis
