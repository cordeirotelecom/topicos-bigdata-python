# 📊 Power BI para Big Data Analytics - Tutorial Completo

## **Visão Geral**

Este tutorial apresenta como usar o Microsoft Power BI para análise de Big Data, incluindo conexões com fontes de dados distribuídas, modelagem avançada e criação de dashboards profissionais.

---

## **📋 Pré-requisitos**

### **Software Necessário:**
- Power BI Desktop (versão mais recente)
- Python 3.8+ (para scripts customizados)
- Driver ODBC para Spark/Hadoop
- Conta Microsoft (para Power BI Service)

### **Conhecimentos Recomendados:**
- Conceitos básicos de BI
- SQL básico
- Noções de modelagem de dados

---

## **🚀 Parte 1: Instalação e Configuração**

### **1.1 Instalação do Power BI Desktop**

```powershell
# Download via Microsoft Store ou site oficial
# Alternativamente, via Chocolatey:
choco install powerbi

# Verificar instalação
Get-AppxPackage *PowerBI*
```

### **1.2 Configuração para Big Data**

#### **Configurar Driver Spark/Hadoop:**
```bash
# Download Spark ODBC Driver
# Simba Spark ODBC Driver
# URL: https://www.simba.com/drivers/spark-odbc-jdbc/

# Configurar string de conexão
# Server: your-spark-cluster.com
# Port: 10000
# Database: default
# Authentication: Username/Password
```

#### **Configurar Python Integration:**
```python
# Instalar bibliotecas necessárias
pip install pandas numpy matplotlib seaborn plotly

# Configurar Power BI para usar Python
# File > Options > Python scripting
# Set Python installation path
```

---

## **🔌 Parte 2: Conexões com Fontes Big Data**

### **2.1 Conectar ao Apache Spark**

**Passo a Passo:**

1. **Abrir Power BI Desktop**
2. **Get Data > More > Other > Spark**
3. **Configurar conexão:**
   ```
   Server: spark-cluster.example.com
   Port: 10000
   Protocol: HTTP
   Database: warehouse
   ```

**Script de Conexão Avançada:**
```powerquery
let
    Source = Spark.Tables("spark-cluster.example.com", [
        Protocol = "HTTP",
        Port = 10000,
        Database = "warehouse",
        CommandTimeout = #duration(0, 0, 5, 0)
    ]),
    Table = Source{[Schema="default",Item="sales_data"]}[Data]
in
    Table
```

### **2.2 Conectar ao Hadoop HDFS**

**Método 1: Via Gateway**
```powerquery
let
    Source = Hdfs.Contents("hdfs://namenode:9000/data/"),
    Navigation = Source{[Name="sales"]}[Content],
    #"Imported CSV" = Csv.Document(Navigation, [Delimiter=",", Encoding=65001])
in
    #"Imported CSV"
```

**Método 2: Via REST API**
```powerquery
let
    BaseUrl = "http://namenode:9870/webhdfs/v1/data/sales.csv",
    Parameters = "?op=OPEN&user.name=hadoop",
    Source = Json.Document(Web.Contents(BaseUrl & Parameters)),
    Data = Csv.Document(Source[location])
in
    Data
```

### **2.3 Conectar ao Azure Data Lake**

```powerquery
let
    Source = AzureStorage.DataLake(
        "https://mystorageaccount.dfs.core.windows.net/container/path/"
    ),
    #"Filtered Rows" = Table.SelectRows(Source, 
        each [Extension] = ".parquet"),
    #"Combined Files" = Table.Combine(
        Table.AddColumn(#"Filtered Rows", "Data", 
            each Parquet.Document([Content]))
    )
in
    #"Combined Files"
```

### **2.4 Conectar ao Amazon S3**

```powerquery
let
    Source = AmazonRedshift.Database(
        "bigdata-cluster.abc123.us-west-2.redshift.amazonaws.com:5439",
        "warehouse",
        [
            RoleArn = "arn:aws:iam::123456789:role/PowerBIRole"
        ]
    ),
    public = Source{[Schema="public"]}[Data],
    sales_table = public{[Name="sales_summary"]}[Data]
in
    sales_table
```

---

## **📊 Parte 3: Modelagem de Dados para Big Data**

### **3.1 Otimização de Performance**

#### **Import vs DirectQuery vs Composite:**

```powerquery
// Configuração DirectQuery para tabelas grandes
let
    Source = Sql.Database("spark-server", "warehouse", [
        Query = "SELECT * FROM fact_sales WHERE year >= 2020",
        CommandTimeout = #duration(0, 1, 0, 0)
    ])
in
    Source
```

#### **Agregações Automáticas:**
```dax
// Criar tabela de agregação
SalesAgg = 
SUMMARIZE(
    Sales,
    Sales[Year],
    Sales[Month],
    Sales[Product_Category],
    "Total_Sales", SUM(Sales[Amount]),
    "Avg_Sales", AVERAGE(Sales[Amount]),
    "Transaction_Count", COUNT(Sales[Transaction_ID])
)
```

### **3.2 Modelagem Star Schema**

#### **Tabela Fato - Vendas:**
```dax
// Medidas da tabela fato
Total Sales = SUM(Sales[Amount])

YTD Sales = 
TOTALYTD(
    [Total Sales],
    'Date'[Date]
)

Sales Growth = 
VAR CurrentPeriodSales = [Total Sales]
VAR PreviousPeriodSales = 
    CALCULATE(
        [Total Sales],
        DATEADD('Date'[Date], -1, YEAR)
    )
RETURN
    DIVIDE(
        CurrentPeriodSales - PreviousPeriodSales,
        PreviousPeriodSales
    )
```

#### **Dimensão Tempo:**
```dax
// Criar tabela de datas
Date = 
ADDCOLUMNS(
    CALENDAR(DATE(2020,1,1), DATE(2025,12,31)),
    "Year", YEAR([Date]),
    "Month", MONTH([Date]),
    "MonthName", FORMAT([Date], "MMMM"),
    "Quarter", "Q" & ROUNDUP(MONTH([Date])/3, 0),
    "WeekOfYear", WEEKNUM([Date]),
    "DayOfWeek", WEEKDAY([Date]),
    "DayName", FORMAT([Date], "DDDD"),
    "IsWeekend", WEEKDAY([Date]) IN {1, 7}
)
```

### **3.3 Performance Tuning**

#### **Otimizações DAX:**
```dax
// ❌ Lento - múltiplas iterações
Sales by Category (Slow) = 
SUMX(
    Products,
    CALCULATE(
        SUM(Sales[Amount]),
        Products[Category] = "Electronics"
    )
)

// ✅ Rápido - contexto de filtro
Sales by Category (Fast) = 
CALCULATE(
    SUM(Sales[Amount]),
    Products[Category] = "Electronics"
)

// ❌ Lento - sem agregação
Avg Daily Sales (Slow) = 
AVERAGEX(
    VALUES('Date'[Date]),
    CALCULATE(SUM(Sales[Amount]))
)

// ✅ Rápido - com agregação
Avg Daily Sales (Fast) = 
DIVIDE(
    [Total Sales],
    DISTINCTCOUNT('Date'[Date])
)
```

#### **Configurações de Modelo:**
```json
{
    "model": {
        "defaultMode": "DirectQuery",
        "dataAccessOptions": {
            "legacyRedirects": false,
            "returnErrorValuesAsNull": true
        },
        "aggregations": [
            {
                "name": "SalesAggregation",
                "table": "Sales",
                "columns": ["Year", "Month", "Category"],
                "measures": ["SalesSum", "SalesCount"]
            }
        ]
    }
}
```

---

## **📈 Parte 4: Análises Avançadas com Python**

### **4.1 Integração Python no Power BI**

#### **Script de Clustering:**
```python
# Python script no Power BI
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 'dataset' é automaticamente disponibilizado pelo Power BI
df = dataset

# Preparar dados para clustering
features = ['annual_spending', 'frequency', 'recency']
X = df[features].fillna(df[features].mean())

# Normalizar dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicar K-Means
kmeans = KMeans(n_clusters=4, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Análise dos clusters
cluster_summary = df.groupby('cluster')[features].agg(['mean', 'count'])

# Visualização
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['annual_spending'], df['frequency'], 
                     c=df['cluster'], cmap='viridis', alpha=0.6)
plt.xlabel('Annual Spending')
plt.ylabel('Frequency')
plt.title('Customer Segmentation')
plt.colorbar(scatter)
plt.show()

# Retornar dados enriquecidos
dataset = df[['customer_id', 'cluster']]
```

#### **Análise de Série Temporal:**
```python
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Preparar dados temporais
df = dataset.copy()
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date').sort_index()

# Decomposição sazonal
decomposition = seasonal_decompose(df['sales'], model='additive', period=12)

# Modelo ARIMA para previsão
model = ARIMA(df['sales'], order=(1,1,1))
fitted_model = model.fit()

# Previsão para próximos 12 meses
forecast = fitted_model.forecast(steps=12)
forecast_dates = pd.date_range(start=df.index[-1], periods=13, freq='M')[1:]

# Criar DataFrame com previsões
forecast_df = pd.DataFrame({
    'date': forecast_dates,
    'forecasted_sales': forecast,
    'type': 'forecast'
})

# Combinar dados históricos e previsão
historical_df = pd.DataFrame({
    'date': df.index,
    'forecasted_sales': df['sales'],
    'type': 'historical'
})

result_df = pd.concat([historical_df, forecast_df], ignore_index=True)

# Visualização
plt.figure(figsize=(12, 6))
historical_data = result_df[result_df['type'] == 'historical']
forecast_data = result_df[result_df['type'] == 'forecast']

plt.plot(historical_data['date'], historical_data['forecasted_sales'], 
         label='Historical', color='blue')
plt.plot(forecast_data['date'], forecast_data['forecasted_sales'], 
         label='Forecast', color='red', linestyle='--')

plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Forecast')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Retornar para Power BI
dataset = result_df
```

### **4.2 Machine Learning Integration**

#### **Modelo de Churn Prediction:**
```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
import joblib

# Preparar dados
df = dataset.copy()

# Feature engineering
df['avg_monthly_spend'] = df['total_spend'] / df['months_active']
df['days_since_last_purchase'] = (pd.Timestamp.now() - pd.to_datetime(df['last_purchase_date'])).dt.days

# Features para o modelo
features = [
    'avg_monthly_spend', 'months_active', 'total_purchases',
    'days_since_last_purchase', 'support_tickets', 'payment_failures'
]

X = df[features].fillna(0)
y = df['churned']

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Fazer previsões
df['churn_probability'] = rf_model.predict_proba(X)[:, 1]
df['churn_risk'] = pd.cut(df['churn_probability'], 
                         bins=[0, 0.3, 0.7, 1.0], 
                         labels=['Low', 'Medium', 'High'])

# Feature importance
feature_importance = pd.DataFrame({
    'feature': features,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print("Feature Importance:")
print(feature_importance)

# Salvar modelo (opcional)
# joblib.dump(rf_model, 'churn_model.pkl')

# Retornar dados enriquecidos
dataset = df[['customer_id', 'churn_probability', 'churn_risk']]
```

---

## **📊 Parte 5: Dashboards Avançados**

### **5.1 Dashboard Executivo - E-commerce**

#### **Métricas Principais:**
```dax
// KPIs principais
Revenue = SUM(Sales[Amount])

Revenue Growth = 
VAR CurrentRevenue = [Revenue]
VAR PreviousRevenue = 
    CALCULATE(
        [Revenue],
        DATEADD('Date'[Date], -1, MONTH)
    )
RETURN
    DIVIDE(CurrentRevenue - PreviousRevenue, PreviousRevenue)

Customer Acquisition Cost = 
DIVIDE(
    SUM(Marketing[Spend]),
    DISTINCTCOUNT(Sales[CustomerID])
)

Customer Lifetime Value = 
DIVIDE(
    [Revenue],
    DISTINCTCOUNT(Sales[CustomerID])
) * 12 // Assumindo 12 meses de vida média

Conversion Rate = 
DIVIDE(
    DISTINCTCOUNT(Sales[CustomerID]),
    SUM(WebAnalytics[Visitors])
)
```

#### **Análise de Cohort:**
```dax
// Tabela de Cohort
CohortTable = 
VAR MinDate = MIN(Sales[Date])
VAR MaxDate = MAX(Sales[Date])
VAR CohortData = 
    ADDCOLUMNS(
        GENERATESERIESVALUE(0, 12, 1),
        "Month", [Value],
        "Cohort Analysis", 
        VAR CurrentMonth = [Value]
        VAR CohortCustomers = 
            CALCULATETABLE(
                VALUES(Sales[CustomerID]),
                Sales[Date] >= MinDate &&
                Sales[Date] < EOMONTH(MinDate, CurrentMonth)
            )
        RETURN
            DIVIDE(
                COUNTROWS(CohortCustomers),
                DISTINCTCOUNT(Sales[CustomerID])
            )
    )
RETURN CohortData
```

### **5.2 Dashboard Operacional - IoT**

#### **Alertas em Tempo Real:**
```dax
// Status dos equipamentos
Equipment Status = 
SWITCH(
    TRUE(),
    [Avg Temperature] > 80, "Critical",
    [Avg Temperature] > 70, "Warning",
    "Normal"
)

// Contagem de alertas
Alert Count = 
COUNTROWS(
    FILTER(
        IoTData,
        IoTData[Status] IN {"Critical", "Warning"}
    )
)

// Eficiência operacional
OEE = 
VAR Availability = 
    DIVIDE(
        SUM(Equipment[UpTime]),
        SUM(Equipment[PlannedTime])
    )
VAR Performance = 
    DIVIDE(
        SUM(Equipment[ActualOutput]),
        SUM(Equipment[PlannedOutput])
    )
VAR Quality = 
    DIVIDE(
        SUM(Equipment[GoodParts]),
        SUM(Equipment[TotalParts])
    )
RETURN
    Availability * Performance * Quality
```

### **5.3 Dashboard Financeiro**

#### **Análise de Risco:**
```dax
// Value at Risk (VaR)
VaR 95% = 
PERCENTILE.INC(
    Portfolio[DailyReturns],
    0.05
) * -1

// Sharpe Ratio
Sharpe Ratio = 
VAR AverageReturn = AVERAGE(Portfolio[Returns])
VAR StandardDeviation = STDEV.P(Portfolio[Returns])
VAR RiskFreeRate = 0.02
RETURN
    DIVIDE(
        AverageReturn - RiskFreeRate,
        StandardDeviation
    )

// Drawdown máximo
Max Drawdown = 
VAR PeakValue = 
    MAXX(
        FILTER(
            ALL(Portfolio),
            Portfolio[Date] <= MAX(Portfolio[Date])
        ),
        Portfolio[CumulativeValue]
    )
VAR CurrentValue = MAX(Portfolio[CumulativeValue])
RETURN
    DIVIDE(CurrentValue - PeakValue, PeakValue)
```

---

## **🔧 Parte 6: Automatização e Deploy**

### **6.1 Power BI Service Configuration**

#### **Dataset Refresh Automation:**
```powershell
# PowerShell script para automação
$TenantId = "your-tenant-id"
$ClientId = "your-client-id"
$ClientSecret = "your-client-secret"
$WorkspaceId = "your-workspace-id"
$DatasetId = "your-dataset-id"

# Autenticação
$Body = @{
    grant_type = "client_credentials"
    client_id = $ClientId
    client_secret = $ClientSecret
    resource = "https://analysis.windows.net/powerbi/api"
}

$TokenResponse = Invoke-RestMethod -Uri "https://login.microsoftonline.com/$TenantId/oauth2/token" -Method Post -Body $Body
$AccessToken = $TokenResponse.access_token

# Refresh dataset
$Headers = @{
    Authorization = "Bearer $AccessToken"
    Content-Type = "application/json"
}

$RefreshUri = "https://api.powerbi.com/v1.0/myorg/groups/$WorkspaceId/datasets/$DatasetId/refreshes"
Invoke-RestMethod -Uri $RefreshUri -Method Post -Headers $Headers
```

### **6.2 Gateway Configuration**

#### **On-premises Data Gateway Setup:**
```json
{
    "gatewayConfig": {
        "name": "BigDataGateway",
        "region": "South Central US",
        "dataSourceType": "Spark",
        "connectionDetails": {
            "server": "spark-cluster.company.com",
            "port": 10000,
            "database": "warehouse",
            "authenticationType": "Username",
            "privacyLevel": "Organizational"
        }
    }
}
```

### **6.3 Row Level Security (RLS)**

#### **Implementação de Segurança:**
```dax
// Tabela de segurança
[User Email] = USERPRINCIPALNAME()

// Filtro por região
Region Security = 
VAR UserEmail = USERPRINCIPALNAME()
VAR UserRegion = 
    LOOKUPVALUE(
        UserSecurity[Region],
        UserSecurity[Email],
        UserEmail
    )
RETURN
    Sales[Region] = UserRegion || UserRegion = "All"

// Filtro por departamento
Department Security = 
Sales[Department] IN 
    CALCULATETABLE(
        VALUES(UserSecurity[Department]),
        UserSecurity[Email] = USERPRINCIPALNAME()
    )
```

---

## **📱 Parte 7: Mobile e Embedded Analytics**

### **7.1 Power BI Mobile Optimization**

#### **Layout Mobile-First:**
```json
{
    "mobileLayout": {
        "pages": [
            {
                "name": "Overview",
                "visuals": [
                    {
                        "type": "card",
                        "position": {"x": 0, "y": 0, "width": 3, "height": 2},
                        "title": "Total Revenue"
                    },
                    {
                        "type": "chart",
                        "position": {"x": 0, "y": 2, "width": 6, "height": 4},
                        "title": "Sales Trend"
                    }
                ]
            }
        ]
    }
}
```

### **7.2 Embedded Analytics**

#### **Power BI Embedded em Aplicação Web:**
```javascript
// JavaScript para embeding
import { models, Report, Embed } from 'powerbi-client';

const embedConfig = {
    type: 'report',
    id: 'your-report-id',
    embedUrl: 'https://app.powerbi.com/reportEmbed',
    accessToken: 'your-access-token',
    permissions: models.Permissions.Read,
    settings: {
        filterPaneEnabled: false,
        navContentPaneEnabled: false,
        background: models.BackgroundType.Transparent
    }
};

// Embed report
const reportContainer = document.getElementById('reportContainer');
const report = powerbi.embed(reportContainer, embedConfig);

// Event handling
report.on('loaded', function() {
    console.log('Report loaded');
});

report.on('error', function(event) {
    console.error('Error occurred:', event.detail);
});
```

---

## **🚀 Parte 8: Casos de Uso Avançados**

### **8.1 Análise de Logs em Tempo Real**

#### **Conexão com Apache Kafka:**
```powerquery
// Power Query para Kafka Stream
let
    Source = AzureEventHubs.Contents("your-eventhub-connection"),
    #"Parsed JSON" = Table.TransformColumns(Source, {
        {"Body", each Json.Document(Text.FromBinary(_))}
    }),
    #"Expanded Data" = Table.ExpandRecordColumn(#"Parsed JSON", "Body", 
        {"timestamp", "level", "message", "source_ip", "user_agent"}
    ),
    #"Added Custom" = Table.AddColumn(#"Expanded Data", "Severity", 
        each if [level] = "ERROR" then 3 
             else if [level] = "WARN" then 2 
             else 1
    )
in
    #"Added Custom"
```

#### **Dashboard de Segurança:**
```dax
// Detecção de anomalias de login
Failed Login Attempts = 
COUNTROWS(
    FILTER(
        SecurityLogs,
        SecurityLogs[EventType] = "Login Failed"
    )
)

// Threshold de segurança
Security Alert = 
IF(
    [Failed Login Attempts] > 10,
    "High Risk",
    IF([Failed Login Attempts] > 5, "Medium Risk", "Low Risk")
)

// Análise geográfica de tentativas de login
Login Attempts by Country = 
SUMMARIZE(
    SecurityLogs,
    SecurityLogs[Country],
    "Attempts", COUNT(SecurityLogs[LogID]),
    "Success Rate", 
        DIVIDE(
            COUNTROWS(FILTER(SecurityLogs, SecurityLogs[Status] = "Success")),
            COUNT(SecurityLogs[LogID])
        )
)
```

### **8.2 Análise de Performance de Sistema**

#### **Métricas de Infraestrutura:**
```dax
// CPU Utilization
Avg CPU Usage = 
AVERAGE(SystemMetrics[CPUPercentage])

// Memory utilization
Memory Usage GB = 
SUM(SystemMetrics[MemoryUsedMB]) / 1024

// Disk I/O performance
Disk IOPS = 
SUM(SystemMetrics[DiskReads]) + SUM(SystemMetrics[DiskWrites])

// Network throughput
Network Throughput Mbps = 
(SUM(SystemMetrics[NetworkIn]) + SUM(SystemMetrics[NetworkOut])) / 1048576

// Alert thresholds
System Health = 
SWITCH(
    TRUE(),
    [Avg CPU Usage] > 90 || [Memory Usage GB] > 30, "Critical",
    [Avg CPU Usage] > 80 || [Memory Usage GB] > 25, "Warning",
    "Healthy"
)
```

---

## **🔍 Parte 9: Troubleshooting e Performance**

### **9.1 Problemas Comuns e Soluções**

#### **Performance Issues:**
```dax
// ❌ Problema: Medida lenta
Slow Measure = 
SUMX(
    Sales,
    IF(
        Sales[Category] = "Electronics",
        Sales[Amount] * 1.1,
        Sales[Amount]
    )
)

// ✅ Solução: Otimizada
Fast Measure = 
SUM(Sales[Amount]) + 
CALCULATE(
    SUM(Sales[Amount]) * 0.1,
    Sales[Category] = "Electronics"
)
```

#### **Memory Optimization:**
```powerquery
// Reduzir tamanho de dados
let
    Source = Sql.Database("server", "database"),
    FilteredData = Table.SelectRows(Source, 
        each [Date] >= #date(2023, 1, 1)),
    RemovedColumns = Table.RemoveColumns(FilteredData, 
        {"UnusedColumn1", "UnusedColumn2"}),
    ChangedTypes = Table.TransformColumnTypes(RemovedColumns, {
        {"Amount", Currency.Type},
        {"Date", type date},
        {"Category", type text}
    })
in
    ChangedTypes
```

### **9.2 Monitoring e Alertas**

#### **Power BI Admin Center Metrics:**
```powershell
# PowerShell para monitoramento
$Headers = @{
    Authorization = "Bearer $AccessToken"
}

# Get dataset refreshes
$RefreshHistoryUri = "https://api.powerbi.com/v1.0/myorg/admin/datasets/$DatasetId/refreshes"
$RefreshHistory = Invoke-RestMethod -Uri $RefreshHistoryUri -Headers $Headers

# Check for failures
$FailedRefreshes = $RefreshHistory.value | Where-Object {$_.status -eq "Failed"}

if ($FailedRefreshes.Count -gt 0) {
    Write-Host "Alert: $($FailedRefreshes.Count) failed refreshes detected"
    # Send alert email
}
```

---

## **📚 Parte 10: Recursos Adicionais**

### **10.1 Templates e Exemplos**

#### **Template de Relatório Financeiro:**
```json
{
    "template": {
        "name": "Financial Dashboard Template",
        "pages": [
            {
                "name": "Executive Summary",
                "visuals": [
                    {"type": "card", "measure": "Total Revenue"},
                    {"type": "card", "measure": "Profit Margin"},
                    {"type": "chart", "data": "Revenue Trend"},
                    {"type": "table", "data": "Top Products"}
                ]
            },
            {
                "name": "Detailed Analysis",
                "visuals": [
                    {"type": "matrix", "data": "P&L Statement"},
                    {"type": "chart", "data": "Budget vs Actual"},
                    {"type": "map", "data": "Sales by Region"}
                ]
            }
        ]
    }
}
```

### **10.2 Melhores Práticas**

#### **Naming Conventions:**
```
Tables: 
- Fact_Sales
- Dim_Customer
- Bridge_ProductCategory

Measures:
- [Revenue]
- [Profit Margin %]
- [YTD Sales]

Calculated Columns:
- Customer.FullName
- Product.PriceCategory
```

#### **Model Documentation:**
```markdown
# Data Model Documentation

## Tables
### Fact_Sales
- **Source**: SQL Server - SalesDB
- **Refresh**: Every 4 hours
- **Rows**: ~10M
- **Key Columns**: CustomerID, ProductID, DateKey

### Dim_Customer
- **Source**: CRM API
- **Refresh**: Daily at 6 AM
- **Rows**: ~100K
- **Key Columns**: CustomerID (Primary Key)

## Relationships
- Fact_Sales[CustomerID] -> Dim_Customer[CustomerID] (Many-to-One)
- Fact_Sales[ProductID] -> Dim_Product[ProductID] (Many-to-One)
```

---

## **🎯 Projeto Prático Final**

### **Cenário: Dashboard de E-commerce Big Data**

#### **Requisitos:**
1. **Fontes de Dados:**
   - Spark cluster (vendas transacionais)
   - MongoDB (dados de produtos)
   - Redis (dados de sessão)
   - API REST (dados de marketing)

2. **Análises Necessárias:**
   - Revenue tracking em tempo real
   - Customer segmentation
   - Product performance
   - Marketing attribution
   - Inventory optimization

3. **Visualizações:**
   - Executive dashboard
   - Operational dashboard
   - Marketing dashboard
   - Mobile views

#### **Implementação Step-by-Step:**

**1. Data Sources Setup:**
```powerquery
// Conexão Spark
let
    SparkSource = Spark.Tables("spark.company.com", [
        Protocol = "HTTP",
        Port = 10000,
        Database = "ecommerce"
    ]),
    SalesTable = SparkSource{[Schema="default",Item="sales"]}[Data]
in
    SalesTable

// Conexão MongoDB via API
let
    MongoAPI = Web.Contents("http://api.company.com/products", [
        Headers = [#"Content-Type"="application/json",
                   #"Authorization"="Bearer " & Token]
    ]),
    JsonData = Json.Document(MongoAPI),
    ProductsTable = Table.FromRecords(JsonData[products])
in
    ProductsTable
```

**2. DAX Measures:**
```dax
// KPIs principais
Revenue = SUM(Sales[Amount])
Orders = DISTINCTCOUNT(Sales[OrderID])
AOV = DIVIDE([Revenue], [Orders])
Conversion Rate = DIVIDE([Orders], SUM(WebData[Sessions]))

// Análises avançadas
Customer LTV = 
VAR AvgOrderValue = [AOV]
VAR PurchaseFrequency = 
    DIVIDE(
        COUNT(Sales[OrderID]),
        DISTINCTCOUNT(Sales[CustomerID])
    )
VAR CustomerLifespan = 12 // meses
RETURN
    AvgOrderValue * PurchaseFrequency * CustomerLifespan

// Inventory turnover
Inventory Turnover = 
DIVIDE(
    SUM(Sales[COGS]),
    AVERAGE(Inventory[StockValue])
)
```

**3. Python Analytics:**
```python
# Customer segmentation
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# RFM Analysis
df = dataset.copy()
current_date = df['order_date'].max()

rfm = df.groupby('customer_id').agg({
    'order_date': lambda x: (current_date - x.max()).days,
    'order_id': 'count',
    'amount': 'sum'
}).reset_index()

rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']

# Normalizar e clusterizar
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[['recency', 'frequency', 'monetary']])

kmeans = KMeans(n_clusters=5, random_state=42)
rfm['segment'] = kmeans.fit_predict(rfm_scaled)

# Labels dos segmentos
segment_labels = {
    0: 'Champions',
    1: 'Loyal Customers',
    2: 'Potential Loyalists',
    3: 'At Risk',
    4: 'Lost Customers'
}

rfm['segment_name'] = rfm['segment'].map(segment_labels)

dataset = rfm[['customer_id', 'segment_name', 'recency', 'frequency', 'monetary']]
```

---

## **📖 Conclusão**

Este tutorial apresentou um guia completo para usar Power BI com Big Data, cobrindo desde conexões básicas até análises avançadas com Python e machine learning. Os principais pontos cobertos foram:

### **Principais Aprendizados:**
1. **Conectividade**: Como conectar Power BI a fontes Big Data
2. **Modelagem**: Técnicas de otimização para grandes volumes
3. **DAX Avançado**: Medidas complexas e cálculos de performance
4. **Python Integration**: Análises avançadas e ML no Power BI
5. **Dashboards**: Criação de visualizações profissionais
6. **Deploy**: Automação e governança

### **Próximos Passos:**
- Explorar Power BI Premium features
- Implementar Real-time streaming
- Desenvolver Custom Visuals
- Integrar com Azure Synapse Analytics
- Estudar Power Platform integration

### **Recursos Complementares:**
- [Microsoft Learn - Power BI](https://docs.microsoft.com/learn/powerbi/)
- [Power BI Community](https://community.powerbi.com/)
- [Power BI Blog](https://powerbi.microsoft.com/blog/)
- [DAX Guide](https://dax.guide/)

---

*Este tutorial é atualizado regularmente com novas funcionalidades e melhores práticas.*
