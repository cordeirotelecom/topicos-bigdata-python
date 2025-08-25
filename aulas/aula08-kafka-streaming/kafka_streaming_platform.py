#!/usr/bin/env python3
"""
Apache Kafka Streaming Implementation
Sistema completo de streaming de dados em tempo real
"""

import os
import sys
import json
import time
import threading
import logging
import random
from datetime import datetime, timedelta
from typing import Dict, List, Any
import asyncio
from dataclasses import dataclass, asdict

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    from kafka import KafkaProducer, KafkaConsumer, KafkaAdminClient
    from kafka.admin import NewTopic, ConfigResource, ConfigResourceType
    from kafka.errors import TopicAlreadyExistsError
    import redis
except ImportError as e:
    logger.error(f"Dependências não instaladas: {e}")
    logger.error("Execute: pip install kafka-python redis")
    sys.exit(1)

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
    timestamp: datetime
    page: str
    referrer: str
    user_agent: str
    ip_address: str
    duration_ms: int

@dataclass
class TransactionEvent:
    """Estrutura de dados para evento de transação"""
    transaction_id: str
    user_id: str
    amount: float
    currency: str
    merchant: str
    timestamp: datetime
    location: Dict[str, str]
    payment_method: str
    risk_score: float

class KafkaManager:
    """Gerenciador para operações Kafka"""
    
    def __init__(self, bootstrap_servers=['localhost:9092']):
        self.bootstrap_servers = bootstrap_servers
        self.admin_client = KafkaAdminClient(
            bootstrap_servers=bootstrap_servers,
            client_id='kafka_manager'
        )
    
    def create_topics(self, topics_config: Dict[str, Dict]):
        """Criar topics com configurações específicas"""
        topics = []
        
        for topic_name, config in topics_config.items():
            topic = NewTopic(
                name=topic_name,
                num_partitions=config.get('partitions', 3),
                replication_factor=config.get('replication_factor', 1),
                topic_configs=config.get('configs', {})
            )
            topics.append(topic)
        
        try:
            result = self.admin_client.create_topics(topics)
            for topic_name, future in result.topic_futures.items():
                try:
                    future.result()
                    logger.info(f"Topic '{topic_name}' criado com sucesso")
                except TopicAlreadyExistsError:
                    logger.info(f"Topic '{topic_name}' já existe")
                except Exception as e:
                    logger.error(f"Erro ao criar topic '{topic_name}': {e}")
        except Exception as e:
            logger.error(f"Erro geral na criação de topics: {e}")
    
    def list_topics(self):
        """Listar todos os topics"""
        metadata = self.admin_client.list_topics()
        return metadata.topics
    
    def delete_topics(self, topic_names: List[str]):
        """Deletar topics"""
        try:
            result = self.admin_client.delete_topics(topic_names)
            for topic_name, future in result.topic_futures.items():
                try:
                    future.result()
                    logger.info(f"Topic '{topic_name}' deletado")
                except Exception as e:
                    logger.error(f"Erro ao deletar topic '{topic_name}': {e}")
        except Exception as e:
            logger.error(f"Erro geral na deleção de topics: {e}")

class IoTSensorProducer:
    """Produtor para simular dados de sensores IoT"""
    
    def __init__(self, bootstrap_servers=['localhost:9092']):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8'),
            key_serializer=lambda k: k.encode('utf-8') if k else None,
            acks='all',  # Aguardar confirmação de todos os replicas
            retries=3,
            batch_size=16384,
            linger_ms=10,
            compression_type='gzip'
        )
        self.running = False
        self.sensors = self._generate_sensor_config()
    
    def _generate_sensor_config(self):
        """Gerar configuração de sensores"""
        locations = [
            {"lat": -23.5505, "lon": -46.6333, "city": "São Paulo"},
            {"lat": -22.9068, "lon": -43.1729, "city": "Rio de Janeiro"},
            {"lat": -19.9167, "lon": -43.9345, "city": "Belo Horizonte"},
            {"lat": -15.7801, "lon": -47.9292, "city": "Brasília"},
            {"lat": -12.9714, "lon": -38.5014, "city": "Salvador"}
        ]
        
        sensors = []
        for i in range(50):  # 50 sensores simulados
            sensor = {
                'sensor_id': f'SENSOR_{i:03d}',
                'location': random.choice(locations),
                'base_temp': random.uniform(15, 35),
                'base_humidity': random.uniform(30, 80),
                'base_pressure': random.uniform(980, 1020)
            }
            sensors.append(sensor)
        
        return sensors
    
    def generate_sensor_reading(self, sensor_config):
        """Gerar leitura de sensor"""
        # Adicionar variação realística
        temp_variation = random.uniform(-5, 5)
        humidity_variation = random.uniform(-10, 10)
        pressure_variation = random.uniform(-5, 5)
        
        reading = IoTSensorReading(
            sensor_id=sensor_config['sensor_id'],
            timestamp=datetime.now(),
            temperature=max(0, sensor_config['base_temp'] + temp_variation),
            humidity=max(0, min(100, sensor_config['base_humidity'] + humidity_variation)),
            pressure=max(0, sensor_config['base_pressure'] + pressure_variation),
            location=sensor_config['location'],
            device_status=random.choice(['online', 'online', 'online', 'warning', 'offline']),
            battery_level=max(0, min(100, random.uniform(10, 100)))
        )
        
        return reading
    
    def start_streaming(self, topic='iot-sensor-data', interval=1.0):
        """Iniciar streaming de dados"""
        self.running = True
        logger.info(f"Iniciando streaming para topic '{topic}'")
        
        while self.running:
            try:
                # Gerar leituras para todos os sensores
                for sensor_config in self.sensors:
                    reading = self.generate_sensor_reading(sensor_config)
                    
                    # Enviar para Kafka
                    future = self.producer.send(
                        topic,
                        key=reading.sensor_id,
                        value=asdict(reading)
                    )
                    
                    # Callback para tratar sucesso/erro
                    future.add_callback(self._on_send_success)
                    future.add_errback(self._on_send_error)
                
                self.producer.flush()
                time.sleep(interval)
                
            except KeyboardInterrupt:
                logger.info("Parando streaming...")
                break
            except Exception as e:
                logger.error(f"Erro no streaming: {e}")
                time.sleep(5)
        
        self.running = False
        self.producer.close()
    
    def _on_send_success(self, record_metadata):
        """Callback para envio bem-sucedido"""
        logger.debug(f"Mensagem enviada para {record_metadata.topic}:{record_metadata.partition}:{record_metadata.offset}")
    
    def _on_send_error(self, exception):
        """Callback para erro no envio"""
        logger.error(f"Erro ao enviar mensagem: {exception}")

class UserActivityProducer:
    """Produtor para simular atividade de usuários"""
    
    def __init__(self, bootstrap_servers=['localhost:9092']):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8'),
            key_serializer=lambda k: k.encode('utf-8') if k else None
        )
        self.running = False
    
    def generate_user_event(self):
        """Gerar evento de usuário"""
        event_types = ['page_view', 'click', 'scroll', 'form_submit', 'purchase', 'logout']
        pages = ['/home', '/products', '/cart', '/checkout', '/profile', '/support']
        referrers = ['google.com', 'facebook.com', 'direct', 'email', 'instagram.com']
        
        event = UserActivityEvent(
            user_id=f"user_{random.randint(1, 10000)}",
            session_id=f"session_{random.randint(1, 50000)}",
            event_type=random.choice(event_types),
            timestamp=datetime.now(),
            page=random.choice(pages),
            referrer=random.choice(referrers),
            user_agent="Mozilla/5.0 (compatible)",
            ip_address=f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}",
            duration_ms=random.randint(100, 30000)
        )
        
        return event
    
    def start_streaming(self, topic='user-activity', interval=0.1):
        """Iniciar streaming de eventos de usuário"""
        self.running = True
        logger.info(f"Iniciando streaming de atividade para topic '{topic}'")
        
        while self.running:
            try:
                event = self.generate_user_event()
                
                self.producer.send(
                    topic,
                    key=event.user_id,
                    value=asdict(event)
                )
                
                time.sleep(interval)
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                logger.error(f"Erro no streaming de atividade: {e}")
                time.sleep(1)
        
        self.running = False
        self.producer.close()

class RealTimeAnalyticsConsumer:
    """Consumer para análise em tempo real"""
    
    def __init__(self, bootstrap_servers=['localhost:9092']):
        self.bootstrap_servers = bootstrap_servers
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        self.running = False
    
    def consume_iot_data(self, topic='iot-sensor-data'):
        """Consumir e processar dados IoT"""
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset='latest',
            enable_auto_commit=True,
            group_id='iot-analytics-group',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        
        logger.info(f"Iniciando consumo de dados IoT do topic '{topic}'")
        
        for message in consumer:
            try:
                sensor_data = message.value
                self._process_iot_reading(sensor_data)
                
            except Exception as e:
                logger.error(f"Erro ao processar dados IoT: {e}")
        
        consumer.close()
    
    def _process_iot_reading(self, data):
        """Processar leitura de sensor"""
        sensor_id = data['sensor_id']
        timestamp = data['timestamp']
        temperature = data['temperature']
        humidity = data['humidity']
        battery_level = data['battery_level']
        device_status = data['device_status']
        
        # Armazenar métricas no Redis
        current_hour = datetime.now().strftime('%Y-%m-%d-%H')
        
        # Contadores por hora
        self.redis_client.incr(f"iot:readings:{current_hour}")
        self.redis_client.incr(f"iot:sensor:{sensor_id}:readings:{current_hour}")
        
        # Valores atuais
        self.redis_client.hset(f"iot:sensor:{sensor_id}:current", mapping={
            'temperature': temperature,
            'humidity': humidity,
            'battery_level': battery_level,
            'status': device_status,
            'last_update': timestamp
        })
        
        # Detectar anomalias
        self._detect_anomalies(sensor_id, data)
        
        # Alertas críticos
        if device_status == 'offline':
            self._send_alert('DEVICE_OFFLINE', f"Sensor {sensor_id} está offline")
        
        if battery_level < 15:
            self._send_alert('LOW_BATTERY', f"Sensor {sensor_id} com bateria baixa: {battery_level}%")
        
        if temperature > 50 or temperature < -10:
            self._send_alert('TEMPERATURE_ALERT', f"Sensor {sensor_id} temperatura crítica: {temperature}°C")
    
    def _detect_anomalies(self, sensor_id, current_data):
        """Detectar anomalias usando janela deslizante"""
        # Buscar histórico recente
        history_key = f"iot:sensor:{sensor_id}:history"
        
        # Adicionar leitura atual ao histórico
        self.redis_client.lpush(
            history_key,
            json.dumps({
                'timestamp': current_data['timestamp'],
                'temperature': current_data['temperature'],
                'humidity': current_data['humidity']
            })
        )
        
        # Manter apenas últimas 100 leituras
        self.redis_client.ltrim(history_key, 0, 99)
        
        # Analisar se há 5+ leituras para detectar anomalias
        history = self.redis_client.lrange(history_key, 0, 9)  # Últimas 10
        
        if len(history) >= 5:
            temperatures = []
            for reading_str in history:
                reading = json.loads(reading_str)
                temperatures.append(reading['temperature'])
            
            # Calcular média e desvio padrão
            avg_temp = sum(temperatures) / len(temperatures)
            variance = sum((t - avg_temp) ** 2 for t in temperatures) / len(temperatures)
            std_dev = variance ** 0.5
            
            current_temp = current_data['temperature']
            
            # Alertar se atual está fora de 2 desvios padrão
            if abs(current_temp - avg_temp) > 2 * std_dev and std_dev > 1:
                self._send_alert(
                    'TEMPERATURE_ANOMALY',
                    f"Sensor {sensor_id} anomalia detectada: {current_temp}°C (média: {avg_temp:.1f}°C)"
                )
    
    def _send_alert(self, alert_type, message):
        """Enviar alerta para sistema de notificações"""
        alert = {
            'type': alert_type,
            'message': message,
            'timestamp': datetime.now().isoformat(),
            'severity': self._get_alert_severity(alert_type)
        }
        
        # Armazenar alerta no Redis
        self.redis_client.lpush('alerts', json.dumps(alert))
        self.redis_client.ltrim('alerts', 0, 999)  # Manter últimos 1000 alertas
        
        logger.warning(f"🚨 ALERTA {alert_type}: {message}")
    
    def _get_alert_severity(self, alert_type):
        """Determinar severidade do alerta"""
        severity_map = {
            'DEVICE_OFFLINE': 'HIGH',
            'LOW_BATTERY': 'MEDIUM',
            'TEMPERATURE_ALERT': 'HIGH',
            'TEMPERATURE_ANOMALY': 'MEDIUM'
        }
        return severity_map.get(alert_type, 'LOW')
    
    def consume_user_activity(self, topic='user-activity'):
        """Consumir e processar atividade de usuários"""
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset='latest',
            enable_auto_commit=True,
            group_id='user-analytics-group',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        
        logger.info(f"Iniciando consumo de atividade de usuários do topic '{topic}'")
        
        for message in consumer:
            try:
                event_data = message.value
                self._process_user_event(event_data)
                
            except Exception as e:
                logger.error(f"Erro ao processar evento de usuário: {e}")
        
        consumer.close()
    
    def _process_user_event(self, data):
        """Processar evento de usuário"""
        user_id = data['user_id']
        session_id = data['session_id']
        event_type = data['event_type']
        page = data['page']
        
        current_minute = datetime.now().strftime('%Y-%m-%d-%H-%M')
        
        # Contadores em tempo real
        self.redis_client.incr(f"user_activity:events:{current_minute}")
        self.redis_client.incr(f"user_activity:event_type:{event_type}:{current_minute}")
        self.redis_client.incr(f"user_activity:page:{page}:{current_minute}")
        
        # Atividade por usuário
        self.redis_client.incr(f"user_activity:user:{user_id}:events")
        
        # Atividade por sessão
        session_key = f"user_activity:session:{session_id}"
        self.redis_client.incr(f"{session_key}:events")
        self.redis_client.hset(f"{session_key}:info", mapping={
            'user_id': user_id,
            'last_event': event_type,
            'last_page': page,
            'last_activity': data['timestamp']
        })
        
        # Detectar sessões muito ativas (possível bot)
        session_events = int(self.redis_client.get(f"{session_key}:events") or 0)
        if session_events > 100:
            self._send_alert(
                'SUSPICIOUS_ACTIVITY',
                f"Sessão {session_id} com atividade suspeita: {session_events} eventos"
            )

class StreamAnalyticsDashboard:
    """Dashboard para visualizar analytics em tempo real"""
    
    def __init__(self):
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    
    def get_iot_metrics(self):
        """Obter métricas IoT em tempo real"""
        current_hour = datetime.now().strftime('%Y-%m-%d-%H')
        
        metrics = {
            'total_readings': int(self.redis_client.get(f"iot:readings:{current_hour}") or 0),
            'active_sensors': 0,
            'offline_sensors': 0,
            'low_battery_sensors': 0,
            'recent_alerts': []
        }
        
        # Verificar status dos sensores
        sensor_keys = self.redis_client.keys("iot:sensor:*:current")
        for key in sensor_keys:
            sensor_data = self.redis_client.hgetall(key)
            if sensor_data:
                if sensor_data.get('status') == 'online':
                    metrics['active_sensors'] += 1
                elif sensor_data.get('status') == 'offline':
                    metrics['offline_sensors'] += 1
                
                battery_level = float(sensor_data.get('battery_level', 100))
                if battery_level < 20:
                    metrics['low_battery_sensors'] += 1
        
        # Buscar alertas recentes
        recent_alerts = self.redis_client.lrange('alerts', 0, 9)
        for alert_str in recent_alerts:
            alert = json.loads(alert_str)
            metrics['recent_alerts'].append(alert)
        
        return metrics
    
    def get_user_activity_metrics(self):
        """Obter métricas de atividade de usuários"""
        current_minute = datetime.now().strftime('%Y-%m-%d-%H-%M')
        
        metrics = {
            'events_per_minute': int(self.redis_client.get(f"user_activity:events:{current_minute}") or 0),
            'event_types': {},
            'popular_pages': {},
            'active_sessions': 0
        }
        
        # Eventos por tipo
        event_types = ['page_view', 'click', 'scroll', 'form_submit', 'purchase', 'logout']
        for event_type in event_types:
            count = int(self.redis_client.get(f"user_activity:event_type:{event_type}:{current_minute}") or 0)
            metrics['event_types'][event_type] = count
        
        # Páginas populares
        pages = ['/home', '/products', '/cart', '/checkout', '/profile', '/support']
        for page in pages:
            count = int(self.redis_client.get(f"user_activity:page:{page}:{current_minute}") or 0)
            if count > 0:
                metrics['popular_pages'][page] = count
        
        # Sessões ativas (aproximação)
        session_keys = self.redis_client.keys("user_activity:session:*:events")
        metrics['active_sessions'] = len(session_keys)
        
        return metrics
    
    def display_dashboard(self):
        """Exibir dashboard no terminal"""
        while True:
            try:
                os.system('clear' if os.name == 'posix' else 'cls')
                
                print("🚀 REAL-TIME ANALYTICS DASHBOARD")
                print("=" * 60)
                
                # Métricas IoT
                iot_metrics = self.get_iot_metrics()
                print(f"\n📡 IoT SENSORS")
                print(f"Total Readings (this hour): {iot_metrics['total_readings']:,}")
                print(f"Active Sensors: {iot_metrics['active_sensors']}")
                print(f"Offline Sensors: {iot_metrics['offline_sensors']}")
                print(f"Low Battery Sensors: {iot_metrics['low_battery_sensors']}")
                
                # Alertas recentes
                if iot_metrics['recent_alerts']:
                    print(f"\n🚨 RECENT ALERTS:")
                    for alert in iot_metrics['recent_alerts'][:3]:
                        timestamp = alert['timestamp'][:19]
                        print(f"  [{timestamp}] {alert['type']}: {alert['message']}")
                
                # Métricas de usuários
                user_metrics = self.get_user_activity_metrics()
                print(f"\n👥 USER ACTIVITY")
                print(f"Events per minute: {user_metrics['events_per_minute']:,}")
                print(f"Active Sessions: {user_metrics['active_sessions']:,}")
                
                # Eventos por tipo
                print(f"\n📊 EVENTS BY TYPE:")
                for event_type, count in user_metrics['event_types'].items():
                    if count > 0:
                        print(f"  {event_type}: {count}")
                
                # Páginas populares
                if user_metrics['popular_pages']:
                    print(f"\n📄 POPULAR PAGES:")
                    for page, count in sorted(user_metrics['popular_pages'].items(), key=lambda x: x[1], reverse=True):
                        print(f"  {page}: {count}")
                
                print(f"\n🕒 Last updated: {datetime.now().strftime('%H:%M:%S')}")
                print("Press Ctrl+C to exit")
                
                time.sleep(5)
                
            except KeyboardInterrupt:
                print("\n👋 Dashboard finalizado!")
                break
            except Exception as e:
                logger.error(f"Erro no dashboard: {e}")
                time.sleep(5)

def setup_kafka_topics():
    """Configurar topics Kafka necessários"""
    kafka_manager = KafkaManager()
    
    topics_config = {
        'iot-sensor-data': {
            'partitions': 6,
            'replication_factor': 1,
            'configs': {
                'retention.ms': '604800000',  # 7 dias
                'compression.type': 'gzip',
                'cleanup.policy': 'delete'
            }
        },
        'user-activity': {
            'partitions': 4,
            'replication_factor': 1,
            'configs': {
                'retention.ms': '259200000',  # 3 dias
                'compression.type': 'snappy'
            }
        },
        'alerts': {
            'partitions': 2,
            'replication_factor': 1,
            'configs': {
                'retention.ms': '2592000000',  # 30 dias
                'cleanup.policy': 'delete'
            }
        }
    }
    
    kafka_manager.create_topics(topics_config)
    
    print("Topics configurados:")
    for topic in kafka_manager.list_topics():
        print(f"  - {topic}")

def main():
    """Função principal para demonstração completa"""
    
    print("🚀 Kafka Streaming Real-Time Analytics")
    print("=" * 50)
    
    # Setup inicial
    setup_kafka_topics()
    
    print("\nEscolha uma opção:")
    print("1. Iniciar Produtor IoT")
    print("2. Iniciar Produtor de Atividade de Usuários")
    print("3. Iniciar Consumer Analytics")
    print("4. Exibir Dashboard")
    print("5. Executar Demo Completo")
    
    choice = input("\nOpção (1-5): ").strip()
    
    if choice == '1':
        producer = IoTSensorProducer()
        producer.start_streaming()
    
    elif choice == '2':
        producer = UserActivityProducer()
        producer.start_streaming()
    
    elif choice == '3':
        consumer = RealTimeAnalyticsConsumer()
        
        # Executar consumers em threads separadas
        iot_thread = threading.Thread(target=consumer.consume_iot_data)
        user_thread = threading.Thread(target=consumer.consume_user_activity)
        
        iot_thread.daemon = True
        user_thread.daemon = True
        
        iot_thread.start()
        user_thread.start()
        
        try:
            iot_thread.join()
            user_thread.join()
        except KeyboardInterrupt:
            print("\nParando consumers...")
    
    elif choice == '4':
        dashboard = StreamAnalyticsDashboard()
        dashboard.display_dashboard()
    
    elif choice == '5':
        print("\n🚀 Iniciando demo completo...")
        
        # Iniciar produtores em background
        iot_producer = IoTSensorProducer()
        user_producer = UserActivityProducer()
        consumer = RealTimeAnalyticsConsumer()
        
        iot_thread = threading.Thread(target=iot_producer.start_streaming)
        user_thread = threading.Thread(target=user_producer.start_streaming)
        iot_consumer_thread = threading.Thread(target=consumer.consume_iot_data)
        user_consumer_thread = threading.Thread(target=consumer.consume_user_activity)
        
        # Configurar threads como daemon
        for thread in [iot_thread, user_thread, iot_consumer_thread, user_consumer_thread]:
            thread.daemon = True
            thread.start()
        
        # Aguardar um pouco para gerar dados
        print("Aguardando geração de dados... (10 segundos)")
        time.sleep(10)
        
        # Mostrar dashboard
        dashboard = StreamAnalyticsDashboard()
        dashboard.display_dashboard()
    
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
