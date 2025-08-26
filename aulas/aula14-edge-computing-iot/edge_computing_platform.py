"""
Aula 14: Edge Computing e IoT - Processamento Distribuído na Borda
Professor: Vagner Cordeiro
Disciplina: Tópicos de Big Data em Python

Implementação completa de soluções de Edge Computing e IoT para Big Data,
incluindo processamento em tempo real na borda, analytics distribuídos,
machine learning embarcado e orquestração de dispositivos IoT.
"""

import asyncio
import json
import time
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import threading
import queue
import sqlite3
import requests
from typing import Dict, List, Any, Optional, Callable
import logging
import warnings
from collections import deque, defaultdict
import random
import hashlib
import ssl
import socket
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing as mp
warnings.filterwarnings('ignore')

# Simulação de bibliotecas específicas de IoT
try:
    import paho.mqtt.client as mqtt
    MQTT_AVAILABLE = True
except ImportError:
    MQTT_AVAILABLE = False
    print("⚠️ Paho MQTT não disponível - simulando funcionalidades")

try:
    import tflite_runtime.interpreter as tflite
    TFLITE_AVAILABLE = True
except ImportError:
    TFLITE_AVAILABLE = False
    print("⚠️ TensorFlow Lite não disponível - simulando edge ML")

class EdgeComputingPlatform:
    """
    Plataforma completa de Edge Computing e IoT
    
    Funcionalidades:
    - Gerenciamento de dispositivos IoT
    - Processamento em tempo real na borda
    - Machine Learning embarcado
    - Análise distribuída de dados
    - Orquestração de edge nodes
    - Sincronização cloud-edge
    - Monitoramento e diagnóstico
    - Protocolos de comunicação IoT
    """
    
    def __init__(self, platform_id: str = "edge_platform_001"):
        """Inicializa a plataforma de Edge Computing"""
        
        self.platform_id = platform_id
        self.edge_nodes = {}
        self.iot_devices = {}
        self.data_streams = {}
        self.ml_models = {}
        self.communication_protocols = {}
        
        # Configurações de rede
        self.mqtt_broker = "localhost"
        self.mqtt_port = 1883
        self.websocket_port = 8765
        
        # Armazenamento local
        self.local_db = self._initialize_local_storage()
        self.data_buffer = deque(maxlen=10000)
        
        # Monitoramento
        self.metrics_collector = MetricsCollector()
        self.logger = self._setup_logging()
        
        # Threads de processamento
        self.processing_threads = []
        self.is_running = True
        
        print("🚀 Edge Computing Platform inicializada!")
        print(f"🆔 Platform ID: {platform_id}")
        print(f"📡 MQTT Broker: {self.mqtt_broker}:{self.mqtt_port}")
        
    def _setup_logging(self):
        """Configura sistema de logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger(f"EdgePlatform_{self.platform_id}")
    
    def _initialize_local_storage(self):
        """Inicializa banco de dados local SQLite"""
        conn = sqlite3.connect(':memory:', check_same_thread=False)
        
        # Tabela para dados de sensores
        conn.execute('''
            CREATE TABLE sensor_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device_id TEXT NOT NULL,
                sensor_type TEXT NOT NULL,
                value REAL NOT NULL,
                timestamp REAL NOT NULL,
                location TEXT,
                processed INTEGER DEFAULT 0
            )
        ''')
        
        # Tabela para eventos processados
        conn.execute('''
            CREATE TABLE processed_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT NOT NULL,
                device_id TEXT NOT NULL,
                result TEXT,
                confidence REAL,
                timestamp REAL NOT NULL
            )
        ''')
        
        conn.commit()
        return conn
    
    def register_edge_node(self, node_id: str, node_config: Dict):
        """
        Registra um edge node na plataforma
        """
        print(f"📱 Registrando edge node: {node_id}")
        
        edge_node = EdgeNode(
            node_id=node_id,
            config=node_config,
            platform=self
        )
        
        self.edge_nodes[node_id] = edge_node
        
        # Inicia processamento do node
        edge_node.start()
        
        print(f"✅ Edge node {node_id} registrado e ativo")
        print(f"💾 Capacidade de processamento: {node_config.get('cpu_cores', 'N/A')} cores")
        print(f"🧠 Memória disponível: {node_config.get('memory_mb', 'N/A')} MB")
        
        return edge_node
    
    def register_iot_device(self, device_id: str, device_config: Dict):
        """
        Registra dispositivo IoT na plataforma
        """
        print(f"🔌 Registrando dispositivo IoT: {device_id}")
        
        iot_device = IoTDevice(
            device_id=device_id,
            config=device_config,
            platform=self
        )
        
        self.iot_devices[device_id] = iot_device
        
        # Conecta dispositivo
        iot_device.connect()
        
        # Inicia coleta de dados
        iot_device.start_data_collection()
        
        print(f"✅ Dispositivo IoT {device_id} conectado")
        print(f"📊 Tipo: {device_config.get('device_type', 'Unknown')}")
        print(f"📍 Localização: {device_config.get('location', 'Unknown')}")
        
        return iot_device
    
    def deploy_ml_model_to_edge(self, model_id: str, model_config: Dict, 
                               target_nodes: List[str] = None):
        """
        Faz deploy de modelo ML para edge nodes
        """
        print(f"🤖 Fazendo deploy do modelo {model_id} para edge nodes...")
        
        # Cria modelo edge-optimized
        edge_model = EdgeMLModel(
            model_id=model_id,
            config=model_config
        )
        
        self.ml_models[model_id] = edge_model
        
        # Deploy para nodes específicos ou todos
        target_nodes = target_nodes or list(self.edge_nodes.keys())
        
        deployment_results = {}
        
        for node_id in target_nodes:
            if node_id in self.edge_nodes:
                node = self.edge_nodes[node_id]
                
                try:
                    # Deploy modelo para o node
                    deployment_result = node.deploy_model(edge_model)
                    deployment_results[node_id] = deployment_result
                    
                    print(f"  ✅ Modelo deployado em {node_id}")
                    
                except Exception as e:
                    print(f"  ❌ Erro no deploy para {node_id}: {e}")
                    deployment_results[node_id] = {'status': 'failed', 'error': str(e)}
            else:
                print(f"  ⚠️ Node {node_id} não encontrado")
        
        print(f"📊 Deploy concluído para {len(deployment_results)} nodes")
        
        return deployment_results
    
    def create_data_stream_pipeline(self, pipeline_id: str, stream_config: Dict):
        """
        Cria pipeline de processamento de stream de dados
        """
        print(f"🌊 Criando pipeline de stream: {pipeline_id}")
        
        # Configuração do pipeline
        pipeline = DataStreamPipeline(
            pipeline_id=pipeline_id,
            config=stream_config,
            platform=self
        )
        
        self.data_streams[pipeline_id] = pipeline
        
        # Inicia pipeline
        pipeline.start()
        
        print(f"✅ Pipeline {pipeline_id} iniciado")
        print(f"📥 Fonte: {stream_config.get('source_type', 'Unknown')}")
        print(f"🔄 Processamento: {stream_config.get('processing_type', 'Unknown')}")
        print(f"📤 Destino: {stream_config.get('sink_type', 'Unknown')}")
        
        return pipeline
    
    def setup_communication_protocol(self, protocol_name: str, protocol_config: Dict):
        """
        Configura protocolo de comunicação (MQTT, CoAP, WebSocket, etc.)
        """
        print(f"📡 Configurando protocolo: {protocol_name}")
        
        if protocol_name.lower() == "mqtt":
            protocol = MQTTCommunication(protocol_config, self)
        elif protocol_name.lower() == "websocket":
            protocol = WebSocketCommunication(protocol_config, self)
        elif protocol_name.lower() == "coap":
            protocol = CoAPCommunication(protocol_config, self)
        elif protocol_name.lower() == "lorawan":
            protocol = LoRaWANCommunication(protocol_config, self)
        else:
            protocol = GenericCommunication(protocol_config, self)
        
        self.communication_protocols[protocol_name] = protocol
        
        # Inicia protocolo
        protocol.start()
        
        print(f"✅ Protocolo {protocol_name} configurado")
        
        return protocol
    
    def process_real_time_analytics(self, data_window_size: int = 100):
        """
        Executa analytics em tempo real nos dados coletados
        """
        print(f"📊 Iniciando analytics em tempo real (janela: {data_window_size})")
        
        analytics_results = {
            'timestamp': datetime.now(),
            'window_size': data_window_size,
            'device_stats': {},
            'anomalies': [],
            'patterns': [],
            'alerts': []
        }
        
        # Coleta dados recentes do buffer
        recent_data = list(self.data_buffer)[-data_window_size:]
        
        if not recent_data:
            print("⚠️ Nenhum dado disponível para análise")
            return analytics_results
        
        # Converte para DataFrame para análise
        df = pd.DataFrame(recent_data)
        
        # Estatísticas por dispositivo
        device_groups = df.groupby('device_id')
        
        for device_id, device_data in device_groups:
            stats = {
                'device_id': device_id,
                'record_count': len(device_data),
                'avg_value': device_data['value'].mean(),
                'std_value': device_data['value'].std(),
                'min_value': device_data['value'].min(),
                'max_value': device_data['value'].max(),
                'last_seen': device_data['timestamp'].max()
            }
            
            analytics_results['device_stats'][device_id] = stats
            
            # Detecção de anomalias (valores > 3 desvios padrão)
            mean_val = stats['avg_value']
            std_val = stats['std_value']
            
            if std_val > 0:  # Evita divisão por zero
                anomalies = device_data[
                    abs(device_data['value'] - mean_val) > 3 * std_val
                ]
                
                for _, anomaly in anomalies.iterrows():
                    analytics_results['anomalies'].append({
                        'device_id': device_id,
                        'timestamp': anomaly['timestamp'],
                        'value': anomaly['value'],
                        'severity': 'high' if abs(anomaly['value'] - mean_val) > 5 * std_val else 'medium'
                    })
        
        # Detecção de padrões globais
        if len(df) > 10:
            # Tendência temporal
            df_sorted = df.sort_values('timestamp')
            recent_trend = np.polyfit(range(len(df_sorted)), df_sorted['value'], 1)[0]
            
            if abs(recent_trend) > 0.1:
                analytics_results['patterns'].append({
                    'type': 'temporal_trend',
                    'direction': 'increasing' if recent_trend > 0 else 'decreasing',
                    'magnitude': abs(recent_trend)
                })
        
        # Geração de alertas
        for device_id, stats in analytics_results['device_stats'].items():
            # Alerta de dispositivo offline
            last_seen = datetime.fromtimestamp(stats['last_seen'])
            if datetime.now() - last_seen > timedelta(minutes=5):
                analytics_results['alerts'].append({
                    'type': 'device_offline',
                    'device_id': device_id,
                    'last_seen': last_seen,
                    'priority': 'high'
                })
            
            # Alerta de valores extremos
            if stats['max_value'] > 1000 or stats['min_value'] < -1000:
                analytics_results['alerts'].append({
                    'type': 'extreme_values',
                    'device_id': device_id,
                    'max_value': stats['max_value'],
                    'min_value': stats['min_value'],
                    'priority': 'medium'
                })
        
        print(f"📈 Analytics concluído:")
        print(f"  Dispositivos analisados: {len(analytics_results['device_stats'])}")
        print(f"  Anomalias detectadas: {len(analytics_results['anomalies'])}")
        print(f"  Padrões identificados: {len(analytics_results['patterns'])}")
        print(f"  Alertas gerados: {len(analytics_results['alerts'])}")
        
        return analytics_results
    
    def orchestrate_edge_workloads(self, workload_config: Dict):
        """
        Orquestra distribuição de workloads entre edge nodes
        """
        print("🎭 Iniciando orquestração de workloads...")
        
        workloads = workload_config.get('workloads', [])
        orchestration_strategy = workload_config.get('strategy', 'round_robin')
        
        orchestration_results = {
            'strategy': orchestration_strategy,
            'workload_assignments': {},
            'load_distribution': {},
            'performance_metrics': {}
        }
        
        # Avalia capacidade dos nodes
        node_capacities = {}
        for node_id, node in self.edge_nodes.items():
            capacity = node.get_capacity_metrics()
            node_capacities[node_id] = capacity
            
            orchestration_results['load_distribution'][node_id] = {
                'cpu_usage': capacity['cpu_usage'],
                'memory_usage': capacity['memory_usage'],
                'active_workloads': capacity['active_workloads']
            }
        
        # Distribui workloads baseado na estratégia
        for i, workload in enumerate(workloads):
            if orchestration_strategy == 'round_robin':
                target_node = list(self.edge_nodes.keys())[i % len(self.edge_nodes)]
            
            elif orchestration_strategy == 'least_loaded':
                target_node = min(node_capacities.keys(), 
                                key=lambda n: node_capacities[n]['cpu_usage'])
            
            elif orchestration_strategy == 'resource_aware':
                # Considera requisitos do workload
                required_cpu = workload.get('cpu_requirement', 0.1)
                required_memory = workload.get('memory_requirement', 100)
                
                suitable_nodes = [
                    node_id for node_id, capacity in node_capacities.items()
                    if (capacity['cpu_usage'] + required_cpu < 0.9 and
                        capacity['memory_usage'] + required_memory < 0.8)
                ]
                
                if suitable_nodes:
                    target_node = suitable_nodes[0]
                else:
                    target_node = min(node_capacities.keys(), 
                                    key=lambda n: node_capacities[n]['cpu_usage'])
            
            else:
                target_node = random.choice(list(self.edge_nodes.keys()))
            
            # Atribui workload ao node
            if target_node in self.edge_nodes:
                node = self.edge_nodes[target_node]
                assignment_result = node.assign_workload(workload)
                
                orchestration_results['workload_assignments'][workload['id']] = {
                    'target_node': target_node,
                    'assignment_result': assignment_result,
                    'timestamp': datetime.now()
                }
                
                # Atualiza capacidade do node
                node_capacities[target_node]['active_workloads'] += 1
                node_capacities[target_node]['cpu_usage'] += workload.get('cpu_requirement', 0.1)
                node_capacities[target_node]['memory_usage'] += workload.get('memory_requirement', 100)
        
        print(f"📊 Orquestração concluída:")
        print(f"  Workloads distribuídos: {len(orchestration_results['workload_assignments'])}")
        print(f"  Estratégia utilizada: {orchestration_strategy}")
        print(f"  Nodes utilizados: {len(set(a['target_node'] for a in orchestration_results['workload_assignments'].values()))}")
        
        return orchestration_results
    
    def sync_with_cloud(self, cloud_config: Dict):
        """
        Sincroniza dados e modelos com a nuvem
        """
        print("☁️ Iniciando sincronização com a nuvem...")
        
        sync_results = {
            'timestamp': datetime.now(),
            'data_uploaded': 0,
            'models_downloaded': 0,
            'sync_status': 'success',
            'errors': []
        }
        
        try:
            # Upload de dados locais para a nuvem
            if cloud_config.get('upload_data', True):
                data_to_upload = self._get_unsynced_data()
                
                for data_batch in self._chunk_data(data_to_upload, 1000):
                    upload_result = self._upload_data_to_cloud(data_batch, cloud_config)
                    
                    if upload_result['success']:
                        sync_results['data_uploaded'] += len(data_batch)
                        self._mark_data_as_synced(data_batch)
                    else:
                        sync_results['errors'].append(upload_result['error'])
            
            # Download de modelos atualizados da nuvem
            if cloud_config.get('download_models', True):
                available_models = self._get_available_cloud_models(cloud_config)
                
                for model_info in available_models:
                    if self._should_update_model(model_info):
                        download_result = self._download_model_from_cloud(model_info, cloud_config)
                        
                        if download_result['success']:
                            sync_results['models_downloaded'] += 1
                            self._update_local_model(model_info, download_result['model_data'])
                        else:
                            sync_results['errors'].append(download_result['error'])
            
            # Sincronização de configurações
            if cloud_config.get('sync_config', True):
                config_updates = self._get_config_updates(cloud_config)
                if config_updates:
                    self._apply_config_updates(config_updates)
            
        except Exception as e:
            sync_results['sync_status'] = 'failed'
            sync_results['errors'].append(str(e))
            self.logger.error(f"Erro na sincronização: {e}")
        
        print(f"📤 Dados enviados: {sync_results['data_uploaded']:,}")
        print(f"📥 Modelos atualizados: {sync_results['models_downloaded']}")
        print(f"⚠️ Erros: {len(sync_results['errors'])}")
        
        return sync_results
    
    def run_system_diagnostics(self):
        """
        Executa diagnóstico completo do sistema
        """
        print("🔍 Executando diagnóstico do sistema...")
        
        diagnostics = {
            'timestamp': datetime.now(),
            'platform_status': 'healthy',
            'edge_nodes': {},
            'iot_devices': {},
            'data_streams': {},
            'communication': {},
            'performance': {},
            'alerts': []
        }
        
        # Diagnóstico dos edge nodes
        for node_id, node in self.edge_nodes.items():
            node_diagnostics = node.run_diagnostics()
            diagnostics['edge_nodes'][node_id] = node_diagnostics
            
            if node_diagnostics['status'] != 'healthy':
                diagnostics['alerts'].append({
                    'type': 'node_issue',
                    'node_id': node_id,
                    'issue': node_diagnostics['issues']
                })
        
        # Diagnóstico dos dispositivos IoT
        for device_id, device in self.iot_devices.items():
            device_diagnostics = device.run_diagnostics()
            diagnostics['iot_devices'][device_id] = device_diagnostics
            
            if device_diagnostics['status'] != 'healthy':
                diagnostics['alerts'].append({
                    'type': 'device_issue',
                    'device_id': device_id,
                    'issue': device_diagnostics['issues']
                })
        
        # Diagnóstico dos streams de dados
        for stream_id, stream in self.data_streams.items():
            stream_diagnostics = stream.run_diagnostics()
            diagnostics['data_streams'][stream_id] = stream_diagnostics
        
        # Diagnóstico da comunicação
        for protocol_name, protocol in self.communication_protocols.items():
            comm_diagnostics = protocol.run_diagnostics()
            diagnostics['communication'][protocol_name] = comm_diagnostics
        
        # Métricas de performance da plataforma
        diagnostics['performance'] = {
            'data_buffer_size': len(self.data_buffer),
            'active_nodes': len([n for n in self.edge_nodes.values() if n.is_active()]),
            'connected_devices': len([d for d in self.iot_devices.values() if d.is_connected()]),
            'active_streams': len([s for s in self.data_streams.values() if s.is_active()]),
            'memory_usage': self._get_memory_usage(),
            'cpu_usage': self._get_cpu_usage()
        }
        
        # Determina status geral da plataforma
        if diagnostics['alerts']:
            critical_alerts = [a for a in diagnostics['alerts'] 
                             if a.get('severity', 'medium') == 'critical']
            if critical_alerts:
                diagnostics['platform_status'] = 'critical'
            else:
                diagnostics['platform_status'] = 'warning'
        
        print(f"📊 Diagnóstico concluído:")
        print(f"  Status da plataforma: {diagnostics['platform_status']}")
        print(f"  Edge nodes ativos: {diagnostics['performance']['active_nodes']}/{len(self.edge_nodes)}")
        print(f"  Dispositivos conectados: {diagnostics['performance']['connected_devices']}/{len(self.iot_devices)}")
        print(f"  Alertas gerados: {len(diagnostics['alerts'])}")
        
        return diagnostics
    
    def run_complete_edge_demo(self):
        """
        Executa demonstração completa da plataforma Edge Computing
        """
        print("🚀 DEMONSTRAÇÃO COMPLETA - EDGE COMPUTING & IoT PLATFORM")
        print("="*70)
        
        results = {}
        
        # 1. Configuração de Edge Nodes
        print("\n1️⃣ CONFIGURAÇÃO DE EDGE NODES")
        print("-" * 50)
        
        # Edge node industrial
        industrial_node = self.register_edge_node("edge_node_001", {
            'node_type': 'industrial',
            'cpu_cores': 4,
            'memory_mb': 8192,
            'storage_gb': 256,
            'location': 'Factory Floor A',
            'capabilities': ['ml_inference', 'real_time_processing', 'data_aggregation']
        })
        
        # Edge node veicular
        vehicle_node = self.register_edge_node("edge_node_002", {
            'node_type': 'vehicle',
            'cpu_cores': 2,
            'memory_mb': 4096,
            'storage_gb': 128,
            'location': 'Mobile Vehicle 001',
            'capabilities': ['gps_tracking', 'image_processing', 'sensor_fusion']
        })
        
        results['edge_nodes'] = [industrial_node.node_id, vehicle_node.node_id]
        
        # 2. Registro de Dispositivos IoT
        print("\n2️⃣ REGISTRO DE DISPOSITIVOS IoT")
        print("-" * 50)
        
        # Sensores industriais
        temp_sensor = self.register_iot_device("temp_sensor_001", {
            'device_type': 'temperature_sensor',
            'location': 'Factory Floor A - Zone 1',
            'sampling_rate': 1.0,  # Hz
            'protocol': 'mqtt',
            'data_format': 'json'
        })
        
        pressure_sensor = self.register_iot_device("pressure_sensor_001", {
            'device_type': 'pressure_sensor',
            'location': 'Factory Floor A - Zone 2',
            'sampling_rate': 0.5,  # Hz
            'protocol': 'mqtt',
            'data_format': 'json'
        })
        
        # Câmera de segurança
        security_camera = self.register_iot_device("camera_001", {
            'device_type': 'security_camera',
            'location': 'Factory Entrance',
            'resolution': '1920x1080',
            'fps': 30,
            'protocol': 'websocket',
            'data_format': 'video_stream'
        })
        
        results['iot_devices'] = [temp_sensor.device_id, pressure_sensor.device_id, security_camera.device_id]
        
        # 3. Deploy de Modelos ML
        print("\n3️⃣ DEPLOY DE MODELOS MACHINE LEARNING")
        print("-" * 50)
        
        # Modelo de detecção de anomalias
        anomaly_model_deploy = self.deploy_ml_model_to_edge("anomaly_detector_v1", {
            'model_type': 'anomaly_detection',
            'framework': 'tensorflow_lite',
            'input_features': ['temperature', 'pressure', 'vibration'],
            'output_classes': ['normal', 'anomaly'],
            'model_size_mb': 15.2,
            'inference_time_ms': 25
        }, target_nodes=["edge_node_001"])
        
        # Modelo de reconhecimento de objetos
        object_detection_deploy = self.deploy_ml_model_to_edge("object_detector_v1", {
            'model_type': 'object_detection',
            'framework': 'tensorflow_lite',
            'input_resolution': '416x416',
            'output_classes': 80,
            'model_size_mb': 45.8,
            'inference_time_ms': 150
        }, target_nodes=["edge_node_002"])
        
        results['ml_deployments'] = [anomaly_model_deploy, object_detection_deploy]
        
        # 4. Configuração de Protocolos de Comunicação
        print("\n4️⃣ PROTOCOLOS DE COMUNICAÇÃO")
        print("-" * 50)
        
        # MQTT para sensores
        mqtt_protocol = self.setup_communication_protocol("mqtt", {
            'broker_host': self.mqtt_broker,
            'broker_port': self.mqtt_port,
            'topics': ['sensors/temperature', 'sensors/pressure', 'alerts/anomalies'],
            'qos': 1,
            'retain': False
        })
        
        # WebSocket para streams de vídeo
        websocket_protocol = self.setup_communication_protocol("websocket", {
            'host': 'localhost',
            'port': self.websocket_port,
            'endpoints': ['/video_stream', '/analytics_results'],
            'compression': True
        })
        
        results['communication_protocols'] = ['mqtt', 'websocket']
        
        # 5. Pipelines de Stream Processing
        print("\n5️⃣ PIPELINES DE STREAM PROCESSING")
        print("-" * 50)
        
        # Pipeline para dados de sensores
        sensor_pipeline = self.create_data_stream_pipeline("sensor_data_pipeline", {
            'source_type': 'mqtt',
            'source_config': {
                'topics': ['sensors/+'],
                'batch_size': 100,
                'window_size_seconds': 60
            },
            'processing_type': 'real_time_analytics',
            'processing_config': {
                'operations': ['aggregation', 'anomaly_detection', 'trend_analysis'],
                'ml_models': ['anomaly_detector_v1']
            },
            'sink_type': 'local_storage',
            'sink_config': {
                'database': 'sqlite',
                'table': 'sensor_analytics'
            }
        })
        
        # Pipeline para análise de vídeo
        video_pipeline = self.create_data_stream_pipeline("video_analytics_pipeline", {
            'source_type': 'websocket',
            'source_config': {
                'endpoint': '/video_stream',
                'frame_rate': 10  # Processa 1 frame a cada 10
            },
            'processing_type': 'computer_vision',
            'processing_config': {
                'operations': ['object_detection', 'person_counting', 'intrusion_detection'],
                'ml_models': ['object_detector_v1']
            },
            'sink_type': 'alert_system',
            'sink_config': {
                'alert_types': ['security_breach', 'unauthorized_access'],
                'notification_methods': ['email', 'sms', 'dashboard']
            }
        })
        
        results['data_pipelines'] = [sensor_pipeline.pipeline_id, video_pipeline.pipeline_id]
        
        # 6. Simulação de Coleta de Dados
        print("\n6️⃣ SIMULAÇÃO DE COLETA DE DADOS")
        print("-" * 50)
        
        # Simula coleta de dados por 30 segundos
        print("📊 Coletando dados dos sensores...")
        
        for i in range(30):
            # Dados do sensor de temperatura
            temp_data = {
                'device_id': 'temp_sensor_001',
                'sensor_type': 'temperature',
                'value': 25.0 + np.random.normal(0, 2) + (i * 0.1),  # Tendência de aquecimento
                'timestamp': time.time(),
                'location': 'Factory Floor A - Zone 1'
            }
            self.data_buffer.append(temp_data)
            
            # Dados do sensor de pressão
            pressure_data = {
                'device_id': 'pressure_sensor_001',
                'sensor_type': 'pressure',
                'value': 101.3 + np.random.normal(0, 0.5),
                'timestamp': time.time(),
                'location': 'Factory Floor A - Zone 2'
            }
            self.data_buffer.append(pressure_data)
            
            # Simula anomalia ocasional
            if np.random.random() < 0.05:  # 5% chance de anomalia
                anomaly_data = {
                    'device_id': 'temp_sensor_001',
                    'sensor_type': 'temperature',
                    'value': 25.0 + np.random.normal(0, 10),  # Valor anômalo
                    'timestamp': time.time(),
                    'location': 'Factory Floor A - Zone 1'
                }
                self.data_buffer.append(anomaly_data)
            
            time.sleep(0.1)  # Simula tempo real
        
        print(f"✅ Coletados {len(self.data_buffer)} pontos de dados")
        
        # 7. Analytics em Tempo Real
        print("\n7️⃣ ANALYTICS EM TEMPO REAL")
        print("-" * 50)
        
        analytics_results = self.process_real_time_analytics(window_size=50)
        results['analytics'] = analytics_results
        
        # 8. Orquestração de Workloads
        print("\n8️⃣ ORQUESTRAÇÃO DE WORKLOADS")
        print("-" * 50)
        
        workload_config = {
            'strategy': 'resource_aware',
            'workloads': [
                {
                    'id': 'batch_ml_training',
                    'type': 'ml_training',
                    'cpu_requirement': 0.6,
                    'memory_requirement': 2048,
                    'priority': 'medium'
                },
                {
                    'id': 'real_time_inference',
                    'type': 'ml_inference',
                    'cpu_requirement': 0.3,
                    'memory_requirement': 512,
                    'priority': 'high'
                },
                {
                    'id': 'data_aggregation',
                    'type': 'data_processing',
                    'cpu_requirement': 0.2,
                    'memory_requirement': 1024,
                    'priority': 'low'
                }
            ]
        }
        
        orchestration_results = self.orchestrate_edge_workloads(workload_config)
        results['orchestration'] = orchestration_results
        
        # 9. Sincronização com Cloud
        print("\n9️⃣ SINCRONIZAÇÃO COM CLOUD")
        print("-" * 50)
        
        cloud_config = {
            'cloud_provider': 'aws',
            'region': 'us-east-1',
            'upload_data': True,
            'download_models': True,
            'sync_config': True,
            'compression': True,
            'encryption': True
        }
        
        sync_results = self.sync_with_cloud(cloud_config)
        results['cloud_sync'] = sync_results
        
        # 10. Diagnóstico do Sistema
        print("\n🔟 DIAGNÓSTICO DO SISTEMA")
        print("-" * 50)
        
        diagnostics = self.run_system_diagnostics()
        results['diagnostics'] = diagnostics
        
        print("\n🎉 DEMONSTRAÇÃO COMPLETA FINALIZADA!")
        print("="*70)
        print("📊 Resumo dos Resultados:")
        print(f"🖥️ Edge nodes registrados: {len(results['edge_nodes'])}")
        print(f"🔌 Dispositivos IoT conectados: {len(results['iot_devices'])}")
        print(f"🤖 Modelos ML deployados: {len(results['ml_deployments'])}")
        print(f"📡 Protocolos configurados: {len(results['communication_protocols'])}")
        print(f"🌊 Pipelines de dados: {len(results['data_pipelines'])}")
        print(f"📊 Pontos de dados coletados: {len(self.data_buffer)}")
        print(f"⚠️ Anomalias detectadas: {len(results['analytics']['anomalies'])}")
        print(f"🎭 Workloads orquestrados: {len(results['orchestration']['workload_assignments'])}")
        print(f"☁️ Dados sincronizados: {results['cloud_sync']['data_uploaded']}")
        print(f"🔍 Status do sistema: {results['diagnostics']['platform_status']}")
        
        return results
    
    def _get_unsynced_data(self):
        """Obtém dados que ainda não foram sincronizados"""
        cursor = self.local_db.cursor()
        cursor.execute('''
            SELECT * FROM sensor_data 
            WHERE processed = 0 
            ORDER BY timestamp ASC
        ''')
        return cursor.fetchall()
    
    def _chunk_data(self, data, chunk_size):
        """Divide dados em chunks para upload"""
        for i in range(0, len(data), chunk_size):
            yield data[i:i + chunk_size]
    
    def _upload_data_to_cloud(self, data_batch, cloud_config):
        """Simula upload de dados para a nuvem"""
        try:
            # Simula processo de upload
            time.sleep(0.1)  # Simula latência de rede
            
            return {
                'success': True,
                'uploaded_records': len(data_batch),
                'timestamp': datetime.now()
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _get_memory_usage(self):
        """Obtém uso de memória do sistema"""
        try:
            import psutil
            return psutil.virtual_memory().percent / 100.0
        except:
            return 0.5  # Valor simulado
    
    def _get_cpu_usage(self):
        """Obtém uso de CPU do sistema"""
        try:
            import psutil
            return psutil.cpu_percent() / 100.0
        except:
            return 0.4  # Valor simulado
    
    def cleanup(self):
        """Limpa recursos e finaliza a plataforma"""
        print("\n🧹 Finalizando Edge Computing Platform...")
        
        self.is_running = False
        
        # Para todos os edge nodes
        for node in self.edge_nodes.values():
            node.stop()
        
        # Desconecta dispositivos IoT
        for device in self.iot_devices.values():
            device.disconnect()
        
        # Para pipelines de dados
        for pipeline in self.data_streams.values():
            pipeline.stop()
        
        # Para protocolos de comunicação
        for protocol in self.communication_protocols.items():
            protocol.stop()
        
        # Fecha banco de dados
        self.local_db.close()
        
        print("✅ Edge Computing Platform finalizada!")

# Classes auxiliares para simulação

class EdgeNode:
    """Representa um edge node na rede"""
    
    def __init__(self, node_id: str, config: Dict, platform):
        self.node_id = node_id
        self.config = config
        self.platform = platform
        self.active = False
        self.deployed_models = {}
        self.active_workloads = []
        self.cpu_usage = 0.1
        self.memory_usage = 0.2
    
    def start(self):
        """Inicia o edge node"""
        self.active = True
    
    def stop(self):
        """Para o edge node"""
        self.active = False
    
    def is_active(self):
        """Verifica se o node está ativo"""
        return self.active
    
    def deploy_model(self, model):
        """Deploy de modelo ML no node"""
        self.deployed_models[model.model_id] = model
        return {'status': 'success', 'deployment_time': datetime.now()}
    
    def assign_workload(self, workload):
        """Atribui workload ao node"""
        self.active_workloads.append(workload)
        self.cpu_usage += workload.get('cpu_requirement', 0.1)
        self.memory_usage += workload.get('memory_requirement', 100) / self.config.get('memory_mb', 4096)
        return {'status': 'assigned', 'workload_id': workload['id']}
    
    def get_capacity_metrics(self):
        """Obtém métricas de capacidade do node"""
        return {
            'cpu_usage': self.cpu_usage,
            'memory_usage': self.memory_usage,
            'active_workloads': len(self.active_workloads),
            'available_cpu': max(0, 1.0 - self.cpu_usage),
            'available_memory': max(0, 1.0 - self.memory_usage)
        }
    
    def run_diagnostics(self):
        """Executa diagnóstico do node"""
        issues = []
        
        if self.cpu_usage > 0.9:
            issues.append("High CPU usage")
        if self.memory_usage > 0.9:
            issues.append("High memory usage")
        if not self.active:
            issues.append("Node inactive")
        
        return {
            'status': 'healthy' if not issues else 'warning',
            'issues': issues,
            'metrics': self.get_capacity_metrics()
        }

class IoTDevice:
    """Representa um dispositivo IoT"""
    
    def __init__(self, device_id: str, config: Dict, platform):
        self.device_id = device_id
        self.config = config
        self.platform = platform
        self.connected = False
        self.collecting_data = False
    
    def connect(self):
        """Conecta o dispositivo"""
        self.connected = True
    
    def disconnect(self):
        """Desconecta o dispositivo"""
        self.connected = False
        self.collecting_data = False
    
    def is_connected(self):
        """Verifica se está conectado"""
        return self.connected
    
    def start_data_collection(self):
        """Inicia coleta de dados"""
        if self.connected:
            self.collecting_data = True
    
    def stop_data_collection(self):
        """Para coleta de dados"""
        self.collecting_data = False
    
    def run_diagnostics(self):
        """Executa diagnóstico do dispositivo"""
        issues = []
        
        if not self.connected:
            issues.append("Device disconnected")
        if not self.collecting_data:
            issues.append("Data collection stopped")
        
        return {
            'status': 'healthy' if not issues else 'warning',
            'issues': issues,
            'connected': self.connected,
            'collecting_data': self.collecting_data
        }

class EdgeMLModel:
    """Representa um modelo ML otimizado para edge"""
    
    def __init__(self, model_id: str, config: Dict):
        self.model_id = model_id
        self.config = config
        self.model_data = None
        self.optimized = True
    
    def predict(self, input_data):
        """Executa inferência"""
        # Simula inferência
        time.sleep(self.config.get('inference_time_ms', 50) / 1000.0)
        return {'prediction': 'normal', 'confidence': 0.95}

class DataStreamPipeline:
    """Pipeline de processamento de stream de dados"""
    
    def __init__(self, pipeline_id: str, config: Dict, platform):
        self.pipeline_id = pipeline_id
        self.config = config
        self.platform = platform
        self.active = False
        self.processed_records = 0
    
    def start(self):
        """Inicia o pipeline"""
        self.active = True
    
    def stop(self):
        """Para o pipeline"""
        self.active = False
    
    def is_active(self):
        """Verifica se está ativo"""
        return self.active
    
    def run_diagnostics(self):
        """Executa diagnóstico do pipeline"""
        return {
            'status': 'healthy' if self.active else 'stopped',
            'processed_records': self.processed_records,
            'active': self.active
        }

class MQTTCommunication:
    """Protocolo de comunicação MQTT"""
    
    def __init__(self, config: Dict, platform):
        self.config = config
        self.platform = platform
        self.connected = False
    
    def start(self):
        """Inicia protocolo MQTT"""
        self.connected = True
    
    def stop(self):
        """Para protocolo MQTT"""
        self.connected = False
    
    def run_diagnostics(self):
        """Diagnóstico do MQTT"""
        return {
            'status': 'connected' if self.connected else 'disconnected',
            'broker': self.config.get('broker_host', 'localhost'),
            'topics': self.config.get('topics', [])
        }

class WebSocketCommunication:
    """Protocolo de comunicação WebSocket"""
    
    def __init__(self, config: Dict, platform):
        self.config = config
        self.platform = platform
        self.active = False
    
    def start(self):
        """Inicia WebSocket server"""
        self.active = True
    
    def stop(self):
        """Para WebSocket server"""
        self.active = False
    
    def run_diagnostics(self):
        """Diagnóstico do WebSocket"""
        return {
            'status': 'active' if self.active else 'inactive',
            'host': self.config.get('host', 'localhost'),
            'port': self.config.get('port', 8765)
        }

class CoAPCommunication:
    """Protocolo CoAP (Constrained Application Protocol)"""
    
    def __init__(self, config: Dict, platform):
        self.config = config
        self.platform = platform
        self.active = False
    
    def start(self):
        self.active = True
    
    def stop(self):
        self.active = False
    
    def run_diagnostics(self):
        return {'status': 'active' if self.active else 'inactive'}

class LoRaWANCommunication:
    """Protocolo LoRaWAN para IoT de longo alcance"""
    
    def __init__(self, config: Dict, platform):
        self.config = config
        self.platform = platform
        self.active = False
    
    def start(self):
        self.active = True
    
    def stop(self):
        self.active = False
    
    def run_diagnostics(self):
        return {'status': 'active' if self.active else 'inactive'}

class GenericCommunication:
    """Protocolo genérico de comunicação"""
    
    def __init__(self, config: Dict, platform):
        self.config = config
        self.platform = platform
        self.active = False
    
    def start(self):
        self.active = True
    
    def stop(self):
        self.active = False
    
    def run_diagnostics(self):
        return {'status': 'active' if self.active else 'inactive'}

class MetricsCollector:
    """Coletor de métricas do sistema"""
    
    def __init__(self):
        self.metrics = {}
    
    def collect_metric(self, name: str, value: Any):
        """Coleta uma métrica"""
        self.metrics[name] = {
            'value': value,
            'timestamp': datetime.now()
        }
    
    def get_metrics(self):
        """Obtém todas as métricas"""
        return self.metrics

# Demonstração principal
if __name__ == "__main__":
    
    print("🚀 Iniciando Edge Computing & IoT Platform Demo")
    print("Este demo simula uma plataforma completa de edge computing")
    print("-" * 70)
    
    # Inicializa plataforma
    edge_platform = EdgeComputingPlatform("edge_demo_platform")
    
    try:
        # Executa demo completo
        results = edge_platform.run_complete_edge_demo()
        
        print(f"\n📈 Demo executado com sucesso!")
        print(f"Funcionalidades demonstradas:")
        print(f"• Edge nodes com processamento distribuído")
        print(f"• Dispositivos IoT com coleta de dados")
        print(f"• Machine Learning embarcado")
        print(f"• Protocolos de comunicação IoT")
        print(f"• Analytics em tempo real")
        print(f"• Orquestração de workloads")
        print(f"• Sincronização cloud-edge")
        print(f"• Monitoramento e diagnóstico")
        
    except Exception as e:
        print(f"❌ Erro durante execução: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        # Cleanup
        edge_platform.cleanup()

"""
CONCEITOS AVANÇADOS DEMONSTRADOS:

1. 🏗️ EDGE COMPUTING ARCHITECTURE
   - Processamento distribuído na borda
   - Orquestração de edge nodes
   - Latência ultra-baixa
   - Autonomia local

2. 🔌 INTERNET OF THINGS (IoT)
   - Gerenciamento de dispositivos
   - Protocolos de comunicação (MQTT, CoAP, LoRaWAN)
   - Coleta de dados em tempo real
   - Device management

3. 🤖 EDGE MACHINE LEARNING
   - Modelos otimizados para edge
   - Inferência em tempo real
   - TensorFlow Lite deployment
   - Model quantization

4. 🌊 REAL-TIME ANALYTICS
   - Stream processing
   - Anomaly detection
   - Pattern recognition
   - Alert generation

5. 📡 COMMUNICATION PROTOCOLS
   - MQTT publish/subscribe
   - WebSocket streaming
   - CoAP for constrained devices
   - LoRaWAN for long-range IoT

6. ☁️ CLOUD-EDGE SYNCHRONIZATION
   - Data synchronization
   - Model updates
   - Configuration management
   - Hybrid cloud deployment

7. 🎭 WORKLOAD ORCHESTRATION
   - Resource-aware scheduling
   - Load balancing
   - Auto-scaling
   - Fault tolerance

8. 🔍 MONITORING & DIAGNOSTICS
   - System health monitoring
   - Performance metrics
   - Automated diagnostics
   - Predictive maintenance

APLICAÇÕES REAIS:
- Indústria 4.0 e manufatura inteligente
- Cidades inteligentes (smart cities)
- Veículos autônomos
- Agricultura de precisão
- Saúde digital e telemedicina
- Segurança e vigilância
- Energia e smart grids
- Varejo e experiência do cliente
"""
