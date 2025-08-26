# Aula 11: Análise de Grafos e Redes Complexas com Big Data

## 🎯 Objetivos de Aprendizagem

Ao concluir esta aula, você será capaz de:

- Implementar algoritmos de análise de grafos para Big Data
- Calcular métricas de centralidade e influência em redes complexas
- Detectar comunidades usando múltiplos algoritmos
- Simular propagação de informação e influência
- Desenvolver sistemas de recomendação baseados em grafos
- Visualizar redes complexas de forma interativa
- Analisar evolução temporal de redes
- Processar grafos em escala usando tecnologias distribuídas

## 📚 Conceitos Fundamentais

### 🌐 Teoria de Grafos Aplicada

**Grafos em Big Data:**
- Representação matemática de relações entre entidades
- Nós (vértices) e arestas (edges) com atributos
- Grafos direcionados vs. não-direcionados
- Grafos ponderados vs. não-ponderados
- Grafos bipartidos e multipartidos

**Métricas de Centralidade:**
- **Degree Centrality:** Número de conexões diretas
- **Betweenness Centrality:** Posição em caminhos mais curtos
- **Closeness Centrality:** Proximidade média a outros nós
- **Eigenvector Centrality:** Influência baseada em conexões importantes
- **PageRank:** Algoritmo de ranking do Google

### 🔍 Detecção de Comunidades

**Algoritmos Principais:**
- **Louvain:** Otimização de modularidade
- **Girvan-Newman:** Remoção de arestas com alta betweenness
- **Label Propagation:** Propagação de rótulos
- **Greedy Modularity:** Maximização gulosa de modularidade

**Métricas de Qualidade:**
- **Modularidade:** Medida de estrutura comunitária
- **Conductance:** Densidade interna vs. externa
- **Silhueta de Grafos:** Similaridade dentro/fora da comunidade

### 📡 Propagação e Dinâmica

**Modelos de Propagação:**
- **Threshold Models:** Adoção baseada em limiar
- **Cascade Models:** Propagação em cascata
- **Epidemic Models:** SIR, SIS para propagação viral
- **Influence Maximization:** Seleção ótima de seeds

## 🛠️ Implementação Técnica

### Estrutura da Plataforma

```python
class GraphAnalyticsPlatform:
    """
    Plataforma completa para análise de grafos
    
    Componentes:
    - Geração de redes sintéticas
    - Cálculo de métricas de centralidade
    - Detecção de comunidades
    - Simulação de propagação
    - Sistemas de recomendação
    - Visualização interativa
    """
```

### 🌐 Geração de Redes Sintéticas

**Rede Social Realística:**
```python
def generate_social_network(self, num_users=10000):
    # Modelo Barabási-Albert (scale-free)
    G = nx.barabasi_albert_graph(num_users, avg_degree // 2)
    
    # Atributos demográficos
    for node in G.nodes():
        G.nodes[node].update({
            'age': np.random.randint(16, 80),
            'interests': random_interests,
            'location': geographic_distribution,
            'influence_score': degree_based_influence
        })
```

**Rede E-commerce (Bipartida):**
```python
def generate_ecommerce_network(self, num_users, num_products):
    # Grafo bipartido usuário-produto
    B = nx.Graph()
    B.add_nodes_from(users, bipartite=0)
    B.add_nodes_from(products, bipartite=1)
    
    # Conexões baseadas em preferências
    for user in users:
        products_selected = preference_based_selection(user)
        for product in products_selected:
            B.add_edge(user, product, 
                      interaction_type=interaction,
                      rating=rating_score)
```

### 📊 Métricas de Centralidade

**Cálculo Distribuído:**
```python
def calculate_centrality_metrics(self, graph_name):
    G = self.graphs[graph_name]
    
    # Centralidades múltiplas
    metrics = {
        'degree': nx.degree_centrality(G),
        'betweenness': nx.betweenness_centrality(G, k=sample_size),
        'closeness': nx.closeness_centrality(G),
        'pagerank': nx.pagerank(G, alpha=0.85),
        'clustering': nx.clustering(G)
    }
    
    return pd.DataFrame(metrics)
```

### 🎯 Detecção de Comunidades

**Múltiplos Algoritmos:**
```python
def detect_communities(self, graph_name):
    G = self.graphs[graph_name]
    
    # Louvain (otimização de modularidade)
    louvain_communities = community_louvain.best_partition(G)
    louvain_modularity = community_louvain.modularity(louvain_communities, G)
    
    # Label Propagation
    label_prop = list(nx.community.label_propagation_communities(G))
    
    # Greedy Modularity
    greedy_communities = list(nx.community.greedy_modularity_communities(G))
    
    return {
        'louvain': louvain_communities,
        'modularity': louvain_modularity,
        'label_propagation': label_prop,
        'greedy': greedy_communities
    }
```

### 📡 Simulação de Propagação

**Modelo de Threshold:**
```python
def influence_propagation_simulation(self, initial_adopters, threshold):
    # Estado inicial
    node_states = {node: 0 for node in G.nodes()}
    for seed in initial_adopters:
        node_states[seed] = 1
    
    # Simulação iterativa
    for step in range(max_steps):
        new_adopters = []
        
        for node in non_adopters:
            # Pressão de adoção dos vizinhos
            neighbors = list(G.neighbors(node))
            adoption_pressure = sum(node_states[n] for n in neighbors) / len(neighbors)
            
            # Considera pesos das conexões
            if G.is_weighted():
                weighted_pressure = weighted_neighbor_influence(node, neighbors)
                adoption_pressure = weighted_pressure
            
            # Adoção se pressão > threshold
            if adoption_pressure >= threshold:
                new_adopters.append(node)
        
        # Atualiza estados
        for adopter in new_adopters:
            node_states[adopter] = 1
            
        if not new_adopters:
            break
    
    return propagation_results
```

### 🎁 Sistema de Recomendação

**Baseado em Grafos:**
```python
def graph_based_recommendation_system(self, user_id):
    B = self.graphs['ecommerce_network']  # Grafo bipartido
    
    # Produtos já interagidos
    user_products = get_user_products(user_id)
    
    # Usuários similares (vizinhos de 2ª ordem)
    similar_users = defaultdict(int)
    for product in user_products:
        for similar_user in B.neighbors(product):
            if similar_user != user_id:
                similarity_score = calculate_similarity(user_id, similar_user)
                similar_users[similar_user] += similarity_score
    
    # Recomendações baseadas em usuários similares
    product_scores = defaultdict(float)
    for similar_user, similarity in similar_users.items():
        for product in get_user_products(similar_user):
            if product not in user_products:
                score = similarity * product_rating_factor
                product_scores[product] += score
    
    # Diversificação por categoria
    diversified_recommendations = apply_category_diversification(product_scores)
    
    return sorted(diversified_recommendations, key=lambda x: x[1], reverse=True)
```

### 🎨 Visualização Interativa

**Plotly Networks:**
```python
def visualize_network(self, graph_name, layout='spring'):
    G = self.graphs[graph_name]
    
    # Layout do grafo
    pos = nx.spring_layout(G, k=1, iterations=50)
    
    # Cores por comunidade
    if graph_name in self.communities:
        communities = self.communities[graph_name]['louvain']
        node_colors = [communities.get(node, 0) for node in G.nodes()]
    
    # Prepara dados para Plotly
    edge_trace = create_edge_trace(G, pos)
    node_trace = create_node_trace(G, pos, node_colors)
    
    # Figura interativa
    fig = go.Figure(data=[edge_trace, node_trace],
                   layout=interactive_layout_config)
    
    return fig
```

### ⏱️ Análise Temporal

**Evolução da Rede:**
```python
def network_evolution_analysis(self, time_steps=10):
    G = self.graphs[graph_name]
    
    # Ordena nós por tempo de entrada
    nodes_by_time = sorted(G.nodes(), key=lambda x: G.nodes[x]['join_date'])
    
    evolution_metrics = []
    nodes_per_step = len(nodes_by_time) // time_steps
    
    for step in range(1, time_steps + 1):
        # Subgrafo até este momento
        current_nodes = nodes_by_time[:step * nodes_per_step]
        G_t = G.subgraph(current_nodes)
        
        # Métricas temporais
        metrics = {
            'nodes': G_t.number_of_nodes(),
            'edges': G_t.number_of_edges(),
            'density': nx.density(G_t),
            'avg_clustering': nx.average_clustering(G_t),
            'largest_component': len(max(nx.connected_components(G_t)))
        }
        
        evolution_metrics.append(metrics)
    
    return pd.DataFrame(evolution_metrics)
```

## 📈 Métricas e Análises

### 🎯 Métricas de Centralidade

| Métrica | Interpretação | Aplicação |
|---------|---------------|-----------|
| **Degree** | Popularidade local | Identificar hubs |
| **Betweenness** | Controle de fluxo | Detectar pontes |
| **Closeness** | Eficiência de comunicação | Posicionamento estratégico |
| **PageRank** | Importância global | Ranking de influência |
| **Eigenvector** | Conexões de qualidade | Prestígio social |

### 🔍 Qualidade de Comunidades

```python
# Modularidade
def calculate_modularity(G, communities):
    m = G.number_of_edges()
    modularity = 0
    
    for community in communities:
        subgraph = G.subgraph(community)
        internal_edges = subgraph.number_of_edges()
        degree_sum = sum(G.degree(node) for node in community)
        
        modularity += (internal_edges / m) - (degree_sum / (2 * m))**2
    
    return modularity

# Coverage e Performance
def community_quality_metrics(G, communities):
    total_edges = G.number_of_edges()
    internal_edges = sum(G.subgraph(comm).number_of_edges() 
                        for comm in communities)
    
    coverage = internal_edges / total_edges
    performance = calculate_performance(G, communities)
    
    return {'coverage': coverage, 'performance': performance}
```

### 📡 Análise de Propagação

```python
# Taxa de Adoção Final
def final_adoption_rate(propagation_results):
    return propagation_results['final_adopters'] / total_nodes

# Velocidade de Propagação
def propagation_velocity(adoption_history):
    return np.gradient([h['adopters'] for h in adoption_history])

# Influência dos Seeds
def seed_influence_analysis(initial_adopters, final_states):
    influence_scores = {}
    for seed in initial_adopters:
        influenced_nodes = bfs_influenced_nodes(seed, final_states)
        influence_scores[seed] = len(influenced_nodes)
    
    return influence_scores
```

## 🎯 Exercícios Práticos

### Exercício 1: Análise de Rede Social Universitária
```python
# Crie uma rede social universitária
def create_university_network():
    """
    Implemente:
    1. Rede com estudantes, professores e cursos
    2. Diferentes tipos de conexões (amizade, mentoria, matrícula)
    3. Análise de centralidade por tipo de ator
    4. Detecção de grupos de estudo
    """
    pass

# Tarefa: Identifique os alunos mais influentes
# Analise a formação natural de grupos de estudo
# Compare métricas entre estudantes e professores
```

### Exercício 2: Sistema de Recomendação Musical
```python
# Desenvolva um sistema de recomendação para música
def music_recommendation_system():
    """
    Implemente:
    1. Grafo usuário-música-artista-gênero
    2. Pesos baseados em tempo de escuta
    3. Recomendações colaborativas e de conteúdo
    4. Diversificação por gênero musical
    """
    pass

# Tarefa: Compare diferentes algoritmos de recomendação
# Avalie precisão e diversidade das recomendações
# Analise o efeito filter bubble
```

### Exercício 3: Análise de Rede de Transportes
```python
# Analise eficiência de rede de transporte público
def transport_network_analysis():
    """
    Implemente:
    1. Modelagem de estações e rotas
    2. Cálculo de centralidade de estações críticas
    3. Análise de robustez da rede
    4. Otimização de rotas
    """
    pass

# Tarefa: Identifique estações mais críticas
# Simule falhas e meça impacto na conectividade
# Proponha melhorias na rede
```

### Exercício 4: Detecção de Fraude em Transações
```python
# Use análise de grafos para detectar fraudes
def fraud_detection_network():
    """
    Implemente:
    1. Grafo de transações financeiras
    2. Detecção de padrões suspeitos
    3. Análise de comunidades anômalas
    4. Scoring de risco baseado em grafos
    """
    pass

# Tarefa: Identifique clusters de transações fraudulentas
# Desenvolva métricas de suspeição
# Avalie precisão e recall do sistema
```

## 🚀 Projeto Final: Análise Completa de Rede Social

### Especificações do Projeto

**Objetivo:** Desenvolver uma plataforma completa de análise de redes sociais

**Componentes Obrigatórios:**

1. **Coleta e Modelagem de Dados**
   - Dataset real ou sintético de rede social
   - Múltiplos tipos de relacionamentos
   - Atributos temporais e demográficos

2. **Análise de Estrutura**
   - Métricas de centralidade completas
   - Detecção de comunidades com múltiplos algoritmos
   - Análise de small-world e scale-free

3. **Dinâmica e Propagação**
   - Simulação de propagação viral
   - Análise de influenciadores
   - Modelagem de crescimento da rede

4. **Aplicações Práticas**
   - Sistema de recomendação de amizades
   - Detecção de contas falsas/bots
   - Análise de polarização e echo chambers

5. **Visualização e Interface**
   - Dashboards interativos
   - Visualizações de rede em tempo real
   - Métricas e KPIs principais

**Critérios de Avaliação:**
- Qualidade técnica da implementação (30%)
- Inovação em algoritmos e métricas (25%)
- Qualidade das visualizações (20%)
- Insights e análises (15%)
- Documentação e apresentação (10%)

## 📊 Datasets Sugeridos

### Redes Sociais Reais
- **Facebook Social Circles:** Círculos sociais do Facebook
- **Twitter Network:** Rede de seguindo/seguidores
- **Reddit Hyperlink Network:** Links entre subreddits
- **GitHub Social Network:** Colaborações em projetos

### Redes de Colaboração
- **DBLP Computer Science:** Coautorias acadêmicas
- **MovieLens:** Avaliações de filmes
- **Amazon Product Network:** Produtos relacionados
- **Citation Networks:** Citações acadêmicas

### Redes de Infraestrutura
- **Airport Networks:** Rotas aéreas mundiais
- **Power Grid:** Rede elétrica dos EUA
- **Internet AS:** Autonomous Systems da internet
- **Road Networks:** Redes rodoviárias urbanas

## 🔗 Recursos Adicionais

### Bibliotecas Python Especializadas
```python
# NetworkX - Análise de grafos
import networkx as nx

# Graph-tool - Performance otimizada
from graph_tool.all import *

# iGraph - Análise estatística
import igraph as ig

# Snap.py - Grafos em larga escala
import snap

# Karateclub - Machine Learning em grafos
from karateclub import *

# DGL - Deep Learning em grafos
import dgl
import torch
```

### Ferramentas de Visualização
```python
# Plotly - Visualizações interativas
import plotly.graph_objects as go

# Bokeh - Dashboards web
from bokeh.plotting import figure

# Pyvis - Redes interativas
from pyvis.network import Network

# Gephi (via Python)
import pygephi

# Cytoscape (via py4cytoscape)
import py4cytoscape as p4c
```

### Algoritmos Avançados
```python
# Embedding de grafos
from node2vec import Node2Vec
from gensim.models import Word2Vec

# Deep Learning em grafos
import torch_geometric
from stellargraph import StellarGraph

# Análise temporal
import networkx.algorithms.community.temporal as temporal

# Grafos probabilísticos
import networkx.algorithms.approximation as approx
```

## 📝 Conceitos Teóricos Importantes

### 🌐 Propriedades de Redes Complexas

**Small World Networks:**
- Alto clustering local + baixo caminho médio
- Característica de muitas redes reais
- Facilita propagação eficiente

**Scale-Free Networks:**
- Distribuição de grau segue lei de potência
- Poucos nós com muitas conexões (hubs)
- Robustas a falhas aleatórias, vulneráveis a ataques dirigidos

**Network Motifs:**
- Subgrafos que aparecem com frequência
- Padrões funcionais fundamentais
- Assinaturas de diferentes tipos de rede

### 🔍 Algoritmos de Clustering

**Modularidade:**
```
Q = (1/2m) Σ[A_ij - (k_i * k_j)/2m] * δ(c_i, c_j)
```

**Conductance:**
```
φ(S) = |∂S| / min(vol(S), vol(S̄))
```

### 📡 Modelos de Propagação

**Linear Threshold Model:**
- Nó adota se fração de vizinhos adotantes > threshold
- Modelagem de pressão social

**Independent Cascade Model:**
- Cada vizinho adotante tem chance independente de influenciar
- Modelagem de propagação viral

## 🎉 Conclusão

A análise de grafos é fundamental para compreender sistemas complexos em Big Data. Esta aula fornece as ferramentas necessárias para:

- Modelar relacionamentos complexos como grafos
- Extrair insights de estruturas de rede
- Desenvolver sistemas inteligentes baseados em grafos
- Visualizar e comunicar descobertas de redes

As aplicações são vastas: redes sociais, sistemas de recomendação, detecção de fraudes, análise de infraestrutura, epidemiologia computacional, e muito mais.

**Próximos Passos:**
1. Pratique com datasets reais
2. Explore algoritmos de deep learning em grafos
3. Desenvolva aplicações específicas do seu domínio
4. Contribua para bibliotecas open-source

---

**Professor:** Vagner Cordeiro  
**Disciplina:** Tópicos de Big Data em Python  
**Instituição:** Universidade do Estado de Santa Catarina (UDESC)
