#!/usr/bin/env python3
"""
Aula 03: Simulação de Serviços Cloud para Big Data
Professor: Vagner Cordeiro
Curso: Tópicos de Big Data em Python

Este script simula diferentes serviços de cloud computing
para processamento de Big Data, incluindo storage, compute e analytics.
"""

import json
import time
import random
import threading
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
import sqlite3
import hashlib
from collections import defaultdict, deque
import uuid
import matplotlib.pyplot as plt

class CloudStorage:
    """Simula serviços de armazenamento cloud (S3, GCS, Blob Storage)"""
    
    def __init__(self, provider="AWS_S3"):
        self.provider = provider
        self.buckets = {}
        self.total_storage = 0
        self.operations = []
        self.costs = {
            "storage_gb_month": 0.023,  # $0.023 per GB/month
            "get_requests": 0.0004,     # $0.0004 per 1000 requests
            "put_requests": 0.005,      # $0.005 per 1000 requests
            "data_transfer": 0.09       # $0.09 per GB
        }
    
    def create_bucket(self, bucket_name, region="us-east-1"):
        """Cria um bucket de armazenamento"""
        if bucket_name not in self.buckets:
            self.buckets[bucket_name] = {
                "region": region,
                "objects": {},
                "created_at": datetime.now(),
                "size_gb": 0
            }
            print(f"☁️  Bucket '{bucket_name}' criado em {region}")
            return True
        return False
    
    def upload_object(self, bucket_name, object_key, data_size_mb):
        """Simula upload de objeto"""
        if bucket_name in self.buckets:
            object_id = str(uuid.uuid4())
            size_gb = data_size_mb / 1024
            
            self.buckets[bucket_name]["objects"][object_key] = {
                "object_id": object_id,
                "size_gb": size_gb,
                "uploaded_at": datetime.now(),
                "access_count": 0
            }
            
            self.buckets[bucket_name]["size_gb"] += size_gb
            self.total_storage += size_gb
            
            # Registrar operação para custo
            self.operations.append({
                "type": "PUT",
                "timestamp": datetime.now(),
                "size_gb": size_gb
            })
            
            print(f"⬆️  Upload: {object_key} ({data_size_mb}MB) para {bucket_name}")
            return object_id
        return None
    
    def download_object(self, bucket_name, object_key):
        """Simula download de objeto"""
        if bucket_name in self.buckets and object_key in self.buckets[bucket_name]["objects"]:
            obj = self.buckets[bucket_name]["objects"][object_key]
            obj["access_count"] += 1
            
            # Registrar operação
            self.operations.append({
                "type": "GET",
                "timestamp": datetime.now(),
                "size_gb": obj["size_gb"]
            })
            
            print(f"⬇️  Download: {object_key} de {bucket_name}")
            return obj
        return None
    
    def list_objects(self, bucket_name, prefix=""):
        """Lista objetos em um bucket"""
        if bucket_name in self.buckets:
            objects = []
            for key, obj in self.buckets[bucket_name]["objects"].items():
                if key.startswith(prefix):
                    objects.append({
                        "key": key,
                        "size_gb": obj["size_gb"],
                        "last_modified": obj["uploaded_at"]
                    })
            return objects
        return []
    
    def calculate_monthly_cost(self):
        """Calcula custo mensal estimado"""
        storage_cost = self.total_storage * self.costs["storage_gb_month"]
        
        get_requests = sum(1 for op in self.operations if op["type"] == "GET")
        put_requests = sum(1 for op in self.operations if op["type"] == "PUT")
        
        request_cost = (get_requests * self.costs["get_requests"] / 1000 + 
                       put_requests * self.costs["put_requests"] / 1000)
        
        transfer_cost = sum(op["size_gb"] for op in self.operations if op["type"] == "GET") * self.costs["data_transfer"]
        
        return {
            "storage_cost": storage_cost,
            "request_cost": request_cost,
            "transfer_cost": transfer_cost,
            "total_cost": storage_cost + request_cost + transfer_cost
        }
    
    def get_analytics(self):
        """Retorna analytics do storage"""
        total_objects = sum(len(bucket["objects"]) for bucket in self.buckets.values())
        
        return {
            "total_buckets": len(self.buckets),
            "total_objects": total_objects,
            "total_storage_gb": self.total_storage,
            "total_operations": len(self.operations),
            "average_object_size_mb": (self.total_storage * 1024 / total_objects) if total_objects > 0 else 0
        }

class CloudCompute:
    """Simula serviços de compute cloud (EC2, Compute Engine, VMs)"""
    
    def __init__(self, provider="AWS_EC2"):
        self.provider = provider
        self.instances = {}
        self.instance_types = {
            "t3.small": {"vcpus": 2, "memory_gb": 2, "cost_per_hour": 0.0208},
            "t3.medium": {"vcpus": 2, "memory_gb": 4, "cost_per_hour": 0.0416},
            "t3.large": {"vcpus": 2, "memory_gb": 8, "cost_per_hour": 0.0832},
            "c5.large": {"vcpus": 2, "memory_gb": 4, "cost_per_hour": 0.085},
            "c5.xlarge": {"vcpus": 4, "memory_gb": 8, "cost_per_hour": 0.17},
            "r5.large": {"vcpus": 2, "memory_gb": 16, "cost_per_hour": 0.126},
            "r5.xlarge": {"vcpus": 4, "memory_gb": 32, "cost_per_hour": 0.252}
        }
        
    def launch_instance(self, instance_type, instance_name, auto_scaling=False):
        """Lança uma instância de compute"""
        if instance_type in self.instance_types:
            instance_id = f"i-{uuid.uuid4().hex[:8]}"
            
            self.instances[instance_id] = {
                "instance_name": instance_name,
                "instance_type": instance_type,
                "state": "running",
                "launched_at": datetime.now(),
                "cpu_utilization": [],
                "memory_utilization": [],
                "auto_scaling": auto_scaling,
                "processing_jobs": []
            }
            
            specs = self.instance_types[instance_type]
            print(f"🚀 Instância {instance_name} ({instance_type}) iniciada: {specs['vcpus']} vCPUs, {specs['memory_gb']}GB RAM")
            return instance_id
        return None
    
    def terminate_instance(self, instance_id):
        """Termina uma instância"""
        if instance_id in self.instances:
            self.instances[instance_id]["state"] = "terminated"
            self.instances[instance_id]["terminated_at"] = datetime.now()
            print(f"🛑 Instância {instance_id} terminada")
            return True
        return False
    
    def submit_job(self, instance_id, job_data):
        """Submete um job para processamento"""
        if instance_id in self.instances and self.instances[instance_id]["state"] == "running":
            job_id = str(uuid.uuid4())
            
            job = {
                "job_id": job_id,
                "submitted_at": datetime.now(),
                "data_size_gb": job_data.get("size_gb", 1),
                "complexity": job_data.get("complexity", "medium"),
                "status": "queued"
            }
            
            self.instances[instance_id]["processing_jobs"].append(job)
            return job_id
        return None
    
    def simulate_processing(self, duration_minutes=5):
        """Simula processamento de jobs"""
        print(f"⚙️  Simulando processamento por {duration_minutes} minutos...")
        
        def process_instance_jobs(instance_id):
            instance = self.instances[instance_id]
            if instance["state"] != "running":
                return
            
            specs = self.instance_types[instance["instance_type"]]
            
            for job in instance["processing_jobs"]:
                if job["status"] == "queued":
                    job["status"] = "running"
                    job["started_at"] = datetime.now()
                    
                    # Simular utilização de recursos
                    base_cpu = 30
                    base_memory = 40
                    
                    if job["complexity"] == "high":
                        base_cpu += 40
                        base_memory += 30
                    elif job["complexity"] == "medium":
                        base_cpu += 20
                        base_memory += 15
                    
                    # Simular variação na utilização
                    cpu_util = min(100, base_cpu + random.randint(-10, 20))
                    memory_util = min(100, base_memory + random.randint(-10, 15))
                    
                    instance["cpu_utilization"].append(cpu_util)
                    instance["memory_utilization"].append(memory_util)
                    
                    # Simular tempo de processamento
                    processing_time = job["data_size_gb"] * random.uniform(0.5, 2.0)
                    time.sleep(min(processing_time, 1))  # Limitar para simulação
                    
                    job["status"] = "completed"
                    job["completed_at"] = datetime.now()
        
        # Processar jobs em paralelo
        with ThreadPoolExecutor(max_workers=len(self.instances)) as executor:
            futures = []
            for instance_id in self.instances:
                future = executor.submit(process_instance_jobs, instance_id)
                futures.append(future)
            
            for future in as_completed(futures):
                future.result()
    
    def get_utilization_stats(self):
        """Retorna estatísticas de utilização"""
        stats = {}
        
        for instance_id, instance in self.instances.items():
            if instance["cpu_utilization"] and instance["memory_utilization"]:
                stats[instance_id] = {
                    "instance_name": instance["instance_name"],
                    "instance_type": instance["instance_type"],
                    "avg_cpu": np.mean(instance["cpu_utilization"]),
                    "avg_memory": np.mean(instance["memory_utilization"]),
                    "jobs_completed": len([j for j in instance["processing_jobs"] if j["status"] == "completed"]),
                    "state": instance["state"]
                }
        
        return stats
    
    def calculate_cost(self, hours_running=24):
        """Calcula custo de compute"""
        total_cost = 0
        cost_breakdown = {}
        
        for instance_id, instance in self.instances.items():
            instance_type = instance["instance_type"]
            cost_per_hour = self.instance_types[instance_type]["cost_per_hour"]
            
            if instance["state"] == "running":
                instance_cost = cost_per_hour * hours_running
                total_cost += instance_cost
                cost_breakdown[instance_id] = {
                    "instance_name": instance["instance_name"],
                    "instance_type": instance_type,
                    "cost": instance_cost
                }
        
        return {"total_cost": total_cost, "breakdown": cost_breakdown}

class StreamingPipeline:
    """Simula pipeline de streaming de dados (Kinesis, Pub/Sub, Event Hubs)"""
    
    def __init__(self, name, provider="AWS_Kinesis"):
        self.name = name
        self.provider = provider
        self.streams = {}
        self.consumers = {}
        self.metrics = {
            "messages_processed": 0,
            "bytes_processed": 0,
            "errors": 0,
            "latency_ms": []
        }
        
    def create_stream(self, stream_name, shard_count=1):
        """Cria um stream de dados"""
        self.streams[stream_name] = {
            "shard_count": shard_count,
            "created_at": datetime.now(),
            "records": deque(maxlen=10000),  # Buffer limitado
            "partition_keys": set()
        }
        print(f"🌊 Stream '{stream_name}' criado com {shard_count} shards")
        
    def put_record(self, stream_name, data, partition_key=None):
        """Adiciona record ao stream"""
        if stream_name in self.streams:
            record = {
                "data": data,
                "partition_key": partition_key or str(uuid.uuid4()),
                "timestamp": datetime.now(),
                "sequence_number": len(self.streams[stream_name]["records"])
            }
            
            self.streams[stream_name]["records"].append(record)
            self.streams[stream_name]["partition_keys"].add(record["partition_key"])
            
            return record["sequence_number"]
        return None
    
    def create_consumer(self, consumer_name, stream_name, processing_function):
        """Cria um consumidor para o stream"""
        if stream_name in self.streams:
            self.consumers[consumer_name] = {
                "stream_name": stream_name,
                "processing_function": processing_function,
                "last_processed": -1,
                "records_processed": 0,
                "errors": 0,
                "is_running": False
            }
            print(f"👤 Consumidor '{consumer_name}' criado para stream '{stream_name}'")
            return True
        return False
    
    def start_consumer(self, consumer_name):
        """Inicia processamento do consumidor"""
        if consumer_name in self.consumers:
            consumer = self.consumers[consumer_name]
            consumer["is_running"] = True
            stream_name = consumer["stream_name"]
            
            def consume_records():
                while consumer["is_running"]:
                    stream = self.streams[stream_name]
                    records = list(stream["records"])
                    
                    # Processar records não processados
                    for i, record in enumerate(records):
                        if i > consumer["last_processed"] and consumer["is_running"]:
                            try:
                                start_time = time.time()
                                
                                # Chamar função de processamento
                                result = consumer["processing_function"](record)
                                
                                processing_time = (time.time() - start_time) * 1000
                                self.metrics["latency_ms"].append(processing_time)
                                
                                consumer["records_processed"] += 1
                                consumer["last_processed"] = i
                                self.metrics["messages_processed"] += 1
                                
                                # Simular dados processados
                                data_size = len(str(record["data"]))
                                self.metrics["bytes_processed"] += data_size
                                
                            except Exception as e:
                                consumer["errors"] += 1
                                self.metrics["errors"] += 1
                                print(f"❌ Erro processando record: {e}")
                    
                    time.sleep(0.1)  # Polling interval
            
            # Iniciar em thread separada
            thread = threading.Thread(target=consume_records)
            thread.daemon = True
            thread.start()
            
            print(f"▶️  Consumidor '{consumer_name}' iniciado")
            return True
        return False
    
    def stop_consumer(self, consumer_name):
        """Para o consumidor"""
        if consumer_name in self.consumers:
            self.consumers[consumer_name]["is_running"] = False
            print(f"⏹️  Consumidor '{consumer_name}' parado")
            return True
        return False
    
    def get_stream_metrics(self):
        """Retorna métricas dos streams"""
        stream_stats = {}
        
        for stream_name, stream in self.streams.items():
            stream_stats[stream_name] = {
                "record_count": len(stream["records"]),
                "partition_count": len(stream["partition_keys"]),
                "shard_count": stream["shard_count"]
            }
        
        consumer_stats = {}
        for consumer_name, consumer in self.consumers.items():
            consumer_stats[consumer_name] = {
                "records_processed": consumer["records_processed"],
                "errors": consumer["errors"],
                "is_running": consumer["is_running"]
            }
        
        # Métricas globais
        global_metrics = self.metrics.copy()
        if global_metrics["latency_ms"]:
            global_metrics["avg_latency_ms"] = np.mean(global_metrics["latency_ms"])
            global_metrics["p95_latency_ms"] = np.percentile(global_metrics["latency_ms"], 95)
        
        return {
            "streams": stream_stats,
            "consumers": consumer_stats,
            "global_metrics": global_metrics
        }

def simulate_cloud_big_data_platform():
    """Simula uma plataforma completa de Big Data na nuvem"""
    print("☁️  SIMULAÇÃO: Plataforma Big Data na Nuvem")
    print("=" * 55)
    
    # 1. Configurar Storage
    print("\n📦 Configurando Cloud Storage...")
    storage = CloudStorage("AWS_S3")
    
    # Criar buckets
    storage.create_bucket("raw-data", "us-east-1")
    storage.create_bucket("processed-data", "us-east-1")
    storage.create_bucket("analytics-results", "us-west-2")
    
    # Simular uploads de dados
    datasets = [
        ("user_events_2025_01.parquet", 250),
        ("transactions_daily.csv", 150),
        ("sensor_data_stream.json", 500),
        ("ml_training_data.npz", 1200),
        ("web_logs_archive.gz", 800)
    ]
    
    for filename, size_mb in datasets:
        storage.upload_object("raw-data", filename, size_mb)
    
    # 2. Configurar Compute
    print("\n⚙️  Configurando Cloud Compute...")
    compute = CloudCompute("AWS_EC2")
    
    # Lançar instâncias para diferentes workloads
    instances = [
        ("data-processing-1", "c5.xlarge"),
        ("analytics-worker-1", "r5.large"),
        ("streaming-processor", "c5.large"),
        ("ml-training", "r5.xlarge")
    ]
    
    instance_ids = []
    for name, instance_type in instances:
        instance_id = compute.launch_instance(instance_type, name)
        instance_ids.append(instance_id)
    
    # 3. Configurar Streaming
    print("\n🌊 Configurando Streaming Pipeline...")
    
    def process_user_event(record):
        """Processa eventos de usuário"""
        data = record["data"]
        # Simular processamento de evento
        return {
            "processed_event": data,
            "processed_at": datetime.now().isoformat(),
            "user_segment": random.choice(["premium", "standard", "basic"])
        }
    
    def process_transaction(record):
        """Processa transações"""
        data = record["data"]
        # Simular detecção de fraude
        fraud_score = random.uniform(0, 1)
        return {
            "transaction": data,
            "fraud_score": fraud_score,
            "is_suspicious": fraud_score > 0.8
        }
    
    # Criar pipeline de streaming
    pipeline = StreamingPipeline("main-pipeline", "AWS_Kinesis")
    pipeline.create_stream("user-events", shard_count=3)
    pipeline.create_stream("transactions", shard_count=2)
    
    # Criar consumidores
    pipeline.create_consumer("event-processor", "user-events", process_user_event)
    pipeline.create_consumer("fraud-detector", "transactions", process_transaction)
    
    # 4. Simular workload
    print("\n🚀 Simulando workload de Big Data...")
    
    # Gerar dados de streaming
    def generate_streaming_data():
        for i in range(1000):
            # Eventos de usuário
            user_event = {
                "user_id": f"user_{random.randint(1, 10000)}",
                "event_type": random.choice(["click", "view", "purchase", "logout"]),
                "timestamp": datetime.now().isoformat(),
                "page": f"/page_{random.randint(1, 100)}"
            }
            pipeline.put_record("user-events", user_event, f"user_{random.randint(1, 1000)}")
            
            # Transações (menos frequentes)
            if random.random() < 0.3:
                transaction = {
                    "transaction_id": str(uuid.uuid4()),
                    "amount": round(random.uniform(10, 1000), 2),
                    "merchant": f"merchant_{random.randint(1, 500)}",
                    "timestamp": datetime.now().isoformat()
                }
                pipeline.put_record("transactions", transaction, transaction["transaction_id"])
            
            time.sleep(0.01)  # 100 eventos por segundo
    
    # Iniciar consumidores
    pipeline.start_consumer("event-processor")
    pipeline.start_consumer("fraud-detector")
    
    # Gerar dados em thread separada
    data_thread = threading.Thread(target=generate_streaming_data)
    data_thread.start()
    
    # Submeter jobs de processamento
    jobs = [
        {"size_gb": 2.5, "complexity": "high"},
        {"size_gb": 1.2, "complexity": "medium"},
        {"size_gb": 0.8, "complexity": "low"},
        {"size_gb": 3.1, "complexity": "high"}
    ]
    
    for i, job in enumerate(jobs):
        instance_id = instance_ids[i % len(instance_ids)]
        compute.submit_job(instance_id, job)
    
    # Executar processamento
    compute.simulate_processing(duration_minutes=2)
    
    # Aguardar dados de streaming
    data_thread.join()
    
    # Parar consumidores
    pipeline.stop_consumer("event-processor")
    pipeline.stop_consumer("fraud-detector")
    
    # 5. Análise de resultados
    print("\n📊 ANÁLISE DE RESULTADOS")
    print("=" * 30)
    
    # Storage analytics
    storage_analytics = storage.get_analytics()
    storage_costs = storage.calculate_monthly_cost()
    
    print(f"\n💾 STORAGE:")
    print(f"  • Total de objetos: {storage_analytics['total_objects']}")
    print(f"  • Armazenamento total: {storage_analytics['total_storage_gb']:.2f} GB")
    print(f"  • Custo mensal estimado: ${storage_costs['total_cost']:.2f}")
    
    # Compute analytics
    compute_stats = compute.get_utilization_stats()
    compute_costs = compute.calculate_cost(hours_running=1)
    
    print(f"\n⚙️  COMPUTE:")
    for instance_id, stats in compute_stats.items():
        print(f"  • {stats['instance_name']}: CPU {stats['avg_cpu']:.1f}%, RAM {stats['avg_memory']:.1f}%")
        print(f"    Jobs completos: {stats['jobs_completed']}")
    print(f"  • Custo por hora: ${compute_costs['total_cost']:.2f}")
    
    # Streaming analytics
    streaming_metrics = pipeline.get_stream_metrics()
    
    print(f"\n🌊 STREAMING:")
    print(f"  • Mensagens processadas: {streaming_metrics['global_metrics']['messages_processed']}")
    print(f"  • Dados processados: {streaming_metrics['global_metrics']['bytes_processed']} bytes")
    if "avg_latency_ms" in streaming_metrics["global_metrics"]:
        print(f"  • Latência média: {streaming_metrics['global_metrics']['avg_latency_ms']:.2f}ms")
        print(f"  • Latência P95: {streaming_metrics['global_metrics']['p95_latency_ms']:.2f}ms")
    
    # Terminar instâncias
    print(f"\n🛑 Terminando instâncias...")
    for instance_id in instance_ids:
        compute.terminate_instance(instance_id)
    
    # Custo total estimado
    total_monthly_cost = storage_costs['total_cost'] + (compute_costs['total_cost'] * 24 * 30)
    print(f"\n💰 CUSTO TOTAL ESTIMADO (mensal): ${total_monthly_cost:.2f}")

def demonstrate_auto_scaling():
    """Demonstra conceitos de auto-scaling"""
    print("\n🔄 DEMONSTRAÇÃO: Auto-Scaling")
    print("=" * 40)
    
    class AutoScaler:
        def __init__(self, min_instances=1, max_instances=10, target_cpu=70):
            self.min_instances = min_instances
            self.max_instances = max_instances
            self.target_cpu = target_cpu
            self.current_instances = min_instances
            self.cpu_history = deque(maxlen=5)
            
        def add_cpu_metric(self, cpu_utilization):
            """Adiciona métrica de CPU"""
            self.cpu_history.append(cpu_utilization)
            
        def should_scale_out(self):
            """Verifica se deve aumentar instâncias"""
            if len(self.cpu_history) >= 3:
                avg_cpu = np.mean(list(self.cpu_history)[-3:])
                return avg_cpu > self.target_cpu and self.current_instances < self.max_instances
            return False
            
        def should_scale_in(self):
            """Verifica se deve diminuir instâncias"""
            if len(self.cpu_history) >= 3:
                avg_cpu = np.mean(list(self.cpu_history)[-3:])
                return avg_cpu < (self.target_cpu * 0.5) and self.current_instances > self.min_instances
            return False
            
        def scale_out(self):
            """Aumenta número de instâncias"""
            if self.current_instances < self.max_instances:
                self.current_instances += 1
                print(f"📈 Scale OUT: {self.current_instances} instâncias")
                return True
            return False
            
        def scale_in(self):
            """Diminui número de instâncias"""
            if self.current_instances > self.min_instances:
                self.current_instances -= 1
                print(f"📉 Scale IN: {self.current_instances} instâncias")
                return True
            return False
    
    # Simular workload variável
    autoscaler = AutoScaler(min_instances=2, max_instances=8, target_cpu=75)
    
    # Simular padrão de carga durante o dia
    hours = 24
    cpu_patterns = []
    
    for hour in range(hours):
        # Simular padrão de uso típico (picos nos horários comerciais)
        if 8 <= hour <= 18:
            base_cpu = 60 + (hour - 8) * 5  # Aumenta gradualmente
            if 12 <= hour <= 14:  # Pico do almoço
                base_cpu += 20
            if 17 <= hour <= 18:  # Pico do final do dia
                base_cpu += 15
        else:
            base_cpu = 20 + random.randint(-10, 10)  # Carga baixa
        
        # Adicionar ruído
        cpu_utilization = max(0, min(100, base_cpu + random.randint(-15, 15)))
        cpu_patterns.append(cpu_utilization)
        
        autoscaler.add_cpu_metric(cpu_utilization)
        
        # Verificar se precisa escalar
        if autoscaler.should_scale_out():
            autoscaler.scale_out()
        elif autoscaler.should_scale_in():
            autoscaler.scale_in()
        
        print(f"⏰ Hora {hour:2d}: CPU {cpu_utilization:3.0f}% | Instâncias: {autoscaler.current_instances}")
    
    print(f"\n📊 Resumo Auto-Scaling:")
    print(f"  • CPU máxima: {max(cpu_patterns):.0f}%")
    print(f"  • CPU média: {np.mean(cpu_patterns):.0f}%")
    print(f"  • Instâncias finais: {autoscaler.current_instances}")

if __name__ == "__main__":
    print("☁️  AULA 03: Plataformas em Nuvem e Streaming")
    print("=" * 60)
    print("Professor: Vagner Cordeiro")
    print("Curso: Tópicos de Big Data em Python")
    print("=" * 60)
    
    try:
        # Executar simulações
        simulate_cloud_big_data_platform()
        demonstrate_auto_scaling()
        
        print("\n✅ SIMULAÇÕES CONCLUÍDAS!")
        print("\n📚 CONCEITOS COBERTOS:")
        print("  • Cloud Storage (S3, GCS, Blob Storage)")
        print("  • Cloud Compute (EC2, Compute Engine, VMs)")
        print("  • Streaming de dados (Kinesis, Pub/Sub, Event Hubs)")
        print("  • Auto-scaling e elasticidade")
        print("  • Cost optimization e resource management")
        
        print("\n🎯 PRÓXIMA AULA:")
        print("  Aula 04: Revisão de Python para Análise de Dados")
        
    except KeyboardInterrupt:
        print("\n⏹️  Simulação interrompida pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro durante a execução: {e}")
        import traceback
        traceback.print_exc()
