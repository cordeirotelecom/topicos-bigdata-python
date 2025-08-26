# CAPÍTULO 4: HADOOP E HDFS - FUNDAMENTOS DO BIG DATA

## 4.1 Introdução ao Apache Hadoop

O Apache Hadoop é um framework de software de código aberto para armazenamento distribuído e processamento de grandes conjuntos de dados usando clusters de computadores. É a base da maioria das soluções de Big Data modernas.

### 4.1.1 História e Evolução

```python
# Timeline do Hadoop
timeline_hadoop = {
    2003: "Google publica paper sobre GFS (Google File System)",
    2004: "Google publica paper sobre MapReduce",
    2006: "Doug Cutting cria o Hadoop na Yahoo!",
    2008: "Hadoop torna-se projeto Apache top-level",
    2011: "Lançamento do Hadoop 1.0",
    2013: "Hadoop 2.0 com YARN",
    2017: "Hadoop 3.0 com melhorias de performance",
    2025: "Hadoop 4.0 (planejado) com IA nativa"
}

for ano, evento in timeline_hadoop.items():
    print(f"{ano}: {evento}")
```

### 4.1.2 Arquitetura do Hadoop

O Hadoop é composto por quatro módulos principais:

1. **Hadoop Common**: Bibliotecas e utilitários
2. **HDFS**: Sistema de arquivos distribuído
3. **YARN**: Gerenciador de recursos
4. **MapReduce**: Framework de processamento

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(1, 1, figsize=(14, 10))

# Desenha arquitetura do Hadoop
def draw_hadoop_architecture():
    # Aplicações
    apps = patches.Rectangle((1, 8), 12, 1.5, linewidth=2, 
                           edgecolor='blue', facecolor='lightblue')
    ax.add_patch(apps)
    ax.text(7, 8.75, 'APLICAÇÕES\n(Pig, Hive, HBase, Spark)', 
           ha='center', va='center', fontweight='bold')
    
    # YARN
    yarn = patches.Rectangle((1, 6), 12, 1.5, linewidth=2, 
                           edgecolor='green', facecolor='lightgreen')
    ax.add_patch(yarn)
    ax.text(7, 6.75, 'YARN\n(Yet Another Resource Negotiator)', 
           ha='center', va='center', fontweight='bold')
    
    # MapReduce
    mapred = patches.Rectangle((1, 4), 5.5, 1.5, linewidth=2, 
                             edgecolor='orange', facecolor='lightyellow')
    ax.add_patch(mapred)
    ax.text(3.75, 4.75, 'MapReduce', ha='center', va='center', fontweight='bold')
    
    # HDFS
    hdfs = patches.Rectangle((7.5, 4), 5.5, 1.5, linewidth=2, 
                           edgecolor='red', facecolor='lightcoral')
    ax.add_patch(hdfs)
    ax.text(10.25, 4.75, 'HDFS', ha='center', va='center', fontweight='bold')
    
    # Hadoop Common
    common = patches.Rectangle((1, 2), 12, 1.5, linewidth=2, 
                             edgecolor='purple', facecolor='plum')
    ax.add_patch(common)
    ax.text(7, 2.75, 'HADOOP COMMON\n(Bibliotecas e Utilitários)', 
           ha='center', va='center', fontweight='bold')
    
    ax.set_xlim(0, 14)
    ax.set_ylim(1, 10)
    ax.set_title('Arquitetura do Apache Hadoop', fontsize=16, fontweight='bold')
    ax.axis('off')

draw_hadoop_architecture()
plt.tight_layout()
plt.show()
```

## 4.2 HDFS - Hadoop Distributed File System

O HDFS é um sistema de arquivos distribuído projetado para armazenar arquivos muito grandes em clusters de hardware commodity.

### 4.2.1 Características Principais

```python
class HDFSCharacteristics:
    """
    Demonstra as características principais do HDFS
    """
    
    def __init__(self):
        self.characteristics = {
            'fault_tolerance': {
                'description': 'Tolerância a falhas através de replicação',
                'default_replication': 3,
                'automatic_recovery': True
            },
            'scalability': {
                'description': 'Escalabilidade horizontal',
                'max_nodes': 'Milhares de nós',
                'max_files': 'Centenas de milhões'
            },
            'high_throughput': {
                'description': 'Alto throughput para acesso sequencial',
                'optimized_for': 'Leitura/escrita de grandes arquivos',
                'block_size': '128MB (padrão)'
            },
            'write_once_read_many': {
                'description': 'Modelo de escrita única, múltiplas leituras',
                'append_support': 'Limitado',
                'random_writes': 'Não suportado'
            }
        }
    
    def display_characteristics(self):
        """Exibe características do HDFS"""
        print("🗂️ CARACTERÍSTICAS DO HDFS")
        print("=" * 50)
        
        for key, value in self.characteristics.items():
            print(f"\n📋 {key.upper().replace('_', ' ')}")
            print(f"   Descrição: {value['description']}")
            
            for attr, val in value.items():
                if attr != 'description':
                    print(f"   {attr.replace('_', ' ').title()}: {val}")

# Demonstração
hdfs_demo = HDFSCharacteristics()
hdfs_demo.display_characteristics()
```

### 4.2.2 Arquitetura do HDFS

```python
import numpy as np
import pandas as pd
from datetime import datetime

class HDFSArchitecture:
    """
    Simula a arquitetura do HDFS
    """
    
    def __init__(self):
        self.namenode = {
            'metadata': {},
            'block_locations': {},
            'status': 'active'
        }
        
        self.datanodes = {}
        self.blocks = {}
        self.replication_factor = 3
        self.block_size = 128 * 1024 * 1024  # 128MB
        
    def add_datanode(self, node_id: str, capacity_gb: int):
        """Adiciona um DataNode ao cluster"""
        self.datanodes[node_id] = {
            'capacity': capacity_gb * 1024 * 1024 * 1024,  # Converte para bytes
            'used': 0,
            'available': capacity_gb * 1024 * 1024 * 1024,
            'blocks': [],
            'status': 'healthy',
            'last_heartbeat': datetime.now()
        }
        print(f"✅ DataNode {node_id} adicionado com {capacity_gb}GB")
    
    def write_file(self, filename: str, file_size_mb: int):
        """Simula escrita de arquivo no HDFS"""
        print(f"\n📝 Escrevendo arquivo: {filename} ({file_size_mb}MB)")
        
        file_size_bytes = file_size_mb * 1024 * 1024
        num_blocks = (file_size_bytes + self.block_size - 1) // self.block_size
        
        print(f"📦 Arquivo dividido em {num_blocks} blocos")
        
        # Cria metadados do arquivo
        self.namenode['metadata'][filename] = {
            'size': file_size_bytes,
            'blocks': [],
            'created': datetime.now(),
            'replication_factor': self.replication_factor
        }
        
        # Distribui blocos
        for i in range(num_blocks):
            block_id = f"{filename}_block_{i}"
            block_size = min(self.block_size, file_size_bytes - i * self.block_size)
            
            # Seleciona DataNodes para replicação
            selected_nodes = self._select_datanodes_for_block()
            
            self.blocks[block_id] = {
                'size': block_size,
                'replicas': selected_nodes,
                'checksum': f"checksum_{block_id}"
            }
            
            # Atualiza metadados
            self.namenode['metadata'][filename]['blocks'].append(block_id)
            self.namenode['block_locations'][block_id] = selected_nodes
            
            # Atualiza DataNodes
            for node_id in selected_nodes:
                self.datanodes[node_id]['blocks'].append(block_id)
                self.datanodes[node_id]['used'] += block_size
                self.datanodes[node_id]['available'] -= block_size
            
            print(f"  📦 Bloco {i+1}: {block_size/1024/1024:.1f}MB → {selected_nodes}")
        
        print(f"✅ Arquivo {filename} escrito com sucesso!")
        return True
    
    def read_file(self, filename: str):
        """Simula leitura de arquivo do HDFS"""
        print(f"\n📖 Lendo arquivo: {filename}")
        
        if filename not in self.namenode['metadata']:
            print(f"❌ Arquivo {filename} não encontrado!")
            return None
        
        file_info = self.namenode['metadata'][filename]
        blocks = file_info['blocks']
        
        print(f"📋 Arquivo possui {len(blocks)} blocos")
        
        # Simula leitura de cada bloco
        total_data = []
        for i, block_id in enumerate(blocks):
            replicas = self.namenode['block_locations'][block_id]
            
            # Seleciona réplica mais próxima (simulado)
            selected_node = self._select_closest_replica(replicas)
            
            print(f"  📦 Bloco {i+1}: Lendo de {selected_node}")
            
            # Simula dados do bloco
            block_data = f"data_from_{block_id}"
            total_data.append(block_data)
        
        print(f"✅ Arquivo {filename} lido com sucesso!")
        return ''.join(total_data)
    
    def _select_datanodes_for_block(self):
        """Seleciona DataNodes para armazenar um bloco"""
        available_nodes = [
            node_id for node_id, info in self.datanodes.items()
            if info['status'] == 'healthy' and info['available'] > self.block_size
        ]
        
        if len(available_nodes) < self.replication_factor:
            print(f"⚠️ Apenas {len(available_nodes)} nós disponíveis")
            return available_nodes
        
        # Seleciona nós com mais espaço disponível
        sorted_nodes = sorted(available_nodes, 
                            key=lambda x: self.datanodes[x]['available'], 
                            reverse=True)
        
        return sorted_nodes[:self.replication_factor]
    
    def _select_closest_replica(self, replicas):
        """Seleciona a réplica mais próxima (simulado)"""
        # Em implementação real, consideraria latência de rede
        healthy_replicas = [
            node for node in replicas 
            if self.datanodes[node]['status'] == 'healthy'
        ]
        return healthy_replicas[0] if healthy_replicas else replicas[0]
    
    def get_cluster_status(self):
        """Retorna status do cluster HDFS"""
        total_capacity = sum(node['capacity'] for node in self.datanodes.values())
        total_used = sum(node['used'] for node in self.datanodes.values())
        total_available = sum(node['available'] for node in self.datanodes.values())
        
        status = {
            'total_nodes': len(self.datanodes),
            'healthy_nodes': len([n for n in self.datanodes.values() if n['status'] == 'healthy']),
            'total_capacity_gb': total_capacity / (1024**3),
            'used_capacity_gb': total_used / (1024**3),
            'available_capacity_gb': total_available / (1024**3),
            'utilization_percent': (total_used / total_capacity) * 100 if total_capacity > 0 else 0,
            'total_files': len(self.namenode['metadata']),
            'total_blocks': len(self.blocks)
        }
        
        return status
    
    def display_cluster_status(self):
        """Exibe status do cluster"""
        status = self.get_cluster_status()
        
        print("\n🖥️ STATUS DO CLUSTER HDFS")
        print("=" * 40)
        print(f"📊 Nós totais: {status['total_nodes']}")
        print(f"✅ Nós saudáveis: {status['healthy_nodes']}")
        print(f"💾 Capacidade total: {status['total_capacity_gb']:.1f} GB")
        print(f"📦 Espaço usado: {status['used_capacity_gb']:.1f} GB")
        print(f"🆓 Espaço disponível: {status['available_capacity_gb']:.1f} GB")
        print(f"📈 Utilização: {status['utilization_percent']:.1f}%")
        print(f"📄 Arquivos: {status['total_files']}")
        print(f"🧱 Blocos: {status['total_blocks']}")

# Demonstração do HDFS
def demonstrate_hdfs():
    """Demonstra operações básicas do HDFS"""
    print("🚀 DEMONSTRAÇÃO DO HDFS")
    print("=" * 50)
    
    # Cria cluster HDFS
    hdfs = HDFSArchitecture()
    
    # Adiciona DataNodes
    hdfs.add_datanode("datanode01", 100)  # 100GB
    hdfs.add_datanode("datanode02", 150)  # 150GB
    hdfs.add_datanode("datanode03", 200)  # 200GB
    hdfs.add_datanode("datanode04", 120)  # 120GB
    
    # Escreve arquivos
    hdfs.write_file("dataset_vendas.csv", 250)      # 250MB
    hdfs.write_file("logs_sistema.txt", 500)        # 500MB
    hdfs.write_file("backup_database.sql", 1200)    # 1.2GB
    
    # Lê arquivo
    hdfs.read_file("dataset_vendas.csv")
    
    # Exibe status
    hdfs.display_cluster_status()
    
    return hdfs

# Executa demonstração
hdfs_cluster = demonstrate_hdfs()
```

## 4.3 MapReduce - Paradigma de Processamento

MapReduce é um paradigma de programação para processamento de grandes volumes de dados de forma distribuída.

### 4.3.1 Conceitos Fundamentais

```python
from collections import defaultdict
import random
import time

class MapReduceFramework:
    """
    Implementação simplificada do framework MapReduce
    """
    
    def __init__(self, num_workers=4):
        self.num_workers = num_workers
        self.intermediate_data = defaultdict(list)
        
    def map_phase(self, data, map_function):
        """Fase Map: aplica função map aos dados"""
        print("🗺️ FASE MAP INICIADA")
        print("-" * 30)
        
        map_results = []
        
        # Simula distribuição para workers
        chunk_size = len(data) // self.num_workers
        
        for worker_id in range(self.num_workers):
            start_idx = worker_id * chunk_size
            end_idx = start_idx + chunk_size if worker_id < self.num_workers - 1 else len(data)
            
            worker_data = data[start_idx:end_idx]
            
            print(f"🤖 Worker {worker_id + 1}: processando {len(worker_data)} registros")
            
            # Aplica função map
            for item in worker_data:
                key_value_pairs = map_function(item)
                map_results.extend(key_value_pairs)
        
        print(f"✅ Fase Map concluída: {len(map_results)} pares chave-valor gerados")
        return map_results
    
    def shuffle_phase(self, map_results):
        """Fase Shuffle: agrupa por chave"""
        print("\n🔀 FASE SHUFFLE INICIADA")
        print("-" * 30)
        
        # Agrupa por chave
        grouped_data = defaultdict(list)
        for key, value in map_results:
            grouped_data[key].append(value)
        
        print(f"📊 Dados agrupados em {len(grouped_data)} chaves distintas")
        
        # Distribui para reducers
        reducer_data = {}
        keys = list(grouped_data.keys())
        
        for i, key in enumerate(keys):
            reducer_id = i % self.num_workers
            if reducer_id not in reducer_data:
                reducer_data[reducer_id] = {}
            reducer_data[reducer_id][key] = grouped_data[key]
        
        print(f"🔄 Dados distribuídos para {len(reducer_data)} reducers")
        return reducer_data
    
    def reduce_phase(self, reducer_data, reduce_function):
        """Fase Reduce: aplica função reduce"""
        print("\n📉 FASE REDUCE INICIADA")
        print("-" * 30)
        
        final_results = {}
        
        for reducer_id, data in reducer_data.items():
            print(f"🤖 Reducer {reducer_id + 1}: processando {len(data)} chaves")
            
            for key, values in data.items():
                result = reduce_function(key, values)
                final_results[key] = result
        
        print(f"✅ Fase Reduce concluída: {len(final_results)} resultados finais")
        return final_results
    
    def run_job(self, data, map_function, reduce_function):
        """Executa job MapReduce completo"""
        print("🚀 INICIANDO JOB MAPREDUCE")
        print("=" * 50)
        
        start_time = time.time()
        
        # Fase Map
        map_results = self.map_phase(data, map_function)
        
        # Fase Shuffle
        reducer_data = self.shuffle_phase(map_results)
        
        # Fase Reduce
        final_results = self.reduce_phase(reducer_data, reduce_function)
        
        execution_time = time.time() - start_time
        
        print(f"\n⏱️ Tempo total de execução: {execution_time:.2f} segundos")
        print(f"📊 Resultados processados: {len(final_results)}")
        
        return final_results

# Exemplo 1: Word Count
def word_count_example():
    """Exemplo clássico de contagem de palavras"""
    print("\n📝 EXEMPLO: WORD COUNT")
    print("=" * 40)
    
    # Dados de entrada (documentos)
    documents = [
        "big data analytics with python",
        "hadoop mapreduce framework",
        "distributed computing with hadoop",
        "python for big data processing",
        "apache spark and hadoop ecosystem",
        "data science with python tools",
        "mapreduce programming model",
        "big data storage solutions"
    ]
    
    # Função Map: extrai palavras
    def map_words(document):
        words = document.lower().split()
        return [(word, 1) for word in words]
    
    # Função Reduce: conta palavras
    def reduce_words(word, counts):
        return sum(counts)
    
    # Executa MapReduce
    mr = MapReduceFramework(num_workers=2)
    word_counts = mr.run_job(documents, map_words, reduce_words)
    
    # Exibe resultados
    print("\n📊 CONTAGEM DE PALAVRAS:")
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    for word, count in sorted_words[:10]:  # Top 10
        print(f"  {word}: {count}")
    
    return word_counts

# Exemplo 2: Análise de Vendas
def sales_analysis_example():
    """Exemplo de análise de vendas por região"""
    print("\n💰 EXEMPLO: ANÁLISE DE VENDAS")
    print("=" * 40)
    
    # Gera dados de vendas
    regions = ['Norte', 'Sul', 'Leste', 'Oeste']
    sales_data = []
    
    for _ in range(1000):
        sale = {
            'region': random.choice(regions),
            'amount': random.uniform(100, 5000),
            'date': f"2025-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
        }
        sales_data.append(sale)
    
    # Função Map: extrai região e valor
    def map_sales(sale):
        return [(sale['region'], sale['amount'])]
    
    # Função Reduce: soma vendas por região
    def reduce_sales(region, amounts):
        total = sum(amounts)
        count = len(amounts)
        average = total / count if count > 0 else 0
        return {
            'total_sales': total,
            'num_transactions': count,
            'average_sale': average
        }
    
    # Executa MapReduce
    mr = MapReduceFramework(num_workers=3)
    sales_summary = mr.run_job(sales_data, map_sales, reduce_sales)
    
    # Exibe resultados
    print("\n📊 RESUMO DE VENDAS POR REGIÃO:")
    for region, stats in sales_summary.items():
        print(f"\n🏪 {region}:")
        print(f"  💰 Total: R$ {stats['total_sales']:,.2f}")
        print(f"  📈 Transações: {stats['num_transactions']}")
        print(f"  📊 Média: R$ {stats['average_sale']:,.2f}")
    
    return sales_summary

# Executa exemplos
word_results = word_count_example()
sales_results = sales_analysis_example()
```

### 4.3.2 Otimizações do MapReduce

```python
class OptimizedMapReduce:
    """
    Versão otimizada do MapReduce com combiners e partitioners
    """
    
    def __init__(self, num_workers=4):
        self.num_workers = num_workers
        
    def map_with_combiner(self, data, map_function, combiner_function=None):
        """Map com combiner local para reduzir dados intermediários"""
        print("🗺️ FASE MAP COM COMBINER")
        print("-" * 30)
        
        chunk_size = len(data) // self.num_workers
        combined_results = []
        
        for worker_id in range(self.num_workers):
            start_idx = worker_id * chunk_size
            end_idx = start_idx + chunk_size if worker_id < self.num_workers - 1 else len(data)
            
            worker_data = data[start_idx:end_idx]
            
            # Fase Map local
            local_results = []
            for item in worker_data:
                local_results.extend(map_function(item))
            
            # Combiner local (se fornecido)
            if combiner_function:
                local_combined = defaultdict(list)
                for key, value in local_results:
                    local_combined[key].append(value)
                
                # Aplica combiner
                for key, values in local_combined.items():
                    combined_value = combiner_function(key, values)
                    combined_results.append((key, combined_value))
                
                print(f"🤖 Worker {worker_id + 1}: {len(local_results)} → {len(local_combined)} (combiner)")
            else:
                combined_results.extend(local_results)
                print(f"🤖 Worker {worker_id + 1}: {len(local_results)} pares")
        
        return combined_results
    
    def custom_partitioner(self, key, num_partitions):
        """Partitioner customizado para distribuição balanceada"""
        # Usa hash da chave para determinar partição
        partition = hash(key) % num_partitions
        return partition
    
    def run_optimized_job(self, data, map_function, reduce_function, 
                         combiner_function=None):
        """Executa job otimizado"""
        print("🚀 JOB MAPREDUCE OTIMIZADO")
        print("=" * 50)
        
        start_time = time.time()
        
        # Map com combiner
        map_results = self.map_with_combiner(data, map_function, combiner_function)
        
        # Shuffle com partitioner customizado
        print(f"\n🔀 SHUFFLE COM PARTITIONER CUSTOMIZADO")
        reducer_data = defaultdict(lambda: defaultdict(list))
        
        for key, value in map_results:
            partition = self.custom_partitioner(key, self.num_workers)
            reducer_data[partition][key].append(value)
        
        # Reduce
        print(f"\n📉 FASE REDUCE OTIMIZADA")
        final_results = {}
        
        for reducer_id, data_partition in reducer_data.items():
            for key, values in data_partition.items():
                final_results[key] = reduce_function(key, values)
        
        execution_time = time.time() - start_time
        print(f"\n⏱️ Tempo otimizado: {execution_time:.2f}s")
        
        return final_results

# Demonstração de otimização
def demonstrate_optimization():
    """Demonstra otimizações do MapReduce"""
    print("\n⚡ DEMONSTRAÇÃO DE OTIMIZAÇÕES")
    print("=" * 50)
    
    # Gera dataset maior
    large_dataset = []
    words = ['python', 'hadoop', 'spark', 'data', 'big', 'analytics', 'mapreduce']
    
    for _ in range(10000):
        text = ' '.join(random.choices(words, k=random.randint(5, 15)))
        large_dataset.append(text)
    
    # Funções para word count
    def map_words(text):
        return [(word, 1) for word in text.split()]
    
    def reduce_words(word, counts):
        return sum(counts)
    
    def combine_words(word, counts):
        return sum(counts)  # Combiner igual ao reducer para word count
    
    # Compara execução normal vs otimizada
    print("📊 COMPARAÇÃO DE PERFORMANCE:")
    
    # Execução normal
    mr_normal = MapReduceFramework(num_workers=4)
    start_time = time.time()
    result_normal = mr_normal.run_job(large_dataset, map_words, reduce_words)
    time_normal = time.time() - start_time
    
    print(f"\n⏱️ Tempo normal: {time_normal:.2f}s")
    
    # Execução otimizada
    mr_optimized = OptimizedMapReduce(num_workers=4)
    start_time = time.time()
    result_optimized = mr_optimized.run_optimized_job(
        large_dataset, map_words, reduce_words, combine_words
    )
    time_optimized = time.time() - start_time
    
    print(f"⏱️ Tempo otimizado: {time_optimized:.2f}s")
    print(f"🚀 Speedup: {time_normal/time_optimized:.2f}x")
    
    return result_normal, result_optimized

# Executa demonstração
normal_result, optimized_result = demonstrate_optimization()
```

## 4.4 YARN - Yet Another Resource Negotiator

YARN é o gerenciador de recursos do Hadoop 2.x que permite múltiplos frameworks de processamento executarem no mesmo cluster.

### 4.4.1 Arquitetura do YARN

```python
class YARNSimulator:
    """
    Simula o funcionamento do YARN
    """
    
    def __init__(self):
        self.resource_manager = {
            'applications': {},
            'node_managers': {},
            'scheduler': 'CapacityScheduler',
            'resource_tracker': {}
        }
        
        self.applications = {}
        self.containers = {}
        
    def register_node_manager(self, node_id: str, resources: dict):
        """Registra um NodeManager"""
        self.resource_manager['node_managers'][node_id] = {
            'total_memory': resources['memory_mb'],
            'total_vcores': resources['vcores'],
            'available_memory': resources['memory_mb'],
            'available_vcores': resources['vcores'],
            'containers': [],
            'status': 'healthy'
        }
        
        print(f"🖥️ NodeManager {node_id} registrado:")
        print(f"   💾 Memória: {resources['memory_mb']} MB")
        print(f"   🔄 vCores: {resources['vcores']}")
    
    def submit_application(self, app_id: str, app_config: dict):
        """Submete aplicação ao YARN"""
        print(f"\n📋 Submetendo aplicação: {app_id}")
        
        self.applications[app_id] = {
            'config': app_config,
            'status': 'submitted',
            'containers': [],
            'submit_time': datetime.now()
        }
        
        # Inicia ApplicationMaster
        am_container = self._allocate_container(
            app_id, 
            app_config.get('am_memory', 512),
            app_config.get('am_vcores', 1)
        )
        
        if am_container:
            self.applications[app_id]['am_container'] = am_container
            self.applications[app_id]['status'] = 'running'
            print(f"✅ ApplicationMaster iniciado: {am_container}")
        else:
            self.applications[app_id]['status'] = 'failed'
            print(f"❌ Falha ao alocar ApplicationMaster")
        
        return self.applications[app_id]['status']
    
    def request_containers(self, app_id: str, container_requests: list):
        """Processa requisições de containers"""
        print(f"\n📦 Requisição de containers para {app_id}")
        
        if app_id not in self.applications:
            print(f"❌ Aplicação {app_id} não encontrada")
            return []
        
        allocated_containers = []
        
        for request in container_requests:
            memory_mb = request['memory_mb']
            vcores = request['vcores']
            
            container = self._allocate_container(app_id, memory_mb, vcores)
            
            if container:
                allocated_containers.append(container)
                self.applications[app_id]['containers'].append(container)
                print(f"   ✅ Container alocado: {container}")
            else:
                print(f"   ❌ Recursos insuficientes: {memory_mb}MB, {vcores} vCores")
        
        print(f"📊 Containers alocados: {len(allocated_containers)}/{len(container_requests)}")
        return allocated_containers
    
    def _allocate_container(self, app_id: str, memory_mb: int, vcores: int):
        """Aloca container em node disponível"""
        for node_id, node_info in self.resource_manager['node_managers'].items():
            if (node_info['available_memory'] >= memory_mb and 
                node_info['available_vcores'] >= vcores and
                node_info['status'] == 'healthy'):
                
                # Cria container
                container_id = f"container_{len(self.containers) + 1}"
                container = {
                    'container_id': container_id,
                    'app_id': app_id,
                    'node_id': node_id,
                    'memory_mb': memory_mb,
                    'vcores': vcores,
                    'status': 'allocated',
                    'start_time': datetime.now()
                }
                
                # Atualiza recursos do node
                node_info['available_memory'] -= memory_mb
                node_info['available_vcores'] -= vcores
                node_info['containers'].append(container_id)
                
                # Registra container
                self.containers[container_id] = container
                
                return container
        
        return None
    
    def release_container(self, container_id: str):
        """Libera container e recursos"""
        if container_id not in self.containers:
            print(f"❌ Container {container_id} não encontrado")
            return False
        
        container = self.containers[container_id]
        node_id = container['node_id']
        
        # Libera recursos no node
        node_info = self.resource_manager['node_managers'][node_id]
        node_info['available_memory'] += container['memory_mb']
        node_info['available_vcores'] += container['vcores']
        node_info['containers'].remove(container_id)
        
        # Remove container
        del self.containers[container_id]
        
        print(f"🗑️ Container {container_id} liberado do node {node_id}")
        return True
    
    def get_cluster_metrics(self):
        """Retorna métricas do cluster"""
        total_memory = sum(node['total_memory'] for node in self.resource_manager['node_managers'].values())
        available_memory = sum(node['available_memory'] for node in self.resource_manager['node_managers'].values())
        total_vcores = sum(node['total_vcores'] for node in self.resource_manager['node_managers'].values())
        available_vcores = sum(node['available_vcores'] for node in self.resource_manager['node_managers'].values())
        
        return {
            'total_nodes': len(self.resource_manager['node_managers']),
            'total_applications': len(self.applications),
            'running_applications': len([app for app in self.applications.values() if app['status'] == 'running']),
            'total_containers': len(self.containers),
            'memory_utilization': ((total_memory - available_memory) / total_memory * 100) if total_memory > 0 else 0,
            'vcores_utilization': ((total_vcores - available_vcores) / total_vcores * 100) if total_vcores > 0 else 0,
            'total_memory_mb': total_memory,
            'available_memory_mb': available_memory,
            'total_vcores': total_vcores,
            'available_vcores': available_vcores
        }
    
    def display_cluster_status(self):
        """Exibe status do cluster YARN"""
        metrics = self.get_cluster_metrics()
        
        print("\n🎯 STATUS DO CLUSTER YARN")
        print("=" * 40)
        print(f"🖥️ Nodes: {metrics['total_nodes']}")
        print(f"📱 Aplicações: {metrics['running_applications']}/{metrics['total_applications']}")
        print(f"📦 Containers: {metrics['total_containers']}")
        print(f"💾 Memória: {metrics['memory_utilization']:.1f}% utilizada")
        print(f"🔄 vCores: {metrics['vcores_utilization']:.1f}% utilizados")
        print(f"📊 Recursos disponíveis:")
        print(f"   💾 {metrics['available_memory_mb']:,} MB")
        print(f"   🔄 {metrics['available_vcores']} vCores")

# Demonstração do YARN
def demonstrate_yarn():
    """Demonstra funcionamento do YARN"""
    print("🎯 DEMONSTRAÇÃO DO YARN")
    print("=" * 50)
    
    # Cria cluster YARN
    yarn = YARNSimulator()
    
    # Registra NodeManagers
    yarn.register_node_manager("nm01", {'memory_mb': 8192, 'vcores': 4})
    yarn.register_node_manager("nm02", {'memory_mb': 16384, 'vcores': 8})
    yarn.register_node_manager("nm03", {'memory_mb': 12288, 'vcores': 6})
    
    # Submete aplicações
    yarn.submit_application("mapreduce_job_001", {
        'type': 'mapreduce',
        'am_memory': 512,
        'am_vcores': 1
    })
    
    yarn.submit_application("spark_job_001", {
        'type': 'spark',
        'am_memory': 1024,
        'am_vcores': 2
    })
    
    # Requisita containers para MapReduce
    mr_containers = yarn.request_containers("mapreduce_job_001", [
        {'memory_mb': 2048, 'vcores': 2},
        {'memory_mb': 2048, 'vcores': 2},
        {'memory_mb': 1024, 'vcores': 1}
    ])
    
    # Requisita containers para Spark
    spark_containers = yarn.request_containers("spark_job_001", [
        {'memory_mb': 4096, 'vcores': 4},
        {'memory_mb': 4096, 'vcores': 4}
    ])
    
    # Exibe status
    yarn.display_cluster_status()
    
    return yarn

# Executa demonstração
yarn_cluster = demonstrate_yarn()
```

## 4.5 Ecossistema Hadoop

O Hadoop evoluiu para um ecossistema complexo de ferramentas especializadas.

### 4.5.1 Principais Componentes

```python
class HadoopEcosystem:
    """
    Representa o ecossistema Hadoop completo
    """
    
    def __init__(self):
        self.components = {
            'storage': {
                'HDFS': 'Sistema de arquivos distribuído',
                'HBase': 'Banco NoSQL distribuído',
                'Cassandra': 'Banco distribuído wide-column'
            },
            'processing': {
                'MapReduce': 'Processamento em batch',
                'Spark': 'Processamento em memória',
                'Storm': 'Processamento em streaming',
                'Flink': 'Processamento unificado'
            },
            'resource_management': {
                'YARN': 'Gerenciador de recursos',
                'Mesos': 'Orquestrador de cluster'
            },
            'data_ingestion': {
                'Flume': 'Coleta de logs',
                'Sqoop': 'Transferência SQL-Hadoop',
                'Kafka': 'Streaming de dados'
            },
            'coordination': {
                'ZooKeeper': 'Coordenação distribuída',
                'Consul': 'Service discovery'
            },
            'workflow': {
                'Oozie': 'Scheduler de workflows',
                'Airflow': 'Orquestração de pipelines'
            },
            'sql_engines': {
                'Hive': 'SQL sobre Hadoop',
                'Impala': 'SQL analytics',
                'Presto': 'Query engine distribuído'
            },
            'machine_learning': {
                'Mahout': 'ML escalável',
                'MLlib': 'ML sobre Spark',
                'H2O': 'ML em memória'
            },
            'monitoring': {
                'Ambari': 'Gestão de cluster',
                'Cloudera Manager': 'Administração',
                'Ganglia': 'Monitoramento'
            }
        }
    
    def display_ecosystem(self):
        """Exibe componentes do ecossistema"""
        print("🏗️ ECOSSISTEMA HADOOP")
        print("=" * 50)
        
        for category, tools in self.components.items():
            print(f"\n📋 {category.upper().replace('_', ' ')}")
            print("-" * 30)
            
            for tool, description in tools.items():
                print(f"  🔧 {tool}: {description}")
    
    def get_stack_recommendation(self, use_case: str):
        """Recomenda stack baseado no caso de uso"""
        recommendations = {
            'batch_analytics': {
                'storage': ['HDFS', 'Hive'],
                'processing': ['Spark', 'MapReduce'],
                'tools': ['Oozie', 'Sqoop']
            },
            'real_time_analytics': {
                'storage': ['HBase', 'Kafka'],
                'processing': ['Storm', 'Spark Streaming'],
                'tools': ['ZooKeeper', 'Flume']
            },
            'data_warehouse': {
                'storage': ['HDFS', 'Hive', 'Impala'],
                'processing': ['Spark SQL', 'Presto'],
                'tools': ['Sqoop', 'Oozie']
            },
            'machine_learning': {
                'storage': ['HDFS', 'HBase'],
                'processing': ['Spark MLlib', 'H2O'],
                'tools': ['Jupyter', 'Zeppelin']
            }
        }
        
        return recommendations.get(use_case, {})

# Demonstração do ecossistema
ecosystem = HadoopEcosystem()
ecosystem.display_ecosystem()

print("\n💡 RECOMENDAÇÕES DE STACK:")
use_cases = ['batch_analytics', 'real_time_analytics', 'data_warehouse', 'machine_learning']

for use_case in use_cases:
    rec = ecosystem.get_stack_recommendation(use_case)
    print(f"\n🎯 {use_case.replace('_', ' ').title()}:")
    
    for component_type, tools in rec.items():
        print(f"  {component_type}: {', '.join(tools)}")
```

## 4.6 Instalação e Configuração

### 4.6.1 Configuração de Ambiente

```python
import os
import subprocess
import platform

class HadoopInstaller:
    """
    Assistente para instalação do Hadoop
    """
    
    def __init__(self):
        self.hadoop_version = "3.3.6"
        self.java_version = "11"
        self.installation_path = "/opt/hadoop"
        
    def check_prerequisites(self):
        """Verifica pré-requisitos do sistema"""
        print("🔍 VERIFICANDO PRÉ-REQUISITOS")
        print("=" * 40)
        
        checks = {
            'os': platform.system(),
            'java': self._check_java(),
            'python': platform.python_version(),
            'memory': self._check_memory(),
            'disk_space': self._check_disk_space()
        }
        
        for component, status in checks.items():
            print(f"  {component}: {status}")
        
        return checks
    
    def _check_java(self):
        """Verifica instalação do Java"""
        try:
            result = subprocess.run(['java', '-version'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                version_line = result.stderr.split('\n')[0]
                return f"✅ {version_line}"
            else:
                return "❌ Java não encontrado"
        except:
            return "❌ Java não instalado"
    
    def _check_memory(self):
        """Verifica memória disponível"""
        try:
            import psutil
            memory_gb = psutil.virtual_memory().total / (1024**3)
            if memory_gb >= 8:
                return f"✅ {memory_gb:.1f} GB (suficiente)"
            else:
                return f"⚠️ {memory_gb:.1f} GB (mínimo 8GB recomendado)"
        except:
            return "❓ Não foi possível verificar"
    
    def _check_disk_space(self):
        """Verifica espaço em disco"""
        try:
            import psutil
            disk_usage = psutil.disk_usage('/')
            free_gb = disk_usage.free / (1024**3)
            if free_gb >= 50:
                return f"✅ {free_gb:.1f} GB livres (suficiente)"
            else:
                return f"⚠️ {free_gb:.1f} GB livres (mínimo 50GB recomendado)"
        except:
            return "❓ Não foi possível verificar"
    
    def generate_config_files(self):
        """Gera arquivos de configuração do Hadoop"""
        print("\n📄 GERANDO ARQUIVOS DE CONFIGURAÇÃO")
        print("=" * 50)
        
        configs = {
            'core-site.xml': self._generate_core_site(),
            'hdfs-site.xml': self._generate_hdfs_site(),
            'mapred-site.xml': self._generate_mapred_site(),
            'yarn-site.xml': self._generate_yarn_site()
        }
        
        for filename, content in configs.items():
            print(f"\n📝 {filename}:")
            print(content)
        
        return configs
    
    def _generate_core_site(self):
        """Gera core-site.xml"""
        return """<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/opt/hadoop/tmp</value>
    </property>
</configuration>"""
    
    def _generate_hdfs_site(self):
        """Gera hdfs-site.xml"""
        return """<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/opt/hadoop/hdfs/namenode</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/opt/hadoop/hdfs/datanode</value>
    </property>
    <property>
        <name>dfs.blocksize</name>
        <value>134217728</value>
    </property>
</configuration>"""
    
    def _generate_mapred_site(self):
        """Gera mapred-site.xml"""
        return """<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>mapreduce.application.classpath</name>
        <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
    </property>
</configuration>"""
    
    def _generate_yarn_site(self):
        """Gera yarn-site.xml"""
        return """<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.env-whitelist</name>
        <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
    </property>
    <property>
        <name>yarn.scheduler.maximum-allocation-mb</name>
        <value>4096</value>
    </property>
    <property>
        <name>yarn.nodemanager.resource.memory-mb</name>
        <value>4096</value>
    </property>
</configuration>"""
    
    def generate_startup_script(self):
        """Gera script de inicialização"""
        script = """#!/bin/bash
# Script de inicialização do Hadoop

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
export HADOOP_HOME=/opt/hadoop
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

echo "🚀 Iniciando cluster Hadoop..."

# Formatar NameNode (apenas primeira vez)
if [ ! -d "$HADOOP_HOME/hdfs/namenode/current" ]; then
    echo "📝 Formatando NameNode..."
    $HADOOP_HOME/bin/hdfs namenode -format -force
fi

# Iniciar HDFS
echo "🗂️ Iniciando HDFS..."
$HADOOP_HOME/sbin/start-dfs.sh

# Iniciar YARN
echo "🎯 Iniciando YARN..."
$HADOOP_HOME/sbin/start-yarn.sh

echo "✅ Cluster Hadoop iniciado!"
echo "🌐 Web UIs disponíveis:"
echo "   NameNode: http://localhost:9870"
echo "   ResourceManager: http://localhost:8088"
echo "   NodeManager: http://localhost:8042"
"""
        
        print("\n🚀 SCRIPT DE INICIALIZAÇÃO:")
        print("=" * 50)
        print(script)
        
        return script

# Demonstração do instalador
installer = HadoopInstaller()
installer.check_prerequisites()
installer.generate_config_files()
installer.generate_startup_script()
```

## 4.7 Exemplos Práticos

### 4.7.1 Processamento de Logs Web

```python
import re
from datetime import datetime
from collections import Counter

class WebLogAnalyzer:
    """
    Analisador de logs web usando paradigma MapReduce
    """
    
    def __init__(self):
        self.log_pattern = re.compile(
            r'(\S+) \S+ \S+ \[(.*?)\] "(\S+) (\S+) (\S+)" (\d+) (\d+) "([^"]*)" "([^"]*)"'
        )
    
    def parse_log_line(self, line):
        """Parse de linha de log Apache/Nginx"""
        match = self.log_pattern.match(line)
        if match:
            return {
                'ip': match.group(1),
                'timestamp': match.group(2),
                'method': match.group(3),
                'url': match.group(4),
                'protocol': match.group(5),
                'status': int(match.group(6)),
                'size': int(match.group(7)) if match.group(7) != '-' else 0,
                'referer': match.group(8),
                'user_agent': match.group(9)
            }
        return None
    
    def analyze_logs_mapreduce(self, log_lines):
        """Análise de logs usando MapReduce"""
        print("📊 ANÁLISE DE LOGS WEB COM MAPREDUCE")
        print("=" * 50)
        
        # Map: extrai informações de cada linha
        def map_log_analysis(line):
            parsed = self.parse_log_line(line)
            if parsed:
                return [
                    ('ip_count', parsed['ip']),
                    ('status_count', parsed['status']),
                    ('url_count', parsed['url']),
                    ('hour_count', parsed['timestamp'].split(':')[1]),
                    ('size_total', parsed['size'])
                ]
            return []
        
        # Reduce: agrega estatísticas
        def reduce_log_stats(key, values):
            if key.endswith('_count'):
                return len(values)
            elif key == 'size_total':
                return sum(values)
            return values
        
        # Executa MapReduce
        mr = MapReduceFramework(num_workers=4)
        results = mr.run_job(log_lines, map_log_analysis, reduce_log_stats)
        
        # Processa resultados
        analysis = {
            'total_requests': sum(v for k, v in results.items() if k.startswith('ip_count')),
            'unique_ips': len([k for k in results.keys() if k.startswith('ip_count')]),
            'status_codes': {},
            'top_urls': {},
            'hourly_traffic': {},
            'total_bytes': sum(v for k, v in results.items() if k == 'size_total')
        }
        
        # Organiza por categoria
        for key, value in results.items():
            if key.startswith('status_count'):
                status = key.split('_')[-1]
                analysis['status_codes'][status] = value
            elif key.startswith('url_count'):
                url = key.replace('url_count_', '')
                analysis['top_urls'][url] = value
            elif key.startswith('hour_count'):
                hour = key.split('_')[-1]
                analysis['hourly_traffic'][hour] = value
        
        return analysis
    
    def display_analysis(self, analysis):
        """Exibe resultados da análise"""
        print("\n📈 RESULTADOS DA ANÁLISE:")
        print("=" * 40)
        
        print(f"📊 Total de requisições: {analysis['total_requests']:,}")
        print(f"🌐 IPs únicos: {analysis['unique_ips']:,}")
        print(f"💾 Total de bytes: {analysis['total_bytes']:,}")
        
        print(f"\n📋 Códigos de status:")
        for status, count in sorted(analysis['status_codes'].items()):
            print(f"   {status}: {count:,}")
        
        print(f"\n🔗 URLs mais acessadas:")
        top_urls = sorted(analysis['top_urls'].items(), 
                         key=lambda x: x[1], reverse=True)[:5]
        for url, count in top_urls:
            print(f"   {url}: {count:,}")
        
        print(f"\n🕐 Tráfego por hora:")
        for hour in sorted(analysis['hourly_traffic'].keys()):
            count = analysis['hourly_traffic'][hour]
            print(f"   {hour}h: {count:,}")

# Gera logs de exemplo
def generate_sample_logs(num_logs=10000):
    """Gera logs de exemplo para teste"""
    import random
    from datetime import datetime, timedelta
    
    ips = [f"192.168.1.{i}" for i in range(1, 101)]
    urls = ['/index.html', '/about.html', '/products.html', '/contact.html', 
            '/api/users', '/api/products', '/static/css/style.css', '/images/logo.png']
    status_codes = [200, 200, 200, 200, 404, 500, 301]
    user_agents = ['Mozilla/5.0 (Chrome)', 'Mozilla/5.0 (Firefox)', 'Bot/1.0']
    
    logs = []
    base_time = datetime.now() - timedelta(days=1)
    
    for i in range(num_logs):
        ip = random.choice(ips)
        timestamp = base_time + timedelta(minutes=random.randint(0, 1440))
        url = random.choice(urls)
        status = random.choice(status_codes)
        size = random.randint(100, 50000)
        user_agent = random.choice(user_agents)
        
        log_line = f'{ip} - - [{timestamp.strftime("%d/%b/%Y:%H:%M:%S +0000")}] "GET {url} HTTP/1.1" {status} {size} "-" "{user_agent}"'
        logs.append(log_line)
    
    return logs

# Demonstração de análise de logs
def demonstrate_log_analysis():
    """Demonstra análise de logs web"""
    print("🌐 DEMONSTRAÇÃO: ANÁLISE DE LOGS WEB")
    print("=" * 60)
    
    # Gera logs de exemplo
    sample_logs = generate_sample_logs(50000)
    print(f"📝 Gerados {len(sample_logs)} logs de exemplo")
    
    # Analisa logs
    analyzer = WebLogAnalyzer()
    analysis = analyzer.analyze_logs_mapreduce(sample_logs)
    
    # Exibe resultados
    analyzer.display_analysis(analysis)
    
    return analysis

# Executa demonstração
log_analysis = demonstrate_log_analysis()
```

## 4.8 Conclusão

O Apache Hadoop revolucionou o processamento de Big Data fornecendo uma plataforma distribuída, escalável e tolerante a falhas. Seus componentes principais - HDFS, MapReduce e YARN - formam a base da maioria das soluções modernas de Big Data.

### 4.8.1 Principais Aprendizados

```python
# Resumo dos conceitos aprendidos
hadoop_concepts = {
    'HDFS': {
        'propósito': 'Armazenamento distribuído de grandes arquivos',
        'características': ['Tolerância a falhas', 'Escalabilidade', 'Alto throughput'],
        'casos_uso': ['Data lakes', 'Backup distribuído', 'Análise de logs']
    },
    'MapReduce': {
        'propósito': 'Processamento paralelo de grandes datasets',
        'fases': ['Map', 'Shuffle', 'Reduce'],
        'casos_uso': ['Contagem de palavras', 'Análise de logs', 'ETL em batch']
    },
    'YARN': {
        'propósito': 'Gerenciamento de recursos do cluster',
        'componentes': ['ResourceManager', 'NodeManager', 'ApplicationMaster'],
        'benefícios': ['Multi-tenancy', 'Melhor utilização', 'Flexibilidade']
    }
}

print("📚 RESUMO DO CAPÍTULO 4: HADOOP E HDFS")
print("=" * 60)

for component, info in hadoop_concepts.items():
    print(f"\n🔧 {component}")
    print(f"   Propósito: {info['propósito']}")
    
    if 'características' in info:
        print(f"   Características: {', '.join(info['características'])}")
    if 'fases' in info:
        print(f"   Fases: {', '.join(info['fases'])}")
    if 'componentes' in info:
        print(f"   Componentes: {', '.join(info['componentes'])}")
    if 'benefícios' in info:
        print(f"   Benefícios: {', '.join(info['benefícios'])}")
    
    print(f"   Casos de uso: {', '.join(info['casos_uso'])}")
```

### 4.8.2 Próximos Passos

O Hadoop estabeleceu os fundamentos, mas o ecossistema evoluiu com tecnologias como Apache Spark, que abordaremos no próximo capítulo. O Spark oferece processamento em memória e APIs mais simples, mantendo compatibilidade com o ecossistema Hadoop.

---

**Próximo Capítulo**: Apache Spark com PySpark - Processamento em Memória de Alta Performance
