# Datasets Específicos de Santa Catarina - 2025

## Panorama Geral de Santa Catarina

### Características Demográficas e Econômicas
- **População**: ~7,6 milhões de habitantes (2022)
- **PIB**: 8° maior do Brasil (R$ 349 bilhões - 2022)
- **IDH**: 0,792 (3° melhor do Brasil)
- **Área**: 95.346 km²
- **Municípios**: 295

## Governo do Estado de Santa Catarina

### Portal de Dados Abertos SC
**URL:** https://dados.sc.gov.br/
**Responsável:** Secretaria de Estado da Administração

#### 1. Secretaria de Estado da Fazenda (SEF/SC)

##### Arrecadação Tributária
```
Dataset: Arrecadação ICMS por Município e Setor
Período: 2015-2024
Frequência: Mensal
Formato: CSV, API REST
Variáveis:
- Município
- Setor econômico (CNAE)
- Valor arrecadado
- Número de contribuintes
- Base de cálculo
```

##### Empresas e Atividade Econômica
```
Dataset: Cadastro Estadual de Contribuintes
Período: Atual (atualização contínua)
Formato: CSV, JSON
Variáveis:
- Inscrição Estadual
- CNPJ
- Razão Social
- Município
- Atividade Principal (CNAE)
- Situação Cadastral
- Porte da Empresa
```

#### 2. Secretaria de Estado da Saúde (SES/SC)

##### Sistema Único de Saúde SC
```
Dataset: Estabelecimentos de Saúde SC
Período: Atualização mensal
Formato: CSV, GeoJSON
Variáveis:
- Código CNES
- Nome do estabelecimento
- Tipo de estabelecimento
- Município
- Coordenadas geográficas
- Serviços oferecidos
- Leitos disponíveis
```

##### Indicadores de Saúde Materno-Infantil
```
Dataset: Nascimentos e Mortalidade Infantil SC
Período: 2010-2023
Frequência: Anual
Formato: CSV
Variáveis:
- Município
- Nascidos vivos
- Óbitos infantis
- Peso ao nascer
- Idade da mãe
- Escolaridade da mãe
- Consultas pré-natal
```

#### 3. Secretaria de Estado da Educação (SED/SC)

##### Rede Estadual de Ensino
```
Dataset: Escolas da Rede Estadual SC
Período: Atualização anual
Formato: CSV, GeoJSON
Variáveis:
- Código da escola
- Nome da escola
- Município
- Modalidades oferecidas
- Número de alunos
- Infraestrutura
- Coordenadas geográficas
```

##### Resultados Educacionais
```
Dataset: IDEB Santa Catarina
Período: 2007-2021
Frequência: Bienal
Formato: CSV
Variáveis:
- Município
- Rede de ensino
- Anos iniciais/finais
- Nota IDEB
- Meta projetada
- Aprovação
- Nota SAEB
```

#### 4. Secretaria de Estado da Segurança Pública (SSP/SC)

##### Criminalidade por Município
```
Dataset: Ocorrências Criminais SC
Período: 2018-2024
Frequência: Mensal
Formato: CSV
Variáveis:
- Município
- Tipo de crime
- Número de ocorrências
- Bairro (quando disponível)
- Período do dia
- Mês/ano
```

##### Efetivo Policial
```
Dataset: Distribuição do Efetivo Policial SC
Período: Anual
Formato: CSV
Variáveis:
- Município
- Batalhão/Companhia
- Número de policiais militares
- Número de policiais civis
- População atendida
- Área de cobertura
```

## Dados Setoriais Específicos

### 5. Empresa de Pesquisa Agropecuária (EPAGRI)

#### Agropecuária Catarinense
```
Dataset: Produção Agrícola SC por Município
Período: 2010-2023
Frequência: Anual (safra)
Formato: CSV
Variáveis:
- Município
- Produto agrícola
- Área plantada (hectares)
- Produção (toneladas)
- Produtividade (kg/ha)
- Valor da produção (R$)
```

#### Meteorologia Agrícola
```
Dataset: Dados Meteorológicos EPAGRI
Período: 1980-2024
Frequência: Diária
Formato: CSV, API
Variáveis:
- Estação meteorológica
- Município
- Temperatura (máx/mín/média)
- Precipitação
- Umidade relativa
- Vento
- Evapotranspiração
```

### 6. Santa Catarina Turismo (SANTUR)

#### Movimento Turístico
```
Dataset: Demanda Turística SC
Período: 2015-2024
Frequência: Mensal
Formato: CSV
Variáveis:
- Região turística
- Município
- Ocupação hoteleira (%)
- Permanência média
- Taxa média diária
- País/estado de origem
- Meio de transporte
```

#### Eventos e Festivais
```
Dataset: Agenda de Eventos SC
Período: 2020-2024
Formato: CSV, JSON
Variáveis:
- Nome do evento
- Município
- Data de realização
- Tipo de evento
- Público estimado
- Receita gerada
- Apoio governamental
```

### 7. Companhia Catarinense de Águas e Saneamento (CASAN)

#### Saneamento Básico
```
Dataset: Cobertura de Saneamento SC
Período: 2015-2024
Frequência: Anual
Formato: CSV
Variáveis:
- Município
- População atendida (água)
- População atendida (esgoto)
- Volume produzido água
- Volume tratado esgoto
- Perdas no sistema (%)
- Qualidade da água
```

### 8. Centrais Elétricas de Santa Catarina (CELESC)

#### Energia Elétrica
```
Dataset: Consumo de Energia SC
Período: 2010-2024
Frequência: Mensal
Formato: CSV
Variáveis:
- Município
- Classe de consumo
- Consumo (MWh)
- Número de consumidores
- Tarifa média
- Unidades geradoras
```

## Universidades e Pesquisa

### 9. Universidade Federal de Santa Catarina (UFSC)

#### Dados Acadêmicos
```
Dataset: Graduação UFSC
Período: 2010-2024
Frequência: Semestral
Formato: CSV
Variáveis:
- Curso
- Campus
- Matrículas
- Ingressantes
- Formandos
- Taxa de evasão
- Nota do curso (ENADE)
```

#### Pesquisa e Inovação
```
Dataset: Produção Científica UFSC
Período: 2015-2024
Formato: CSV, API
Variáveis:
- Departamento
- Área do conhecimento
- Publicações científicas
- Patentes
- Projetos de pesquisa
- Recursos captados
```

### 10. Universidade do Estado de Santa Catarina (UDESC)

#### Indicadores Institucionais
```
Dataset: Dados Acadêmicos UDESC
Período: 2010-2024
Formato: CSV
Variáveis:
- Centro de ensino
- Curso
- Modalidade
- Matrículas ativas
- Taxa de conclusão
- Programas de pós-graduação
```

### 11. Fundação de Amparo à Pesquisa de SC (FAPESC)

#### Investimento em Pesquisa
```
Dataset: Projetos Financiados FAPESC
Período: 2008-2024
Formato: CSV
Variáveis:
- Título do projeto
- Área do conhecimento
- Instituição executora
- Valor aprovado
- Duração
- Pesquisador responsável
- Resultados obtidos
```

## Dados Ambientais

### 12. Instituto do Meio Ambiente de SC (IMA)

#### Licenciamento Ambiental
```
Dataset: Licenças Ambientais SC
Período: 2015-2024
Formato: CSV, GeoJSON
Variáveis:
- Empresa/empreendimento
- Município
- Tipo de licença
- Atividade licenciada
- Data de emissão
- Validade
- Coordenadas
```

#### Qualidade Ambiental
```
Dataset: Monitoramento Ambiental SC
Período: 2018-2024
Frequência: Contínua
Formato: CSV, API
Variáveis:
- Estação de monitoramento
- Município
- Parâmetro (ar, água, solo)
- Valor medido
- Data/hora
- Padrão de qualidade
```

### 13. Fundação do Meio Ambiente (FATMA) - Dados Históricos

#### Áreas Contaminadas
```
Dataset: Cadastro de Áreas Contaminadas SC
Período: 2005-2024
Formato: CSV, Shapefile
Variáveis:
- Identificação da área
- Município
- Fonte de contaminação
- Contaminantes identificados
- Fase do gerenciamento
- Coordenadas geográficas
```

## Transportes e Logística

### 14. Departamento Estadual de Infraestrutura (DEINFRA)

#### Infraestrutura Rodoviária
```
Dataset: Malha Rodoviária SC
Período: Atualização contínua
Formato: Shapefile, GeoJSON
Variáveis:
- Rodovia
- Extensão
- Tipo de pavimento
- Estado de conservação
- Tráfego médio diário
- Acidentes
```

### 15. Agência Nacional de Transportes Terrestres (ANTT) - Dados SC

#### Transporte de Cargas
```
Dataset: Movimento de Cargas SC
Período: 2018-2024
Frequência: Mensal
Formato: CSV
Variáveis:
- Origem/destino
- Produto transportado
- Toneladas transportadas
- Modal utilizado
- Distância
- Valor do frete
```

## Dados Econômicos Municipais

### 16. Instituto Brasileiro de Geografia e Estatística (IBGE) - Recorte SC

#### PIB Municipal
```
Dataset: PIB Municípios SC
Período: 2010-2021
Frequência: Anual
Formato: CSV
Variáveis:
- Município
- PIB total
- PIB per capita
- Valor Adicionado por setor
- Impostos sobre produtos
- População
```

#### Pesquisa Anual de Serviços (PAS)
```
Dataset: Setor de Serviços SC
Período: 2010-2020
Formato: CSV
Variáveis:
- Município
- Número de empresas
- Pessoal ocupado
- Salários e retiradas
- Receita operacional líquida
- Segmento de serviços
```

## Dados de Inovação e Tecnologia

### 17. Associação Catarinense de Tecnologia (ACATE)

#### Setor de TI em SC
```
Dataset: Empresas de Tecnologia SC
Período: 2018-2024
Formato: CSV
Variáveis:
- Empresa
- Município
- Setor de atuação
- Número de funcionários
- Faturamento
- Ano de fundação
- Investimentos recebidos
```

### 18. Federação das Indústrias de SC (FIESC)

#### Indústria Catarinense
```
Dataset: Indicadores Industriais SC
Período: 2015-2024
Frequência: Mensal
Formato: CSV
Variáveis:
- Município
- Setor industrial
- Produção física
- Faturamento
- Emprego industrial
- Exportações
- Investimentos
```

## Dados de Cooperativismo

### 19. Organização das Cooperativas de SC (OCESC)

#### Cooperativismo Catarinense
```
Dataset: Cooperativas SC
Período: 2015-2024
Formato: CSV
Variáveis:
- Nome da cooperativa
- Município sede
- Ramo de atividade
- Número de cooperados
- Faturamento anual
- Patrimônio líquido
- Empregos gerados
```

## Ferramentas e APIs

### Como Acessar os Dados

#### Portal Oficial
- **URL Principal**: https://dados.sc.gov.br/
- **Formato**: CSV, JSON, XML, API REST
- **Documentação**: Disponível para cada dataset
- **Atualizações**: Varia por fonte (diária a anual)

#### APIs Disponíveis
```python
# Exemplo de acesso via API
import requests
import pandas as pd

# API de dados de saúde SC
url = "https://dados.sc.gov.br/api/saude/estabelecimentos"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)
```

#### Ferramentas Recomendadas
- **Python**: pandas, geopandas, requests
- **R**: readr, httr, sf
- **QGIS**: Para dados geoespaciais
- **Tableau/Power BI**: Visualização

### Considerações Técnicas

#### Qualidade dos Dados
- **Metadados**: Sempre consultar documentação
- **Periodicidade**: Verificar frequência de atualização
- **Completude**: Alguns municípios podem ter dados faltantes
- **Consistência**: Validar dados entre diferentes fontes

#### Aspectos Legais
- **Lei de Acesso à Informação**
- **LGPD**: Dados pessoais são anonimizados
- **Licenças**: Creative Commons para maioria dos datasets
- **Citação**: Sempre citar a fonte original

### Próximos Desenvolvimentos
- **Integração de dados**: Plataforma unificada em desenvolvimento
- **Dados em tempo real**: Mais APIs para dados dinâmicos
- **Geolocalização**: Expansão de dados georreferenciados
- **Machine Learning**: Modelos preditivos baseados em dados públicos

---

*Compilado por: Prof. Vagner Cordeiro*  
*Disciplina: Tópicos de Big Data em Python*  
*Última atualização: Agosto 2025*
