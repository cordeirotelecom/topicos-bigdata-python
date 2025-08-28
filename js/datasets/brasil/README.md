# Datasets do Brasil 🇧🇷

## Datasets Nacionais Atualizados (2024-2025)

### 📊 Dados Governamentais Abertos
- **Portal Brasileiro de Dados Abertos**: https://dados.gov.br/
- **IBGE Dados**: https://dadosabertos.ibge.gov.br/
- **TSE Dados Eleitorais**: https://dadosabertos.tse.jus.br/
- **INEP Educação**: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos
- **SUS DataSUS**: https://datasus.saude.gov.br/
- **ANEEL Energia**: https://dadosabertos.aneel.gov.br/

### 🏙️ Dados de Cidades Brasileiras
- **Censo 2022 IBGE**: Dados populacionais e demográficos atualizados
- **RAIS/CAGED**: Mercado de trabalho e emprego
- **PIB Municipal**: Produto Interno Bruto por município
- **IDH Municipal**: Índice de Desenvolvimento Humano

### 🌊 Dados Ambientais
- **INPE**: Dados de desmatamento, queimadas e clima
- **ANA**: Agência Nacional de Águas e Saneamento
- **IBAMA**: Dados de fiscalização ambiental
- **MapBiomas**: Mapas de cobertura e uso da terra

### 💰 Dados Econômicos
- **Banco Central**: SELIC, inflação, câmbio
- **BNDES**: Financiamentos e investimentos
- **Receita Federal**: Arrecadação tributária
- **MDIC**: Comércio exterior

### 🚗 Dados de Mobilidade e Transporte
- **DENATRAN**: Frota de veículos
- **ANTT**: Transporte terrestre
- **ANTAQ**: Transporte aquaviário
- **ANAC**: Transporte aéreo

### 📱 Dados de Telecomunicações
- **ANATEL**: Telefonia, internet e radiodifusão
- **CETIC.br**: TIC Domicílios, TIC Empresas

## 🔗 APIs Disponíveis

### APIs Governamentais
```python
# Exemplo de uso da API do IBGE
import requests

# PIB Municipal
url = "https://servicodados.ibge.gov.br/api/v1/pesquisas/indicadores/47001/resultados"
response = requests.get(url)
pib_data = response.json()

# População estimada
url = "https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2023/variaveis/9324"
response = requests.get(url)
pop_data = response.json()
```

### APIs Financeiras
```python
# API Banco Central
import requests

# Taxa SELIC
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/30?formato=json"
response = requests.get(url)
selic_data = response.json()

# Câmbio USD/BRL
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos/30?formato=json"
response = requests.get(url)
cambio_data = response.json()
```

## 📈 Casos de Uso com Big Data

### 1. Análise de Polarização Política
- Dados eleitorais TSE 2022
- Análise de redes sociais
- Sentiment analysis de debates

### 2. Monitoramento Ambiental
- Dados INPE de desmatamento
- Análise de queimadas em tempo real
- Predição de eventos climáticos extremos

### 3. Análise Econômica Regional
- PIB municipal vs investimentos
- Correlação emprego e educação
- Fluxos migratórios internos

### 4. Smart Cities
- Dados de mobilidade urbana
- Consumo energético
- Qualidade do ar e poluição

## 🛠️ Ferramentas Recomendadas

```python
# Principais bibliotecas para dados brasileiros
import pandas as pd
import geopandas as gpd
import folium
import plotly.express as px
import requests
import basedosdados as bd  # Base dos Dados (Google)
```

## 📚 Recursos Adicionais

- **Base dos Dados**: https://basedosdados.org/ (BigQuery com dados brasileiros)
- **Brasil.IO**: https://brasil.io/ (Dados públicos brasileiros)
- **SERENATA**: https://serenata.ai/ (IA para transparência)
- **Open Knowledge Brasil**: https://ok.org.br/

## 🔄 Atualização dos Dados

Este documento é atualizado regularmente com novos datasets e APIs. 
Última atualização: Agosto 2025
