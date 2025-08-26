#!/usr/bin/env python3
"""
Aula 05: Pipeline Simples de Análise de Dados
Professor: Vagner Cordeiro
Curso: Tópicos de Big Data em Python

Versão SIMPLIFICADA sem problemas de tipos - FUNCIONAL 100%
"""

import random
import json
from datetime import datetime

# Verificação de bibliotecas
HAS_PANDAS = False
HAS_NUMPY = False
HAS_MATPLOTLIB = False

try:
    import pandas as pd
    HAS_PANDAS = True
    print("✅ Pandas disponível")
except ImportError:
    print("📊 Pandas não disponível - usando simulação")

try:
    import numpy as np
    HAS_NUMPY = True
    print("✅ NumPy disponível")
except ImportError:
    print("📊 NumPy não disponível - usando simulação")

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
    print("✅ Matplotlib disponível")
except ImportError:
    print("📊 Matplotlib não disponível - usando simulação")

# Simulador de dados simples
def gerar_dados_vendas(num_registros=1000):
    """Gera dados simulados de vendas de forma simples"""
    print(f"🏭 Gerando {num_registros} registros de dados de vendas...")
    
    dados = []
    produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Webcam"]
    categorias = ["Eletrônicos", "Informática", "Periféricos"]
    regioes = ["Norte", "Sul", "Leste", "Oeste", "Centro"]
    
    for i in range(num_registros):
        registro = {
            'id': i + 1,
            'produto': random.choice(produtos),
            'categoria': random.choice(categorias),
            'preco': round(random.uniform(50, 2000), 2),
            'quantidade': random.randint(1, 10),
            'desconto': round(random.uniform(0, 0.3), 2),
            'regiao': random.choice(regioes),
            'vendedor_id': random.randint(1, 50),
            'data_venda': f"2024-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
            'satisfacao': round(random.uniform(1, 5), 1)
        }
        
        # Calcular valor total
        registro['valor_total'] = round(
            registro['preco'] * registro['quantidade'] * (1 - registro['desconto']), 2
        )
        
        # Adicionar alguns valores nulos (5% dos dados)
        if random.random() < 0.05:
            campo_nulo = random.choice(['satisfacao', 'desconto'])
            registro[campo_nulo] = None
            
        dados.append(registro)
    
    print(f"✅ {len(dados)} registros gerados com sucesso!")
    return dados

def analisar_dados_simples(dados):
    """Análise simples dos dados sem dependências complexas"""
    print("\n📊 INICIANDO ANÁLISE DOS DADOS")
    print("=" * 50)
    
    total_registros = len(dados)
    print(f"📈 Total de registros: {total_registros}")
    
    # Análise de vendas por produto
    vendas_por_produto = {}
    vendas_por_regiao = {}
    valores_totais = []
    valores_nao_nulos = []
    
    for registro in dados:
        produto = registro['produto']
        regiao = registro['regiao']
        valor = registro['valor_total']
        
        # Contagem por produto
        if produto in vendas_por_produto:
            vendas_por_produto[produto] += 1
        else:
            vendas_por_produto[produto] = 1
            
        # Contagem por região
        if regiao in vendas_por_regiao:
            vendas_por_regiao[regiao] += 1
        else:
            vendas_por_regiao[regiao] = 1
            
        # Coleta de valores
        valores_totais.append(valor)
        if registro['satisfacao'] is not None:
            valores_nao_nulos.append(registro['satisfacao'])
    
    # Estatísticas básicas
    if valores_totais:
        valor_medio = sum(valores_totais) / len(valores_totais)
        valor_maximo = max(valores_totais)
        valor_minimo = min(valores_totais)
        
        print(f"\n💰 ANÁLISE FINANCEIRA:")
        print(f"   💵 Valor médio por venda: R$ {valor_medio:.2f}")
        print(f"   📈 Maior venda: R$ {valor_maximo:.2f}")
        print(f"   📉 Menor venda: R$ {valor_minimo:.2f}")
        print(f"   💸 Receita total: R$ {sum(valores_totais):.2f}")
    
    # Análise por produto
    print(f"\n🛍️ VENDAS POR PRODUTO:")
    for produto, count in sorted(vendas_por_produto.items(), key=lambda x: x[1], reverse=True):
        percentual = (count / total_registros) * 100
        print(f"   📦 {produto}: {count} vendas ({percentual:.1f}%)")
    
    # Análise por região
    print(f"\n🌍 VENDAS POR REGIÃO:")
    for regiao, count in sorted(vendas_por_regiao.items(), key=lambda x: x[1], reverse=True):
        percentual = (count / total_registros) * 100
        print(f"   📍 {regiao}: {count} vendas ({percentual:.1f}%)")
    
    # Análise de satisfação
    if valores_nao_nulos:
        satisfacao_media = sum(valores_nao_nulos) / len(valores_nao_nulos)
        print(f"\n⭐ SATISFAÇÃO DO CLIENTE:")
        print(f"   😊 Satisfação média: {satisfacao_media:.2f}/5.0")
        print(f"   📊 Respostas válidas: {len(valores_nao_nulos)}/{total_registros}")
    
    return {
        'total_registros': total_registros,
        'vendas_por_produto': vendas_por_produto,
        'vendas_por_regiao': vendas_por_regiao,
        'valor_medio': valor_medio if valores_totais else 0,
        'receita_total': sum(valores_totais) if valores_totais else 0
    }

def limpeza_dados_simples(dados):
    """Limpeza básica dos dados"""
    print("\n🧹 LIMPEZA DOS DADOS")
    print("=" * 30)
    
    registros_originais = len(dados)
    dados_limpos = []
    
    registros_com_problemas = 0
    
    for registro in dados:
        # Verificar se tem dados essenciais
        if (registro.get('preco', 0) > 0 and 
            registro.get('quantidade', 0) > 0 and
            registro.get('produto') and
            registro.get('regiao')):
            
            # Tratar valores nulos
            if registro.get('satisfacao') is None:
                registro['satisfacao'] = 3.0  # Valor padrão neutro
            
            if registro.get('desconto') is None:
                registro['desconto'] = 0.0  # Sem desconto por padrão
            
            dados_limpos.append(registro)
        else:
            registros_com_problemas += 1
    
    print(f"   📊 Registros originais: {registros_originais}")
    print(f"   🗑️ Registros com problemas: {registros_com_problemas}")
    print(f"   ✅ Registros limpos: {len(dados_limpos)}")
    print(f"   📈 Taxa de aproveitamento: {(len(dados_limpos)/registros_originais)*100:.1f}%")
    
    return dados_limpos

def detectar_outliers_simples(dados):
    """Detecção simples de outliers"""
    print("\n🔍 DETECÇÃO DE OUTLIERS")
    print("=" * 30)
    
    valores = [registro['valor_total'] for registro in dados]
    
    if len(valores) < 4:
        print("   ⚠️ Dados insuficientes para análise de outliers")
        return dados
    
    # Método simples: valores muito acima da média
    valores_ordenados = sorted(valores)
    q1_index = len(valores_ordenados) // 4
    q3_index = 3 * len(valores_ordenados) // 4
    
    q1 = valores_ordenados[q1_index]
    q3 = valores_ordenados[q3_index]
    iqr = q3 - q1
    
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    
    outliers = []
    dados_sem_outliers = []
    
    for registro in dados:
        valor = registro['valor_total']
        if limite_inferior <= valor <= limite_superior:
            dados_sem_outliers.append(registro)
        else:
            outliers.append(registro)
    
    print(f"   📊 Q1 (25%): R$ {q1:.2f}")
    print(f"   📊 Q3 (75%): R$ {q3:.2f}")
    print(f"   📏 IQR: R$ {iqr:.2f}")
    print(f"   📉 Limite inferior: R$ {limite_inferior:.2f}")
    print(f"   📈 Limite superior: R$ {limite_superior:.2f}")
    print(f"   ⚠️ Outliers detectados: {len(outliers)}")
    print(f"   ✅ Registros mantidos: {len(dados_sem_outliers)}")
    
    return dados_sem_outliers

def gerar_insights_simples(resultados):
    """Gera insights simples baseados nos resultados"""
    print("\n💡 INSIGHTS E RECOMENDAÇÕES")
    print("=" * 40)
    
    # Produto mais vendido
    produto_top = max(resultados['vendas_por_produto'].items(), key=lambda x: x[1])
    print(f"🏆 Produto campeão: {produto_top[0]} ({produto_top[1]} vendas)")
    
    # Região mais forte
    regiao_top = max(resultados['vendas_por_regiao'].items(), key=lambda x: x[1])
    print(f"🌟 Região líder: {regiao_top[0]} ({regiao_top[1]} vendas)")
    
    # Análise de receita
    if resultados['receita_total'] > 0:
        print(f"💰 Ticket médio: R$ {resultados['valor_medio']:.2f}")
        
        if resultados['valor_medio'] > 500:
            print("   💡 Alto valor médio - foque em produtos premium")
        elif resultados['valor_medio'] < 200:
            print("   💡 Baixo valor médio - oportunidade para upselling")
        else:
            print("   💡 Valor médio equilibrado - mantenha estratégia")
    
    # Distribuição de produtos
    total_vendas = sum(resultados['vendas_por_produto'].values())
    produtos_concentrados = 0
    
    for produto, vendas in resultados['vendas_por_produto'].items():
        if vendas / total_vendas > 0.3:  # Mais de 30%
            produtos_concentrados += 1
    
    if produtos_concentrados > 0:
        print("   ⚠️ Concentração alta em poucos produtos - diversifique!")
    else:
        print("   ✅ Boa distribuição de vendas entre produtos")

def salvar_resultados(resultados):
    """Salva resultados em arquivo JSON"""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"analise_vendas_{timestamp}.json"
        
        # Preparar dados para JSON
        dados_para_salvar = {
            'timestamp': timestamp,
            'analise': resultados,
            'metadata': {
                'total_registros': resultados['total_registros'],
                'bibliotecas_usadas': {
                    'pandas': HAS_PANDAS,
                    'numpy': HAS_NUMPY,
                    'matplotlib': HAS_MATPLOTLIB
                }
            }
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dados_para_salvar, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Resultados salvos em: {filename}")
        return filename
        
    except Exception as e:
        print(f"\n❌ Erro ao salvar: {e}")
        return None

def pipeline_completo_simples():
    """Executa o pipeline completo de forma simples e robusta"""
    print("🚀 PIPELINE SIMPLES DE ANÁLISE DE DADOS")
    print("=" * 60)
    print("✨ Versão simplificada - 100% funcional")
    print("=" * 60)
    
    try:
        # 1. Geração de dados
        dados_brutos = gerar_dados_vendas(1000)
        
        # 2. Limpeza
        dados_limpos = limpeza_dados_simples(dados_brutos)
        
        # 3. Remoção de outliers
        dados_finais = detectar_outliers_simples(dados_limpos)
        
        # 4. Análise
        resultados = analisar_dados_simples(dados_finais)
        
        # 5. Insights
        gerar_insights_simples(resultados)
        
        # 6. Salvar resultados
        salvar_resultados(resultados)
        
        print("\n🎉 PIPELINE EXECUTADO COM SUCESSO!")
        print("=" * 50)
        print("📊 Resumo da execução:")
        print(f"   📈 Registros processados: {resultados['total_registros']}")
        print(f"   💰 Receita analisada: R$ {resultados['receita_total']:.2f}")
        print(f"   🛍️ Produtos únicos: {len(resultados['vendas_por_produto'])}")
        print(f"   🌍 Regiões analisadas: {len(resultados['vendas_por_regiao'])}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERRO NO PIPELINE: {e}")
        print("⚠️ Pipeline interrompido, mas operações parciais podem ter sido realizadas.")
        return False

# Conceitos educacionais
def mostrar_conceitos():
    """Mostra conceitos fundamentais de análise de dados"""
    print("\n📚 CONCEITOS FUNDAMENTAIS DE ANÁLISE DE DADOS")
    print("=" * 60)
    
    conceitos = {
        "📊 Exploração de Dados (EDA)": [
            "Entender a estrutura e qualidade dos dados",
            "Identificar padrões, tendências e anomalias",
            "Calcular estatísticas descritivas básicas",
            "Visualizar distribuições e relacionamentos"
        ],
        "🧹 Limpeza de Dados": [
            "Identificar e tratar valores nulos/ausentes",
            "Detectar e remover outliers quando apropriado",
            "Padronizar formatos e encoding",
            "Validar consistência e integridade"
        ],
        "📈 Análise Estatística": [
            "Medidas de tendência central (média, mediana)",
            "Medidas de dispersão (desvio padrão, variância)",
            "Análise de correlações entre variáveis",
            "Distribuições e testes de normalidade"
        ],
        "💡 Geração de Insights": [
            "Identificar padrões de negócio relevantes",
            "Formular hipóteses baseadas em dados",
            "Propor ações baseadas em evidências",
            "Comunicar resultados de forma clara"
        ]
    }
    
    for categoria, itens in conceitos.items():
        print(f"\n{categoria}")
        for item in itens:
            print(f"   • {item}")

def main():
    """Função principal"""
    print("🎯 AULA 05: Pipeline Completo de Análise de Dados")
    print("Autor: Professor Vagner Cordeiro")
    print("=" * 60)
    
    # Mostrar conceitos
    mostrar_conceitos()
    
    # Executar pipeline
    print(f"\n🎓 DEMONSTRAÇÃO: Pipeline de Análise de Dados")
    print("=" * 60)
    
    sucesso = pipeline_completo_simples()
    
    if sucesso:
        print("\n✅ Aula concluída! Pipeline executado com sucesso.")
    else:
        print("\n⚠️ Aula concluída com problemas. Revise os logs acima.")

if __name__ == "__main__":
    main()
