#!/usr/bin/env python3
"""
Aula 02: Processamento Distribuído com Message Queues
Professor: Vagner Cordeiro
Curso: Tópicos de Big Data em Python

Demonstra conceitos de processamento distribuído usando filas de mensagens,
padrões producer-consumer e balanceamento de carga.
"""

import json
import time
import random
import threading
import queue
from datetime import datetime
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
import sqlite3
import hashlib
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

class MessageQueue:
    """Sistema simples de filas de mensagens"""
    
    def __init__(self, max_size=1000):
        self.queues = defaultdict(lambda: queue.Queue(maxsize=max_size))
        self.subscribers = defaultdict(list)
        self.message_count = defaultdict(int)
        self.lock = threading.Lock()
        
    def publish(self, topic, message):
        """Publica uma mensagem em um tópico"""
        with self.lock:
            try:
                self.queues[topic].put(message, block=False)
                self.message_count[topic] += 1
                return True
            except queue.Full:
                print(f"⚠️  Fila {topic} cheia! Mensagem descartada.")
                return False
    
    def subscribe(self, topic, consumer_id):
        """Inscreve um consumidor em um tópico"""
        with self.lock:
            if consumer_id not in self.subscribers[topic]:
                self.subscribers[topic].append(consumer_id)
    
    def consume(self, topic, timeout=1):
        """Consome uma mensagem de um tópico"""
        try:
            message = self.queues[topic].get(timeout=timeout)
            return message
        except queue.Empty:
            return None
    
    def get_stats(self):
        """Retorna estatísticas das filas"""
        with self.lock:
            stats = {}
            for topic in self.queues:
                stats[topic] = {
                    "queue_size": self.queues[topic].qsize(),
                    "total_messages": self.message_count[topic],
                    "subscribers": len(self.subscribers[topic])
                }
            return stats

class DataProducer:
    """Produtor de dados para simulação distribuída"""
    
    def __init__(self, producer_id, message_queue, topics):
        self.producer_id = producer_id
        self.message_queue = message_queue
        self.topics = topics
        self.messages_sent = 0
        self.is_running = False
        
    def generate_message(self, topic):
        """Gera uma mensagem baseada no tópico"""
        base_message = {
            "producer_id": self.producer_id,
            "timestamp": datetime.now().isoformat(),
            "message_id": f"{self.producer_id}_{self.messages_sent}",
            "topic": topic
        }
        
        if topic == "sensor_data":
            base_message.update({
                "sensor_id": f"sensor_{random.randint(1, 100)}",
                "value": round(random.uniform(0, 100), 2),
                "unit": random.choice(["celsius", "percentage", "watts"])
            })
        elif topic == "user_events":
            base_message.update({
                "user_id": f"user_{random.randint(1, 1000)}",
                "event_type": random.choice(["login", "logout", "click", "purchase"]),
                "page": f"/page_{random.randint(1, 50)}"
            })
        elif topic == "system_logs":
            base_message.update({
                "level": random.choice(["INFO", "WARNING", "ERROR", "DEBUG"]),
                "service": random.choice(["api", "database", "cache", "auth"]),
                "message": f"Log message {random.randint(1, 1000)}"
            })
        
        return base_message
    
    def start_producing(self, duration_seconds=60, messages_per_second=10):
        """Inicia produção de mensagens"""
        print(f"🚀 Produtor {self.producer_id} iniciado - {messages_per_second} msg/s")
        self.is_running = True
        start_time = time.time()
        
        while time.time() - start_time < duration_seconds and self.is_running:
            topic = random.choice(self.topics)
            message = self.generate_message(topic)
            
            if self.message_queue.publish(topic, message):
                self.messages_sent += 1
            
            time.sleep(1.0 / messages_per_second)
        
        print(f"✅ Produtor {self.producer_id} finalizado - {self.messages_sent} mensagens enviadas")
    
    def stop_producing(self):
        """Para a produção de mensagens"""
        self.is_running = False

class DataConsumer:
    """Consumidor de dados para processamento distribuído"""
    
    def __init__(self, consumer_id, message_queue, topics):
        self.consumer_id = consumer_id
        self.message_queue = message_queue
        self.topics = topics
        self.messages_processed = 0
        self.processing_times = []
        self.is_running = False
        
        # Inscrever nos tópicos
        for topic in topics:
            message_queue.subscribe(topic, consumer_id)
    
    def process_message(self, message):
        """Processa uma mensagem (simula trabalho computacional)"""
        start_time = time.time()
        
        # Simular processamento baseado no tipo de mensagem
        if message["topic"] == "sensor_data":
            # Processamento de dados de sensor
            value = message.get("value", 0)
            processed_value = value * random.uniform(0.8, 1.2)  # Calibração
            time.sleep(random.uniform(0.01, 0.05))  # Simular I/O
            
        elif message["topic"] == "user_events":
            # Processamento de eventos de usuário
            user_id = message.get("user_id")
            event_hash = hashlib.md5(f"{user_id}_{message['timestamp']}".encode()).hexdigest()
            time.sleep(random.uniform(0.005, 0.02))
            
        elif message["topic"] == "system_logs":
            # Processamento de logs de sistema
            if message.get("level") == "ERROR":
                time.sleep(random.uniform(0.1, 0.2))  # Análise mais demorada para erros
            else:
                time.sleep(random.uniform(0.001, 0.01))
        
        processing_time = time.time() - start_time
        self.processing_times.append(processing_time)
        
        return {
            "original_message": message,
            "processed_by": self.consumer_id,
            "processing_time": processing_time,
            "processed_at": datetime.now().isoformat()
        }
    
    def start_consuming(self, duration_seconds=60):
        """Inicia consumo de mensagens"""
        print(f"🔄 Consumidor {self.consumer_id} iniciado")
        self.is_running = True
        start_time = time.time()
        
        while time.time() - start_time < duration_seconds and self.is_running:
            for topic in self.topics:
                message = self.message_queue.consume(topic, timeout=0.1)
                if message:
                    try:
                        processed = self.process_message(message)
                        self.messages_processed += 1
                        
                        # Log de progresso a cada 100 mensagens
                        if self.messages_processed % 100 == 0:
                            avg_time = np.mean(self.processing_times[-100:])
                            print(f"  📊 {self.consumer_id}: {self.messages_processed} processadas, tempo médio: {avg_time:.3f}s")
                            
                    except Exception as e:
                        print(f"❌ Erro processando mensagem: {e}")
        
        avg_processing_time = np.mean(self.processing_times) if self.processing_times else 0
        print(f"✅ Consumidor {self.consumer_id} finalizado - {self.messages_processed} mensagens processadas")
        print(f"   Tempo médio de processamento: {avg_processing_time:.3f}s")
    
    def stop_consuming(self):
        """Para o consumo de mensagens"""
        self.is_running = False

class LoadBalancer:
    """Balanceador de carga simples para distribuir trabalho"""
    
    def __init__(self):
        self.workers = []
        self.current_worker = 0
        self.work_distribution = defaultdict(int)
    
    def add_worker(self, worker_id):
        """Adiciona um worker ao pool"""
        self.workers.append(worker_id)
    
    def get_next_worker(self, strategy="round_robin"):
        """Retorna o próximo worker baseado na estratégia"""
        if not self.workers:
            return None
        
        if strategy == "round_robin":
            worker = self.workers[self.current_worker]
            self.current_worker = (self.current_worker + 1) % len(self.workers)
            
        elif strategy == "least_loaded":
            worker = min(self.workers, key=lambda w: self.work_distribution[w])
            
        elif strategy == "random":
            worker = random.choice(self.workers)
        
        self.work_distribution[worker] += 1
        return worker
    
    def get_distribution_stats(self):
        """Retorna estatísticas de distribuição de trabalho"""
        return dict(self.work_distribution)

def simulate_distributed_system():
    """Simula um sistema distribuído completo"""
    print("🌐 SIMULAÇÃO: Sistema Distribuído com Message Queue")
    print("=" * 55)
    
    # Configurar sistema
    message_queue = MessageQueue(max_size=5000)
    load_balancer = LoadBalancer()
    
    # Tópicos de mensagens
    topics = ["sensor_data", "user_events", "system_logs"]
    
    # Criar produtores
    producers = []
    for i in range(3):
        producer = DataProducer(f"producer_{i}", message_queue, topics)
        producers.append(producer)
    
    # Criar consumidores
    consumers = []
    for i in range(5):
        consumer = DataConsumer(f"consumer_{i}", message_queue, topics)
        consumers.append(consumer)
        load_balancer.add_worker(f"consumer_{i}")
    
    # Iniciar sistema com threading
    print("🚀 Iniciando sistema distribuído...")
    
    # Threads para produtores
    producer_threads = []
    for producer in producers:
        thread = threading.Thread(target=producer.start_producing, args=(120, 15))
        thread.start()
        producer_threads.append(thread)
    
    # Threads para consumidores
    consumer_threads = []
    for consumer in consumers:
        thread = threading.Thread(target=consumer.start_consuming, args=(120,))
        thread.start()
        consumer_threads.append(thread)
    
    # Monitor de estatísticas
    def monitor_system():
        for i in range(24):  # Monitor por 2 minutos
            time.sleep(5)
            stats = message_queue.get_stats()
            print(f"\n📊 ESTATÍSTICAS (t={i*5}s):")
            for topic, data in stats.items():
                print(f"  • {topic}: {data['queue_size']} na fila, {data['total_messages']} total")
    
    monitor_thread = threading.Thread(target=monitor_system)
    monitor_thread.start()
    
    # Aguardar conclusão
    for thread in producer_threads:
        thread.join()
    
    for thread in consumer_threads:
        thread.join()
    
    monitor_thread.join()
    
    # Estatísticas finais
    print("\n📈 RELATÓRIO FINAL:")
    print("=" * 30)
    
    total_produced = sum(p.messages_sent for p in producers)
    total_consumed = sum(c.messages_processed for c in consumers)
    
    print(f"📤 Total produzido: {total_produced} mensagens")
    print(f"📥 Total consumido: {total_consumed} mensagens")
    print(f"📊 Taxa de processamento: {(total_consumed/total_produced)*100:.1f}%")
    
    # Distribuição de trabalho
    print(f"\n⚖️  DISTRIBUIÇÃO DE TRABALHO:")
    distribution = load_balancer.get_distribution_stats()
    for worker, count in distribution.items():
        print(f"  • {worker}: {count} tarefas")
    
    # Análise de performance
    all_processing_times = []
    for consumer in consumers:
        all_processing_times.extend(consumer.processing_times)
    
    if all_processing_times:
        print(f"\n⏱️  PERFORMANCE:")
        print(f"  • Tempo médio de processamento: {np.mean(all_processing_times):.3f}s")
        print(f"  • Tempo mínimo: {np.min(all_processing_times):.3f}s")
        print(f"  • Tempo máximo: {np.max(all_processing_times):.3f}s")
        print(f"  • Desvio padrão: {np.std(all_processing_times):.3f}s")

def demonstrate_mapreduce_pattern():
    """Demonstra o padrão MapReduce para processamento distribuído"""
    print("\n🗺️  DEMONSTRAÇÃO: Padrão MapReduce")
    print("=" * 45)
    
    # Dataset exemplo: logs de acesso web
    def generate_web_logs(count=10000):
        """Gera logs de acesso web simulados"""
        ip_pools = [f"192.168.1.{i}" for i in range(1, 255)]
        pages = ["/home", "/login", "/dashboard", "/products", "/checkout", "/profile"]
        methods = ["GET", "POST", "PUT", "DELETE"]
        status_codes = [200, 301, 404, 500]
        
        logs = []
        for _ in range(count):
            log = {
                "ip": random.choice(ip_pools),
                "method": random.choice(methods),
                "page": random.choice(pages),
                "status": random.choice(status_codes),
                "size": random.randint(100, 50000),
                "timestamp": datetime.now().isoformat()
            }
            logs.append(log)
        
        return logs
    
    # Função Map: extrai pares chave-valor
    def mapper(log_batch):
        """Mapper: extrai estatísticas dos logs"""
        results = []
        for log in log_batch:
            # Mapear por página visitada
            results.append(("page_count", (log["page"], 1)))
            
            # Mapear por código de status
            results.append(("status_count", (log["status"], 1)))
            
            # Mapear por IP (para contar acessos únicos)
            results.append(("ip_count", (log["ip"], 1)))
            
            # Mapear tamanho de resposta por página
            results.append(("page_size", (log["page"], log["size"])))
        
        return results
    
    # Função Reduce: agrega os resultados
    def reducer(key, values):
        """Reducer: agrega valores por chave"""
        if key == "page_count" or key == "status_count" or key == "ip_count":
            # Contar ocorrências
            counts = defaultdict(int)
            for item, count in values:
                counts[item] += count
            return (key, dict(counts))
        
        elif key == "page_size":
            # Calcular estatísticas de tamanho por página
            page_sizes = defaultdict(list)
            for page, size in values:
                page_sizes[page].append(size)
            
            page_stats = {}
            for page, sizes in page_sizes.items():
                page_stats[page] = {
                    "avg_size": np.mean(sizes),
                    "total_size": sum(sizes),
                    "requests": len(sizes)
                }
            
            return (key, page_stats)
    
    # Executar MapReduce
    print("📊 Gerando dataset de logs...")
    logs = generate_web_logs(50000)
    print(f"✅ {len(logs)} logs gerados")
    
    print("\n🗺️  Fase MAP (paralela)...")
    # Dividir dados em chunks para processamento paralelo
    chunk_size = 1000
    chunks = [logs[i:i+chunk_size] for i in range(0, len(logs), chunk_size)]
    
    start_time = time.time()
    
    # Processar chunks em paralelo
    with ProcessPoolExecutor(max_workers=4) as executor:
        map_futures = [executor.submit(mapper, chunk) for chunk in chunks]
        map_results = []
        
        for future in as_completed(map_futures):
            map_results.extend(future.result())
    
    map_time = time.time() - start_time
    print(f"✅ MAP completado em {map_time:.2f}s - {len(map_results)} pares chave-valor")
    
    print("\n🔄 Fase SHUFFLE (agrupamento)...")
    start_time = time.time()
    
    # Agrupar por chave
    grouped = defaultdict(list)
    for key, value in map_results:
        grouped[key].append(value)
    
    shuffle_time = time.time() - start_time
    print(f"✅ SHUFFLE completado em {shuffle_time:.2f}s - {len(grouped)} grupos")
    
    print("\n📉 Fase REDUCE (agregação)...")
    start_time = time.time()
    
    # Reduzir em paralelo
    with ThreadPoolExecutor(max_workers=4) as executor:
        reduce_futures = [executor.submit(reducer, key, values) for key, values in grouped.items()]
        final_results = {}
        
        for future in as_completed(reduce_futures):
            key, result = future.result()
            final_results[key] = result
    
    reduce_time = time.time() - start_time
    print(f"✅ REDUCE completado em {reduce_time:.2f}s")
    
    # Mostrar resultados
    print(f"\n📊 RESULTADOS MapReduce:")
    print(f"  • Tempo total: {map_time + shuffle_time + reduce_time:.2f}s")
    
    if "page_count" in final_results:
        print(f"\n📄 Páginas mais acessadas:")
        page_counts = sorted(final_results["page_count"].items(), key=lambda x: x[1], reverse=True)
        for page, count in page_counts[:5]:
            print(f"  • {page}: {count} acessos")
    
    if "status_count" in final_results:
        print(f"\n📊 Códigos de status:")
        for status, count in sorted(final_results["status_count"].items()):
            print(f"  • {status}: {count} ocorrências")
    
    if "ip_count" in final_results:
        unique_ips = len(final_results["ip_count"])
        total_requests = sum(final_results["ip_count"].values())
        print(f"\n🌐 IPs únicos: {unique_ips}")
        print(f"📈 Total de requests: {total_requests}")

def demonstrate_fault_tolerance():
    """Demonstra conceitos de tolerância a falhas"""
    print("\n🛡️  DEMONSTRAÇÃO: Tolerância a Falhas")
    print("=" * 45)
    
    class FaultTolerantProcessor:
        """Processador com tolerância a falhas"""
        
        def __init__(self, name, failure_rate=0.1):
            self.name = name
            self.failure_rate = failure_rate
            self.processed_count = 0
            self.failed_count = 0
            self.retry_count = 0
        
        def process_with_retry(self, data, max_retries=3):
            """Processa dados com retry automático"""
            for attempt in range(max_retries + 1):
                try:
                    result = self.process_data(data)
                    self.processed_count += 1
                    if attempt > 0:
                        self.retry_count += 1
                        print(f"  ✅ {self.name}: Sucesso após {attempt} tentativas")
                    return result
                
                except Exception as e:
                    if attempt < max_retries:
                        self.retry_count += 1
                        wait_time = 2 ** attempt  # Backoff exponencial
                        print(f"  ⚠️  {self.name}: Falha {attempt+1}, tentando novamente em {wait_time}s...")
                        time.sleep(wait_time)
                    else:
                        self.failed_count += 1
                        print(f"  ❌ {self.name}: Falha definitiva após {max_retries} tentativas")
                        raise e
        
        def process_data(self, data):
            """Simula processamento com possibilidade de falha"""
            # Simular falha baseada na taxa de falha
            if random.random() < self.failure_rate:
                raise Exception(f"Falha simulada no processador {self.name}")
            
            # Simular processamento
            time.sleep(random.uniform(0.01, 0.1))
            return f"Processado por {self.name}: {data}"
        
        def get_stats(self):
            """Retorna estatísticas do processador"""
            total_attempts = self.processed_count + self.failed_count
            success_rate = (self.processed_count / total_attempts * 100) if total_attempts > 0 else 0
            
            return {
                "processed": self.processed_count,
                "failed": self.failed_count,
                "retries": self.retry_count,
                "success_rate": success_rate
            }
    
    # Criar processadores com diferentes taxas de falha
    processors = [
        FaultTolerantProcessor("Processor_A", 0.05),  # 5% falha
        FaultTolerantProcessor("Processor_B", 0.15),  # 15% falha
        FaultTolerantProcessor("Processor_C", 0.25),  # 25% falha
    ]
    
    # Dataset de teste
    test_data = [f"data_item_{i}" for i in range(200)]
    
    print("🔄 Processando dados com tolerância a falhas...")
    
    # Processar dados distribuindo entre processadores
    for i, data in enumerate(test_data):
        processor = processors[i % len(processors)]
        try:
            result = processor.process_with_retry(data, max_retries=2)
        except Exception:
            print(f"  💀 Dados perdidos: {data}")
    
    # Mostrar estatísticas
    print(f"\n📊 ESTATÍSTICAS DE TOLERÂNCIA A FALHAS:")
    total_processed = 0
    total_failed = 0
    total_retries = 0
    
    for processor in processors:
        stats = processor.get_stats()
        print(f"\n  🔧 {processor.name}:")
        print(f"     • Processados: {stats['processed']}")
        print(f"     • Falhados: {stats['failed']}")
        print(f"     • Tentativas: {stats['retries']}")
        print(f"     • Taxa de sucesso: {stats['success_rate']:.1f}%")
        
        total_processed += stats['processed']
        total_failed += stats['failed']
        total_retries += stats['retries']
    
    print(f"\n📈 TOTAIS:")
    print(f"  • Total processado: {total_processed}/{len(test_data)}")
    print(f"  • Total falhado: {total_failed}")
    print(f"  • Total de retries: {total_retries}")
    print(f"  • Taxa geral de sucesso: {(total_processed/len(test_data))*100:.1f}%")

if __name__ == "__main__":
    print("🔄 AULA 02: Processamento Distribuído")
    print("=" * 50)
    print("Professor: Vagner Cordeiro")
    print("Curso: Tópicos de Big Data em Python")
    print("=" * 50)
    
    try:
        # Executar demonstrações
        simulate_distributed_system()
        demonstrate_mapreduce_pattern()
        demonstrate_fault_tolerance()
        
        print("\n✅ DEMONSTRAÇÕES CONCLUÍDAS!")
        print("\n📚 CONCEITOS COBERTOS:")
        print("  • Message Queues e Publisher-Subscriber")
        print("  • Load Balancing e distribuição de trabalho")
        print("  • Padrão MapReduce para Big Data")
        print("  • Tolerância a falhas e retry patterns")
        print("  • Processamento paralelo e concorrente")
        
        print("\n🎯 PRÓXIMA AULA:")
        print("  Aula 03: Plataformas em Nuvem e Streaming")
        
    except KeyboardInterrupt:
        print("\n⏹️  Execução interrompida pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro durante a execução: {e}")
        import traceback
        traceback.print_exc()
