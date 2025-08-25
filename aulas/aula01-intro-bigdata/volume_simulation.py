"""
Aula 01 - Big Data: Simulação de Volume de Dados
Professor: Vagner Cordeiro
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import time
import random

def gerar_dados_ecommerce(num_registros=1000000):
    """
    Gera um dataset simulado de e-commerce com grande volume
    
    Args:
        num_registros (int): Número de registros a gerar
    
    Returns:
        pandas.DataFrame: Dataset simulado
    """
    print(f"🚀 Gerando {num_registros:,} registros de e-commerce...")
    inicio = time.time()
    
    # Seed para reprodutibilidade
    np.random.seed(42)
    random.seed(42)
    
    # Produtos possíveis
    produtos = [
        'Smartphone', 'Laptop', 'Tablet', 'Fone de Ouvido', 'Smartwatch',
        'Câmera', 'Livro', 'Roupa', 'Sapato', 'Perfume', 'Jogo', 'Filme'
    ]
    
    # Categorias
    categorias = [
        'Eletrônicos', 'Informática', 'Livros', 'Moda', 'Casa', 'Esportes'
    ]
    
    # Cidades brasileiras
    cidades = [
        'São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador', 'Fortaleza',
        'Belo Horizonte', 'Manaus', 'Curitiba', 'Recife', 'Goiânia'
    ]
    
    # Gerando dados
    dados = {
        'id_transacao': range(1, num_registros + 1),
        'data_compra': [
            datetime.now() - timedelta(days=random.randint(0, 365))
            for _ in range(num_registros)
        ],
        'produto': np.random.choice(produtos, num_registros),
        'categoria': np.random.choice(categorias, num_registros),
        'preco': np.random.exponential(scale=100, size=num_registros).round(2),
        'quantidade': np.random.poisson(lam=2, size=num_registros) + 1,
        'cidade': np.random.choice(cidades, num_registros),
        'idade_cliente': np.random.normal(35, 12, num_registros).astype(int),
        'avaliacao': np.random.choice([1, 2, 3, 4, 5], num_registros, 
                                    p=[0.05, 0.10, 0.20, 0.35, 0.30])
    }
    
    # Criando DataFrame
    df = pd.DataFrame(dados)
    
    # Calculando valor total
    df['valor_total'] = df['preco'] * df['quantidade']
    
    # Limpeza de dados (idades inválidas)
    df = df[(df['idade_cliente'] >= 18) & (df['idade_cliente'] <= 80)]
    
    fim = time.time()
    print(f"✅ Dataset criado em {fim - inicio:.2f} segundos")
    print(f"📊 Shape final: {df.shape}")
    print(f"💾 Tamanho aproximado em memória: {df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
    
    return df

def analisar_volume_dados(df):
    """
    Realiza análises básicas demonstrando o conceito de Volume
    """
    print("\n" + "="*50)
    print("📈 ANÁLISE DE VOLUME DE DADOS")
    print("="*50)
    
    # Informações básicas
    print(f"📋 Número total de registros: {len(df):,}")
    print(f"📊 Número de colunas: {len(df.columns)}")
    print(f"💾 Uso de memória: {df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
    
    # Análise por categoria
    print(f"\n🏷️ Produtos por categoria:")
    categoria_counts = df['categoria'].value_counts()
    for categoria, count in categoria_counts.items():
        print(f"   {categoria}: {count:,} registros")
    
    # Análise temporal
    print(f"\n📅 Período dos dados:")
    print(f"   Data mais antiga: {df['data_compra'].min()}")
    print(f"   Data mais recente: {df['data_compra'].max()}")
    
    # Estatísticas financeiras
    print(f"\n💰 Estatísticas financeiras:")
    print(f"   Receita total: R$ {df['valor_total'].sum():,.2f}")
    print(f"   Ticket médio: R$ {df['valor_total'].mean():.2f}")
    print(f"   Maior venda: R$ {df['valor_total'].max():.2f}")

def demonstrar_processamento_lento_vs_rapido(df):
    """
    Demonstra diferenças de performance em processamento de dados
    """
    print("\n" + "="*50)
    print("⚡ DEMONSTRAÇÃO: PROCESSAMENTO LENTO vs RÁPIDO")
    print("="*50)
    
    # Método LENTO: Loop Python tradicional
    print("🐌 Método LENTO - Loop Python:")
    inicio = time.time()
    
    total_lento = 0
    for _, row in df.head(10000).iterrows():  # Apenas 10k para não demorar muito
        total_lento += row['valor_total']
    
    fim = time.time()
    tempo_lento = fim - inicio
    print(f"   Resultado: R$ {total_lento:,.2f}")
    print(f"   Tempo: {tempo_lento:.4f} segundos")
    
    # Método RÁPIDO: Pandas vetorizado
    print("\n🚀 Método RÁPIDO - Pandas vetorizado:")
    inicio = time.time()
    
    total_rapido = df['valor_total'].sum()
    
    fim = time.time()
    tempo_rapido = fim - inicio
    print(f"   Resultado: R$ {total_rapido:,.2f}")
    print(f"   Tempo: {tempo_rapido:.4f} segundos")
    
    # Comparação
    if tempo_lento > 0:
        speedup = tempo_lento / tempo_rapido
        print(f"\n📊 Pandas é {speedup:.1f}x mais rápido!")

def criar_visualizacoes(df):
    """
    Cria visualizações para demonstrar insights dos dados
    """
    print("\n" + "="*50)
    print("📊 CRIANDO VISUALIZAÇÕES")
    print("="*50)
    
    # Configurar estilo
    plt.style.use('seaborn-v0_8')
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Análise de Big Data - E-commerce', fontsize=16, fontweight='bold')
    
    # 1. Vendas por categoria
    categoria_vendas = df.groupby('categoria')['valor_total'].sum().sort_values(ascending=False)
    axes[0, 0].bar(categoria_vendas.index, categoria_vendas.values)
    axes[0, 0].set_title('Receita por Categoria')
    axes[0, 0].set_ylabel('Receita (R$)')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Distribuição de idades
    axes[0, 1].hist(df['idade_cliente'], bins=30, alpha=0.7, color='skyblue')
    axes[0, 1].set_title('Distribuição de Idade dos Clientes')
    axes[0, 1].set_xlabel('Idade')
    axes[0, 1].set_ylabel('Frequência')
    
    # 3. Vendas por cidade
    cidade_vendas = df.groupby('cidade')['valor_total'].sum().sort_values(ascending=False).head(5)
    axes[1, 0].barh(cidade_vendas.index, cidade_vendas.values)
    axes[1, 0].set_title('Top 5 Cidades por Receita')
    axes[1, 0].set_xlabel('Receita (R$)')
    
    # 4. Avaliações
    avaliacoes = df['avaliacao'].value_counts().sort_index()
    axes[1, 1].pie(avaliacoes.values, labels=avaliacoes.index, autopct='%1.1f%%')
    axes[1, 1].set_title('Distribuição de Avaliações')
    
    plt.tight_layout()
    plt.savefig('analise_bigdata_volume.png', dpi=300, bbox_inches='tight')
    print("✅ Gráficos salvos em 'analise_bigdata_volume.png'")
    plt.show()

def main():
    """
    Função principal demonstrando conceitos de Volume em Big Data
    """
    print("🎓 AULA 01 - BIG DATA: CONCEITO DE VOLUME")
    print("👨‍🏫 Professor: Vagner Cordeiro")
    print("="*60)
    
    # Permitir que o usuário escolha o tamanho do dataset
    print("\n📊 Escolha o tamanho do dataset para demonstração:")
    print("1. Pequeno (10.000 registros) - Rápido")
    print("2. Médio (100.000 registros) - Moderado")
    print("3. Grande (1.000.000 registros) - Lento")
    
    escolha = input("\nDigite sua escolha (1-3): ").strip()
    
    tamanhos = {'1': 10000, '2': 100000, '3': 1000000}
    num_registros = tamanhos.get(escolha, 10000)
    
    # Gerar dados
    df_ecommerce = gerar_dados_ecommerce(num_registros)
    
    # Análises
    analisar_volume_dados(df_ecommerce)
    demonstrar_processamento_lento_vs_rapido(df_ecommerce)
    
    # Salvar dados para próximas aulas
    print(f"\n💾 Salvando dados...")
    df_ecommerce.to_csv('dados_ecommerce.csv', index=False)
    print(f"✅ Dados salvos em 'dados_ecommerce.csv'")
    
    # Criar visualizações
    criar_visualizacoes(df_ecommerce.head(10000))  # Limitar para visualização
    
    print(f"\n🎯 RESUMO DA AULA:")
    print(f"✅ Geramos {num_registros:,} registros simulados")
    print(f"✅ Demonstramos o conceito de VOLUME")
    print(f"✅ Comparamos métodos de processamento")
    print(f"✅ Criamos visualizações dos dados")
    print(f"✅ Aprendemos pandas na prática!")

if __name__ == "__main__":
    main()
