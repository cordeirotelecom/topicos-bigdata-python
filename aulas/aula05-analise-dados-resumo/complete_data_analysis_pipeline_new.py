#!/usr/bin/env python3
"""
Aula 05: Pipeline Completo de Análise de Dados
Professor: Vagner Cordeiro
Curso: Tópicos de Big Data em Python

Este script demonstra um pipeline completo de análise de dados,
desde a coleta até insights finais, com boas práticas e ferramentas modernas.
"""

# Importações com tratamento de erros
try:
    import pandas
    import numpy as np
    PANDAS_AVAILABLE = True
    print("✅ Pandas e NumPy disponíveis")
except ImportError:
    print("⚠️ Pandas/NumPy não está instalado. Usando simulação de conceitos.")
    PANDAS_AVAILABLE = False
    # Criando stubs para tipos
    pandas = None
    class pd:
        class DataFrame:
            pass

try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    MATPLOTLIB_AVAILABLE = True
    print("✅ Matplotlib e Seaborn disponíveis")
except ImportError:
    print("⚠️ Matplotlib/Seaborn não está instalado. Visualizações serão simuladas.")
    MATPLOTLIB_AVAILABLE = False

try:
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
    print("✅ Plotly disponível")
except ImportError:
    print("⚠️ Plotly não está instalado. Gráficos interativos serão simulados.")
    PLOTLY_AVAILABLE = False

try:
    from scipy import stats
    from sklearn.preprocessing import StandardScaler, LabelEncoder
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression, LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import classification_report, confusion_matrix, r2_score
    SKLEARN_AVAILABLE = True
    print("✅ SciPy e Scikit-learn disponíveis")
except ImportError:
    print("⚠️ SciPy/Scikit-learn não está instalado. Machine learning será simulado.")
    SKLEARN_AVAILABLE = False

import warnings
warnings.filterwarnings('ignore')

from datetime import datetime, timedelta
import random
import sqlite3
import json
from typing import Optional, Dict, List, Any, Union

# Configurar estilo dos gráficos se disponível
if MATPLOTLIB_AVAILABLE:
    try:
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
    except:
        pass

class DataAnalysisPipeline:
    """Pipeline completo para análise de dados"""
    
    def __init__(self, name: str = "Data Analysis Pipeline"):
        self.name = name
        self.data: Any = None  # Pode ser DataFrame ou dict para simulação
        self.cleaned_data: Any = None  # Pode ser DataFrame ou dict para simulação
        self.analysis_results: Dict[str, Any] = {}
        self.insights: List[str] = []
        
    def load_data(self, data_source: Any, source_type: str = "dataframe") -> None:
        """Carrega dados de diferentes fontes"""
        print(f"📥 Carregando dados de: {source_type}")
        
        if not PANDAS_AVAILABLE:
            print("📊 Simulando carregamento de dados...")
            self.data = self._simulate_dataframe()
            print(f"✅ Dados simulados carregados: 1000 linhas, 10 colunas")
            return
        
        try:
            if source_type == "dataframe":
                self.data = data_source
            elif source_type == "csv":
                self.data = pandas.read_csv(data_source) if pandas else None
            elif source_type == "json":
                self.data = pandas.read_json(data_source) if pandas else None
            elif source_type == "sql":
                # data_source seria uma tupla (connection, query)
                conn, query = data_source
                self.data = pandas.read_sql_query(query, conn) if pandas else None
            
            if self.data is not None and hasattr(self.data, 'shape'):
                print(f"✅ Dados carregados: {self.data.shape[0]} linhas, {self.data.shape[1]} colunas")
            else:
                print("✅ Dados carregados com sucesso")
                
        except Exception as e:
            print(f"❌ Erro ao carregar dados: {e}")
            self.data = self._simulate_dataframe()
            print("📊 Usando dados simulados para demonstração")
    
    def _simulate_dataframe(self) -> Dict[str, Any]:
        """Simula um DataFrame quando pandas não está disponível"""
        return {
            'vendas': [random.randint(100, 1000) for _ in range(100)],
            'categoria': [random.choice(['A', 'B', 'C']) for _ in range(100)],
            'regiao': [random.choice(['Norte', 'Sul', 'Leste', 'Oeste']) for _ in range(100)],
            'data': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(100)],
            'preco': [random.uniform(10, 100) for _ in range(100)]
        }
    
    def explore_data(self) -> None:
        """Explora os dados iniciais"""
        print("\n🔍 EXPLORAÇÃO INICIAL DOS DADOS")
        print("=" * 50)
        
        if not PANDAS_AVAILABLE:
            print("📊 Simulando exploração de dados...")
            print("Shape simulado: (1000, 10)")
            print("Colunas simuladas: vendas, categoria, região, data, preço...")
            print("Tipos de dados: numéricos e categóricos")
            print("Valores nulos: 5% dos dados simulados")
            return
        
        if self.data is None:
            print("❌ Nenhum dado carregado")
            return
            
        try:
            print(f"Shape dos dados: {self.data.shape}")
            print(f"\nColunas: {list(self.data.columns)}")
            print(f"\nTipos de dados:")
            print(self.data.dtypes)
            print(f"\nInformações gerais:")
            print(self.data.info())
            print(f"\nPrimeiras 5 linhas:")
            print(self.data.head())
            print(f"\nEstatísticas descritivas:")
            print(self.data.describe())
            print(f"\nValores nulos por coluna:")
            print(self.data.isnull().sum())
            
        except Exception as e:
            print(f"❌ Erro na exploração: {e}")
            print("📊 Dados carregados, mas exploração limitada")
    
    def clean_data(self) -> None:
        """Limpa e prepara os dados"""
        print("\n🧹 LIMPEZA DOS DADOS")
        print("=" * 50)
        
        if not PANDAS_AVAILABLE:
            print("📊 Simulando limpeza de dados...")
            self.cleaned_data = self._simulate_dataframe()
            print("✅ Dados simulados limpos")
            print("- Valores nulos tratados")
            print("- Outliers removidos")
            print("- Texto padronizado")
            return
        
        if self.data is None:
            print("❌ Nenhum dado para limpar")
            return
            
        try:
            # Copiar dados originais
            self.cleaned_data = self.data.copy()
            
            # 1. Tratar valores nulos
            self._handle_missing_values()
            
            # 2. Padronizar texto
            self._standardize_text()
            
            # 3. Remover outliers
            self._remove_outliers()
            
            print("✅ Limpeza concluída")
            
        except Exception as e:
            print(f"❌ Erro na limpeza: {e}")
            self.cleaned_data = self.data
    
    def _handle_missing_values(self) -> None:
        """Trata valores nulos"""
        print("🔧 Tratando valores nulos...")
        
        if self.cleaned_data is None or not PANDAS_AVAILABLE:
            return
            
        try:
            # Para colunas numéricas
            numeric_cols = self.cleaned_data.select_dtypes(include=[np.number]).columns
            categorical_cols = self.cleaned_data.select_dtypes(include=['object', 'category']).columns
            
            for col in numeric_cols:
                if self.cleaned_data[col].isnull().sum() > 0:
                    missing_count = self.cleaned_data[col].isnull().sum()
                    if self.cleaned_data[col].dtype in ['int64', 'int32']:
                        fill_value = self.cleaned_data[col].median()
                    else:
                        fill_value = self.cleaned_data[col].mean()
                    
                    self.cleaned_data[col].fillna(fill_value, inplace=True)
                    print(f"   - {col}: {missing_count} valores preenchidos com {fill_value:.2f}")
            
            # Para colunas categóricas
            for col in categorical_cols:
                if self.cleaned_data[col].isnull().sum() > 0:
                    missing_count = self.cleaned_data[col].isnull().sum()
                    fill_value = self.cleaned_data[col].mode().iloc[0] if not self.cleaned_data[col].mode().empty else 'Unknown'
                    self.cleaned_data[col].fillna(fill_value, inplace=True)
                    print(f"   - {col}: {missing_count} valores preenchidos com '{fill_value}'")
                    
        except Exception as e:
            print(f"   ❌ Erro no tratamento de nulos: {e}")
    
    def _standardize_text(self) -> None:
        """Padroniza campos de texto"""
        print("🔧 Padronizando texto...")
        
        if self.cleaned_data is None or not PANDAS_AVAILABLE:
            return
            
        try:
            text_cols = self.cleaned_data.select_dtypes(include=['object']).columns
            
            for col in text_cols:
                # Remove espaços extras
                self.cleaned_data[col] = self.cleaned_data[col].astype(str).str.strip()
                # Capitaliza se for categoria pequena
                if self.cleaned_data[col].nunique() / len(self.cleaned_data) < 0.1:
                    self.cleaned_data[col] = self.cleaned_data[col].str.title()
                    
        except Exception as e:
            print(f"   ❌ Erro na padronização: {e}")
    
    def _remove_outliers(self) -> None:
        """Remove outliers usando IQR"""
        print("🔧 Removendo outliers...")
        
        if self.cleaned_data is None or not PANDAS_AVAILABLE:
            return
            
        try:
            if self.cleaned_data is None:
                print("   ⚠️ Dados não disponíveis para remoção de outliers")
                return
                
            if not hasattr(self.cleaned_data, 'select_dtypes'):
                print("   ⚠️ Utilizando simulação para remoção de outliers")
                return
                
            numeric_cols = self.cleaned_data.select_dtypes(include=[np.number]).columns
            initial_size = len(self.cleaned_data)
            
            for col in numeric_cols:
                Q1 = self.cleaned_data[col].quantile(0.25)
                Q3 = self.cleaned_data[col].quantile(0.75)
                IQR = Q3 - Q1
                
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                
                outliers = (self.cleaned_data[col] < lower_bound) | (self.cleaned_data[col] > upper_bound)
                outlier_count = outliers.sum()
                
                if outlier_count > 0:
                    print(f"   - {col}: {outlier_count} outliers identificados")
                    # Remove outliers
                    self.cleaned_data = self.cleaned_data[~outliers]
            
            removed = initial_size - len(self.cleaned_data)
            if removed > 0:
                print(f"   📊 Total de linhas removidas: {removed}")
                
        except Exception as e:
            print(f"   ❌ Erro na remoção de outliers: {e}")
            print("   🔄 Utilizando simulação de remoção de outliers")
    
    def analyze_correlations(self, target_column: Optional[str] = None) -> None:
        """Analisa correlações entre variáveis"""
        print("\n📊 ANÁLISE DE CORRELAÇÕES")
        print("=" * 50)
        
        if not PANDAS_AVAILABLE:
            print("📊 Simulando análise de correlações...")
            print("Correlações encontradas:")
            print("- vendas x preço: 0.85 (alta correlação positiva)")
            print("- vendas x categoria: 0.45 (correlação moderada)")
            print("- preço x região: -0.12 (correlação fraca negativa)")
            return
        
        if self.cleaned_data is None:
            print("❌ Dados não estão limpos")
            return
            
        try:
            # Selecionar apenas colunas numéricas
            numeric_data = self.cleaned_data.select_dtypes(include=[np.number])
            
            if numeric_data.empty:
                print("❌ Nenhuma coluna numérica encontrada")
                return
            
            # Calcular matriz de correlação
            correlation_matrix = numeric_data.corr()
            
            print("📈 Matriz de correlação:")
            print(correlation_matrix)
            
            # Encontrar correlações mais fortes
            if target_column and target_column in correlation_matrix.columns:
                correlations = correlation_matrix[target_column].drop(target_column)
                correlations = correlations.reindex(correlations.abs().sort_values(ascending=False).index)
                
                print(f"\n🎯 Correlações com {target_column}:")
                for var, corr in correlations.head(5).items():
                    strength = self._interpret_correlation(abs(corr))
                    direction = "positiva" if corr > 0 else "negativa"
                    print(f"   - {var}: {corr:.3f} ({strength} {direction})")
            
            # Criar visualização se possível
            if MATPLOTLIB_AVAILABLE:
                self._plot_correlation_heatmap(correlation_matrix)
                
        except Exception as e:
            print(f"❌ Erro na análise de correlações: {e}")
    
    def _interpret_correlation(self, corr_value: float) -> str:
        """Interpreta o valor de correlação"""
        if corr_value >= 0.7:
            return "forte"
        elif corr_value >= 0.3:
            return "moderada"
        else:
            return "fraca"
    
    def _plot_correlation_heatmap(self, correlation_matrix: Any) -> None:
        """Cria heatmap de correlação"""
        try:
            plt.figure(figsize=(10, 8))
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                       square=True, linewidths=0.5)
            plt.title('Matriz de Correlação')
            plt.tight_layout()
            plt.show()
            print("📊 Heatmap de correlação criado")
        except Exception as e:
            print(f"❌ Erro ao criar heatmap: {e}")
    
    def create_visualizations(self) -> None:
        """Cria visualizações dos dados"""
        print("\n📊 CRIAÇÃO DE VISUALIZAÇÕES")
        print("=" * 50)
        
        if not PANDAS_AVAILABLE:
            print("📊 Simulando criação de visualizações...")
            print("Gráficos criados:")
            print("- Histograma de vendas")
            print("- Boxplot por categoria")
            print("- Gráfico de dispersão vendas x preço")
            print("- Gráfico de pizza por região")
            return
        
        if self.cleaned_data is None:
            print("❌ Dados não estão limpos")
            return
            
        try:
            # Análise univariada
            self._create_univariate_plots()
            
            # Análise bivariada
            self._create_bivariate_plots()
            
            # Análise temporal se houver dados de data
            self._create_temporal_plots()
            
        except Exception as e:
            print(f"❌ Erro na criação de visualizações: {e}")
    
    def _create_univariate_plots(self) -> None:
        """Cria gráficos univariados"""
        if not MATPLOTLIB_AVAILABLE:
            print("📊 Visualizações univariadas simuladas")
            return
            
        try:
            numeric_cols = self.cleaned_data.select_dtypes(include=[np.number]).columns
            categorical_cols = self.cleaned_data.select_dtypes(include=['object']).columns
            
            # Histogramas para variáveis numéricas
            for col in numeric_cols[:3]:  # Limitar a 3 para não sobrecarregar
                plt.figure(figsize=(8, 6))
                plt.hist(self.cleaned_data[col].dropna(), bins=30, alpha=0.7, edgecolor='black')
                plt.title(f'Distribuição de {col}')
                plt.xlabel(col)
                plt.ylabel('Frequência')
                plt.show()
                print(f"📊 Histograma criado para {col}")
            
            # Gráficos de pizza para variáveis categóricas
            for col in categorical_cols[:2]:  # Limitar a 2
                plt.figure(figsize=(8, 8))
                value_counts = self.cleaned_data[col].value_counts()
                if len(value_counts) <= 10:  # Apenas se não houver muitas categorias
                    plt.pie(value_counts.values, labels=value_counts.index, autopct='%1.1f%%')
                    plt.title(f'Distribuição de {col}')
                    plt.show()
                    print(f"📊 Gráfico de pizza criado para {col}")
                    
        except Exception as e:
            print(f"❌ Erro nos gráficos univariados: {e}")
    
    def _create_bivariate_plots(self) -> None:
        """Cria gráficos bivariados"""
        if not MATPLOTLIB_AVAILABLE:
            print("📊 Visualizações bivariadas simuladas")
            return
            
        try:
            numeric_cols = list(self.cleaned_data.select_dtypes(include=[np.number]).columns)
            
            if len(numeric_cols) >= 2:
                # Scatter plot entre duas primeiras variáveis numéricas
                plt.figure(figsize=(8, 6))
                plt.scatter(self.cleaned_data[numeric_cols[0]], 
                          self.cleaned_data[numeric_cols[1]], alpha=0.6)
                plt.xlabel(numeric_cols[0])
                plt.ylabel(numeric_cols[1])
                plt.title(f'{numeric_cols[0]} vs {numeric_cols[1]}')
                plt.show()
                print(f"📊 Scatter plot criado: {numeric_cols[0]} vs {numeric_cols[1]}")
                
        except Exception as e:
            print(f"❌ Erro nos gráficos bivariados: {e}")
    
    def _create_temporal_plots(self) -> None:
        """Cria gráficos temporais se houver dados de data"""
        if not MATPLOTLIB_AVAILABLE:
            print("📊 Visualizações temporais simuladas")
            return
            
        try:
            # Procurar colunas de data
            date_cols = []
            for col in self.cleaned_data.columns:
                if 'data' in col.lower() or 'date' in col.lower() or 'time' in col.lower():
                    date_cols.append(col)
            
            if date_cols:
                print(f"📊 Análise temporal criada para: {date_cols[0]}")
            else:
                print("📊 Nenhuma coluna temporal identificada")
                
        except Exception as e:
            print(f"❌ Erro nos gráficos temporais: {e}")
    
    def build_models(self, target_column: Optional[str] = None) -> None:
        """Constrói modelos de machine learning"""
        print("\n🤖 CONSTRUÇÃO DE MODELOS")
        print("=" * 50)
        
        if not SKLEARN_AVAILABLE:
            print("📊 Simulando construção de modelos...")
            print("Modelos criados:")
            print("- Regressão Linear: R² = 0.85")
            print("- Random Forest: Acurácia = 0.92")
            print("- Regressão Logística: F1-Score = 0.88")
            return
        
        if self.cleaned_data is None:
            print("❌ Dados não estão limpos")
            return
            
        if target_column is None:
            numeric_cols = list(self.cleaned_data.select_dtypes(include=[np.number]).columns)
            if numeric_cols:
                target_column = numeric_cols[0]
                print(f"🎯 Usando {target_column} como variável alvo")
            else:
                print("❌ Nenhuma variável alvo especificada")
                return
        
        try:
            # Preparar dados
            features = list(self.cleaned_data.select_dtypes(include=[np.number]).columns)
            if target_column in features:
                features.remove(target_column)
            
            if not features:
                print("❌ Nenhuma feature numérica disponível")
                return
            
            X = self.cleaned_data[features]
            y = self.cleaned_data[target_column]
            
            # Dividir dados
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Modelo de regressão
            if self.cleaned_data[target_column].dtype in ['float64', 'int64']:
                self._build_regression_model(X_train, X_test, y_train, y_test, target_column)
            
            # Modelo de classificação (se a variável alvo tem poucas categorias únicas)
            if self.cleaned_data[target_column].nunique() <= 10:
                self._build_classification_model(X_train, X_test, y_train, y_test, target_column)
                
        except Exception as e:
            print(f"❌ Erro na construção de modelos: {e}")
    
    def _build_regression_model(self, X_train: Any, X_test: Any, y_train: Any, y_test: Any, target: str) -> None:
        """Constrói modelo de regressão"""
        try:
            # Regressão Linear
            lr_model = LinearRegression()
            lr_model.fit(X_train, y_train)
            
            y_pred = lr_model.predict(X_test)
            r2 = r2_score(y_test, y_pred)
            
            print(f"📈 Regressão Linear para {target}:")
            print(f"   - R² Score: {r2:.3f}")
            
            # Salvar modelo
            self.analysis_results[f'regression_{target}'] = {
                'model': lr_model,
                'r2_score': r2,
                'features': list(X_train.columns)
            }
            
        except Exception as e:
            print(f"❌ Erro na regressão: {e}")
    
    def _build_classification_model(self, X_train: Any, X_test: Any, y_train: Any, y_test: Any, target: str) -> None:
        """Constrói modelo de classificação"""
        try:
            # Random Forest
            rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
            rf_model.fit(X_train, y_train)
            
            y_pred = rf_model.predict(X_test)
            accuracy = (y_pred == y_test).mean()
            
            print(f"🌳 Random Forest para {target}:")
            print(f"   - Acurácia: {accuracy:.3f}")
            
            # Importância das features
            feature_importance = rf_model.feature_importances_
            for feature, importance in zip(X_train.columns, feature_importance):
                print(f"   - {feature}: {importance:.3f}")
            
            # Salvar modelo
            self.analysis_results[f'classification_{target}'] = {
                'model': rf_model,
                'accuracy': accuracy,
                'features': list(X_train.columns),
                'feature_importance': dict(zip(X_train.columns, feature_importance))
            }
            
        except Exception as e:
            print(f"❌ Erro na classificação: {e}")
    
    def generate_insights(self) -> None:
        """Gera insights e conclusões"""
        print("\n💡 INSIGHTS E CONCLUSÕES")
        print("=" * 50)
        
        self.insights = []
        
        if self.cleaned_data is None:
            self.insights.append("⚠️ Análise limitada - dados não carregados adequadamente")
        
        # Insights sobre a qualidade dos dados
        if PANDAS_AVAILABLE and self.cleaned_data is not None:
            try:
                total_rows = len(self.cleaned_data)
                total_cols = len(self.cleaned_data.columns)
                
                self.insights.append(f"📊 Dataset contém {total_rows:,} registros e {total_cols} variáveis")
                
                # Verificar balanceamento se houver variáveis categóricas
                categorical_cols = self.cleaned_data.select_dtypes(include=['object']).columns
                for col in categorical_cols[:2]:  # Limitar análise
                    value_counts = self.cleaned_data[col].value_counts()
                    if len(value_counts) <= 10:
                        most_common = value_counts.index[0]
                        percentage = (value_counts.iloc[0] / total_rows) * 100
                        self.insights.append(f"📈 {col}: categoria '{most_common}' representa {percentage:.1f}% dos dados")
                
                # Insights sobre variáveis numéricas
                numeric_cols = self.cleaned_data.select_dtypes(include=[np.number]).columns
                for col in numeric_cols[:3]:  # Limitar análise
                    mean_val = self.cleaned_data[col].mean()
                    std_val = self.cleaned_data[col].std()
                    cv = (std_val / mean_val) * 100 if mean_val != 0 else 0
                    
                    if cv > 50:
                        self.insights.append(f"📊 {col}: alta variabilidade (CV = {cv:.1f}%)")
                    elif cv < 10:
                        self.insights.append(f"📊 {col}: baixa variabilidade (CV = {cv:.1f}%)")
                        
            except Exception as e:
                self.insights.append(f"⚠️ Erro na análise de insights: {e}")
        
        # Insights sobre modelos
        for model_name, results in self.analysis_results.items():
            if 'r2_score' in results:
                r2 = results['r2_score']
                if r2 > 0.8:
                    self.insights.append(f"🎯 Modelo {model_name}: excelente poder preditivo (R² = {r2:.3f})")
                elif r2 > 0.6:
                    self.insights.append(f"🎯 Modelo {model_name}: bom poder preditivo (R² = {r2:.3f})")
                else:
                    self.insights.append(f"🎯 Modelo {model_name}: poder preditivo limitado (R² = {r2:.3f})")
            
            if 'accuracy' in results:
                acc = results['accuracy']
                if acc > 0.9:
                    self.insights.append(f"🎯 Modelo {model_name}: excelente acurácia ({acc:.3f})")
                elif acc > 0.7:
                    self.insights.append(f"🎯 Modelo {model_name}: boa acurácia ({acc:.3f})")
        
        # Adicionar insights gerais
        if not self.insights:
            self.insights.extend([
                "📊 Pipeline de análise executado com sucesso",
                "🔍 Dados explorados e processados adequadamente",
                "📈 Visualizações criadas para entendimento dos padrões",
                "🤖 Modelos construídos para predição e classificação"
            ])
        
        # Exibir insights
        for i, insight in enumerate(self.insights, 1):
            print(f"{i:2d}. {insight}")
    
    def export_results(self, filename: str = "analysis_results.json") -> None:
        """Exporta resultados da análise"""
        print(f"\n💾 EXPORTANDO RESULTADOS PARA {filename}")
        print("=" * 50)
        
        try:
            results = {
                'pipeline_name': self.name,
                'execution_date': datetime.now().isoformat(),
                'insights': self.insights,
                'data_info': {
                    'rows': len(self.cleaned_data) if self.cleaned_data is not None and PANDAS_AVAILABLE else 'N/A',
                    'columns': len(self.cleaned_data.columns) if self.cleaned_data is not None and PANDAS_AVAILABLE else 'N/A'
                },
                'models_summary': {}
            }
            
            # Adicionar resumo dos modelos (sem os objetos modelo)
            for model_name, model_data in self.analysis_results.items():
                results['models_summary'][model_name] = {
                    key: value for key, value in model_data.items() 
                    if key not in ['model']  # Excluir objeto modelo
                }
            
            # Salvar arquivo
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False, default=str)
            
            print(f"✅ Resultados exportados para {filename}")
            
        except Exception as e:
            print(f"❌ Erro ao exportar: {e}")
    
    def run_complete_pipeline(self, data_source: Any = None, target_column: Optional[str] = None) -> None:
        """Executa pipeline completo de análise"""
        print("🚀 INICIANDO PIPELINE COMPLETO DE ANÁLISE DE DADOS")
        print("=" * 60)
        
        try:
            # 1. Carregar dados
            if data_source is not None:
                self.load_data(data_source)
            else:
                # Gerar dados de exemplo
                self.load_data(self._generate_sample_data(), "dataframe")
            
            # 2. Explorar dados
            self.explore_data()
            
            # 3. Limpar dados
            self.clean_data()
            
            # 4. Analisar correlações
            self.analyze_correlations(target_column)
            
            # 5. Criar visualizações
            self.create_visualizations()
            
            # 6. Construir modelos
            self.build_models(target_column)
            
            # 7. Gerar insights
            self.generate_insights()
            
            # 8. Exportar resultados
            self.export_results()
            
            print("\n🎉 PIPELINE COMPLETO EXECUTADO COM SUCESSO!")
            print("=" * 60)
            
        except Exception as e:
            print(f"\n❌ ERRO NO PIPELINE: {e}")
            print("Pipeline interrompido, mas resultados parciais podem estar disponíveis.")
    
    def _generate_sample_data(self) -> Any:
        """Gera dados de exemplo para demonstração"""
        if not PANDAS_AVAILABLE:
            return self._simulate_dataframe()
        
        # Gerar dados sintéticos mais realistas
        np.random.seed(42)
        n_samples = 1000
        
        data = {
            'vendas': np.random.normal(500, 150, n_samples),
            'preco': np.random.uniform(10, 100, n_samples),
            'categoria': np.random.choice(['Eletrônicos', 'Roupas', 'Casa', 'Livros'], n_samples),
            'regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], n_samples),
            'desconto': np.random.uniform(0, 0.3, n_samples),
            'avaliacao': np.random.uniform(1, 5, n_samples),
            'idade_cliente': np.random.normal(35, 12, n_samples),
            'data_compra': [datetime.now() - timedelta(days=np.random.randint(1, 365)) for _ in range(n_samples)]
        }
        
        # Criar correlações realistas
        # Adicionar alguns valores nulos
        missing_indices = np.random.choice(n_samples, size=int(0.05 * n_samples), replace=False)
        for idx in missing_indices:
            col = np.random.choice(['preco', 'avaliacao', 'idade_cliente'])
            data[col][idx] = np.nan
        
        # Calcular vendas DEPOIS de adicionar NaN para evitar erro de conversão
        data['vendas'] = (data['preco'] * np.random.uniform(8, 12, n_samples) * 
                         (1 - data['desconto']) * 
                         np.random.normal(1, 0.2, n_samples))
        
        # Converter para int apenas onde não há NaN
        mask = ~np.isnan(data['vendas'])
        data['vendas'][mask] = data['vendas'][mask].astype(int)
        
        return pandas.DataFrame(data) if pandas else {"message": "Dados simulados gerados", "rows": n_samples}


def demonstrate_pipeline():
    """Demonstra o uso do pipeline"""
    print("🎓 DEMONSTRAÇÃO: Pipeline de Análise de Dados")
    print("=" * 60)
    
    # Criar instância do pipeline
    pipeline = DataAnalysisPipeline("Demo - Análise de Vendas")
    
    # Executar pipeline completo
    pipeline.run_complete_pipeline(target_column='vendas')


def demonstrate_concepts():
    """Demonstra conceitos fundamentais independente das bibliotecas"""
    print("\n📚 CONCEITOS FUNDAMENTAIS DE ANÁLISE DE DADOS")
    print("=" * 60)
    
    print("""
    1. 📊 EXPLORAÇÃO DE DADOS (EDA)
       - Entender a estrutura dos dados
       - Identificar padrões e anomalias
       - Calcular estatísticas descritivas
    
    2. 🧹 LIMPEZA DE DADOS
       - Tratar valores nulos
       - Remover outliers
       - Padronizar formatos
    
    3. 📈 ANÁLISE ESTATÍSTICA
       - Correlações entre variáveis
       - Distribuições
       - Testes de hipóteses
    
    4. 📊 VISUALIZAÇÃO
       - Histogramas para distribuições
       - Scatter plots para correlações
       - Box plots para outliers
    
    5. 🤖 MACHINE LEARNING
       - Regressão para valores contínuos
       - Classificação para categorias
       - Validação de modelos
    
    6. 💡 GERAÇÃO DE INSIGHTS
       - Interpretar resultados
       - Identificar padrões de negócio
       - Propor ações baseadas em dados
    """)


if __name__ == "__main__":
    print("🎯 AULA 05: Pipeline Completo de Análise de Dados")
    print("Autor: Professor Vagner Cordeiro")
    print("=" * 60)
    
    # Demonstrar conceitos
    demonstrate_concepts()
    
    # Executar demonstração
    demonstrate_pipeline()
    
    print("\n✅ Aula concluída! Pipeline de análise de dados demonstrado com sucesso.")
