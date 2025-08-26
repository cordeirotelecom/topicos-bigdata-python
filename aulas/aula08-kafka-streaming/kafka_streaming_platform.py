#!/usr/bin/env python3
"""
Apache Kafka Streaming Implementation
Sistema completo de streaming de dados em tempo real
Professor: Vagner Cordeiro
Curso: Tópicos de Big Data em Python
"""

import os
import sys
import json
import time
import threading
import logging
import random
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import asyncio
from dataclasses import dataclass, asdict
import queue
import uuid

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Importações com tratamento de erros
try:
    from kafka import KafkaProducer, KafkaConsumer, KafkaAdminClient
    from kafka.admin import NewTopic, ConfigResource, ConfigResourceType
    from kafka.errors import TopicAlreadyExistsError
    KAFKA_AVAILABLE = True
    print("✅ Kafka-python disponível")
except ImportError:
    print("⚠️ Kafka-python não está instalado. Usando simulação.")
    KAFKA_AVAILABLE = False

try:
    import redis
    REDIS_AVAILABLE = True
    print("✅ Redis disponível")
except ImportError:
    print("⚠️ Redis não está instalado. Usando simulação.")
    REDIS_AVAILABLE = False

@dataclass
class IoTSensorReading:
    """Estrutura de dados para leitura de sensor IoT"""
    sensor_id: str
    timestamp: datetime
    temperature: float
    humidity: float
    pressure: float
    location: Dict[str, float]
    device_status: str
    battery_level: float

@dataclass
class UserActivityEvent:
    """Estrutura de dados para evento de atividade de usuário"""
    user_id: str
    session_id: str
    event_type: str
    page_url: str
    timestamp: datetime
    user_agent: str
    ip_address: str
    duration: int

@dataclass
class TransactionEvent:
    """Estrutura de dados para transação financeira"""
    transaction_id: str
    user_id: str
    merchant_id: str
    amount: float
    currency: str
    timestamp: datetime
    payment_method: str
    status: str

class MockKafkaProducer:
    """Simulação do KafkaProducer quando kafka não está disponível"""
    
    def __init__(self, **kwargs):
        self.config = kwargs
        self.sent_messages = []
        print(f"🎭 Mock Kafka Producer criado com config: {kwargs}")
    
    def send(self, topic: str, value: bytes = None, key: bytes = None):
        """Simula envio de mensagem"""
        message = {
            'topic': topic,
            'key': key.decode() if key else None,
            'value': value.decode() if value else None,
            'timestamp': datetime.now().isoformat()
        }
        self.sent_messages.append(message)
        print(f"📤 Mock enviado para tópico '{topic}': {len(value)} bytes")
        return MockFuture()
    
    def flush(self):
        """Simula flush"""
        print(f"🔄 Mock flush: {len(self.sent_messages)} mensagens enviadas")
    
    def close(self):
        """Simula fechamento"""
        print("🔒 Mock Producer fechado")

class MockFuture:
    """Simula Future do Kafka"""
    
    def get(self, timeout=None):
        return MockRecordMetadata()

class MockRecordMetadata:
    """Simula metadata de record"""
    
    def __init__(self):
        self.topic = "mock_topic"
        self.partition = 0
        self.offset = random.randint(1000, 9999)

class MockKafkaConsumer:
    """Simulação do KafkaConsumer quando kafka não está disponível"""
    
    def __init__(self, *topics, **kwargs):
        self.topics = topics
        self.config = kwargs
        self.messages_queue = queue.Queue()
        self.running = False
        print(f"🎭 Mock Kafka Consumer criado para tópicos: {topics}")
    
    def subscribe(self, topics):
        """Simula subscription"""
        self.topics = topics
        print(f"📋 Mock subscrito aos tópicos: {topics}")
    
    def poll(self, timeout_ms=1000):
        """Simula polling de mensagens"""
        if not self.running:
            return {}
        
        try:
            message = self.messages_queue.get(timeout=timeout_ms/1000)
            return {0: [message]}
        except queue.Empty:
            return {}
    
    def close(self):
        """Simula fechamento"""
        self.running = False
        print("🔒 Mock Consumer fechado")

class MockRedis:
    """Simulação do Redis quando não está disponível"""
    
    def __init__(self, **kwargs):
        self.data = {}
        self.config = kwargs
        print(f"🎭 Mock Redis criado com config: {kwargs}")
    
    def set(self, key, value, ex=None):
        """Simula set no Redis"""
        self.data[key] = {'value': value, 'expires': time.time() + (ex or 3600)}
        print(f"💾 Mock Redis SET: {key} = {len(str(value))} chars")
    
    def get(self, key):
        """Simula get do Redis"""
        if key in self.data:
            if time.time() < self.data[key]['expires']:
                return self.data[key]['value']
            else:
                del self.data[key]
        return None
    
    def delete(self, key):
        """Simula delete do Redis"""
        if key in self.data:
            del self.data[key]
            return 1
        return 0

class KafkaStreamingPlatform:
    """Plataforma completa de streaming com Apache Kafka"""
    
    def __init__(self, kafka_config: Optional[Dict] = None, redis_config: Optional[Dict] = None):
        """Inicializa a plataforma de streaming"""
        
        # Configuração padrão do Kafka
        self.kafka_config = kafka_config or {
            'bootstrap_servers': ['localhost:9092'],
            'value_serializer': lambda x: json.dumps(x, default=str).encode('utf-8'),
            'key_serializer': lambda x: x.encode('utf-8') if x else None
        }
        
        # Configuração padrão do Redis
        self.redis_config = redis_config or {
            'host': 'localhost',
            'port': 6379,
            'db': 0,
            'decode_responses': True
        }
        
        # Inicializar componentes
        self.producer = None
        self.consumers = {}
        self.cache = None
        self.running = False
        self.topics_created = set()
        
        # Estatísticas
        self.stats = {
            'messages_sent': 0,
            'messages_received': 0,
            'errors': 0,
            'start_time': None
        }
        
        self._initialize_components()
    
    def _initialize_components(self):
        """Inicializa componentes Kafka e Redis"""
        try:
            if KAFKA_AVAILABLE:
                self.producer = KafkaProducer(**self.kafka_config)
                print("✅ Kafka Producer inicializado")
            else:
                self.producer = MockKafkaProducer(**self.kafka_config)
            
            if REDIS_AVAILABLE:
                self.cache = redis.Redis(**self.redis_config)
                # Testar conexão
                self.cache.ping()
                print("✅ Redis cache inicializado")
            else:
                self.cache = MockRedis(**self.redis_config)
                
        except Exception as e:
            logger.error(f"Erro ao inicializar componentes: {e}")
            # Usar versões simuladas
            self.producer = MockKafkaProducer(**self.kafka_config)
            self.cache = MockRedis(**self.redis_config)
    
    def create_topic(self, topic_name: str, num_partitions: int = 3, replication_factor: int = 1):
        """Cria um tópico no Kafka"""
        if not KAFKA_AVAILABLE:
            print(f"🎭 Mock: Tópico '{topic_name}' criado (simulação)")
            return
        
        try:
            admin_client = KafkaAdminClient(
                bootstrap_servers=self.kafka_config['bootstrap_servers']
            )
            
            topic = NewTopic(
                name=topic_name,
                num_partitions=num_partitions,
                replication_factor=replication_factor
            )
            
            admin_client.create_topics([topic])
            self.topics_created.add(topic_name)
            print(f"✅ Tópico '{topic_name}' criado com sucesso")
            
        except TopicAlreadyExistsError:
            print(f"⚠️ Tópico '{topic_name}' já existe")
        except Exception as e:
            logger.error(f"Erro ao criar tópico '{topic_name}': {e}")
    
    def start_iot_sensor_producer(self, topic: str = "iot-sensors", sensors_count: int = 10):
        """Inicia producer de dados de sensores IoT"""
        
        def generate_sensor_data():
            """Gera dados de sensores IoT"""
            sensor_ids = [f"sensor_{i:03d}" for i in range(1, sensors_count + 1)]
            
            while self.running:
                try:
                    for sensor_id in sensor_ids:
                        reading = IoTSensorReading(
                            sensor_id=sensor_id,
                            timestamp=datetime.now(),
                            temperature=random.uniform(18.0, 35.0),
                            humidity=random.uniform(30.0, 90.0),
                            pressure=random.uniform(990.0, 1020.0),
                            location={
                                'latitude': random.uniform(-90.0, 90.0),
                                'longitude': random.uniform(-180.0, 180.0)
                            },
                            device_status=random.choice(['online', 'offline', 'maintenance']),
                            battery_level=random.uniform(0.1, 1.0)
                        )
                        
                        # Converter para dict e enviar
                        data = asdict(reading)
                        self.send_message(topic, data, key=sensor_id)
                        
                        # Cache dos últimos dados
                        self.cache.set(f"sensor_last_{sensor_id}", json.dumps(data, default=str), ex=300)
                        
                        time.sleep(random.uniform(0.5, 2.0))
                        
                except Exception as e:
                    logger.error(f"Erro no producer IoT: {e}")
                    self.stats['errors'] += 1
                    time.sleep(1)
        
        # Criar tópico se necessário
        self.create_topic(topic)
        
        # Iniciar thread do producer
        thread = threading.Thread(target=generate_sensor_data, daemon=True)
        thread.start()
        print(f"🚀 Producer IoT iniciado para {sensors_count} sensores no tópico '{topic}'")
        
        return thread
    
    def start_user_activity_producer(self, topic: str = "user-activity", users_count: int = 100):
        """Inicia producer de atividade de usuários"""
        
        def generate_user_activity():
            """Gera eventos de atividade de usuário"""
            user_ids = [f"user_{i:05d}" for i in range(1, users_count + 1)]
            event_types = ['page_view', 'click', 'purchase', 'login', 'logout', 'search']
            pages = ['/home', '/products', '/cart', '/checkout', '/profile', '/support']
            
            while self.running:
                try:
                    user_id = random.choice(user_ids)
                    session_id = str(uuid.uuid4())
                    
                    event = UserActivityEvent(
                        user_id=user_id,
                        session_id=session_id,
                        event_type=random.choice(event_types),
                        page_url=random.choice(pages),
                        timestamp=datetime.now(),
                        user_agent="Mozilla/5.0 (compatible; StreamingBot/1.0)",
                        ip_address=f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                        duration=random.randint(1, 300)
                    )
                    
                    data = asdict(event)
                    self.send_message(topic, data, key=user_id)
                    
                    # Cache da sessão
                    self.cache.set(f"session_{session_id}", json.dumps(data, default=str), ex=1800)
                    
                    time.sleep(random.uniform(0.1, 1.0))
                    
                except Exception as e:
                    logger.error(f"Erro no producer de atividade: {e}")
                    self.stats['errors'] += 1
                    time.sleep(1)
        
        # Criar tópico se necessário
        self.create_topic(topic)
        
        # Iniciar thread do producer
        thread = threading.Thread(target=generate_user_activity, daemon=True)
        thread.start()
        print(f"🚀 Producer de atividade iniciado para {users_count} usuários no tópico '{topic}'")
        
        return thread
    
    def start_transaction_producer(self, topic: str = "transactions"):
        """Inicia producer de transações financeiras"""
        
        def generate_transactions():
            """Gera transações financeiras"""
            merchants = ['Amazon', 'PayPal', 'Stripe', 'Square', 'Shopify']
            currencies = ['USD', 'EUR', 'BRL', 'GBP', 'JPY']
            payment_methods = ['credit_card', 'debit_card', 'paypal', 'bank_transfer', 'crypto']
            
            while self.running:
                try:
                    transaction = TransactionEvent(
                        transaction_id=str(uuid.uuid4()),
                        user_id=f"user_{random.randint(1, 10000):05d}",
                        merchant_id=random.choice(merchants),
                        amount=round(random.uniform(10.0, 5000.0), 2),
                        currency=random.choice(currencies),
                        timestamp=datetime.now(),
                        payment_method=random.choice(payment_methods),
                        status=random.choice(['pending', 'completed', 'failed', 'refunded'])
                    )
                    
                    data = asdict(transaction)
                    self.send_message(topic, data, key=transaction.transaction_id)
                    
                    # Cache da transação
                    self.cache.set(f"tx_{transaction.transaction_id}", json.dumps(data, default=str), ex=86400)
                    
                    time.sleep(random.uniform(1.0, 5.0))
                    
                except Exception as e:
                    logger.error(f"Erro no producer de transações: {e}")
                    self.stats['errors'] += 1
                    time.sleep(1)
        
        # Criar tópico se necessário
        self.create_topic(topic)
        
        # Iniciar thread do producer
        thread = threading.Thread(target=generate_transactions, daemon=True)
        thread.start()
        print(f"🚀 Producer de transações iniciado no tópico '{topic}'")
        
        return thread
    
    def send_message(self, topic: str, data: Dict, key: str = None):
        """Envia mensagem para um tópico"""
        try:
            future = self.producer.send(
                topic,
                value=json.dumps(data, default=str).encode('utf-8'),
                key=key.encode('utf-8') if key else None
            )
            
            self.stats['messages_sent'] += 1
            
            if KAFKA_AVAILABLE:
                # Aguardar confirmação
                record_metadata = future.get(timeout=10)
                logger.debug(f"Mensagem enviada para {record_metadata.topic}[{record_metadata.partition}] offset {record_metadata.offset}")
            
        except Exception as e:
            logger.error(f"Erro ao enviar mensagem: {e}")
            self.stats['errors'] += 1
    
    def start_consumer(self, topics: List[str], consumer_id: str, processor_func=None):
        """Inicia um consumer para os tópicos especificados"""
        
        def default_processor(message):
            """Processador padrão de mensagens"""
            data = json.loads(message.value.decode('utf-8'))
            print(f"📨 [{consumer_id}] Processando: {data.get('timestamp', 'N/A')} - {message.topic}")
            self.stats['messages_received'] += 1
        
        def consume_messages():
            """Consome mensagens dos tópicos"""
            if KAFKA_AVAILABLE:
                consumer_config = {
                    'bootstrap_servers': self.kafka_config['bootstrap_servers'],
                    'group_id': consumer_id,
                    'auto_offset_reset': 'latest',
                    'value_deserializer': lambda m: m.decode('utf-8') if m else None
                }
                consumer = KafkaConsumer(**consumer_config)
            else:
                consumer = MockKafkaConsumer()
            
            consumer.subscribe(topics)
            
            print(f"🔄 Consumer '{consumer_id}' iniciado para tópicos: {topics}")
            
            processor = processor_func or default_processor
            
            while self.running:
                try:
                    message_batch = consumer.poll(timeout_ms=1000)
                    
                    for partition_messages in message_batch.values():
                        for message in partition_messages:
                            processor(message)
                            
                except Exception as e:
                    logger.error(f"Erro no consumer {consumer_id}: {e}")
                    self.stats['errors'] += 1
                    time.sleep(1)
            
            consumer.close()
            print(f"🔒 Consumer '{consumer_id}' finalizado")
        
        # Iniciar thread do consumer
        thread = threading.Thread(target=consume_messages, daemon=True)
        thread.start()
        self.consumers[consumer_id] = thread
        
        return thread
    
    def start_analytics_consumer(self):
        """Inicia consumer de analytics em tempo real"""
        
        analytics_data = {
            'iot_sensors': {'count': 0, 'avg_temp': 0, 'last_update': None},
            'user_activity': {'count': 0, 'events_per_minute': 0, 'last_update': None},
            'transactions': {'count': 0, 'total_amount': 0, 'last_update': None}
        }
        
        def analytics_processor(message):
            """Processa mensagens para analytics"""
            try:
                data = json.loads(message.value.decode('utf-8'))
                topic = message.topic
                now = datetime.now()
                
                if 'iot' in topic:
                    analytics_data['iot_sensors']['count'] += 1
                    if 'temperature' in data:
                        current_avg = analytics_data['iot_sensors']['avg_temp']
                        count = analytics_data['iot_sensors']['count']
                        new_avg = ((current_avg * (count - 1)) + data['temperature']) / count
                        analytics_data['iot_sensors']['avg_temp'] = round(new_avg, 2)
                    analytics_data['iot_sensors']['last_update'] = now
                
                elif 'activity' in topic:
                    analytics_data['user_activity']['count'] += 1
                    analytics_data['user_activity']['last_update'] = now
                
                elif 'transaction' in topic:
                    analytics_data['transactions']['count'] += 1
                    if 'amount' in data:
                        analytics_data['transactions']['total_amount'] += data['amount']
                    analytics_data['transactions']['last_update'] = now
                
                # Salvar analytics no cache
                self.cache.set('analytics_data', json.dumps(analytics_data, default=str), ex=60)
                
                # Log periódico
                if analytics_data['iot_sensors']['count'] % 50 == 0:
                    print(f"📊 Analytics: {analytics_data}")
                
            except Exception as e:
                logger.error(f"Erro no processamento analytics: {e}")
        
        return self.start_consumer(
            ['iot-sensors', 'user-activity', 'transactions'],
            'analytics-consumer',
            analytics_processor
        )
    
    def get_analytics(self) -> Dict:
        """Retorna dados de analytics"""
        cached_data = self.cache.get('analytics_data')
        if cached_data:
            return json.loads(cached_data)
        return {}
    
    def get_stats(self) -> Dict:
        """Retorna estatísticas da plataforma"""
        runtime = 0
        if self.stats['start_time']:
            runtime = (datetime.now() - self.stats['start_time']).total_seconds()
        
        return {
            **self.stats,
            'runtime_seconds': runtime,
            'messages_per_second': self.stats['messages_sent'] / max(runtime, 1),
            'topics_created': len(self.topics_created),
            'active_consumers': len(self.consumers)
        }
    
    def start(self):
        """Inicia a plataforma de streaming"""
        print("🚀 INICIANDO PLATAFORMA KAFKA STREAMING")
        print("=" * 60)
        
        self.running = True
        self.stats['start_time'] = datetime.now()
        
        try:
            # Iniciar producers
            print("\n📤 Iniciando Producers...")
            iot_thread = self.start_iot_sensor_producer()
            activity_thread = self.start_user_activity_producer()
            transaction_thread = self.start_transaction_producer()
            
            # Aguardar um pouco para producers iniciarem
            time.sleep(2)
            
            # Iniciar consumers
            print("\n📥 Iniciando Consumers...")
            analytics_thread = self.start_analytics_consumer()
            
            print(f"\n✅ Plataforma iniciada com sucesso!")
            print(f"📊 Tópicos: {list(self.topics_created)}")
            print(f"🏃 Threads ativas: {threading.active_count()}")
            
            return {
                'producers': [iot_thread, activity_thread, transaction_thread],
                'consumers': [analytics_thread]
            }
            
        except Exception as e:
            logger.error(f"Erro ao iniciar plataforma: {e}")
            self.stop()
            raise
    
    def stop(self):
        """Para a plataforma de streaming"""
        print("\n🛑 Parando plataforma de streaming...")
        
        self.running = False
        
        # Aguardar threads finalizarem
        time.sleep(2)
        
        # Fechar producer
        if self.producer:
            self.producer.flush()
            self.producer.close()
        
        print("✅ Plataforma parada com sucesso")
    
    def run_demo(self, duration_seconds: int = 30):
        """Executa demonstração da plataforma"""
        print("🎓 DEMONSTRAÇÃO: Kafka Streaming Platform")
        print("=" * 60)
        
        try:
            # Iniciar plataforma
            threads = self.start()
            
            # Executar por tempo determinado
            print(f"\n⏱️ Executando demonstração por {duration_seconds} segundos...")
            
            start_time = time.time()
            while time.time() - start_time < duration_seconds:
                time.sleep(5)
                
                # Mostrar estatísticas
                stats = self.get_stats()
                analytics = self.get_analytics()
                
                print(f"📊 Stats: {stats['messages_sent']} enviadas, {stats['messages_received']} recebidas")
                if analytics:
                    print(f"📈 Analytics: IoT={analytics.get('iot_sensors', {}).get('count', 0)}, "
                          f"Activity={analytics.get('user_activity', {}).get('count', 0)}, "
                          f"Transactions={analytics.get('transactions', {}).get('count', 0)}")
            
            # Mostrar relatório final
            print(f"\n📋 RELATÓRIO FINAL")
            print("=" * 40)
            final_stats = self.get_stats()
            final_analytics = self.get_analytics()
            
            for key, value in final_stats.items():
                print(f"📊 {key}: {value}")
            
            if final_analytics:
                print(f"\n📈 ANALYTICS FINAIS:")
                for topic, data in final_analytics.items():
                    print(f"📊 {topic}: {data}")
            
        except KeyboardInterrupt:
            print("\n⚠️ Demonstração interrompida pelo usuário")
        
        finally:
            self.stop()

def demonstrate_kafka_concepts():
    """Demonstra conceitos fundamentais do Apache Kafka"""
    print("\n📚 CONCEITOS FUNDAMENTAIS DO APACHE KAFKA")
    print("=" * 60)
    
    concepts = {
        "🏢 Arquitetura": [
            "Broker: Servidor Kafka que armazena e serve mensagens",
            "Topic: Canal de dados para organizar mensagens por categoria",
            "Partition: Divisão de tópico para paralelismo e escalabilidade",
            "Producer: Aplicação que envia mensagens para tópicos",
            "Consumer: Aplicação que lê mensagens dos tópicos",
            "Consumer Group: Grupo de consumers que colaboram"
        ],
        
        "📨 Mensagens": [
            "Key: Identificador opcional para roteamento de partições",
            "Value: Conteúdo da mensagem (JSON, Avro, etc.)",
            "Timestamp: Momento da criação ou recebimento",
            "Offset: Posição única da mensagem na partição",
            "Header: Metadados opcionais da mensagem"
        ],
        
        "🔄 Streaming": [
            "Real-time: Processamento de dados em tempo real",
            "Durability: Mensagens são persistidas em disco",
            "Scalability: Distribuição horizontal automática",
            "Fault-tolerance: Replicação e recuperação automática",
            "Ordering: Garantia de ordem dentro da partição"
        ],
        
        "📊 Casos de Uso": [
            "Event Sourcing: Log de eventos como fonte da verdade",
            "CDC: Captura de mudanças em bancos de dados",
            "Microservices: Comunicação assíncrona entre serviços",
            "IoT: Coleta de dados de sensores em tempo real",
            "Analytics: Pipelines de dados para business intelligence"
        ]
    }
    
    for category, items in concepts.items():
        print(f"\n{category}")
        print("-" * 40)
        for item in items:
            print(f"  • {item}")

def main():
    """Função principal"""
    print("🎯 AULA 08: Apache Kafka - Streaming de Dados")
    print("Autor: Professor Vagner Cordeiro")
    print("=" * 60)
    
    # Demonstrar conceitos
    demonstrate_kafka_concepts()
    
    # Executar demonstração prática
    platform = KafkaStreamingPlatform()
    
    try:
        platform.run_demo(duration_seconds=20)
    except Exception as e:
        logger.error(f"Erro na demonstração: {e}")
    
    print("\n✅ Aula concluída! Conceitos de Apache Kafka demonstrados.")

if __name__ == "__main__":
    main()
