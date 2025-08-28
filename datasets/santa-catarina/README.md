# Datasets Santa Catarina 🏖️

## Dados Específicos de Santa Catarina

### 🏛️ Governo do Estado
- **Portal SC Transparente**: https://www.portaltransparencia.sc.gov.br/
- **SEF/SC**: Secretaria de Fazenda - dados tributários
- **EPAGRI**: Dados agropecuários e meteorológicos
- **FATMA/IMA**: Dados ambientais

### 🏙️ Dados Municipais

#### Florianópolis
- **Portal PMF Transparência**: https://transparencia.pmf.sc.gov.br/
- **FloripAmanhã**: Dados de planejamento urbano
- **IPUF**: Instituto de Planejamento Urbano
- **Transporte Público**: Dados do sistema integrado

#### São José
- **Portal Transparência São José**: https://www.saojose.sc.gov.br/transparencia/
- **Dados Demográficos**: IBGE 2022
- **Desenvolvimento Urbano**: Secretaria de Urbanismo

#### Região da Grande Florianópolis
- **SUDERF**: Superintendência de Desenvolvimento da Região Sul
- **GRANFPOLIS**: Associação dos Municípios da Grande Florianópolis

### 📊 Datasets Específicos Disponíveis

#### Economia e Desenvolvimento
```python
# PIB Municipal SC (2022)
municipios_sc_pib = {
    'Florianópolis': 28_500_000_000,  # R$ 28,5 bilhões
    'São José': 8_200_000_000,       # R$ 8,2 bilhões  
    'Joinville': 25_800_000_000,     # R$ 25,8 bilhões
    'Blumenau': 15_600_000_000,      # R$ 15,6 bilhões
    'Chapecó': 8_900_000_000,        # R$ 8,9 bilhões
}

# Setores econômicos SC
setores_sc = {
    'Agronegócio': '12%',
    'Indústria': '28%', 
    'Serviços': '55%',
    'Turismo': '5%'
}
```

#### Demografia Atualizada (Censo 2022)
```python
populacao_sc_2022 = {
    'Florianópolis': 516_524,
    'São José': 254_228,
    'Joinville': 597_658,
    'Blumenau': 366_418,
    'Chapecó': 224_013,
    'Criciúma': 218_173,
    'Itajaí': 223_112,
    'Lages': 157_544
}

# Região da Grande Florianópolis
grande_floripa = {
    'Florianópolis': 516_524,
    'São José': 254_228,
    'São Pedro de Alcântara': 7_751,
    'Palhoça': 176_749,
    'Biguaçu': 70_071,
    'Santo Amaro da Imperatriz': 23_017,
    'Águas Mornas': 6_141,
    'Antônio Carlos': 8_598,
    'Governador Celso Ramos': 14_183
}
```

### 🌊 Dados Ambientais e Geográficos

#### Oceanográficos
- **CTTMar/UNIVALI**: Centro de Ciências do Mar
- **Qualidade da água**: Praias SC
- **Marés e correntes**: Porto de Itajaí/Florianópolis
- **Pesca artesanal**: Dados EPAGRI

#### Meteorológicos
```python
# Estações meteorológicas SC (INMET)
estacoes_sc = [
    {'nome': 'Florianópolis', 'codigo': 'A806', 'lat': -27.5954, 'lon': -48.5480},
    {'nome': 'São José', 'codigo': 'A807', 'lat': -27.5969, 'lon': -48.6394},
    {'nome': 'Joinville', 'codigo': 'A803', 'lat': -26.3044, 'lon': -48.8487},
    {'nome': 'Chapecó', 'codigo': 'A805', 'lat': -27.1004, 'lon': -52.6167}
]

# Dados climáticos médios
clima_floripa = {
    'temperatura_media': 20.3,  # °C
    'precipitacao_anual': 1500,  # mm
    'umidade_relativa': 82,      # %
    'ventos_predominantes': 'NE'
}
```

### 🚌 Mobilidade Urbana

#### Sistema Integrado de Mobilidade (SIM)
```python
# Dados de transporte público Florianópolis
sim_dados = {
    'linhas_onibus': 120,
    'frota_onibus': 450,
    'passageiros_dia': 180_000,
    'integracao_bicicleta': 'Bike Floripa',
    'terminais': 5
}

# Bike Floripa
bike_floripa = {
    'estacoes': 25,
    'bicicletas': 250,
    'viagens_mes': 15_000,
    'usuarios_cadastrados': 8_500
}
```

### 🏫 Educação

#### Universidades e Institutos
- **UFSC**: Universidade Federal de Santa Catarina
- **UDESC**: Universidade do Estado de Santa Catarina  
- **IFSC**: Instituto Federal de Santa Catarina
- **UNISUL**: Universidade do Sul de Santa Catarina

```python
# Dados educacionais SC
educacao_sc = {
    'universidades_publicas': 3,
    'universidades_privadas': 45,
    'estudantes_superior': 285_000,
    'mestrados_doutorados': 125,
    'centros_pesquisa': 180
}
```

### 💻 Setor de TI e Inovação

#### Polos Tecnológicos
- **ACATE**: Associação Catarinense de Tecnologia
- **Porto Digital SC**: Florianópolis
- **Sapiens Parque**: Santo Amaro da Imperatriz
- **ParqTec Alfa**: São José

```python
# Ecossistema de inovação SC
inovacao_sc = {
    'empresas_ti': 3_500,
    'startups': 850,
    'empregos_ti': 45_000,
    'faturamento_anual': '8.2 bilhões',
    'cidades_polo': ['Florianópolis', 'São José', 'Blumenau', 'Joinville']
}
```

### 🏖️ Turismo

#### Dados Turísticos 2024
```python
turismo_sc_2024 = {
    'turistas_ano': 8_500_000,
    'turistas_estrangeiros': 450_000,
    'receita_turismo': '12.8 bilhões',
    'empregos_turismo': 380_000,
    'taxa_ocupacao_verao': 85,
    'destinos_principais': [
        'Florianópolis', 'Balneário Camboriú', 'Bombinhas', 
        'Porto Belo', 'Itapema', 'Penha'
    ]
}

# Eventos importantes
eventos_sc = [
    {'nome': 'Oktoberfest', 'cidade': 'Blumenau', 'visitantes': 600_000},
    {'nome': 'Festival de Inverno', 'cidade': 'Bonito', 'visitantes': 180_000},
    {'nome': 'ANIMA MUNDI', 'cidade': 'Florianópolis', 'visitantes': 75_000}
]
```

## 🔗 APIs e Fontes de Dados

### APIs Locais
```python
# Exemplo: API dados meteorológicos SC
import requests

def get_clima_floripa():
    url = "https://api.inmet.gov.br/estacao/dados/A806"
    response = requests.get(url)
    return response.json()

# Exemplo: API transporte público Florianópolis  
def get_onibus_tempo_real():
    # API do SIM (quando disponível)
    url = "https://api.sim.floripa.sc.gov.br/onibus"
    # Implementação específica
    pass
```

### Dados Geoespaciais
```python
import geopandas as gpd

# Shapefile municípios SC
url_sc = "https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/UFs/SC/"

# Carregar dados geográficos
gdf_sc = gpd.read_file(url_sc + "sc_municipios.shp")

# Filtrar região da Grande Florianópolis
municipios_granfpolis = [
    'Florianópolis', 'São José', 'Palhoça', 'Biguaçu', 
    'São Pedro de Alcântara', 'Santo Amaro da Imperatriz'
]
gdf_granfpolis = gdf_sc[gdf_sc['NM_MUN'].isin(municipios_granfpolis)]
```

## 📈 Projetos de Análise Sugeridos

### 1. Análise do Crescimento Urbano na Grande Florianópolis
- Dados demográficos 2010 vs 2022
- Expansão urbana via imagens de satélite
- Impacto no trânsito e mobilidade

### 2. Monitoramento da Qualidade das Águas
- Balneabilidade das praias SC
- Impacto do turismo na qualidade ambiental
- Análise sazonal (verão vs inverno)

### 3. Ecossistema de Inovação Catarinense
- Mapeamento de startups e empresas de TI
- Análise de investimentos e funding
- Correlação com formação universitária

### 4. Análise do Setor Portuário
- Porto de Itajaí: movimentação de cargas
- Exportações do agronegócio SC
- Impacto econômico regional

## 📱 Dados em Tempo Real

### Monitoramento Ambiental
- **Qualidade do ar**: Estações FATMA/IMA
- **Nível dos rios**: ANA - Agência Nacional de Águas
- **Condições do mar**: Marinha do Brasil

### Trânsito e Mobilidade
- **Trânsito em tempo real**: Google Maps API
- **Condições das rodovias**: DEINFRA/SC
- **Voos**: Aeroporto Hercílio Luz

## 🏗️ Projetos de Smart City

### Florianópolis Digital
- **IoT urbano**: Sensores de qualidade do ar
- **Iluminação inteligente**: LED com sensores
- **Gestão de resíduos**: Coleta otimizada
- **Mobilidade inteligente**: Semáforos adaptativos

Última atualização: Agosto 2025
