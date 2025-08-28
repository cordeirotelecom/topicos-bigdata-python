# 📊 Datasets Públicos para Big Data - Lista Completa

## **🏢 Datasets Corporativos e E-commerce**

### **Amazon Product Reviews**
**Descrição:** Milhões de reviews de produtos da Amazon  
**Volume:** 233+ milhões de reviews  
**Formato:** JSON, CSV  
**URL:** https://nijianmo.github.io/amazon/index.html  
**Casos de Uso:** NLP, sistemas de recomendação, análise de sentimento  

**Exemplo de Estrutura:**
```json
{
  "reviewerID": "A2SUAM1J3GNN3B",
  "asin": "0000013714",
  "reviewerName": "J. McDonald",
  "helpful": [2, 3],
  "reviewText": "I bought this for my husband...",
  "overall": 5.0,
  "summary": "Great product!",
  "unixReviewTime": 1362096000,
  "reviewTime": "03 1, 2013"
}
```

---

### **Instacart Market Basket Analysis**
**Descrição:** 3+ milhões de pedidos de grocery do Instacart  
**Volume:** 32+ milhões de produtos em carrinho  
**Formato:** CSV  
**URL:** https://www.kaggle.com/c/instacart-market-basket-analysis  
**Casos de Uso:** Análise de cesta de compras, recomendações  

**Tabelas:**
- orders.csv (3.4M orders)
- order_products.csv (32M order-product relationships)
- products.csv (49K products)
- departments.csv, aisles.csv

---

### **Walmart Sales Forecasting**
**Descrição:** Dados de vendas históricas de 45 lojas Walmart  
**Volume:** 421,570 registros  
**Formato:** CSV  
**URL:** https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting  
**Casos de Uso:** Previsão de demanda, time series analysis  

---

## **🚗 Transporte e Mobilidade**

### **NYC Taxi Trip Data**
**Descrição:** Dados de viagens de táxi em Nova York  
**Volume:** 1+ bilhão de viagens (2009-presente)  
**Formato:** CSV, Parquet  
**URL:** https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page  
**Casos de Uso:** Análise de mobilidade urbana, otimização de rotas  

**Exemplo de Schema:**
```
VendorID, tpep_pickup_datetime, tpep_dropoff_datetime,
passenger_count, trip_distance, pickup_longitude,
pickup_latitude, dropoff_longitude, dropoff_latitude,
payment_type, fare_amount, tip_amount, total_amount
```

---

### **Uber Movement Data**
**Descrição:** Dados de movimento agregados do Uber  
**Volume:** Milhões de viagens anonimizadas  
**Formato:** CSV, JSON  
**URL:** https://movement.uber.com/  
**Casos de Uso:** Planejamento urbano, análise de tráfego  

---

### **Citibike Trip Data**
**Descrição:** Sistema de bike sharing de NYC  
**Volume:** 200+ milhões de viagens  
**Formato:** CSV  
**URL:** https://www.citibikenyc.com/system-data  
**Casos de Uso:** Mobilidade sustentável, otimização de estações  

---

## **💰 Dados Financeiros**

### **Stock Market Data**
**Descrição:** Preços históricos de ações  
**Volume:** Décadas de dados de milhares de ações  
**Formato:** CSV, API  
**URL:** https://finance.yahoo.com/, https://www.quandl.com/  
**Casos de Uso:** Trading algorítmico, análise de risco  

**APIs Gratuitas:**
- Alpha Vantage: https://www.alphavantage.co/
- Yahoo Finance API: https://pypi.org/project/yfinance/
- Quandl: https://www.quandl.com/

**Exemplo Python:**
```python
import yfinance as yf
import pandas as pd

# Download dados históricos
ticker = yf.Ticker("AAPL")
data = ticker.history(period="10y")
print(data.head())
```

---

### **Bitcoin Blockchain Data**
**Descrição:** Todas as transações Bitcoin  
**Volume:** 700+ GB de dados  
**Formato:** JSON, SQL dumps  
**URL:** https://www.blockchain.com/api, https://gz.blockchair.com/  
**Casos de Uso:** Análise de redes, detecção de fraudes  

---

### **Credit Card Fraud Detection**
**Descrição:** Transações de cartão de crédito com labels de fraude  
**Volume:** 284,807 transações  
**Formato:** CSV  
**URL:** https://www.kaggle.com/mlg-ulb/creditcardfraud  
**Casos de Uso:** Machine learning para detecção de fraudes  

---

## **🏥 Saúde e Medicina**

### **COVID-19 Data**
**Descrição:** Dados globais da pandemia COVID-19  
**Volume:** Dados diários desde janeiro 2020  
**Formato:** CSV, JSON  
**URL:** https://github.com/CSSEGISandData/COVID-19  
**Casos de Uso:** Epidemiologia, modelagem de surtos  

**Estrutura:**
- Casos confirmados por país/região
- Mortes por país/região
- Recuperados por país/região
- Dados temporais e geográficos

---

### **MIMIC-III Critical Care Database**
**Descrição:** Dados de pacientes em UTI  
**Volume:** 40,000+ pacientes críticos  
**Formato:** SQL, CSV  
**URL:** https://mimic.mit.edu/  
**Casos de Uso:** Análise clínica, ML em saúde  
**Nota:** Requer certificação para acesso

---

### **FDA Drug Recalls**
**Descrição:** Recalls de medicamentos pela FDA  
**Volume:** 10,000+ recalls  
**Formato:** JSON, XML  
**URL:** https://open.fda.gov/  
**Casos de Uso:** Farmacovigilância, análise regulatória  

---

## **🌍 Dados Ambientais e Climáticos**

### **NOAA Climate Data**
**Descrição:** Dados climáticos históricos globais  
**Volume:** Séculos de dados meteorológicos  
**Formato:** NetCDF, CSV, XML  
**URL:** https://www.ncdc.noaa.gov/data-access  
**Casos de Uso:** Modelagem climática, agricultura  

**Tipos de Dados:**
- Temperatura global
- Precipitação
- Velocidade do vento
- Pressão atmosférica
- Dados de satélite

---

### **NASA Earth Data**
**Descrição:** Dados de observação da Terra  
**Volume:** Petabytes de dados satelitais  
**Formato:** HDF, NetCDF, GeoTIFF  
**URL:** https://earthdata.nasa.gov/  
**Casos de Uso:** Mudanças climáticas, monitoramento ambiental  

---

### **Global Power Plant Database**
**Descrição:** Usinas de energia globais  
**Volume:** 35,000+ usinas  
**Formato:** CSV  
**URL:** https://datasets.wri.org/dataset/globalpowerplantdatabase  
**Casos de Uso:** Análise energética, sustentabilidade  

---

## **📱 Redes Sociais e Web**

### **Twitter API**
**Descrição:** Tweets em tempo real e históricos  
**Volume:** 500+ milhões de tweets/dia  
**Formato:** JSON  
**URL:** https://developer.twitter.com/en/docs/twitter-api  
**Casos de Uso:** Análise de sentimento, trending topics  

**Exemplo de Coleta:**
```python
import tweepy
import pandas as pd

# Configuração da API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Coleta de tweets
tweets = tweepy.Cursor(api.search_tweets, q="#bigdata", lang="en").items(1000)
tweet_data = [[tweet.created_at, tweet.text, tweet.user.screen_name] for tweet in tweets]
df = pd.DataFrame(tweet_data, columns=['Date', 'Text', 'User'])
```

---

### **Reddit Comments Dataset**
**Descrição:** Comentários históricos do Reddit  
**Volume:** 1.7+ bilhões de comentários  
**Formato:** JSON, BigQuery  
**URL:** https://www.reddit.com/r/datasets/  
**Casos de Uso:** NLP, análise de comunidades  

---

### **Wikipedia Page Views**
**Descrição:** Visualizações de páginas da Wikipedia  
**Volume:** Trilhões de page views  
**Formato:** Gzip, Parquet  
**URL:** https://dumps.wikimedia.org/other/pageviews/  
**Casos de Uso:** Análise de interesse público, trending  

---

## **🎵 Mídia e Entretenimento**

### **Spotify Music Data**
**Descrição:** Características de milhões de músicas  
**Volume:** 1.2+ milhão de faixas  
**Formato:** CSV  
**URL:** https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-600k-tracks  
**Casos de Uso:** Sistemas de recomendação musical  

**Features:**
- acousticness, danceability, energy
- instrumentalness, liveness, loudness
- speechiness, tempo, valence

---

### **MovieLens Dataset**
**Descrição:** Ratings de filmes por usuários  
**Volume:** 27+ milhões de ratings  
**Formato:** CSV  
**URL:** https://grouplens.org/datasets/movielens/  
**Casos de Uso:** Sistemas de recomendação, filtros colaborativos  

**Tamanhos Disponíveis:**
- MovieLens 100K (100,000 ratings)
- MovieLens 1M (1 million ratings)
- MovieLens 10M (10 million ratings)
- MovieLens 25M (25 million ratings)

---

### **YouTube Trending Videos**
**Descrição:** Vídeos em trending do YouTube  
**Volume:** 200,000+ vídeos  
**Formato:** CSV  
**URL:** https://www.kaggle.com/datasnaek/youtube-new  
**Casos de Uso:** Análise de viral content, predição de tendências  

---

## **🏛️ Dados Governamentais**

### **US Government Open Data**
**Descrição:** Dados abertos do governo americano  
**Volume:** 300,000+ datasets  
**Formato:** CSV, JSON, XML, API  
**URL:** https://www.data.gov/  
**Casos de Uso:** Análise de políticas públicas, transparência  

**Categorias:**
- Agriculture, Climate, Consumer, Ecosystems
- Education, Energy, Finance, Health
- Manufacturing, Science & Research

---

### **UK Government Data**
**Descrição:** Dados abertos do governo britânico  
**Volume:** 50,000+ datasets  
**Formato:** CSV, JSON, XML  
**URL:** https://data.gov.uk/  
**Casos de Uso:** Análise comparativa internacional  

---

### **World Bank Open Data**
**Descrição:** Indicadores de desenvolvimento mundial  
**Volume:** 1,400+ indicadores para 217 economias  
**Formato:** CSV, XML, JSON, API  
**URL:** https://data.worldbank.org/  
**Casos de Uso:** Análise macroeconômica, desenvolvimento  

**Exemplo de Acesso:**
```python
import wbdata
import pandas as pd

# Indicadores disponíveis
indicators = wbdata.get_indicators()

# Dados específicos
data = wbdata.get_dataframe({
    "SP.POP.TOTL": "Population",
    "NY.GDP.MKTP.CD": "GDP"
}, country="all", date="2020")
```

---

## **🏃‍♂️ Esportes e Fitness**

### **Sports Statistics**
**Descrição:** Estatísticas esportivas históricas  
**Volume:** Décadas de dados esportivos  
**Formato:** CSV, JSON, API  
**URL:** https://www.sports-reference.com/  
**Casos de Uso:** Analytics esportivos, predição de resultados  

**APIs Populares:**
- ESPN API
- The Sports DB
- Football-Data.org
- NBA Stats API

---

### **Strava Activity Data**
**Descrição:** Dados de atividades físicas  
**Volume:** Bilhões de atividades  
**Formato:** JSON via API  
**URL:** https://developers.strava.com/  
**Casos de Uso:** Análise de fitness, padrões de exercício  

---

## **🚀 Como Usar os Datasets**

### **1. Downloading Large Datasets**
```python
import requests
import pandas as pd
from tqdm import tqdm

def download_large_file(url, filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(filename, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as pbar:
        for chunk in response.iter_content(chunk_size=8192):
            size = file.write(chunk)
            pbar.update(size)

# Uso
url = "https://example.com/large_dataset.csv"
download_large_file(url, "dataset.csv")
```

### **2. Efficient Data Loading**
```python
# Para CSVs grandes
df = pd.read_csv('large_dataset.csv', 
                 chunksize=10000,  # Processa em chunks
                 dtype={'column': 'category'},  # Otimiza tipos
                 parse_dates=['date_column'])

# Para Parquet (mais eficiente)
import pyarrow.parquet as pq
df = pq.read_table('dataset.parquet').to_pandas()
```

### **3. Sampling for Development**
```python
# Sample aleatório para desenvolvimento
df_sample = df.sample(n=10000, random_state=42)

# Sample estratificado
from sklearn.model_selection import train_test_split
df_sample = df.groupby('category').apply(
    lambda x: x.sample(min(len(x), 1000))
).reset_index(drop=True)
```

---

## **📁 Datasets por Nível de Dificuldade**

### **🟢 Iniciante (< 1GB)**
- Titanic Dataset (Kaggle)
- Iris Dataset
- Boston Housing Dataset
- Wine Quality Dataset

### **🟡 Intermediário (1-10GB)**
- NYC Taxi Data (1 ano)
- Amazon Reviews (categoria específica)
- MovieLens 25M
- Spotify Dataset

### **🔴 Avançado (>10GB)**
- Full NYC Taxi Data
- Complete Amazon Reviews
- Google Books N-grams
- Common Crawl Web Data

---

## **🔧 Ferramentas para Gerenciar Datasets**

### **DVC (Data Version Control)**
```bash
# Instalação
pip install dvc

# Adicionar dataset
dvc add large_dataset.csv
git add large_dataset.csv.dv .gitignore
git commit -m "Add dataset"

# Push para storage remoto
dvc push
```

### **Kaggle API**
```bash
# Instalação
pip install kaggle

# Download de dataset
kaggle datasets download -d owner/dataset-name

# Upload de dataset
kaggle datasets create -p /path/to/dataset
```

### **AWS S3 para Datasets**
```python
import boto3

s3 = boto3.client('s3')

# Upload
s3.upload_file('local_dataset.csv', 'my-bucket', 'datasets/dataset.csv')

# Download
s3.download_file('my-bucket', 'datasets/dataset.csv', 'local_dataset.csv')
```

---

## **📊 Templates de Análise**

### **Template EDA**
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def basic_eda(df):
    print("=== DATASET OVERVIEW ===")
    print(f"Shape: {df.shape}")
    print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    print("\n=== DATA TYPES ===")
    print(df.dtypes.value_counts())
    
    print("\n=== MISSING VALUES ===")
    missing = df.isnull().sum()
    print(missing[missing > 0])
    
    print("\n=== NUMERICAL SUMMARY ===")
    print(df.describe())
    
    # Visualizations
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Missing values heatmap
    sns.heatmap(df.isnull(), ax=axes[0,0])
    axes[0,0].set_title('Missing Values Pattern')
    
    # Correlation matrix
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 1:
        sns.heatmap(df[numeric_cols].corr(), annot=True, ax=axes[0,1])
        axes[0,1].set_title('Correlation Matrix')
    
    plt.tight_layout()
    plt.show()

# Uso
df = pd.read_csv('your_dataset.csv')
basic_eda(df)
```

---

*Esta lista é atualizada regularmente. Sempre verifique os termos de uso dos datasets antes de utilizá-los em projetos comerciais.*
