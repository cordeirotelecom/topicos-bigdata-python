"""
Aula 11: Análise de Grafos e Redes Complexas com Big Data
Professor: Vagner Cordeiro
Disciplina: Tópicos de Big Data em Python

Implementação completa de algoritmos de análise de grafos para processamento
de redes complexas em larga escala, incluindo redes sociais, detecção de
comunidades, análise de influência e sistemas de recomendação baseados em grafos.
"""

import networkx as nx
import numpy as np
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import random
import json
import time
import logging
from collections import defaultdict, Counter
import community as community_louvain
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

class GraphAnalyticsPlatform:
    """
    Plataforma completa para análise de grafos e redes complexas
    
    Funcionalidades:
    - Geração de redes sintéticas realistas
    - Análise de métricas de centralidade
    - Detecção de comunidades
    - Análise de influência e propagação
    - Sistemas de recomendação baseados em grafos
    - Visualização interativa de redes
    - Processamento distribuído com PySpark
    """
    
    def __init__(self, app_name="Graph_Analytics_Platform"):
        """Inicializa a plataforma de análise de grafos"""
        
        # Configuração Spark para grafos
        self.spark = SparkSession.builder \
            .appName(app_name) \
            .config("spark.sql.adaptive.enabled", "true") \
            .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
            .config("spark.sql.shuffle.partitions", "200") \
            .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
            .getOrCreate()
        
        self.spark.sparkContext.setLogLevel("WARN")
        self.logger = self._setup_logging()
        
        # Configurações de visualização
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        # Armazenamento de grafos e métricas
        self.graphs = {}
        self.metrics = {}
        self.communities = {}
        
        print("🚀 Plataforma de Análise de Grafos inicializada!")
        print(f"📊 Spark Version: {self.spark.version}")
        print(f"🔗 NetworkX Version: {nx.__version__}")
        
    def _setup_logging(self):
        """Configura sistema de logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger(__name__)
    
    def generate_social_network(self, num_users=10000, avg_degree=50):
        """
        Gera rede social sintética com características realistas
        """
        print(f"🌐 Gerando rede social com {num_users:,} usuários...")
        
        # Modelo Barabási-Albert para rede scale-free
        G = nx.barabasi_albert_graph(num_users, avg_degree // 2)
        
        # Adiciona atributos realistas aos nós
        print("👥 Adicionando atributos de usuários...")
        
        for node in G.nodes():
            # Demografia
            age = np.random.randint(16, 80)
            gender = np.random.choice(['M', 'F'], p=[0.49, 0.51])
            
            # Interesses (simulando clusters temáticos)
            interests = np.random.choice([
                'technology', 'sports', 'music', 'travel', 'food',
                'art', 'science', 'politics', 'entertainment', 'health'
            ], size=np.random.randint(2, 6), replace=False).tolist()
            
            # Localização (simulando distribuição geográfica)
            location = np.random.choice([
                'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador',
                'Brasília', 'Fortaleza', 'Curitiba', 'Recife', 'Porto Alegre',
                'Florianópolis', 'Goiânia', 'Belém'
            ], p=[0.2, 0.12, 0.05, 0.04, 0.04, 0.04, 0.04, 0.03, 0.03, 0.02, 0.02, 0.02])
            
            # Nível de atividade
            activity_level = np.random.choice(['low', 'medium', 'high'], p=[0.3, 0.5, 0.2])
            
            # Influência baseada no grau do nó
            degree = G.degree(node)
            influence_score = min(100, degree * np.random.uniform(0.5, 2.0))
            
            G.nodes[node].update({
                'age': age,
                'gender': gender,
                'interests': interests,
                'location': location,
                'activity_level': activity_level,
                'influence_score': influence_score,
                'join_date': datetime.now() - timedelta(days=np.random.randint(1, 3650))
            })
        
        # Adiciona pesos às arestas (força da conexão)
        print("🔗 Adicionando pesos às conexões...")
        
        for edge in G.edges():
            user1, user2 = edge
            
            # Peso baseado em interesses comuns e proximidade geográfica
            interests1 = set(G.nodes[user1]['interests'])
            interests2 = set(G.nodes[user2]['interests'])
            common_interests = len(interests1.intersection(interests2))
            
            same_location = G.nodes[user1]['location'] == G.nodes[user2]['location']
            age_similarity = 1 / (1 + abs(G.nodes[user1]['age'] - G.nodes[user2]['age']) / 10)
            
            # Peso composto
            weight = (common_interests * 0.4 + 
                     (2 if same_location else 0.5) * 0.3 + 
                     age_similarity * 0.3) * np.random.uniform(0.7, 1.3)
            
            G.edges[edge]['weight'] = round(weight, 3)
            G.edges[edge]['interaction_count'] = np.random.poisson(weight * 10)
            G.edges[edge]['last_interaction'] = datetime.now() - timedelta(days=np.random.randint(1, 365))
        
        self.graphs['social_network'] = G
        
        print(f"✅ Rede social gerada com sucesso!")
        print(f"👥 Nós: {G.number_of_nodes():,}")
        print(f"🔗 Arestas: {G.number_of_edges():,}")
        print(f"📊 Grau médio: {2 * G.number_of_edges() / G.number_of_nodes():.2f}")
        print(f"🌐 Densidade: {nx.density(G):.6f}")
        
        return G
    
    def generate_ecommerce_network(self, num_users=5000, num_products=1000):
        """
        Gera rede bipartida usuário-produto para e-commerce
        """
        print(f"🛒 Gerando rede de e-commerce...")
        print(f"👥 Usuários: {num_users:,}")
        print(f"📦 Produtos: {num_products:,}")
        
        # Grafo bipartido
        B = nx.Graph()
        
        # Adiciona nós de usuários
        user_nodes = [f"user_{i}" for i in range(num_users)]
        B.add_nodes_from(user_nodes, bipartite=0, node_type='user')
        
        # Adiciona nós de produtos
        product_nodes = [f"product_{i}" for i in range(num_products)]
        B.add_nodes_from(product_nodes, bipartite=1, node_type='product')
        
        # Categorias de produtos
        categories = [
            'electronics', 'clothing', 'home', 'sports', 'books',
            'health', 'automotive', 'toys', 'beauty', 'food'
        ]
        
        # Atributos dos produtos
        for product in product_nodes:
            B.nodes[product].update({
                'category': np.random.choice(categories),
                'price': round(np.random.lognormal(3, 1), 2),
                'rating': round(np.random.normal(4.0, 0.8), 1),
                'num_reviews': np.random.poisson(50),
                'launch_date': datetime.now() - timedelta(days=np.random.randint(1, 1825))
            })
        
        # Atributos dos usuários
        for user in user_nodes:
            preferred_categories = np.random.choice(
                categories, 
                size=np.random.randint(2, 5), 
                replace=False
            ).tolist()
            
            B.nodes[user].update({
                'age': np.random.randint(18, 70),
                'preferred_categories': preferred_categories,
                'spending_level': np.random.choice(['low', 'medium', 'high'], p=[0.4, 0.4, 0.2]),
                'account_age': np.random.randint(1, 2000)
            })
        
        # Gera conexões usuário-produto (compras/visualizações)
        print("🔗 Gerando interações usuário-produto...")
        
        for user in user_nodes:
            user_prefs = B.nodes[user]['preferred_categories']
            spending = B.nodes[user]['spending_level']
            
            # Número de produtos com que interage
            if spending == 'high':
                num_interactions = np.random.poisson(20)
            elif spending == 'medium':
                num_interactions = np.random.poisson(10)
            else:
                num_interactions = np.random.poisson(5)
            
            # Seleciona produtos preferencialmente da categoria preferida
            available_products = []
            for product in product_nodes:
                if B.nodes[product]['category'] in user_prefs:
                    available_products.extend([product] * 3)  # 3x mais provável
                else:
                    available_products.append(product)
            
            # Adiciona arestas
            selected_products = np.random.choice(
                available_products, 
                size=min(num_interactions, len(product_nodes)), 
                replace=False
            )
            
            for product in selected_products:
                interaction_type = np.random.choice(
                    ['view', 'cart', 'purchase'], 
                    p=[0.6, 0.25, 0.15]
                )
                
                rating = None
                if interaction_type == 'purchase':
                    rating = np.random.randint(1, 6)
                
                B.add_edge(user, product, 
                          interaction_type=interaction_type,
                          rating=rating,
                          timestamp=datetime.now() - timedelta(days=np.random.randint(1, 365)))
        
        self.graphs['ecommerce_network'] = B
        
        print(f"✅ Rede de e-commerce gerada!")
        print(f"🔗 Interações: {B.number_of_edges():,}")
        
        return B
    
    def calculate_centrality_metrics(self, graph_name='social_network'):
        """
        Calcula métricas de centralidade para análise de influência
        """
        print(f"📊 Calculando métricas de centralidade para {graph_name}...")
        
        G = self.graphs[graph_name]
        
        # Centralidades básicas
        print("🔢 Calculando centralidades básicas...")
        degree_centrality = nx.degree_centrality(G)
        betweenness_centrality = nx.betweenness_centrality(G, k=min(1000, G.number_of_nodes()))
        closeness_centrality = nx.closeness_centrality(G)
        
        # Eigenvector centrality (pode falhar em grafos desconectados)
        try:
            eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)
        except:
            print("⚠️ Eigenvector centrality falhou, usando grau normalizado")
            eigenvector_centrality = degree_centrality
        
        # PageRank
        print("🔍 Calculando PageRank...")
        pagerank = nx.pagerank(G, alpha=0.85, max_iter=1000)
        
        # Clustering coefficient
        print("🌐 Calculando coeficientes de clustering...")
        clustering = nx.clustering(G)
        
        # Combina métricas em DataFrame
        nodes = list(G.nodes())
        
        centrality_df = pd.DataFrame({
            'node': nodes,
            'degree': [G.degree(node) for node in nodes],
            'degree_centrality': [degree_centrality[node] for node in nodes],
            'betweenness_centrality': [betweenness_centrality[node] for node in nodes],
            'closeness_centrality': [closeness_centrality[node] for node in nodes],
            'eigenvector_centrality': [eigenvector_centrality[node] for node in nodes],
            'pagerank': [pagerank[node] for node in nodes],
            'clustering_coefficient': [clustering[node] for node in nodes]
        })
        
        # Adiciona atributos dos nós se disponíveis
        if graph_name == 'social_network':
            centrality_df['age'] = [G.nodes[node]['age'] for node in nodes]
            centrality_df['location'] = [G.nodes[node]['location'] for node in nodes]
            centrality_df['influence_score'] = [G.nodes[node]['influence_score'] for node in nodes]
        
        self.metrics[f'{graph_name}_centrality'] = centrality_df
        
        print("📈 Análise estatística das centralidades:")
        print(centrality_df[['degree_centrality', 'betweenness_centrality', 
                           'closeness_centrality', 'pagerank']].describe())
        
        # Top influenciadores
        print("\n🌟 Top 10 Influenciadores (PageRank):")
        top_influencers = centrality_df.nlargest(10, 'pagerank')
        for idx, row in top_influencers.iterrows():
            print(f"  Nó {row['node']}: PageRank = {row['pagerank']:.6f}, Grau = {row['degree']}")
        
        return centrality_df
    
    def detect_communities(self, graph_name='social_network'):
        """
        Detecção de comunidades usando múltiplos algoritmos
        """
        print(f"🔍 Detectando comunidades em {graph_name}...")
        
        G = self.graphs[graph_name]
        
        # Algoritmo de Louvain
        print("🎯 Aplicando algoritmo de Louvain...")
        louvain_communities = community_louvain.best_partition(G)
        louvain_modularity = community_louvain.modularity(louvain_communities, G)
        
        # Girvan-Newman (para grafos menores)
        girvan_newman_communities = None
        if G.number_of_nodes() <= 1000:
            print("🌊 Aplicando algoritmo Girvan-Newman...")
            communities_generator = nx.community.girvan_newman(G)
            girvan_newman_communities = next(communities_generator)
        
        # Label Propagation
        print("📢 Aplicando Label Propagation...")
        label_prop_communities = list(nx.community.label_propagation_communities(G))
        
        # Greedy Modularity
        print("🎢 Aplicando Greedy Modularity...")
        greedy_communities = list(nx.community.greedy_modularity_communities(G))
        
        # Análise das comunidades Louvain
        num_louvain_communities = len(set(louvain_communities.values()))
        community_sizes = Counter(louvain_communities.values())
        
        print(f"\n📊 Resultados da Detecção de Comunidades:")
        print(f"🎯 Louvain: {num_louvain_communities} comunidades (Modularidade: {louvain_modularity:.4f})")
        print(f"📢 Label Propagation: {len(label_prop_communities)} comunidades")
        print(f"🎢 Greedy Modularity: {len(greedy_communities)} comunidades")
        
        if girvan_newman_communities:
            print(f"🌊 Girvan-Newman: {len(girvan_newman_communities)} comunidades")
        
        # Distribuição do tamanho das comunidades
        print(f"\n📏 Distribuição do tamanho das comunidades (Louvain):")
        size_distribution = Counter(community_sizes.values())
        for size, count in sorted(size_distribution.items()):
            print(f"  Tamanho {size}: {count} comunidades")
        
        # Armazena resultados
        community_results = {
            'louvain': louvain_communities,
            'louvain_modularity': louvain_modularity,
            'label_propagation': label_prop_communities,
            'greedy_modularity': greedy_communities,
            'girvan_newman': girvan_newman_communities
        }
        
        self.communities[graph_name] = community_results
        
        # Análise das características das comunidades
        if graph_name == 'social_network':
            self._analyze_community_characteristics(G, louvain_communities)
        
        return community_results
    
    def _analyze_community_characteristics(self, G, communities):
        """
        Analisa características demográficas das comunidades
        """
        print("\n👥 Análise das características das comunidades:")
        
        community_stats = defaultdict(lambda: {
            'size': 0,
            'ages': [],
            'locations': [],
            'interests': [],
            'avg_influence': 0
        })
        
        # Coleta dados por comunidade
        for node, community_id in communities.items():
            attrs = G.nodes[node]
            community_stats[community_id]['size'] += 1
            community_stats[community_id]['ages'].append(attrs['age'])
            community_stats[community_id]['locations'].append(attrs['location'])
            community_stats[community_id]['interests'].extend(attrs['interests'])
        
        # Top 5 maiores comunidades
        top_communities = sorted(community_stats.items(), 
                               key=lambda x: x[1]['size'], reverse=True)[:5]
        
        for comm_id, stats in top_communities:
            print(f"\n📍 Comunidade {comm_id} (Tamanho: {stats['size']}):")
            
            # Idade média
            avg_age = np.mean(stats['ages'])
            print(f"  Idade média: {avg_age:.1f} anos")
            
            # Localização mais comum
            location_counter = Counter(stats['locations'])
            top_location = location_counter.most_common(1)[0]
            print(f"  Localização principal: {top_location[0]} ({top_location[1]}/{stats['size']})")
            
            # Interesses mais comuns
            interest_counter = Counter(stats['interests'])
            top_interests = interest_counter.most_common(3)
            print(f"  Interesses principais: {[i[0] for i in top_interests]}")
    
    def influence_propagation_simulation(self, graph_name='social_network', 
                                      initial_adopters=10, threshold=0.3, max_steps=20):
        """
        Simula propagação de influência/informação na rede
        """
        print(f"📡 Simulando propagação de influência em {graph_name}...")
        
        G = self.graphs[graph_name]
        
        # Seleciona adotantes iniciais (nós com maior PageRank)
        if f'{graph_name}_centrality' not in self.metrics:
            self.calculate_centrality_metrics(graph_name)
        
        centrality_df = self.metrics[f'{graph_name}_centrality']
        initial_nodes = centrality_df.nlargest(initial_adopters, 'pagerank')['node'].tolist()
        
        print(f"🎯 Iniciando com {initial_adopters} adotantes iniciais")
        print(f"🚪 Threshold de adoção: {threshold}")
        
        # Estado dos nós: 0 = não-adotante, 1 = adotante
        node_states = {node: 0 for node in G.nodes()}
        for node in initial_nodes:
            node_states[node] = 1
        
        adoption_history = []
        step = 0
        
        while step < max_steps:
            adopters_count = sum(node_states.values())
            adoption_history.append({
                'step': step,
                'adopters': adopters_count,
                'percentage': adopters_count / G.number_of_nodes() * 100
            })
            
            print(f"  Passo {step}: {adopters_count:,} adotantes ({adopters_count/G.number_of_nodes()*100:.1f}%)")
            
            new_adopters = []
            
            # Para cada não-adotante, verifica se deve adotar
            for node in G.nodes():
                if node_states[node] == 0:  # Não-adotante
                    neighbors = list(G.neighbors(node))
                    if len(neighbors) == 0:
                        continue
                    
                    # Calcula proporção de vizinhos adotantes
                    adopter_neighbors = sum(node_states[neighbor] for neighbor in neighbors)
                    adoption_pressure = adopter_neighbors / len(neighbors)
                    
                    # Considera peso das conexões se disponível
                    if G.is_weighted():
                        weighted_pressure = 0
                        total_weight = 0
                        for neighbor in neighbors:
                            weight = G[node][neighbor].get('weight', 1)
                            weighted_pressure += node_states[neighbor] * weight
                            total_weight += weight
                        
                        if total_weight > 0:
                            adoption_pressure = weighted_pressure / total_weight
                    
                    # Adiciona influência pessoal do nó
                    if 'influence_score' in G.nodes[node]:
                        personal_influence = G.nodes[node]['influence_score'] / 100
                        adoption_pressure *= (1 + personal_influence * 0.1)
                    
                    # Adota se pressão excede threshold
                    if adoption_pressure >= threshold:
                        new_adopters.append(node)
            
            # Atualiza estados
            if not new_adopters:
                print("  🛑 Propagação estabilizada (sem novos adotantes)")
                break
            
            for node in new_adopters:
                node_states[node] = 1
            
            step += 1
        
        # Estatísticas finais
        final_adopters = sum(node_states.values())
        final_percentage = final_adopters / G.number_of_nodes() * 100
        
        print(f"\n📊 Resultados da Propagação:")
        print(f"  Adotantes finais: {final_adopters:,} ({final_percentage:.1f}%)")
        print(f"  Passos até estabilização: {step}")
        print(f"  Taxa de crescimento: {(final_adopters - initial_adopters) / initial_adopters * 100:.1f}%")
        
        propagation_results = {
            'initial_adopters': initial_adopters,
            'final_adopters': final_adopters,
            'final_percentage': final_percentage,
            'steps': step,
            'history': adoption_history,
            'final_states': node_states
        }
        
        return propagation_results
    
    def graph_based_recommendation_system(self, user_id, graph_name='ecommerce_network', 
                                        num_recommendations=10):
        """
        Sistema de recomendação baseado em análise de grafos
        """
        print(f"🎯 Gerando recomendações para usuário {user_id}...")
        
        if graph_name not in self.graphs:
            self.generate_ecommerce_network()
        
        B = self.graphs[graph_name]  # Grafo bipartido
        
        if user_id not in B.nodes():
            print(f"❌ Usuário {user_id} não encontrado na rede")
            return []
        
        # Produtos já interagidos pelo usuário
        user_products = set()
        for neighbor in B.neighbors(user_id):
            if B.nodes[neighbor]['node_type'] == 'product':
                user_products.add(neighbor)
        
        print(f"📦 Usuário já interagiu com {len(user_products)} produtos")
        
        # Encontra usuários similares (vizinhos de segunda ordem)
        similar_users = defaultdict(int)
        
        for product in user_products:
            for user in B.neighbors(product):
                if (user != user_id and 
                    B.nodes[user]['node_type'] == 'user'):
                    
                    # Pontuação baseada em interações comuns
                    interaction_weight = 1
                    if 'weight' in B[user_id][product]:
                        interaction_weight = B[user_id][product]['weight']
                    
                    similar_users[user] += interaction_weight
        
        # Top usuários similares
        top_similar_users = sorted(similar_users.items(), 
                                 key=lambda x: x[1], reverse=True)[:20]
        
        print(f"👥 Encontrados {len(top_similar_users)} usuários similares")
        
        # Recomendações baseadas em usuários similares
        product_scores = defaultdict(float)
        
        for similar_user, similarity_score in top_similar_users:
            for neighbor in B.neighbors(similar_user):
                if (B.nodes[neighbor]['node_type'] == 'product' and 
                    neighbor not in user_products):
                    
                    # Score baseado em similaridade e rating do produto
                    base_score = similarity_score
                    
                    # Considera rating se disponível
                    edge_data = B[similar_user][neighbor]
                    if edge_data.get('rating'):
                        base_score *= (edge_data['rating'] / 5.0)
                    
                    # Considera popularidade do produto
                    product_degree = B.degree(neighbor)
                    popularity_factor = min(2.0, product_degree / 10.0)
                    
                    product_scores[neighbor] += base_score * popularity_factor
        
        # Aplica diversificação por categoria
        user_categories = B.nodes[user_id]['preferred_categories']
        
        for product, score in product_scores.items():
            product_category = B.nodes[product]['category']
            
            # Boost para categorias preferidas
            if product_category in user_categories:
                product_scores[product] *= 1.5
            
            # Considera rating médio do produto
            if 'rating' in B.nodes[product]:
                rating_factor = B.nodes[product]['rating'] / 5.0
                product_scores[product] *= rating_factor
        
        # Top recomendações
        recommendations = sorted(product_scores.items(), 
                               key=lambda x: x[1], reverse=True)[:num_recommendations]
        
        print(f"🎁 Geradas {len(recommendations)} recomendações")
        
        # Formata resultados
        recommendation_list = []
        for product, score in recommendations:
            product_info = B.nodes[product]
            recommendation_list.append({
                'product_id': product,
                'score': round(score, 3),
                'category': product_info['category'],
                'price': product_info['price'],
                'rating': product_info['rating'],
                'num_reviews': product_info['num_reviews']
            })
        
        print("\n🏆 Top 5 Recomendações:")
        for i, rec in enumerate(recommendation_list[:5]):
            print(f"  {i+1}. {rec['product_id']} ({rec['category']})")
            print(f"     Score: {rec['score']}, Preço: ${rec['price']}, Rating: {rec['rating']}")
        
        return recommendation_list
    
    def visualize_network(self, graph_name='social_network', layout='spring', 
                         show_communities=True, sample_size=500):
        """
        Visualização interativa da rede usando Plotly
        """
        print(f"🎨 Criando visualização da rede {graph_name}...")
        
        G = self.graphs[graph_name]
        
        # Amostra do grafo para visualização (se muito grande)
        if G.number_of_nodes() > sample_size:
            print(f"📊 Amostrando {sample_size} nós para visualização...")
            nodes_sample = random.sample(list(G.nodes()), sample_size)
            G_vis = G.subgraph(nodes_sample).copy()
        else:
            G_vis = G
        
        # Layout do grafo
        if layout == 'spring':
            pos = nx.spring_layout(G_vis, k=1, iterations=50)
        elif layout == 'circular':
            pos = nx.circular_layout(G_vis)
        elif layout == 'kamada_kawai':
            pos = nx.kamada_kawai_layout(G_vis)
        else:
            pos = nx.random_layout(G_vis)
        
        # Cores dos nós
        if show_communities and graph_name in self.communities:
            communities = self.communities[graph_name]['louvain']
            node_colors = [communities.get(node, 0) for node in G_vis.nodes()]
        else:
            node_colors = ['lightblue'] * G_vis.number_of_nodes()
        
        # Tamanho dos nós baseado no grau
        node_sizes = [G_vis.degree(node) * 5 + 10 for node in G_vis.nodes()]
        
        # Prepara dados para Plotly
        edge_x = []
        edge_y = []
        for edge in G_vis.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
        
        node_x = [pos[node][0] for node in G_vis.nodes()]
        node_y = [pos[node][1] for node in G_vis.nodes()]
        
        # Informações dos nós para hover
        node_info = []
        for node in G_vis.nodes():
            if graph_name == 'social_network':
                info = f"Nó: {node}<br>Grau: {G_vis.degree(node)}<br>"
                info += f"Idade: {G_vis.nodes[node]['age']}<br>"
                info += f"Localização: {G_vis.nodes[node]['location']}"
            else:
                info = f"Nó: {node}<br>Grau: {G_vis.degree(node)}"
            node_info.append(info)
        
        # Cria figura Plotly
        fig = go.Figure()
        
        # Adiciona arestas
        fig.add_trace(go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='lightgray'),
            hoverinfo='none',
            mode='lines',
            showlegend=False
        ))
        
        # Adiciona nós
        fig.add_trace(go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            text=node_info,
            marker=dict(
                size=node_sizes,
                color=node_colors,
                colorscale='Viridis' if show_communities else None,
                line=dict(width=1, color='black')
            ),
            showlegend=False
        ))
        
        # Layout da figura
        fig.update_layout(
            title=f'Visualização da Rede {graph_name.title()}',
            titlefont_size=16,
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20,l=5,r=5,t=40),
            annotations=[
                dict(
                    text=f"Nós: {G_vis.number_of_nodes():,} | Arestas: {G_vis.number_of_edges():,}",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002,
                    xanchor='left', yanchor='bottom',
                    font=dict(size=12)
                )
            ],
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            plot_bgcolor='white'
        )
        
        fig.show()
        
        return fig
    
    def network_evolution_analysis(self, graph_name='social_network', time_steps=10):
        """
        Simula e analisa a evolução temporal da rede
        """
        print(f"⏱️ Analisando evolução temporal da rede {graph_name}...")
        
        G = self.graphs[graph_name]
        
        # Simula crescimento da rede ao longo do tempo
        evolution_metrics = []
        
        # Ordena nós por data de entrada (simulada)
        if graph_name == 'social_network':
            nodes_by_time = sorted(G.nodes(), 
                                 key=lambda x: G.nodes[x]['join_date'])
        else:
            nodes_by_time = list(G.nodes())
        
        # Análise em time steps
        nodes_per_step = len(nodes_by_time) // time_steps
        
        for step in range(1, time_steps + 1):
            # Subgrafo até este ponto no tempo
            end_idx = step * nodes_per_step
            current_nodes = nodes_by_time[:end_idx]
            G_t = G.subgraph(current_nodes)
            
            # Calcula métricas da rede
            num_nodes = G_t.number_of_nodes()
            num_edges = G_t.number_of_edges()
            
            if num_nodes > 1 and num_edges > 0:
                density = nx.density(G_t)
                avg_clustering = nx.average_clustering(G_t)
                
                # Componente gigante
                components = list(nx.connected_components(G_t))
                largest_component_size = len(max(components, key=len)) if components else 0
                
                # Diâmetro (aproximado para grafos grandes)
                try:
                    if largest_component_size > 1000:
                        # Approximação para grafos grandes
                        diameter = nx.approximation.diameter(G_t)
                    else:
                        diameter = nx.diameter(G_t) if nx.is_connected(G_t) else np.inf
                except:
                    diameter = np.inf
                
                avg_degree = 2 * num_edges / num_nodes if num_nodes > 0 else 0
                
            else:
                density = avg_clustering = avg_degree = diameter = 0
                largest_component_size = num_nodes
            
            evolution_metrics.append({
                'time_step': step,
                'nodes': num_nodes,
                'edges': num_edges,
                'density': density,
                'avg_clustering': avg_clustering,
                'avg_degree': avg_degree,
                'largest_component': largest_component_size,
                'diameter': diameter if diameter != np.inf else None
            })
            
            print(f"  Passo {step}: {num_nodes:,} nós, {num_edges:,} arestas")
        
        # Cria DataFrame para análise
        evolution_df = pd.DataFrame(evolution_metrics)
        
        # Visualização da evolução
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=['Crescimento da Rede', 'Densidade e Clustering', 
                           'Grau Médio', 'Componente Gigante'],
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # Gráfico 1: Crescimento
        fig.add_trace(
            go.Scatter(x=evolution_df['time_step'], y=evolution_df['nodes'],
                      mode='lines+markers', name='Nós', line=dict(color='blue')),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(x=evolution_df['time_step'], y=evolution_df['edges'],
                      mode='lines+markers', name='Arestas', line=dict(color='red')),
            row=1, col=1
        )
        
        # Gráfico 2: Densidade e Clustering
        fig.add_trace(
            go.Scatter(x=evolution_df['time_step'], y=evolution_df['density'],
                      mode='lines+markers', name='Densidade', line=dict(color='green')),
            row=1, col=2
        )
        fig.add_trace(
            go.Scatter(x=evolution_df['time_step'], y=evolution_df['avg_clustering'],
                      mode='lines+markers', name='Clustering', line=dict(color='orange')),
            row=1, col=2
        )
        
        # Gráfico 3: Grau Médio
        fig.add_trace(
            go.Scatter(x=evolution_df['time_step'], y=evolution_df['avg_degree'],
                      mode='lines+markers', name='Grau Médio', line=dict(color='purple')),
            row=2, col=1
        )
        
        # Gráfico 4: Componente Gigante
        fig.add_trace(
            go.Scatter(x=evolution_df['time_step'], y=evolution_df['largest_component'],
                      mode='lines+markers', name='Componente Gigante', line=dict(color='brown')),
            row=2, col=2
        )
        
        fig.update_layout(height=600, title_text="Evolução Temporal da Rede")
        fig.show()
        
        print(f"\n📊 Análise da Evolução:")
        print(f"  Crescimento de nós: {evolution_df['nodes'].iloc[-1] / evolution_df['nodes'].iloc[0]:.2f}x")
        print(f"  Crescimento de arestas: {evolution_df['edges'].iloc[-1] / evolution_df['edges'].iloc[0]:.2f}x")
        print(f"  Densidade final: {evolution_df['density'].iloc[-1]:.6f}")
        print(f"  Clustering final: {evolution_df['avg_clustering'].iloc[-1]:.4f}")
        
        return evolution_df
    
    def run_complete_graph_analysis(self):
        """
        Executa análise completa de grafos e redes
        """
        print("🚀 INICIANDO ANÁLISE COMPLETA DE GRAFOS E REDES")
        print("="*60)
        
        results = {}
        
        # 1. Gera redes sintéticas
        print("\n1️⃣ GERAÇÃO DE REDES SINTÉTICAS")
        print("-" * 40)
        social_network = self.generate_social_network(num_users=5000)
        ecommerce_network = self.generate_ecommerce_network(num_users=2000, num_products=500)
        
        # 2. Análise de centralidade
        print("\n2️⃣ ANÁLISE DE CENTRALIDADE")
        print("-" * 40)
        results['centrality'] = self.calculate_centrality_metrics('social_network')
        
        # 3. Detecção de comunidades
        print("\n3️⃣ DETECÇÃO DE COMUNIDADES")
        print("-" * 40)
        results['communities'] = self.detect_communities('social_network')
        
        # 4. Propagação de influência
        print("\n4️⃣ SIMULAÇÃO DE PROPAGAÇÃO")
        print("-" * 40)
        results['propagation'] = self.influence_propagation_simulation('social_network')
        
        # 5. Sistema de recomendação
        print("\n5️⃣ SISTEMA DE RECOMENDAÇÃO")
        print("-" * 40)
        sample_user = "user_0"
        results['recommendations'] = self.graph_based_recommendation_system(sample_user)
        
        # 6. Evolução temporal
        print("\n6️⃣ EVOLUÇÃO TEMPORAL")
        print("-" * 40)
        results['evolution'] = self.network_evolution_analysis('social_network')
        
        # 7. Visualização
        print("\n7️⃣ VISUALIZAÇÃO DA REDE")
        print("-" * 40)
        results['visualization'] = self.visualize_network('social_network', sample_size=300)
        
        print("\n🎉 ANÁLISE COMPLETA FINALIZADA!")
        print("="*60)
        print("📊 Resumo dos Resultados:")
        print(f"🌐 Rede Social: {social_network.number_of_nodes():,} nós, {social_network.number_of_edges():,} arestas")
        print(f"🛒 Rede E-commerce: {ecommerce_network.number_of_nodes():,} nós, {ecommerce_network.number_of_edges():,} arestas")
        print(f"🎯 Comunidades detectadas: {len(set(results['communities']['louvain'].values()))}")
        print(f"📡 Propagação final: {results['propagation']['final_percentage']:.1f}% da rede")
        print(f"🎁 Recomendações geradas: {len(results['recommendations'])}")
        
        return results
    
    def cleanup(self):
        """Limpa recursos e finaliza Spark"""
        print("\n🧹 Finalizando recursos...")
        self.spark.stop()
        print("✅ Análise de grafos finalizada!")

# Demonstração principal
if __name__ == "__main__":
    # Inicializa plataforma
    graph_platform = GraphAnalyticsPlatform("Graph_Analytics_Demo")
    
    try:
        # Executa análise completa
        results = graph_platform.run_complete_graph_analysis()
        
        print(f"\n📈 Análise de Grafos executada com sucesso!")
        print(f"Algoritmos aplicados: Centralidade, Comunidades, Propagação, Recomendação")
        print(f"Redes analisadas: Social e E-commerce")
        print(f"Visualizações geradas: Layouts interativos")
        
    except Exception as e:
        print(f"❌ Erro durante execução: {e}")
        
    finally:
        # Cleanup
        graph_platform.cleanup()

"""
CONCEITOS AVANÇADOS DEMONSTRADOS:

1. 🌐 ANÁLISE DE REDES SOCIAIS
   - Métricas de centralidade (degree, betweenness, closeness, PageRank)
   - Detecção de comunidades (Louvain, Girvan-Newman, Label Propagation)
   - Análise de influência e propagação
   - Características demográficas de comunidades

2. 🛒 REDES DE E-COMMERCE
   - Grafos bipartidos usuário-produto
   - Sistemas de recomendação baseados em grafos
   - Análise de padrões de compra
   - Filtragem colaborativa

3. 📊 ALGORITMOS DE GRAFOS
   - Cálculo distribuído de métricas
   - Algoritmos de clustering
   - Simulação de processos dinâmicos
   - Análise de evolução temporal

4. 🎨 VISUALIZAÇÃO INTERATIVA
   - Layouts de grafos (spring, circular, force-directed)
   - Plotly para visualizações web
   - Mapeamento de cores por comunidades
   - Informações hover detalhadas

5. ⚡ PERFORMANCE E ESCALABILIDADE
   - Processamento distribuído com Spark
   - Otimizações para grafos grandes
   - Sampling para visualização
   - Algoritmos aproximados

APLICAÇÕES REAIS:
- Análise de redes sociais
- Sistemas de recomendação
- Detecção de fraudes
- Marketing viral
- Análise de influenciadores
- Estudos epidemiológicos
- Redes de transporte
- Análise organizacional
"""
