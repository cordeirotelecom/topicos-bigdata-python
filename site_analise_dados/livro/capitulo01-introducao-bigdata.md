# CAPÍTULO 1: INTRODUÇÃO AO BIG DATA

## 1.1 O Que é Big Data?

Big Data refere-se a conjuntos de dados tão grandes, complexos ou de crescimento tão rápido que as ferramentas tradicionais de processamento de dados são inadequadas para lidar com eles de forma eficaz.

### Os 5 V's do Big Data

#### 1. Volume 📊
- **Definição**: Quantidade massiva de dados gerados continuamente
- **Escala**: Terabytes, Petabytes, Exabytes
- **Exemplo**: O Facebook gera mais de 4 petabytes de dados diariamente

```python
# Exemplo: Simulação de crescimento de volume de dados
import numpy as np
import matplotlib.pyplot as plt

anos = np.array([2010, 2015, 2020, 2025])
dados_globais_zb = np.array([2, 15, 64, 175])  # Zettabytes

plt.figure(figsize=(10, 6))
plt.plot(anos, dados_globais_zb, 'bo-', linewidth=2, markersize=8)
plt.title('Crescimento do Volume Global de Dados', fontsize=14)
plt.xlabel('Ano')
plt.ylabel('Volume (Zettabytes)')
plt.grid(True, alpha=0.3)
plt.show()

print(f"Crescimento projetado: {dados_globais_zb[-1]/dados_globais_zb[0]:.1f}x em 15 anos")
```

#### 2. Velocidade ⚡
- **Definição**: Rapidez com que os dados são gerados e processados
- **Tipos**: Batch, Near Real-time, Real-time, Streaming
- **Exemplo**: Transações financeiras (milhões por segundo)

```python
import time
from datetime import datetime

class DataVelocityDemo:
    def __init__(self):
        self.data_buffer = []
    
    def simulate_high_velocity_data(self, duration_seconds=10):
        """Simula geração de dados em alta velocidade"""
        start_time = time.time()
        count = 0
        
        while time.time() - start_time < duration_seconds:
            # Simula dados de sensor IoT
            data_point = {
                'timestamp': datetime.now().isoformat(),
                'sensor_id': f'sensor_{count % 1000}',
                'temperature': 20 + np.random.normal(0, 5),
                'humidity': 60 + np.random.normal(0, 10),
                'pressure': 1013 + np.random.normal(0, 20)
            }
            self.data_buffer.append(data_point)
            count += 1
            time.sleep(0.001)  # 1000 registros/segundo
        
        return count, len(self.data_buffer)

# Demonstração
demo = DataVelocityDemo()
records, buffer_size = demo.simulate_high_velocity_data(5)
print(f"Gerados {records} registros em 5 segundos")
print(f"Taxa: {records/5:.0f} registros/segundo")
```

#### 3. Variedade 🎭
- **Estruturados**: Tabelas, bancos relacionais
- **Semi-estruturados**: JSON, XML, logs
- **Não-estruturados**: Texto, imagens, vídeos, áudio

```python
import json
import pandas as pd
from datetime import datetime

# Exemplo de dados com diferentes estruturas
def demonstrate_data_variety():
    # 1. Dados Estruturados (CSV/DataFrame)
    structured_data = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
        'idade': [25, 30, 35, 28, 42],
        'salario': [5000, 7500, 6200, 5800, 9200]
    })
    
    # 2. Dados Semi-estruturados (JSON)
    semi_structured_data = [
        {
            "usuario": "joao123",
            "acao": "login",
            "timestamp": "2025-08-25T10:30:00Z",
            "metadata": {
                "ip": "192.168.1.100",
                "dispositivo": "mobile",
                "localizacao": {"lat": -27.5954, "lon": -48.5480}
            }
        },
        {
            "usuario": "maria456", 
            "acao": "compra",
            "timestamp": "2025-08-25T11:15:30Z",
            "produto": {
                "id": "ABC123",
                "categoria": "eletrônicos",
                "preco": 1299.99
            }
        }
    ]
    
    # 3. Dados Não-estruturados (Texto)
    unstructured_data = [
        "Cliente muito satisfeito com o produto. Recomenda para amigos!",
        "Entrega atrasou 3 dias. Produto chegou com defeito.",
        "Excelente qualidade, vale cada centavo gasto. Voltarei a comprar.",
        "Atendimento péssimo, não respondem no chat de suporte."
    ]
    
    return structured_data, semi_structured_data, unstructured_data

# Demonstração
struct, semi_struct, unstruct = demonstrate_data_variety()
print("=== DADOS ESTRUTURADOS ===")
print(struct.head())
print("\n=== DADOS SEMI-ESTRUTURADOS ===")
print(json.dumps(semi_struct[0], indent=2, ensure_ascii=False))
print("\n=== DADOS NÃO-ESTRUTURADOS ===")
print(unstruct[0])
```

#### 4. Veracidade ✅
- **Definição**: Qualidade e confiabilidade dos dados
- **Desafios**: Dados incompletos, incorretos, inconsistentes
- **Importância**: "Garbage in, garbage out"

```python
import pandas as pd
import numpy as np

def data_quality_analysis(df):
    """Análise de qualidade dos dados"""
    quality_report = {
        'total_registros': len(df),
        'valores_nulos': df.isnull().sum().to_dict(),
        'duplicatas': df.duplicated().sum(),
        'completude': ((df.notna().sum() / len(df)) * 100).to_dict()
    }
    
    return quality_report

# Exemplo com dataset com problemas de qualidade
problematic_data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 5],  # ID duplicado
    'nome': ['João', 'Maria', None, 'Ana', 'Carlos', 'Carlos'],  # Valor nulo
    'idade': [25, -5, 35, 150, 42, 42],  # Idades impossíveis
    'email': ['joao@email.com', 'maria@', 'pedro@email.com', 
              'ana@email.com', None, 'carlos@email.com']  # Email inválido e nulo
})

quality_report = data_quality_analysis(problematic_data)
print("=== RELATÓRIO DE QUALIDADE ===")
for key, value in quality_report.items():
    print(f"{key}: {value}")

# Função para limpeza de dados
def clean_data(df):
    """Aplicar regras de limpeza"""
    df_clean = df.copy()
    
    # Remover duplicatas
    df_clean = df_clean.drop_duplicates()
    
    # Tratar idades impossíveis
    df_clean = df_clean[(df_clean['idade'] >= 0) & (df_clean['idade'] <= 120)]
    
    # Remover registros com emails inválidos
    df_clean = df_clean[df_clean['email'].str.contains('@', na=False)]
    
    return df_clean

clean_df = clean_data(problematic_data)
print(f"\nRegistros antes da limpeza: {len(problematic_data)}")
print(f"Registros após limpeza: {len(clean_df)}")
```

#### 5. Valor 💎
- **Definição**: Capacidade de extrair insights acionáveis
- **Objetivo**: Transformar dados em conhecimento e vantagem competitiva
- **ROI**: Retorno sobre investimento em Big Data

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def extract_business_value(sales_data):
    """Extrai valor de negócio dos dados de vendas"""
    
    # Análise de padrões sazonais
    sales_data['data'] = pd.to_datetime(sales_data['data'])
    sales_data['mes'] = sales_data['data'].dt.month
    sales_data['dia_semana'] = sales_data['data'].dt.day_name()
    
    # Insights valiosos
    insights = {
        'vendas_por_mes': sales_data.groupby('mes')['valor'].sum(),
        'vendas_por_dia_semana': sales_data.groupby('dia_semana')['valor'].sum(),
        'produto_mais_vendido': sales_data.groupby('produto')['quantidade'].sum().idxmax(),
        'receita_total': sales_data['valor'].sum(),
        'ticket_medio': sales_data['valor'].mean()
    }
    
    return insights

# Dados simulados de vendas
np.random.seed(42)
n_records = 10000

sales_data = pd.DataFrame({
    'data': pd.date_range('2024-01-01', periods=n_records, freq='H'),
    'produto': np.random.choice(['Produto A', 'Produto B', 'Produto C'], n_records),
    'quantidade': np.random.randint(1, 10, n_records),
    'preco_unitario': np.random.uniform(10, 100, n_records)
})
sales_data['valor'] = sales_data['quantidade'] * sales_data['preco_unitario']

business_insights = extract_business_value(sales_data)

print("=== INSIGHTS DE NEGÓCIO ===")
print(f"Receita Total: R$ {business_insights['receita_total']:,.2f}")
print(f"Ticket Médio: R$ {business_insights['ticket_medio']:,.2f}")
print(f"Produto Mais Vendido: {business_insights['produto_mais_vendido']}")

# Visualização dos insights
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Vendas por mês
business_insights['vendas_por_mes'].plot(kind='bar', ax=axes[0])
axes[0].set_title('Vendas por Mês')
axes[0].set_ylabel('Valor (R$)')

# Vendas por dia da semana
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
vendas_dia = business_insights['vendas_por_dia_semana'].reindex(day_order)
vendas_dia.plot(kind='bar', ax=axes[1])
axes[1].set_title('Vendas por Dia da Semana')
axes[1].set_ylabel('Valor (R$)')

plt.tight_layout()
plt.show()
```

## 1.2 Evolução Histórica do Big Data

### Timeline do Big Data

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Timeline histórico
timeline_data = [
    (datetime(1944, 1, 1), "Termo 'Big Data' usado pela primeira vez", "Conceitual"),
    (datetime(1997, 1, 1), "Termo moderno 'Big Data' cunhado", "Acadêmico"),
    (datetime(2003, 1, 1), "Google File System (GFS)", "Tecnológico"),
    (datetime(2004, 1, 1), "Google MapReduce", "Framework"),
    (datetime(2006, 1, 1), "Hadoop (Apache)", "Open Source"),
    (datetime(2009, 1, 1), "NoSQL ganha tração", "Banco de Dados"),
    (datetime(2010, 1, 1), "Apache Spark", "Performance"),
    (datetime(2011, 1, 1), "Apache Kafka", "Streaming"),
    (datetime(2014, 1, 1), "Apache Flink", "Real-time"),
    (datetime(2020, 1, 1), "Edge Computing + AI", "Modernização"),
    (datetime(2025, 1, 1), "Quantum + Big Data", "Futuro")
]

# Visualização da timeline
fig, ax = plt.subplots(figsize=(15, 8))

dates = [item[0] for item in timeline_data]
events = [item[1] for item in timeline_data]
categories = [item[2] for item in timeline_data]

# Cores por categoria
color_map = {
    'Conceitual': 'red', 'Acadêmico': 'blue', 'Tecnológico': 'green',
    'Framework': 'orange', 'Open Source': 'purple', 'Banco de Dados': 'brown',
    'Performance': 'pink', 'Streaming': 'gray', 'Real-time': 'olive',
    'Modernização': 'cyan', 'Futuro': 'magenta'
}

colors = [color_map[cat] for cat in categories]

ax.scatter(dates, range(len(dates)), c=colors, s=100, alpha=0.7)

for i, (date, event, category) in enumerate(timeline_data):
    ax.annotate(f"{event}\n({category})", 
                (date, i), 
                xytext=(10, 0), 
                textcoords='offset points',
                fontsize=9,
                bbox=dict(boxstyle='round,pad=0.3', facecolor=color_map[category], alpha=0.3))

ax.set_xlabel('Ano')
ax.set_ylabel('Marcos Históricos')
ax.set_title('Evolução Histórica do Big Data', fontsize=16)
ax.grid(True, alpha=0.3)

# Formatação do eixo X
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_major_locator(mdates.YearLocator(5))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

## 1.3 Características dos Sistemas Big Data

### Escalabilidade

```python
class ScalabilityDemo:
    """Demonstração de conceitos de escalabilidade"""
    
    @staticmethod
    def horizontal_vs_vertical_scaling():
        """Compare escalabilidade horizontal vs vertical"""
        
        # Cenário: Processamento de 1TB de dados
        data_size_tb = 1
        
        # Escala Vertical (Scale Up)
        vertical_configs = [
            {'cpu_cores': 4, 'ram_gb': 16, 'cost_per_hour': 0.50},
            {'cpu_cores': 8, 'ram_gb': 32, 'cost_per_hour': 1.00},
            {'cpu_cores': 16, 'ram_gb': 64, 'cost_per_hour': 2.00},
            {'cpu_cores': 32, 'ram_gb': 128, 'cost_per_hour': 4.00}
        ]
        
        # Escala Horizontal (Scale Out)
        horizontal_configs = [
            {'nodes': 4, 'cpu_per_node': 4, 'ram_per_node': 16, 'cost_per_node_hour': 0.50},
            {'nodes': 8, 'cpu_per_node': 4, 'ram_per_node': 16, 'cost_per_node_hour': 0.50},
            {'nodes': 16, 'cpu_per_node': 4, 'ram_per_node': 16, 'cost_per_node_hour': 0.50},
            {'nodes': 32, 'cpu_per_node': 4, 'ram_per_node': 16, 'cost_per_node_hour': 0.50}
        ]
        
        print("=== ESCALABILIDADE VERTICAL ===")
        for config in vertical_configs:
            throughput = config['cpu_cores'] * 0.1  # TB/hora simplificado
            time_hours = data_size_tb / throughput
            total_cost = time_hours * config['cost_per_hour']
            print(f"CPU: {config['cpu_cores']} cores, RAM: {config['ram_gb']}GB")
            print(f"Tempo: {time_hours:.1f}h, Custo: ${total_cost:.2f}\n")
        
        print("=== ESCALABILIDADE HORIZONTAL ===")
        for config in horizontal_configs:
            total_cpu = config['nodes'] * config['cpu_per_node']
            throughput = total_cpu * 0.1  # TB/hora simplificado
            time_hours = data_size_tb / throughput
            total_cost = time_hours * config['nodes'] * config['cost_per_node_hour']
            print(f"Nós: {config['nodes']}, CPU Total: {total_cpu} cores")
            print(f"Tempo: {time_hours:.1f}h, Custo: ${total_cost:.2f}\n")

# Executar demonstração
demo = ScalabilityDemo()
demo.horizontal_vs_vertical_scaling()
```

### Tolerância a Falhas

```python
import random
import time

class FaultToleranceDemo:
    """Demonstração de tolerância a falhas"""
    
    def __init__(self, num_nodes=5):
        self.nodes = [f"node_{i}" for i in range(num_nodes)]
        self.node_status = {node: True for node in self.nodes}  # True = online
        self.replication_factor = 3
    
    def simulate_node_failure(self, failure_probability=0.1):
        """Simula falhas aleatórias de nós"""
        failed_nodes = []
        for node in self.nodes:
            if random.random() < failure_probability:
                self.node_status[node] = False
                failed_nodes.append(node)
        return failed_nodes
    
    def check_data_availability(self):
        """Verifica se dados ainda estão disponíveis com replicação"""
        online_nodes = sum(1 for status in self.node_status.values() if status)
        return online_nodes >= self.replication_factor
    
    def demonstrate_fault_tolerance(self, simulation_hours=24):
        """Simula 24h de operação com possíveis falhas"""
        print("=== SIMULAÇÃO DE TOLERÂNCIA A FALHAS ===")
        print(f"Nós iniciais: {len(self.nodes)}")
        print(f"Fator de replicação: {self.replication_factor}")
        print(f"Simulação: {simulation_hours} horas\n")
        
        availability_history = []
        
        for hour in range(simulation_hours):
            # Simular falhas horárias
            failed = self.simulate_node_failure(0.05)  # 5% chance de falha por hora
            
            # Verificar disponibilidade
            is_available = self.check_data_availability()
            availability_history.append(is_available)
            
            online_count = sum(1 for status in self.node_status.values() if status)
            
            if failed:
                print(f"Hora {hour:02d}: Falha em {failed}, Nós online: {online_count}, Disponível: {'✅' if is_available else '❌'}")
            
            # Simular recuperação de alguns nós
            if hour % 6 == 0:  # A cada 6 horas, tentar recuperar nós
                for node in self.nodes:
                    if not self.node_status[node] and random.random() < 0.3:
                        self.node_status[node] = True
                        print(f"Hora {hour:02d}: Nó {node} recuperado")
        
        # Calcular uptime
        uptime_percentage = (sum(availability_history) / len(availability_history)) * 100
        print(f"\nUptime total: {uptime_percentage:.1f}%")
        
        return availability_history

# Executar simulação
fault_demo = FaultToleranceDemo(num_nodes=8)
availability = fault_demo.demonstrate_fault_tolerance(24)

# Visualizar uptime
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(range(24), [1 if available else 0 for available in availability], 'bo-')
plt.title('Disponibilidade do Sistema ao Longo de 24 Horas')
plt.xlabel('Hora')
plt.ylabel('Sistema Disponível (1=Sim, 0=Não)')
plt.grid(True, alpha=0.3)
plt.ylim(-0.1, 1.1)
plt.show()
```

## 1.4 Casos de Uso do Big Data

### 1. E-commerce e Recomendações

```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationEngine:
    """Sistema de recomendação baseado em Big Data"""
    
    def __init__(self):
        self.user_item_matrix = None
        self.item_similarity = None
        
    def generate_sample_data(self, n_users=1000, n_products=100):
        """Gera dados simulados de e-commerce"""
        np.random.seed(42)
        
        # Produtos com características
        products = pd.DataFrame({
            'product_id': range(n_products),
            'category': np.random.choice(['Eletrônicos', 'Roupas', 'Casa', 'Livros'], n_products),
            'price': np.random.uniform(10, 500, n_products),
            'description': [f"Produto de qualidade {np.random.choice(['premium', 'básico', 'intermediário'])}" 
                          for _ in range(n_products)]
        })
        
        # Interações usuário-produto (compras, visualizações, etc.)
        interactions = []
        for user_id in range(n_users):
            # Cada usuário interage com 5-20 produtos
            n_interactions = np.random.randint(5, 21)
            user_products = np.random.choice(n_products, n_interactions, replace=False)
            
            for product_id in user_products:
                interaction = {
                    'user_id': user_id,
                    'product_id': product_id,
                    'rating': np.random.randint(1, 6),  # 1-5 estrelas
                    'interaction_type': np.random.choice(['view', 'cart', 'purchase'], 
                                                       p=[0.6, 0.3, 0.1])
                }
                interactions.append(interaction)
        
        interactions_df = pd.DataFrame(interactions)
        return products, interactions_df
    
    def build_recommendation_model(self, interactions_df):
        """Constrói modelo de recomendação colaborativa"""
        # Matriz usuário-item
        self.user_item_matrix = interactions_df.pivot_table(
            index='user_id', 
            columns='product_id', 
            values='rating', 
            fill_value=0
        )
        
        # Similaridade entre itens
        self.item_similarity = cosine_similarity(self.user_item_matrix.T)
        
    def recommend_products(self, user_id, n_recommendations=5):
        """Recomenda produtos para um usuário"""
        if self.user_item_matrix is None:
            return []
        
        user_ratings = self.user_item_matrix.loc[user_id]
        
        # Produtos que o usuário já avaliou
        rated_products = user_ratings[user_ratings > 0].index
        
        # Calcular scores para produtos não avaliados
        recommendations = {}
        
        for product_id in self.user_item_matrix.columns:
            if product_id not in rated_products:
                # Score baseado em similaridade com produtos já avaliados
                score = 0
                similarity_sum = 0
                
                for rated_product in rated_products:
                    similarity = self.item_similarity[product_id][rated_product]
                    score += similarity * user_ratings[rated_product]
                    similarity_sum += similarity
                
                if similarity_sum > 0:
                    recommendations[product_id] = score / similarity_sum
        
        # Top N recomendações
        top_recommendations = sorted(recommendations.items(), 
                                   key=lambda x: x[1], 
                                   reverse=True)[:n_recommendations]
        
        return [product_id for product_id, score in top_recommendations]

# Demonstração do sistema de recomendação
print("=== SISTEMA DE RECOMENDAÇÃO E-COMMERCE ===")

rec_engine = RecommendationEngine()
products, interactions = rec_engine.generate_sample_data(1000, 100)

print(f"Dados gerados:")
print(f"- {len(products)} produtos")
print(f"- {len(interactions)} interações")
print(f"- {interactions['user_id'].nunique()} usuários únicos")

# Análise de padrões
print(f"\nPadrões identificados:")
print(f"- Categoria mais popular: {interactions.merge(products, on='product_id')['category'].mode()[0]}")
print(f"- Rating médio: {interactions['rating'].mean():.2f}")
print(f"- Interações por usuário: {interactions.groupby('user_id').size().mean():.1f}")

# Construir modelo
rec_engine.build_recommendation_model(interactions)

# Fazer recomendações para usuário exemplo
sample_user = 0
recommendations = rec_engine.recommend_products(sample_user, 5)
print(f"\nRecomendações para usuário {sample_user}: {recommendations}")
```

### 2. Análise de Sentimentos em Tempo Real

```python
import re
import numpy as np
from textblob import TextBlob
from collections import defaultdict
import matplotlib.pyplot as plt

class SentimentAnalysisEngine:
    """Engine de análise de sentimentos para Big Data"""
    
    def __init__(self):
        self.sentiment_history = defaultdict(list)
        self.keywords_tracking = defaultdict(int)
    
    def clean_text(self, text):
        """Limpa e preprocessa texto"""
        # Remove URLs, menções, hashtags
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'@\w+', '', text)
        text = re.sub(r'#\w+', '', text)
        text = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', text)
        return text.lower().strip()
    
    def analyze_sentiment(self, text):
        """Analisa sentimento do texto"""
        cleaned_text = self.clean_text(text)
        blob = TextBlob(cleaned_text)
        
        # Polaridade: -1 (negativo) a 1 (positivo)
        polarity = blob.sentiment.polarity
        
        # Classificação
        if polarity > 0.1:
            sentiment = 'positivo'
        elif polarity < -0.1:
            sentiment = 'negativo'
        else:
            sentiment = 'neutro'
            
        return {
            'text': text,
            'cleaned_text': cleaned_text,
            'polarity': polarity,
            'sentiment': sentiment,
            'subjectivity': blob.sentiment.subjectivity
        }
    
    def process_social_media_stream(self, posts, topic):
        """Processa stream de posts de redes sociais"""
        results = []
        sentiment_counts = {'positivo': 0, 'negativo': 0, 'neutro': 0}
        
        for post in posts:
            analysis = self.analyze_sentiment(post)
            results.append(analysis)
            sentiment_counts[analysis['sentiment']] += 1
            
            # Rastrear palavras-chave
            words = analysis['cleaned_text'].split()
            for word in words:
                if len(word) > 3:  # Palavras com mais de 3 caracteres
                    self.keywords_tracking[word] += 1
        
        # Armazenar histórico
        self.sentiment_history[topic] = results
        
        return {
            'total_posts': len(posts),
            'sentiment_distribution': sentiment_counts,
            'average_polarity': np.mean([r['polarity'] for r in results]),
            'top_keywords': sorted(self.keywords_tracking.items(), 
                                 key=lambda x: x[1], reverse=True)[:10]
        }
    
    def generate_sample_social_data(self, topic="Big Data", n_posts=1000):
        """Gera dados simulados de redes sociais"""
        templates_positive = [
            f"Adorei o curso de {topic}! Muito bem explicado.",
            f"{topic} está revolucionando nossa empresa.",
            f"Excelente palestra sobre {topic} hoje!",
            f"Consegui meu primeiro emprego em {topic}!",
            f"O futuro é {topic}, sem dúvidas."
        ]
        
        templates_negative = [
            f"{topic} é muito complicado de entender.",
            f"Terrível implementação de {topic} na empresa.",
            f"Curso de {topic} péssimo, perda de tempo.",
            f"Frustrado com os resultados de {topic}.",
            f"Não recomendo trabalhar com {topic}."
        ]
        
        templates_neutral = [
            f"Estudando {topic} nas horas vagas.",
            f"Alguém conhece bom material sobre {topic}?",
            f"Evento sobre {topic} amanhã às 14h.",
            f"Pesquisando vagas em {topic}.",
            f"Qual a melhor ferramenta de {topic}?"
        ]
        
        posts = []
        for _ in range(n_posts):
            sentiment_type = np.random.choice(['positive', 'negative', 'neutral'], 
                                            p=[0.4, 0.2, 0.4])
            
            if sentiment_type == 'positive':
                post = np.random.choice(templates_positive)
            elif sentiment_type == 'negative':
                post = np.random.choice(templates_negative)
            else:
                post = np.random.choice(templates_neutral)
            
            # Adicionar ruído realista
            post += f" #{topic.replace(' ', '')}" if np.random.random() < 0.3 else ""
            posts.append(post)
        
        return posts

# Demonstração de análise de sentimentos
print("=== ANÁLISE DE SENTIMENTOS EM TEMPO REAL ===")

sentiment_engine = SentimentAnalysisEngine()

# Simular dados de diferentes tópicos
topics = ["Big Data", "Python", "Machine Learning", "Inteligência Artificial"]

results_summary = {}

for topic in topics:
    print(f"\nAnalisando sentimentos sobre: {topic}")
    posts = sentiment_engine.generate_sample_social_data(topic, 500)
    results = sentiment_engine.process_social_media_stream(posts, topic)
    results_summary[topic] = results
    
    print(f"Posts analisados: {results['total_posts']}")
    print(f"Sentimento médio: {results['average_polarity']:.3f}")
    print(f"Distribuição: {results['sentiment_distribution']}")
    print(f"Top palavras-chave: {results['top_keywords'][:5]}")

# Visualização comparativa
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.flatten()

for i, (topic, results) in enumerate(results_summary.items()):
    sentiment_dist = results['sentiment_distribution']
    
    # Gráfico de pizza para cada tópico
    axes[i].pie(sentiment_dist.values(), 
                labels=sentiment_dist.keys(),
                autopct='%1.1f%%',
                startangle=90)
    axes[i].set_title(f'Sentimentos: {topic}')

plt.tight_layout()
plt.show()

# Dashboard de métricas
print("\n=== DASHBOARD DE SENTIMENTOS ===")
df_summary = pd.DataFrame(results_summary).T
print(df_summary[['total_posts', 'average_polarity']])
```

## 1.5 Desafios do Big Data

### Desafios Técnicos

```python
class BigDataChallenges:
    """Demonstração dos principais desafios técnicos"""
    
    @staticmethod
    def storage_challenge():
        """Desafio de armazenamento"""
        print("=== DESAFIO DE ARMAZENAMENTO ===")
        
        # Crescimento exponencial de dados
        data_growth = {
            'Email (1GB)': 1,
            'Música (100GB)': 100,
            'Fotos HD (1TB)': 1000,
            'Vídeos 4K (10TB)': 10000,
            'Dados IoT (100TB/dia)': 100000,
            'Dados Científicos (1PB)': 1000000
        }
        
        for source, size_gb in data_growth.items():
            storage_cost = size_gb * 0.02  # $0.02 por GB/mês
            print(f"{source}: {size_gb:,} GB - Custo mensal: ${storage_cost:,.2f}")
    
    @staticmethod
    def processing_challenge():
        """Desafio de processamento"""
        print("\n=== DESAFIO DE PROCESSAMENTO ===")
        
        # Comparação de tempos de processamento
        data_sizes = [1, 10, 100, 1000, 10000]  # GB
        
        print("Tempo estimado para diferentes volumes:")
        print("Volume (GB) | CPU Single | CPU Multi | Cluster")
        print("-" * 50)
        
        for size in data_sizes:
            single_cpu = size * 10  # 10 min/GB
            multi_cpu = size * 2    # 2 min/GB (5 cores)
            cluster = size * 0.2    # 0.2 min/GB (50 nós)
            
            print(f"{size:8} GB | {single_cpu:8.1f} min | {multi_cpu:7.1f} min | {cluster:7.1f} min")
    
    @staticmethod
    def network_challenge():
        """Desafio de rede"""
        print("\n=== DESAFIO DE REDE ===")
        
        # Largura de banda vs tempo de transferência
        bandwidths = {
            '10 Mbps (DSL)': 10,
            '100 Mbps (Fibra)': 100,
            '1 Gbps (Ethernet)': 1000,
            '10 Gbps (Data Center)': 10000,
            '100 Gbps (Backbone)': 100000
        }
        
        data_size_gb = 1000  # 1TB
        
        print("Tempo para transferir 1TB:")
        for connection, mbps in bandwidths.items():
            # Conversão: GB para bits, depois para segundos
            time_seconds = (data_size_gb * 8 * 1024) / mbps
            time_hours = time_seconds / 3600
            
            print(f"{connection}: {time_hours:.1f} horas")

# Executar demonstrações dos desafios
challenges = BigDataChallenges()
challenges.storage_challenge()
challenges.processing_challenge()
challenges.network_challenge()
```

### Desafios de Privacidade e Ética

```python
import hashlib
import random

class PrivacyProtection:
    """Demonstração de técnicas de proteção de privacidade"""
    
    @staticmethod
    def data_anonymization():
        """Anonimização de dados pessoais"""
        print("=== ANONIMIZAÇÃO DE DADOS ===")
        
        # Dados originais (simulados)
        original_data = [
            {'nome': 'João Silva', 'cpf': '123.456.789-00', 'email': 'joao@email.com', 'idade': 35},
            {'nome': 'Maria Santos', 'cpf': '987.654.321-00', 'email': 'maria@email.com', 'idade': 28},
            {'nome': 'Pedro Costa', 'cpf': '456.789.123-00', 'email': 'pedro@email.com', 'idade': 42}
        ]
        
        print("Dados originais:")
        for person in original_data:
            print(f"  {person}")
        
        # Anonimização
        anonymized_data = []
        for person in original_data:
            # Hash dos identificadores
            name_hash = hashlib.sha256(person['nome'].encode()).hexdigest()[:8]
            cpf_hash = hashlib.sha256(person['cpf'].encode()).hexdigest()[:8]
            
            # Generalização da idade (faixas etárias)
            age_range = f"{(person['idade'] // 10) * 10}-{(person['idade'] // 10) * 10 + 9}"
            
            anonymized = {
                'id_hash': name_hash,
                'cpf_hash': cpf_hash,
                'domain': person['email'].split('@')[1],  # Apenas domínio
                'faixa_etaria': age_range
            }
            anonymized_data.append(anonymized)
        
        print("\nDados anonimizados:")
        for person in anonymized_data:
            print(f"  {person}")
    
    @staticmethod
    def differential_privacy():
        """Demonstração de privacidade diferencial"""
        print("\n=== PRIVACIDADE DIFERENCIAL ===")
        
        # Dataset original
        salaries = [50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000]
        true_average = sum(salaries) / len(salaries)
        
        print(f"Média real dos salários: ${true_average:,.2f}")
        
        # Aplicar ruído para privacidade diferencial
        epsilon = 1.0  # Parâmetro de privacidade
        sensitivity = max(salaries) - min(salaries)  # Sensibilidade
        
        # Adicionar ruído Laplaciano
        noise_scale = sensitivity / epsilon
        noisy_averages = []
        
        for i in range(5):
            noise = random.gauss(0, noise_scale)
            noisy_average = true_average + noise
            noisy_averages.append(noisy_average)
            print(f"Consulta {i+1}: ${noisy_average:,.2f} (ruído: {noise:+.2f})")
        
        print(f"Erro médio: ${abs(sum(noisy_averages)/len(noisy_averages) - true_average):,.2f}")

# Executar demonstrações de privacidade
privacy_demo = PrivacyProtection()
privacy_demo.data_anonymization()
privacy_demo.differential_privacy()
```

## 1.6 Conclusão do Capítulo

Big Data representa uma mudança paradigmática na forma como lidamos com informação. Os cinco V's (Volume, Velocidade, Variedade, Veracidade e Valor) definem não apenas as características técnicas, mas também os desafios e oportunidades desta era.

### Pontos-Chave:

1. **Volume**: Capacidade de processar petabytes e exabytes de dados
2. **Velocidade**: Processamento em tempo real e streaming
3. **Variedade**: Integração de dados estruturados, semi-estruturados e não-estruturados
4. **Veracidade**: Garantia de qualidade e confiabilidade dos dados
5. **Valor**: Extração de insights acionáveis para tomada de decisão

### Preparação para os Próximos Capítulos:

Nos próximos capítulos, exploraremos como Python e seu ecossistema de bibliotecas nos permitem implementar soluções práticas para cada um desses desafios, começando pela preparação do ambiente de desenvolvimento e explorando as principais tecnologias do ecossistema Big Data.

---

**Exercícios Práticos:**

1. Implemente um sistema de monitoramento de qualidade de dados
2. Crie uma simulação de crescimento exponencial de dados
3. Desenvolva um pipeline de anonimização de dados pessoais
4. Analise um dataset brasileiro usando os conceitos dos 5 V's

**Próximo Capítulo:** Python para Big Data - Fundamentos e Bibliotecas Essenciais
