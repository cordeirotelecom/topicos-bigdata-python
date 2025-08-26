"""
Aula 04 - Python Básico para Análise de Dados
Professor: Vagner Cordeiro

Revisão completa de Python com foco em análise de dados
"""

import math
import random
from datetime import datetime, timedelta
from collections import Counter, defaultdict
import statistics

def revisar_tipos_dados():
    """
    Revisão de tipos de dados fundamentais para análise
    """
    print("🐍 PYTHON BÁSICO - TIPOS DE DADOS PARA ANÁLISE")
    print("="*50)
    
    # Números e operações matemáticas
    print("🔢 1. NÚMEROS E OPERAÇÕES")
    print("-" * 30)
    
    vendas = [1500.50, 2300.75, 1800.00, 2100.25, 1950.80]
    
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    maior_venda = max(vendas)
    menor_venda = min(vendas)
    
    print(f"📊 Vendas: {vendas}")
    print(f"💰 Total: R$ {total_vendas:,.2f}")
    print(f"📈 Média: R$ {media_vendas:,.2f}")
    print(f"🔝 Maior: R$ {maior_venda:,.2f}")
    print(f"🔻 Menor: R$ {menor_venda:,.2f}")
    
    # Strings para dados textuais
    print(f"\n📝 2. STRINGS E DADOS TEXTUAIS")
    print("-" * 30)
    
    comentarios = [
        "Excelente produto! Recomendo",
        "Qualidade boa, mas caro",
        "Entrega rápida, produto conforme",
        "Não gostei, vou devolver"
    ]
    
    # Análise básica de texto
    total_chars = sum(len(comentario) for comentario in comentarios)
    media_chars = total_chars / len(comentarios)
    
    # Contar palavras positivas/negativas
    palavras_positivas = ['excelente', 'bom', 'boa', 'recomendo', 'rápida']
    palavras_negativas = ['não', 'caro', 'devolver']
    
    sentimento_score = 0
    for comentario in comentarios:
        comentario_lower = comentario.lower()
        for palavra in palavras_positivas:
            if palavra in comentario_lower:
                sentimento_score += 1
        for palavra in palavras_negativas:
            if palavra in comentario_lower:
                sentimento_score -= 1
    
    print(f"💬 Comentários analisados: {len(comentarios)}")
    print(f"📏 Média de caracteres: {media_chars:.1f}")
    print(f"😊 Score de sentimento: {sentimento_score}")
    
    # Booleanos para flags e condições
    print(f"\n✅ 3. BOOLEANOS E CONDIÇÕES")
    print("-" * 30)
    
    cliente_premium = True
    desconto_ativo = False
    valor_compra = 1500.00
    
    # Lógica de desconto
    desconto = 0
    if cliente_premium and valor_compra > 1000:
        desconto = 0.15  # 15%
    elif valor_compra > 500:
        desconto = 0.05  # 5%
    
    valor_final = valor_compra * (1 - desconto)
    
    print(f"👤 Cliente Premium: {cliente_premium}")
    print(f"🏷️ Desconto ativo: {desconto_ativo}")
    print(f"💰 Valor original: R$ {valor_compra:,.2f}")
    print(f"🎯 Desconto aplicado: {desconto*100:.0f}%")
    print(f"💳 Valor final: R$ {valor_final:,.2f}")

def trabalhar_listas_dados():
    """
    Trabalhando com listas para análise de dados
    """
    print(f"\n📋 LISTAS PARA ANÁLISE DE DADOS")
    print("="*50)
    
    # Dados de vendas por mês
    vendas_mensais = [15000, 18000, 22000, 19000, 25000, 21000, 
                     23000, 26000, 24000, 28000, 30000, 35000]
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
             'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    
    print("📈 ANÁLISE DE VENDAS ANUAIS")
    print("-" * 30)
    
    # Operações básicas
    total_ano = sum(vendas_mensais)
    media_mensal = total_ano / 12
    crescimento = ((vendas_mensais[-1] - vendas_mensais[0]) / vendas_mensais[0]) * 100
    
    print(f"💰 Total do ano: R$ {total_ano:,}")
    print(f"📊 Média mensal: R$ {media_mensal:,.0f}")
    print(f"📈 Crescimento anual: {crescimento:.1f}%")
    
    # Encontrar melhor e pior mês
    melhor_mes_idx = vendas_mensais.index(max(vendas_mensais))
    pior_mes_idx = vendas_mensais.index(min(vendas_mensais))
    
    print(f"🏆 Melhor mês: {meses[melhor_mes_idx]} (R$ {vendas_mensais[melhor_mes_idx]:,})")
    print(f"📉 Pior mês: {meses[pior_mes_idx]} (R$ {vendas_mensais[pior_mes_idx]:,})")
    
    # List comprehensions para análise
    print(f"\n🔍 ANÁLISES COM LIST COMPREHENSIONS")
    print("-" * 30)
    
    # Meses acima da média
    meses_acima_media = [meses[i] for i, venda in enumerate(vendas_mensais) 
                        if venda > media_mensal]
    
    # Crescimento mês a mês
    crescimento_mensal = [(vendas_mensais[i] - vendas_mensais[i-1]) / vendas_mensais[i-1] * 100 
                         for i in range(1, len(vendas_mensais))]
    
    # Trimestres
    trimestres = [sum(vendas_mensais[i:i+3]) for i in range(0, 12, 3)]
    nomes_trimestres = ['Q1', 'Q2', 'Q3', 'Q4']
    
    print(f"📊 Meses acima da média: {', '.join(meses_acima_media)}")
    print(f"📈 Maior crescimento mensal: {max(crescimento_mensal):.1f}%")
    
    print(f"\n📅 VENDAS POR TRIMESTRE:")
    for i, (nome, valor) in enumerate(zip(nomes_trimestres, trimestres)):
        print(f"   {nome}: R$ {valor:,}")

def usar_dicionarios_dados():
    """
    Usando dicionários para estruturar dados
    """
    print(f"\n🗂️ DICIONÁRIOS PARA DADOS ESTRUTURADOS")
    print("="*50)
    
    # Base de clientes
    clientes = {
        'C001': {
            'nome': 'Ana Silva',
            'idade': 28,
            'cidade': 'São Paulo',
            'compras': [1500, 2200, 1800],
            'categoria': 'Premium'
        },
        'C002': {
            'nome': 'João Santos',
            'idade': 35,
            'cidade': 'Rio de Janeiro',
            'compras': [800, 1200],
            'categoria': 'Regular'
        },
        'C003': {
            'nome': 'Maria Oliveira',
            'idade': 42,
            'cidade': 'Belo Horizonte',
            'compras': [3000, 2500, 4000, 1500],
            'categoria': 'VIP'
        }
    }
    
    print("👥 ANÁLISE DE CLIENTES")
    print("-" * 30)
    
    # Análises usando dicionários
    total_clientes = len(clientes)
    idade_media = sum(cliente['idade'] for cliente in clientes.values()) / total_clientes
    
    # Análise por categoria
    categorias = defaultdict(int)
    total_vendas_categoria = defaultdict(float)
    
    for cliente_id, dados in clientes.items():
        categoria = dados['categoria']
        total_compras = sum(dados['compras'])
        
        categorias[categoria] += 1
        total_vendas_categoria[categoria] += total_compras
        
        print(f"🆔 {cliente_id}: {dados['nome']}")
        print(f"   📍 {dados['cidade']} | 🎂 {dados['idade']} anos")
        print(f"   💰 Total gasto: R$ {total_compras:,.2f}")
        print(f"   🏷️ Categoria: {categoria}")
        print()
    
    print("📊 RESUMO POR CATEGORIA:")
    for categoria, count in categorias.items():
        vendas_cat = total_vendas_categoria[categoria]
        media_cat = vendas_cat / count
        print(f"   {categoria}: {count} clientes | R$ {vendas_cat:,.2f} | Média: R$ {media_cat:,.2f}")
    
    # Análise geográfica
    cidades = Counter(cliente['cidade'] for cliente in clientes.values())
    print(f"\n🗺️ DISTRIBUIÇÃO GEOGRÁFICA:")
    for cidade, count in cidades.most_common():
        print(f"   {cidade}: {count} cliente(s)")

def funcoes_para_analise():
    """
    Criando funções reutilizáveis para análise de dados
    """
    print(f"\n⚙️ FUNÇÕES PARA ANÁLISE DE DADOS")
    print("="*50)
    
    def calcular_estatisticas(dados, nome_dataset="Dataset"):
        """
        Calcula estatísticas básicas de uma lista de números
        """
        if not dados:
            return {"erro": "Dataset vazio"}
        
        resultado = {
            'nome': nome_dataset,
            'count': len(dados),
            'soma': sum(dados),
            'media': sum(dados) / len(dados),
            'mediana': statistics.median(dados),
            'minimo': min(dados),
            'maximo': max(dados),
            'amplitude': max(dados) - min(dados),
            'desvio_padrao': statistics.stdev(dados) if len(dados) > 1 else 0
        }
        
        return resultado
    
    def analisar_crescimento(valores, periodos):
        """
        Analisa crescimento entre períodos
        """
        if len(valores) != len(periodos) or len(valores) < 2:
            return None
        
        crescimentos = []
        for i in range(1, len(valores)):
            crescimento = ((valores[i] - valores[i-1]) / valores[i-1]) * 100
            crescimentos.append({
                'periodo': f"{periodos[i-1]} → {periodos[i]}",
                'valor_anterior': valores[i-1],
                'valor_atual': valores[i],
                'crescimento_pct': crescimento,
                'crescimento_abs': valores[i] - valores[i-1]
            })
        
        return crescimentos
    
    def classificar_performance(valor, benchmarks):
        """
        Classifica performance baseada em benchmarks
        """
        if valor >= benchmarks['excelente']:
            return 'Excelente'
        elif valor >= benchmarks['bom']:
            return 'Bom'
        elif valor >= benchmarks['regular']:
            return 'Regular'
        else:
            return 'Ruim'
    
    # Testando as funções
    print("🧪 TESTANDO FUNÇÕES DE ANÁLISE")
    print("-" * 30)
    
    # Dados de exemplo
    vendas_produto_a = [1200, 1350, 1180, 1420, 1580, 1650]
    vendas_produto_b = [800, 950, 1100, 1080, 1200, 1150]
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
    
    # Análise estatística
    stats_a = calcular_estatisticas(vendas_produto_a, "Produto A")
    stats_b = calcular_estatisticas(vendas_produto_b, "Produto B")
    
    print(f"📊 {stats_a['nome']}:")
    print(f"   Média: R$ {stats_a['media']:.2f} | Mediana: R$ {stats_a['mediana']:.2f}")
    print(f"   Min: R$ {stats_a['minimo']} | Max: R$ {stats_a['maximo']}")
    print(f"   Desvio Padrão: R$ {stats_a['desvio_padrao']:.2f}")
    
    print(f"\n📊 {stats_b['nome']}:")
    print(f"   Média: R$ {stats_b['media']:.2f} | Mediana: R$ {stats_b['mediana']:.2f}")
    print(f"   Min: R$ {stats_b['minimo']} | Max: R$ {stats_b['maximo']}")
    print(f"   Desvio Padrão: R$ {stats_b['desvio_padrao']:.2f}")
    
    # Análise de crescimento
    crescimento_a = analisar_crescimento(vendas_produto_a, meses)
    print(f"\n📈 CRESCIMENTO PRODUTO A:")
    if crescimento_a:
        for periodo in crescimento_a[-3:]:  # Últimos 3 períodos
            print(f"   {periodo['periodo']}: {periodo['crescimento_pct']:+.1f}%")
    else:
        print("   ⚠️ Dados insuficientes para análise de crescimento")
    
    # Classificação de performance
    benchmarks = {'excelente': 1500, 'bom': 1200, 'regular': 1000}
    
    print(f"\n🏆 CLASSIFICAÇÃO DE PERFORMANCE (último mês):")
    perf_a = classificar_performance(vendas_produto_a[-1], benchmarks)
    perf_b = classificar_performance(vendas_produto_b[-1], benchmarks)
    print(f"   Produto A: {perf_a} (R$ {vendas_produto_a[-1]})")
    print(f"   Produto B: {perf_b} (R$ {vendas_produto_b[-1]})")

def tratamento_erros_dados():
    """
    Tratamento de erros comum em análise de dados
    """
    print(f"\n🛡️ TRATAMENTO DE ERROS EM DADOS")
    print("="*50)
    
    # Dados com problemas comuns
    dados_com_problemas = [
        "1500.50",  # String que deveria ser número
        None,       # Valor nulo
        "abc",      # Texto inválido
        "2200.75",  # String válida
        "",         # String vazia
        "1800.00"   # String válida
    ]
    
    print("🔍 DADOS ORIGINAIS (com problemas):")
    print(dados_com_problemas)
    
    # Função para limpar e converter dados
    def limpar_dados_numericos(dados):
        """
        Limpa e converte dados para numérico, tratando erros
        """
        dados_limpos = []
        erros = []
        
        for i, valor in enumerate(dados):
            try:
                # Tentar converter para float
                if valor is None or valor == "":
                    erros.append(f"Posição {i}: Valor vazio/nulo")
                    continue
                
                # Converter string para número
                numero = float(str(valor).replace(',', '.'))
                dados_limpos.append(numero)
                
            except ValueError:
                erros.append(f"Posição {i}: '{valor}' não é um número válido")
            except Exception as e:
                erros.append(f"Posição {i}: Erro inesperado - {e}")
        
        return dados_limpos, erros
    
    # Limpar dados
    dados_limpos, erros_encontrados = limpar_dados_numericos(dados_com_problemas)
    
    print(f"\n✅ DADOS APÓS LIMPEZA:")
    print(dados_limpos)
    
    if erros_encontrados:
        print(f"\n⚠️ ERROS ENCONTRADOS:")
        for erro in erros_encontrados:
            print(f"   {erro}")
    
    # Estatísticas dos dados limpos
    if dados_limpos:
        print(f"\n📊 ESTATÍSTICAS DOS DADOS LIMPOS:")
        print(f"   Registros válidos: {len(dados_limpos)}")
        print(f"   Registros perdidos: {len(dados_com_problemas) - len(dados_limpos)}")
        print(f"   Taxa de sucesso: {len(dados_limpos)/len(dados_com_problemas)*100:.1f}%")
        print(f"   Soma: R$ {sum(dados_limpos):,.2f}")
        print(f"   Média: R$ {sum(dados_limpos)/len(dados_limpos):,.2f}")

def main():
    """
    Função principal executando todas as revisões
    """
    print("🎓 AULA 04 - REVISÃO DE PYTHON PARA ANÁLISE DE DADOS")
    print("👨‍🏫 Professor: Vagner Cordeiro")
    print("="*65)
    
    print("\n🎯 OBJETIVO: Revisar Python com foco em análise de dados")
    print("📚 TÓPICOS: Tipos, estruturas, funções e tratamento de erros")
    
    # Executar todas as seções
    revisar_tipos_dados()
    trabalhar_listas_dados()
    usar_dicionarios_dados()
    funcoes_para_analise()
    tratamento_erros_dados()
    
    print(f"\n🎯 RESUMO DA REVISÃO:")
    print(f"✅ Tipos de dados para análise")
    print(f"✅ Listas e list comprehensions")
    print(f"✅ Dicionários para dados estruturados")
    print(f"✅ Funções reutilizáveis")
    print(f"✅ Tratamento de erros em dados")
    
    print(f"\n💡 PRÓXIMOS PASSOS:")
    print(f"🔹 Praticar com datasets reais")
    print(f"🔹 Explorar NumPy para arrays")
    print(f"🔹 Dominar Pandas para DataFrames")
    print(f"🔹 Criar visualizações com Matplotlib")
    
    print(f"\n📚 PARA CASA:")
    print(f"✏️ Complete todos os exercícios práticos")
    print(f"✏️ Crie seu próprio mini-projeto de análise")
    print(f"✏️ Explore a documentação oficial do Python")

if __name__ == "__main__":
    main()
