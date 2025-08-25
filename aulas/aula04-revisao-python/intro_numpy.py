"""
Aula 04 - Introdução ao NumPy para Análise de Dados
Professor: Vagner Cordeiro

NumPy é fundamental para computação científica e Big Data
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import random

def introducao_numpy():
    """
    Introdução aos conceitos fundamentais do NumPy
    """
    print("🔢 INTRODUÇÃO AO NUMPY")
    print("="*40)
    
    # Por que NumPy?
    print("❓ POR QUE USAR NUMPY?")
    print("-" * 25)
    
    # Comparação de performance
    size = 1000000
    
    # Lista Python tradicional
    start = time.time()
    python_list = list(range(size))
    python_sum = sum([x * 2 for x in python_list])
    python_time = time.time() - start
    
    # Array NumPy
    start = time.time()
    numpy_array = np.arange(size)
    numpy_sum = np.sum(numpy_array * 2)
    numpy_time = time.time() - start
    
    print(f"🐍 Lista Python: {python_time:.4f}s")
    print(f"🚀 Array NumPy: {numpy_time:.4f}s")
    print(f"⚡ NumPy é {python_time/numpy_time:.1f}x mais rápido!")
    
    # Uso de memória
    python_memory = size * 28  # bytes por inteiro em Python
    numpy_memory = numpy_array.nbytes
    
    print(f"\n💾 USO DE MEMÓRIA:")
    print(f"🐍 Lista Python: ~{python_memory/1024/1024:.1f} MB")
    print(f"🚀 Array NumPy: {numpy_memory/1024/1024:.1f} MB")
    print(f"📉 NumPy usa {python_memory/numpy_memory:.1f}x menos memória!")

def arrays_basicos():
    """
    Trabalhando com arrays NumPy básicos
    """
    print(f"\n📊 ARRAYS NUMPY BÁSICOS")
    print("="*40)
    
    # Criação de arrays
    print("🔨 CRIANDO ARRAYS")
    print("-" * 20)
    
    # Diferentes formas de criar arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.arange(10)
    arr3 = np.linspace(0, 10, 11)
    arr4 = np.zeros(5)
    arr5 = np.ones(5)
    arr6 = np.random.random(5)
    
    print(f"Array da lista: {arr1}")
    print(f"Range 0-9: {arr2}")
    print(f"Linspace 0-10: {arr3}")
    print(f"Zeros: {arr4}")
    print(f"Ones: {arr5}")
    print(f"Random: {arr6.round(3)}")
    
    # Propriedades dos arrays
    print(f"\n📐 PROPRIEDADES DOS ARRAYS")
    print("-" * 30)
    
    vendas = np.array([1500, 2300, 1800, 2100, 1950, 2400, 2200, 1700, 2500, 2800])
    
    print(f"Array de vendas: {vendas}")
    print(f"Shape (forma): {vendas.shape}")
    print(f"Size (tamanho): {vendas.size}")
    print(f"Dtype (tipo): {vendas.dtype}")
    print(f"Dimensões: {vendas.ndim}")
    print(f"Bytes: {vendas.nbytes}")

def operacoes_matematicas():
    """
    Operações matemáticas com arrays NumPy
    """
    print(f"\n🧮 OPERAÇÕES MATEMÁTICAS")
    print("="*40)
    
    # Dados de exemplo: vendas trimestrais
    vendas_q1 = np.array([15000, 18000, 22000])
    vendas_q2 = np.array([17000, 19000, 24000])
    vendas_q3 = np.array([16000, 21000, 25000])
    vendas_q4 = np.array([20000, 23000, 28000])
    
    print("📈 ANÁLISE DE VENDAS TRIMESTRAIS")
    print("-" * 35)
    
    # Operações elemento por elemento
    crescimento_q2 = ((vendas_q2 - vendas_q1) / vendas_q1) * 100
    crescimento_q3 = ((vendas_q3 - vendas_q2) / vendas_q2) * 100
    crescimento_q4 = ((vendas_q4 - vendas_q3) / vendas_q3) * 100
    
    print(f"Q1 vendas: {vendas_q1}")
    print(f"Q2 vendas: {vendas_q2}")
    print(f"Crescimento Q1→Q2: {crescimento_q2.round(1)}%")
    print(f"Crescimento Q2→Q3: {crescimento_q3.round(1)}%")
    print(f"Crescimento Q3→Q4: {crescimento_q4.round(1)}%")
    
    # Consolidação anual
    vendas_anuais = vendas_q1 + vendas_q2 + vendas_q3 + vendas_q4
    print(f"Total anual por produto: {vendas_anuais}")
    
    # Estatísticas
    print(f"\n📊 ESTATÍSTICAS DESCRITIVAS")
    print("-" * 30)
    
    todos_valores = np.concatenate([vendas_q1, vendas_q2, vendas_q3, vendas_q4])
    
    print(f"Todos os valores: {todos_valores}")
    print(f"Média: {np.mean(todos_valores):,.0f}")
    print(f"Mediana: {np.median(todos_valores):,.0f}")
    print(f"Desvio padrão: {np.std(todos_valores):,.0f}")
    print(f"Mínimo: {np.min(todos_valores):,.0f}")
    print(f"Máximo: {np.max(todos_valores):,.0f}")
    print(f"Soma total: {np.sum(todos_valores):,.0f}")

def arrays_multidimensionais():
    """
    Trabalhando com arrays multidimensionais
    """
    print(f"\n🏢 ARRAYS MULTIDIMENSIONAIS")
    print("="*40)
    
    # Matriz de vendas: produtos x meses
    # Linhas = produtos, Colunas = meses
    vendas_matriz = np.array([
        [1500, 1600, 1700, 1800, 1900, 2000],  # Produto A
        [1200, 1300, 1400, 1350, 1450, 1500],  # Produto B
        [800, 850, 900, 950, 1000, 1100],      # Produto C
        [2000, 2100, 2200, 2300, 2400, 2500]   # Produto D
    ])
    
    produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D']
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
    
    print(f"📊 MATRIZ DE VENDAS (Produtos x Meses)")
    print("-" * 40)
    print(f"Shape da matriz: {vendas_matriz.shape}")
    print(f"Total de elementos: {vendas_matriz.size}")
    
    # Análises por linha (produtos)
    vendas_por_produto = np.sum(vendas_matriz, axis=1)
    media_por_produto = np.mean(vendas_matriz, axis=1)
    
    print(f"\n📈 ANÁLISE POR PRODUTO:")
    for i, produto in enumerate(produtos):
        print(f"{produto}: Total R$ {vendas_por_produto[i]:,} | Média R$ {media_por_produto[i]:,.0f}")
    
    # Análises por coluna (meses)
    vendas_por_mes = np.sum(vendas_matriz, axis=0)
    crescimento_mensal = np.diff(vendas_por_mes) / vendas_por_mes[:-1] * 100
    
    print(f"\n📅 ANÁLISE POR MÊS:")
    for i, mes in enumerate(meses):
        if i == 0:
            print(f"{mes}: R$ {vendas_por_mes[i]:,}")
        else:
            print(f"{mes}: R$ {vendas_por_mes[i]:,} ({crescimento_mensal[i-1]:+.1f}%)")
    
    # Produto e mês com melhor performance
    produto_idx, mes_idx = np.unravel_index(np.argmax(vendas_matriz), vendas_matriz.shape)
    melhor_venda = vendas_matriz[produto_idx, mes_idx]
    
    print(f"\n🏆 MELHOR PERFORMANCE:")
    print(f"{produtos[produto_idx]} em {meses[mes_idx]}: R$ {melhor_venda:,}")

def indexacao_slicing():
    """
    Indexação e fatiamento de arrays
    """
    print(f"\n🔍 INDEXAÇÃO E FATIAMENTO")
    print("="*40)
    
    # Array de temperaturas por dia
    temperaturas = np.array([22.5, 24.0, 23.8, 25.2, 26.1, 24.9, 23.3, 22.8, 24.5, 25.8])
    dias = np.arange(1, 11)
    
    print(f"🌡️ TEMPERATURAS DIÁRIAS (°C)")
    print("-" * 30)
    print(f"Todas: {temperaturas}")
    
    # Indexação simples
    print(f"\nPrimeiro dia: {temperaturas[0]}°C")
    print(f"Último dia: {temperaturas[-1]}°C")
    print(f"Quinto dia: {temperaturas[4]}°C")
    
    # Fatiamento
    primeira_semana = temperaturas[:7]
    segunda_metade = temperaturas[5:]
    dias_alternados = temperaturas[::2]
    
    print(f"\n📅 ANÁLISES POR PERÍODO:")
    print(f"Primeira semana: {primeira_semana}")
    print(f"Média primeira semana: {np.mean(primeira_semana):.1f}°C")
    print(f"Segunda metade: {segunda_metade}")
    print(f"Média segunda metade: {np.mean(segunda_metade):.1f}°C")
    print(f"Dias alternados: {dias_alternados}")
    
    # Indexação booleana
    dias_quentes = temperaturas > 24.0
    temp_quentes = temperaturas[dias_quentes]
    dias_quentes_nums = dias[dias_quentes]
    
    print(f"\n🔥 DIAS QUENTES (>24°C):")
    print(f"Dias: {dias_quentes_nums}")
    print(f"Temperaturas: {temp_quentes}")
    print(f"Quantidade: {len(temp_quentes)} dias")
    
    # Condições múltiplas
    dias_ideais = (temperaturas >= 23.0) & (temperaturas <= 25.0)
    temp_ideais = temperaturas[dias_ideais]
    
    print(f"\n🌞 DIAS IDEAIS (23-25°C):")
    print(f"Temperaturas: {temp_ideais}")
    print(f"Quantidade: {len(temp_ideais)} dias")

def simulacao_dados_sensor():
    """
    Simulação de análise de dados de sensores IoT
    """
    print(f"\n🌐 SIMULAÇÃO: DADOS DE SENSORES IOT")
    print("="*45)
    
    # Simular 24 horas de dados (1 leitura por hora)
    np.random.seed(42)  # Para reprodutibilidade
    
    horas = np.arange(24)
    
    # Temperatura com padrão diário
    temp_base = 20 + 5 * np.sin(2 * np.pi * horas / 24)  # Ciclo diário
    temperatura = temp_base + np.random.normal(0, 1, 24)  # Adicionar ruído
    
    # Umidade inversamente relacionada à temperatura
    umidade = 70 - (temperatura - 20) * 2 + np.random.normal(0, 3, 24)
    umidade = np.clip(umidade, 30, 90)  # Limitar entre 30-90%
    
    # Pressão com variação aleatória
    pressao = 1013 + np.random.normal(0, 5, 24)
    
    print(f"📊 DADOS COLETADOS (24 horas)")
    print("-" * 30)
    print(f"Temperatura: {temperatura.round(1)}")
    print(f"Umidade: {umidade.round(1)}")
    print(f"Pressão: {pressao.round(1)}")
    
    # Análises estatísticas
    print(f"\n📈 ANÁLISES ESTATÍSTICAS")
    print("-" * 30)
    
    dados_consolidados = np.array([
        ['Temperatura', np.mean(temperatura), np.std(temperatura), np.min(temperatura), np.max(temperatura)],
        ['Umidade', np.mean(umidade), np.std(umidade), np.min(umidade), np.max(umidade)],
        ['Pressão', np.mean(pressao), np.std(pressao), np.min(pressao), np.max(pressao)]
    ])
    
    for i, (sensor, media, desvio, minimo, maximo) in enumerate(dados_consolidados):
        print(f"{sensor}:")
        print(f"  Média: {float(media):.1f} | Desvio: {float(desvio):.1f}")
        print(f"  Min: {float(minimo):.1f} | Max: {float(maximo):.1f}")
    
    # Detectar anomalias (valores fora de 2 desvios padrão)
    print(f"\n🚨 DETECÇÃO DE ANOMALIAS")
    print("-" * 30)
    
    def detectar_anomalias(dados, nome_sensor):
        media = np.mean(dados)
        desvio = np.std(dados)
        limite_inf = media - 2 * desvio
        limite_sup = media + 2 * desvio
        
        anomalias = (dados < limite_inf) | (dados > limite_sup)
        horas_anomalas = horas[anomalias]
        valores_anomalos = dados[anomalias]
        
        if len(horas_anomalas) > 0:
            print(f"{nome_sensor}: {len(horas_anomalas)} anomalia(s)")
            for hora, valor in zip(horas_anomalas, valores_anomalos):
                print(f"  Hora {hora:02d}h: {valor:.1f}")
        else:
            print(f"{nome_sensor}: Nenhuma anomalia detectada")
    
    detectar_anomalias(temperatura, "Temperatura")
    detectar_anomalias(umidade, "Umidade")
    detectar_anomalias(pressao, "Pressão")
    
    # Correlação entre sensores
    correlacao_temp_umidade = np.corrcoef(temperatura, umidade)[0, 1]
    print(f"\n🔗 CORRELAÇÃO TEMPERATURA-UMIDADE: {correlacao_temp_umidade:.3f}")
    
    if abs(correlacao_temp_umidade) > 0.5:
        tipo_corr = "forte" if abs(correlacao_temp_umidade) > 0.7 else "moderada"
        sinal = "negativa" if correlacao_temp_umidade < 0 else "positiva"
        print(f"Correlação {tipo_corr} {sinal} detectada!")

def visualizacao_numpy():
    """
    Criando visualizações simples com dados NumPy
    """
    print(f"\n📊 VISUALIZAÇÕES COM NUMPY E MATPLOTLIB")
    print("="*50)
    
    # Dados de vendas anuais
    meses = np.arange(1, 13)
    vendas = np.array([15, 18, 22, 25, 28, 32, 35, 33, 30, 27, 24, 38]) * 1000
    
    # Criar figura com subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Análise de Dados com NumPy', fontsize=16, fontweight='bold')
    
    # 1. Gráfico de linha - Vendas mensais
    axes[0, 0].plot(meses, vendas, marker='o', linewidth=2, color='blue')
    axes[0, 0].set_title('Vendas Mensais')
    axes[0, 0].set_xlabel('Mês')
    axes[0, 0].set_ylabel('Vendas (R$)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Histograma - Distribuição de vendas
    axes[0, 1].hist(vendas, bins=8, color='green', alpha=0.7, edgecolor='black')
    axes[0, 1].set_title('Distribuição de Vendas')
    axes[0, 1].set_xlabel('Faixa de Vendas (R$)')
    axes[0, 1].set_ylabel('Frequência')
    
    # 3. Gráfico de barras - Comparação trimestral
    trimestres = ['Q1', 'Q2', 'Q3', 'Q4']
    vendas_trimestre = [np.sum(vendas[i:i+3]) for i in range(0, 12, 3)]
    
    axes[1, 0].bar(trimestres, vendas_trimestre, color=['red', 'orange', 'yellow', 'purple'])
    axes[1, 0].set_title('Vendas por Trimestre')
    axes[1, 0].set_ylabel('Vendas (R$)')
    
    # 4. Gráfico de pizza - Participação trimestral
    axes[1, 1].pie(vendas_trimestre, labels=trimestres, autopct='%1.1f%%', startangle=90)
    axes[1, 1].set_title('Participação por Trimestre')
    
    plt.tight_layout()
    plt.savefig('numpy_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Gráfico salvo como 'numpy_analysis.png'")

def main():
    """
    Função principal executando todos os conceitos de NumPy
    """
    print("🎓 AULA 04 - INTRODUÇÃO AO NUMPY")
    print("👨‍🏫 Professor: Vagner Cordeiro")
    print("="*50)
    
    print("\n🎯 OBJETIVOS:")
    print("✅ Entender por que NumPy é essencial")
    print("✅ Dominar arrays e operações básicas")
    print("✅ Trabalhar com arrays multidimensionais")
    print("✅ Aplicar em cenários de análise de dados")
    
    # Executar todas as seções
    introducao_numpy()
    arrays_basicos()
    operacoes_matematicas()
    arrays_multidimensionais()
    indexacao_slicing()
    simulacao_dados_sensor()
    visualizacao_numpy()
    
    print(f"\n🎯 RESUMO DA AULA:")
    print(f"✅ NumPy é muito mais rápido que Python puro")
    print(f"✅ Arrays são a base para análise de dados")
    print(f"✅ Operações vetorizadas são eficientes")
    print(f"✅ Arrays multidimensionais organizam dados complexos")
    print(f"✅ Indexação booleana filtra dados facilmente")
    print(f"✅ NumPy é fundamental para Big Data")
    
    print(f"\n💡 PONTOS IMPORTANTES:")
    print(f"🔹 Use NumPy para cálculos matemáticos")
    print(f"🔹 Arrays são mais eficientes que listas")
    print(f"🔹 Operações vetorizadas evitam loops")
    print(f"🔹 NumPy é base para Pandas e outras bibliotecas")
    print(f"🔹 Essential para Machine Learning e Big Data")

if __name__ == "__main__":
    main()
