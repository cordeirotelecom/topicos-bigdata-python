"""
Aula 01 - Big Data: Demonstração de Velocidade
Professor: Vagner Cordeiro
"""

import pandas as pd
import numpy as np
import time
import threading
import queue
from datetime import datetime
import matplotlib.pyplot as plt
import random

class StreamDataGenerator:
    """
    Simula um gerador de dados em tempo real (streaming)
    """
    
    def __init__(self, delay=0.1):
        self.delay = delay
        self.running = False
        self.data_queue = queue.Queue()
        
    def start_stream(self, duration=30):
        """
        Inicia a geração de dados em tempo real
        
        Args:
            duration (int): Duração em segundos
        """
        self.running = True
        
        def generate_data():
            start_time = time.time()
            count = 0
            
            while self.running and (time.time() - start_time) < duration:
                # Simular dados de sensor IoT
                data_point = {
                    'timestamp': datetime.now(),
                    'sensor_id': f"SENSOR_{random.randint(1, 10):02d}",
                    'temperatura': round(random.uniform(15.0, 35.0), 2),
                    'umidade': round(random.uniform(30.0, 90.0), 2),
                    'pressao': round(random.uniform(1000, 1050), 1),
                    'count': count
                }
                
                self.data_queue.put(data_point)
                count += 1
                time.sleep(self.delay)
                
        # Iniciar thread para geração de dados
        self.thread = threading.Thread(target=generate_data)
        self.thread.start()
        
    def stop_stream(self):
        """Para a geração de dados"""
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join()
    
    def get_data(self):
        """Retorna dados acumulados"""
        data_list = []
        while not self.data_queue.empty():
            data_list.append(self.data_queue.get())
        return data_list

def demonstrar_velocidade_streaming():
    """
    Demonstra o conceito de velocidade com dados streaming
    """
    print("⚡ DEMONSTRAÇÃO: VELOCIDADE DE DADOS")
    print("="*50)
    print("🌊 Simulando stream de dados de sensores IoT...")
    print("📊 Coletando dados por 10 segundos...")
    
    # Criar gerador de stream
    stream = StreamDataGenerator(delay=0.05)  # 20 dados por segundo
    
    # Iniciar coleta
    stream.start_stream(duration=10)
    
    # Coletar dados em tempo real
    all_data = []
    start_time = time.time()
    
    try:
        while stream.running:
            # Coletar dados disponíveis
            new_data = stream.get_data()
            all_data.extend(new_data)
            
            # Mostrar progresso a cada segundo
            elapsed = time.time() - start_time
            if len(all_data) > 0 and int(elapsed) != int(elapsed - 0.1):
                print(f"📈 {elapsed:.1f}s: {len(all_data)} registros coletados")
            
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("\n⏹️ Interrompido pelo usuário")
    
    finally:
        stream.stop_stream()
    
    # Processar dados coletados
    if all_data:
        df = pd.DataFrame(all_data)
        print(f"\n✅ Coleta finalizada!")
        print(f"📊 Total coletado: {len(df)} registros")
        print(f"⚡ Taxa média: {len(df)/10:.1f} registros/segundo")
        
        return df
    else:
        print("❌ Nenhum dado foi coletado")
        return pd.DataFrame()

def comparar_velocidades_processamento():
    """
    Compara diferentes velocidades de processamento
    """
    print("\n" + "="*50)
    print("🏃‍♂️ COMPARAÇÃO DE VELOCIDADES DE PROCESSAMENTO")
    print("="*50)
    
    # Criar dataset de teste
    sizes = [1000, 10000, 100000, 500000]
    methods = ['Python Loop', 'List Comprehension', 'NumPy', 'Pandas']
    results = {method: [] for method in methods}
    
    for size in sizes:
        print(f"\n📊 Testando com {size:,} números...")
        
        # Gerar dados
        data = np.random.randn(size)
        
        # Método 1: Loop Python tradicional
        start = time.time()
        result1 = 0
        for i in range(len(data)):
            result1 += data[i] ** 2
        time1 = time.time() - start
        results['Python Loop'].append(time1)
        print(f"   🐌 Python Loop: {time1:.4f}s")
        
        # Método 2: List Comprehension
        start = time.time()
        result2 = sum([x**2 for x in data])
        time2 = time.time() - start
        results['List Comprehension'].append(time2)
        print(f"   🚶 List Comprehension: {time2:.4f}s")
        
        # Método 3: NumPy
        start = time.time()
        result3 = np.sum(data ** 2)
        time3 = time.time() - start
        results['NumPy'].append(time3)
        print(f"   🏃 NumPy: {time3:.4f}s")
        
        # Método 4: Pandas
        start = time.time()
        df_temp = pd.DataFrame({'values': data})
        result4 = (df_temp['values'] ** 2).sum()
        time4 = time.time() - start
        results['Pandas'].append(time4)
        print(f"   🚀 Pandas: {time4:.4f}s")
        
        # Speedup
        if time1 > 0:
            print(f"   📈 NumPy é {time1/time3:.1f}x mais rápido que loop Python")
    
    return sizes, results

def criar_grafico_velocidade(sizes, results):
    """
    Cria gráfico comparativo de velocidades
    """
    print(f"\n📊 Criando gráfico de performance...")
    
    plt.figure(figsize=(12, 8))
    
    for method, times in results.items():
        plt.plot(sizes, times, marker='o', linewidth=2, label=method)
    
    plt.xlabel('Tamanho do Dataset')
    plt.ylabel('Tempo de Processamento (segundos)')
    plt.title('Comparação de Velocidade de Processamento\nBig Data: Conceito de Velocidade')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.yscale('log')  # Escala logarítmica para melhor visualização
    plt.xscale('log')
    
    # Adicionar anotações
    plt.text(0.02, 0.95, 'Menor é melhor', transform=plt.gca().transAxes,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.5))
    
    plt.tight_layout()
    plt.savefig('velocidade_processamento.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Gráfico salvo em 'velocidade_processamento.png'")

def simular_big_data_real_time():
    """
    Simula processamento de Big Data em tempo real
    """
    print("\n" + "="*50)
    print("🌐 SIMULAÇÃO: BIG DATA EM TEMPO REAL")
    print("="*50)
    print("📱 Simulando dados de aplicativo móvel...")
    
    # Simular dados de múltiplas fontes
    sources = ['Mobile App', 'Website', 'IoT Sensors', 'Social Media', 'Payments']
    
    for i in range(5):
        print(f"\n🔄 Ciclo {i+1}/5 - Processando dados de múltiplas fontes...")
        
        batch_data = []
        
        for source in sources:
            # Simular chegada de dados de cada fonte
            records = random.randint(100, 1000)
            start_time = time.time()
            
            # Simular processamento
            data = np.random.randn(records)
            processed = np.sum(data ** 2)  # Simular algum processamento
            
            processing_time = time.time() - start_time
            
            batch_data.append({
                'source': source,
                'records': records,
                'processing_time': processing_time,
                'result': processed
            })
            
            print(f"   📊 {source}: {records} registros em {processing_time:.4f}s")
        
        # Consolidar resultados do batch
        total_records = sum([d['records'] for d in batch_data])
        total_time = sum([d['processing_time'] for d in batch_data])
        
        print(f"   ✅ Batch processado: {total_records} registros em {total_time:.4f}s")
        print(f"   ⚡ Taxa: {total_records/total_time:.0f} registros/segundo")
        
        time.sleep(1)  # Simular intervalo entre batches

def main():
    """
    Função principal demonstrando conceitos de Velocidade em Big Data
    """
    print("🎓 AULA 01 - BIG DATA: CONCEITO DE VELOCIDADE")
    print("👨‍🏫 Professor: Vagner Cordeiro")
    print("="*60)
    
    print("\n🎯 OBJETIVOS:")
    print("✅ Entender o conceito de VELOCIDADE em Big Data")
    print("✅ Comparar diferentes métodos de processamento")
    print("✅ Simular dados em tempo real (streaming)")
    print("✅ Aprender otimização com NumPy e Pandas")
    
    # 1. Demonstração de streaming
    df_stream = demonstrar_velocidade_streaming()
    
    # 2. Comparação de velocidades
    sizes, results = comparar_velocidades_processamento()
    
    # 3. Criar visualizações
    criar_grafico_velocidade(sizes, results)
    
    # 4. Simulação de tempo real
    simular_big_data_real_time()
    
    # Salvar dados de streaming se houver
    if not df_stream.empty:
        df_stream.to_csv('dados_streaming.csv', index=False)
        print(f"\n💾 Dados de streaming salvos em 'dados_streaming.csv'")
    
    print(f"\n🎯 RESUMO DA AULA:")
    print(f"✅ Entendemos o conceito de VELOCIDADE")
    print(f"✅ Vimos streaming de dados em tempo real")
    print(f"✅ Comparamos métodos de processamento")
    print(f"✅ NumPy/Pandas são MUITO mais rápidos!")
    print(f"✅ Simulamos cenários de Big Data real")
    
    print(f"\n💡 DICAS IMPORTANTES:")
    print(f"🔹 Use NumPy/Pandas para cálculos massivos")
    print(f"🔹 Evite loops Python para grandes datasets")
    print(f"🔹 Processamento em tempo real requer otimização")
    print(f"🔹 Velocidade é crucial em aplicações Big Data")

if __name__ == "__main__":
    main()
