#!/usr/bin/env python3
"""
Aula 02: Simulação de Sensores IoT
Professor: Vagner Cordeiro
Curso: Tópicos de Big Data em Python

Este script simula múltiplos sensores IoT gerando dados em tempo real
e demonstra conceitos de computação distribuída.
"""

import json
import time
import random
import threading
import queue
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from concurrent.futures import ThreadPoolExecutor
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

class IoTSensor:
    """Classe base para sensores IoT"""
    
    def __init__(self, sensor_id, sensor_type, location):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.location = location
        self.is_active = True
        self.data_queue = queue.Queue()
        
    def generate_data(self):
        """Método base para geração de dados - deve ser sobrescrito"""
        raise NotImplementedError("Subclasses devem implementar generate_data()")
    
    def start_streaming(self, duration_seconds=60, interval=1):
        """Inicia streaming de dados por um período determinado"""
        start_time = time.time()
        while time.time() - start_time < duration_seconds and self.is_active:
            data = self.generate_data()
            self.data_queue.put(data)
            time.sleep(interval)
    
    def stop_streaming(self):
        """Para o streaming de dados"""
        self.is_active = False

class TemperatureSensor(IoTSensor):
    """Sensor de temperatura com padrões realistas"""
    
    def __init__(self, sensor_id, location, base_temp=22, variation=5):
        super().__init__(sensor_id, "temperature", location)
        self.base_temp = base_temp
        self.variation = variation
        self.time_offset = random.uniform(0, 24)  # Para simular diferentes fusos
        
    def generate_data(self):
        """Gera dados de temperatura com padrão circadiano"""
        current_time = datetime.now()
        
        # Padrão circadiano (mais quente durante o dia)
        hour_factor = np.sin((current_time.hour + self.time_offset) * np.pi / 12) * 3
        
        # Ruído aleatório
        noise = random.gauss(0, 1)
        
        # Temperatura final
        temperature = self.base_temp + hour_factor + noise
        
        # Adicionar falhas ocasionais (1% de chance)
        if random.random() < 0.01:
            temperature = None  # Sensor falhou
        
        return {
            "sensor_id": self.sensor_id,
            "sensor_type": self.sensor_type,
            "location": self.location,
            "timestamp": current_time.isoformat(),
            "temperature": temperature,
            "unit": "celsius",
            "status": "active" if temperature is not None else "error"
        }

class HumiditySensor(IoTSensor):
    """Sensor de umidade"""
    
    def __init__(self, sensor_id, location, base_humidity=50):
        super().__init__(sensor_id, "humidity", location)
        self.base_humidity = base_humidity
        
    def generate_data(self):
        """Gera dados de umidade"""
        current_time = datetime.now()
        
        # Umidade varia com temperatura e hora do dia
        hour_factor = np.cos((current_time.hour) * np.pi / 12) * 10
        weather_factor = random.gauss(0, 5)
        
        humidity = max(0, min(100, self.base_humidity + hour_factor + weather_factor))
        
        return {
            "sensor_id": self.sensor_id,
            "sensor_type": self.sensor_type,
            "location": self.location,
            "timestamp": current_time.isoformat(),
            "humidity": round(humidity, 2),
            "unit": "percentage",
            "status": "active"
        }

class MotionSensor(IoTSensor):
    """Sensor de movimento PIR"""
    
    def __init__(self, sensor_id, location, activity_level="medium"):
        super().__init__(sensor_id, "motion", location)
        self.activity_levels = {
            "low": 0.05,
            "medium": 0.15,
            "high": 0.30
        }
        self.activity_prob = self.activity_levels.get(activity_level, 0.15)
        
    def generate_data(self):
        """Gera dados de movimento baseados em padrões de atividade"""
        current_time = datetime.now()
        
        # Mais atividade durante horas comerciais
        if 8 <= current_time.hour <= 18:
            motion_prob = self.activity_prob * 2
        elif 22 <= current_time.hour or current_time.hour <= 6:
            motion_prob = self.activity_prob * 0.2
        else:
            motion_prob = self.activity_prob
        
        motion_detected = random.random() < motion_prob
        
        return {
            "sensor_id": self.sensor_id,
            "sensor_type": self.sensor_type,
            "location": self.location,
            "timestamp": current_time.isoformat(),
            "motion_detected": motion_detected,
            "confidence": round(random.uniform(0.8, 1.0), 2),
            "status": "active"
        }

class EnergyMeter(IoTSensor):
    """Medidor de energia elétrica"""
    
    def __init__(self, sensor_id, location, base_consumption=100):
        super().__init__(sensor_id, "energy", location)
        self.base_consumption = base_consumption
        self.cumulative_consumption = 0
        
    def generate_data(self):
        """Gera dados de consumo de energia"""
        current_time = datetime.now()
        
        # Consumo varia com hora do dia
        if 6 <= current_time.hour <= 9 or 17 <= current_time.hour <= 23:
            # Picos de consumo (manhã e noite)
            consumption = self.base_consumption * random.uniform(1.2, 2.0)
        elif 23 <= current_time.hour or current_time.hour <= 6:
            # Consumo baixo (madrugada)
            consumption = self.base_consumption * random.uniform(0.3, 0.6)
        else:
            # Consumo normal
            consumption = self.base_consumption * random.uniform(0.8, 1.2)
        
        self.cumulative_consumption += consumption / 60  # Por minuto
        
        return {
            "sensor_id": self.sensor_id,
            "sensor_type": self.sensor_type,
            "location": self.location,
            "timestamp": current_time.isoformat(),
            "instant_consumption": round(consumption, 2),
            "cumulative_consumption": round(self.cumulative_consumption, 2),
            "unit": "watts",
            "status": "active"
        }

class IoTDataCollector:
    """Sistema de coleta e processamento de dados IoT"""
    
    def __init__(self, db_path="iot_data.db"):
        self.sensors = []
        self.data_buffer = queue.Queue()
        self.db_path = db_path
        self.setup_database()
        
    def setup_database(self):
        """Configura banco de dados SQLite"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id TEXT,
            sensor_type TEXT,
            location TEXT,
            timestamp TEXT,
            data JSON,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        conn.commit()
        conn.close()
        
    def add_sensor(self, sensor):
        """Adiciona sensor ao sistema"""
        self.sensors.append(sensor)
        
    def start_data_collection(self, duration_seconds=300):
        """Inicia coleta de dados de todos os sensores"""
        print(f"🚀 Iniciando coleta de dados de {len(self.sensors)} sensores por {duration_seconds}s...")
        
        # Usar ThreadPoolExecutor para processamento paralelo
        with ThreadPoolExecutor(max_workers=len(self.sensors) + 2) as executor:
            # Iniciar threads dos sensores
            sensor_futures = []
            for sensor in self.sensors:
                future = executor.submit(sensor.start_streaming, duration_seconds, 1)
                sensor_futures.append(future)
            
            # Thread para coletar dados dos sensores
            collector_future = executor.submit(self._collect_sensor_data, duration_seconds)
            
            # Thread para processamento em tempo real
            processor_future = executor.submit(self._process_real_time_data, duration_seconds)
            
            # Aguardar conclusão
            for future in sensor_futures:
                future.result()
            collector_future.result()
            processor_future.result()
        
        print("✅ Coleta de dados finalizada!")
        
    def _collect_sensor_data(self, duration_seconds):
        """Coleta dados de todos os sensores e armazena"""
        start_time = time.time()
        data_count = 0
        
        while time.time() - start_time < duration_seconds:
            for sensor in self.sensors:
                try:
                    if not sensor.data_queue.empty():
                        data = sensor.data_queue.get_nowait()
                        self.data_buffer.put(data)
                        self._store_data(data)
                        data_count += 1
                except queue.Empty:
                    continue
            
            time.sleep(0.1)  # Pequena pausa para não sobrecarregar CPU
            
        print(f"📊 Total de {data_count} registros coletados")
        
    def _store_data(self, data):
        """Armazena dados no banco SQLite"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO sensor_data (sensor_id, sensor_type, location, timestamp, data)
        VALUES (?, ?, ?, ?, ?)
        ''', (data['sensor_id'], data['sensor_type'], data['location'], 
              data['timestamp'], json.dumps(data)))
        
        conn.commit()
        conn.close()
        
    def _process_real_time_data(self, duration_seconds):
        """Processamento em tempo real para alertas e análises"""
        start_time = time.time()
        alert_count = 0
        
        while time.time() - start_time < duration_seconds:
            try:
                if not self.data_buffer.empty():
                    data = self.data_buffer.get_nowait()
                    
                    # Verificar condições de alerta
                    if self._check_alerts(data):
                        alert_count += 1
                        
            except queue.Empty:
                time.sleep(0.1)
                continue
                
        if alert_count > 0:
            print(f"⚠️  {alert_count} alertas gerados durante a coleta")
            
    def _check_alerts(self, data):
        """Verifica condições para gerar alertas"""
        alerts = False
        
        if data['sensor_type'] == 'temperature' and data.get('temperature'):
            if data['temperature'] > 35 or data['temperature'] < 10:
                print(f"🌡️  ALERTA: Temperatura extrema ({data['temperature']}°C) em {data['location']}")
                alerts = True
                
        elif data['sensor_type'] == 'energy':
            if data['instant_consumption'] > 200:
                print(f"⚡ ALERTA: Alto consumo de energia ({data['instant_consumption']}W) em {data['location']}")
                alerts = True
                
        return alerts
        
    def generate_analytics_report(self):
        """Gera relatório de análise dos dados coletados"""
        print("\n📈 RELATÓRIO DE ANÁLISE DE DADOS IoT")
        print("=" * 50)
        
        # Carregar dados do banco
        conn = sqlite3.connect(self.db_path)
        
        # Estatísticas gerais
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM sensor_data")
        total_records = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(DISTINCT sensor_id) FROM sensor_data")
        unique_sensors = cursor.fetchone()[0]
        
        cursor.execute("SELECT sensor_type, COUNT(*) FROM sensor_data GROUP BY sensor_type")
        sensor_stats = cursor.fetchall()
        
        print(f"📊 Total de registros: {total_records}")
        print(f"🔌 Sensores únicos: {unique_sensors}")
        print("\n📋 Distribuição por tipo de sensor:")
        for sensor_type, count in sensor_stats:
            print(f"  • {sensor_type}: {count} registros")
        
        # Análises específicas por tipo de sensor
        self._analyze_temperature_data(conn)
        self._analyze_energy_data(conn)
        
        conn.close()
        
    def _analyze_temperature_data(self, conn):
        """Análise específica de dados de temperatura"""
        df = pd.read_sql_query('''
        SELECT sensor_id, location, timestamp, json_extract(data, '$.temperature') as temperature
        FROM sensor_data 
        WHERE sensor_type = 'temperature' AND json_extract(data, '$.temperature') IS NOT NULL
        ''', conn)
        
        if not df.empty:
            print(f"\n🌡️  ANÁLISE DE TEMPERATURA")
            print(f"  • Temperatura média: {df['temperature'].mean():.2f}°C")
            print(f"  • Temperatura máxima: {df['temperature'].max():.2f}°C")
            print(f"  • Temperatura mínima: {df['temperature'].min():.2f}°C")
            print(f"  • Desvio padrão: {df['temperature'].std():.2f}°C")
            
    def _analyze_energy_data(self, conn):
        """Análise específica de dados de energia"""
        df = pd.read_sql_query('''
        SELECT sensor_id, location, timestamp, 
               json_extract(data, '$.instant_consumption') as consumption
        FROM sensor_data 
        WHERE sensor_type = 'energy'
        ''', conn)
        
        if not df.empty:
            print(f"\n⚡ ANÁLISE DE ENERGIA")
            print(f"  • Consumo médio: {df['consumption'].mean():.2f}W")
            print(f"  • Consumo máximo: {df['consumption'].max():.2f}W")
            print(f"  • Consumo total estimado: {df['consumption'].sum()/60:.2f}Wh")

def simulate_smart_home():
    """Simula um sistema IoT de casa inteligente"""
    print("🏠 SIMULAÇÃO: Casa Inteligente IoT")
    print("=" * 40)
    
    # Criar sistema coletor
    collector = IoTDataCollector("smart_home.db")
    
    # Criar sensores para diferentes cômodos
    sensors = [
        TemperatureSensor("temp_001", "Sala de Estar", 23, 3),
        TemperatureSensor("temp_002", "Quarto Principal", 21, 2),
        TemperatureSensor("temp_003", "Cozinha", 25, 4),
        HumiditySensor("hum_001", "Sala de Estar", 45),
        HumiditySensor("hum_002", "Banheiro", 65),
        MotionSensor("mot_001", "Entrada Principal", "high"),
        MotionSensor("mot_002", "Sala de Estar", "medium"),
        MotionSensor("mot_003", "Quarto Principal", "low"),
        EnergyMeter("ene_001", "Quadro Principal", 150),
        EnergyMeter("ene_002", "Ar Condicionado", 800),
    ]
    
    # Adicionar sensores ao coletor
    for sensor in sensors:
        collector.add_sensor(sensor)
    
    # Iniciar coleta por 2 minutos
    collector.start_data_collection(120)
    
    # Gerar relatório
    collector.generate_analytics_report()

def simulate_industrial_iot():
    """Simula um sistema IoT industrial"""
    print("\n🏭 SIMULAÇÃO: IoT Industrial")
    print("=" * 40)
    
    collector = IoTDataCollector("industrial_iot.db")
    
    # Sensores industriais
    sensors = [
        TemperatureSensor("temp_maq_001", "Máquina Produção A", 45, 8),
        TemperatureSensor("temp_maq_002", "Máquina Produção B", 42, 6),
        TemperatureSensor("temp_maq_003", "Compressor Principal", 65, 10),
        EnergyMeter("ene_maq_001", "Linha Produção 1", 2500),
        EnergyMeter("ene_maq_002", "Linha Produção 2", 2200),
        EnergyMeter("ene_comp_001", "Sistema Ar Comprimido", 1800),
        MotionSensor("mot_esteira_001", "Esteira Principal", "high"),
        MotionSensor("mot_esteira_002", "Esteira Secundária", "high"),
    ]
    
    for sensor in sensors:
        collector.add_sensor(sensor)
    
    collector.start_data_collection(90)
    collector.generate_analytics_report()

def demonstrate_distributed_processing():
    """Demonstra conceitos de processamento distribuído"""
    print("\n🔄 DEMONSTRAÇÃO: Processamento Distribuído")
    print("=" * 50)
    
    # Simular processamento de dados de múltiplas fontes
    def process_sensor_batch(sensor_data_batch):
        """Processa um lote de dados de sensores"""
        start_time = time.time()
        
        # Simular processamento complexo
        processed_data = []
        for data in sensor_data_batch:
            # Análise e transformação dos dados
            processed = {
                "original": data,
                "processed_at": datetime.now().isoformat(),
                "anomaly_score": random.uniform(0, 1),
                "trend": "up" if random.random() > 0.5 else "down"
            }
            processed_data.append(processed)
            time.sleep(0.01)  # Simular processamento
        
        processing_time = time.time() - start_time
        return len(processed_data), processing_time
    
    # Gerar dados de teste
    test_data = []
    for i in range(1000):
        test_data.append({
            "sensor_id": f"sensor_{i%10}",
            "value": random.uniform(0, 100),
            "timestamp": datetime.now().isoformat()
        })
    
    # Processamento sequencial
    print("🔄 Processamento Sequencial...")
    start_sequential = time.time()
    sequential_results = []
    
    # Dividir em lotes de 100
    batch_size = 100
    for i in range(0, len(test_data), batch_size):
        batch = test_data[i:i+batch_size]
        count, proc_time = process_sensor_batch(batch)
        sequential_results.append((count, proc_time))
    
    sequential_total = time.time() - start_sequential
    print(f"  ⏱️  Tempo total: {sequential_total:.2f}s")
    
    # Processamento paralelo
    print("\n⚡ Processamento Paralelo...")
    start_parallel = time.time()
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for i in range(0, len(test_data), batch_size):
            batch = test_data[i:i+batch_size]
            future = executor.submit(process_sensor_batch, batch)
            futures.append(future)
        
        parallel_results = []
        for future in futures:
            result = future.result()
            parallel_results.append(result)
    
    parallel_total = time.time() - start_parallel
    print(f"  ⏱️  Tempo total: {parallel_total:.2f}s")
    
    # Comparação
    speedup = sequential_total / parallel_total
    print(f"\n📊 RESULTADOS:")
    print(f"  • Speedup: {speedup:.2f}x")
    print(f"  • Eficiência: {(speedup/4)*100:.1f}%")
    print(f"  • Registros processados: {len(test_data)}")

if __name__ == "__main__":
    print("🌐 AULA 02: IoT e Computação Distribuída")
    print("=" * 60)
    print("Professor: Vagner Cordeiro")
    print("Curso: Tópicos de Big Data em Python")
    print("=" * 60)
    
    try:
        # Executar simulações
        simulate_smart_home()
        simulate_industrial_iot()
        demonstrate_distributed_processing()
        
        print("\n✅ AULA CONCLUÍDA COM SUCESSO!")
        print("\n📝 PRÓXIMOS PASSOS:")
        print("  1. Analisar os dados gerados nos arquivos .db")
        print("  2. Implementar seus próprios tipos de sensores")
        print("  3. Criar dashboards em tempo real")
        print("  4. Experimentar com diferentes protocolos IoT")
        
    except KeyboardInterrupt:
        print("\n⏹️  Simulação interrompida pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro durante a execução: {e}")
        import traceback
        traceback.print_exc()
