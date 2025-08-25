#!/usr/bin/env python3
"""
Aula 05: Pipeline Completo de Análise de Dados
Professor: Vagner Cordeiro
Curso: Tópicos de Big Data em Python

Este script demonstra um pipeline completo de análise de dados,
desde a coleta até insights finais, com boas práticas e ferramentas modernas.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

from datetime import datetime, timedelta
import random
from scipy import stats
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, r2_score
import sqlite3
import json

# Configurar estilo dos gráficos
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class DataAnalysisPipeline:
    """Pipeline completo para análise de dados"""
    
    def __init__(self, name="Data Analysis Pipeline"):
        self.name = name
        self.data = None
        self.cleaned_data = None
        self.analysis_results = {}
        self.insights = []
        
    def load_data(self, data_source, source_type="dataframe"):
        """Carrega dados de diferentes fontes"""
        print(f"📥 Carregando dados de: {source_type}")
        
        if source_type == "dataframe":
            self.data = data_source
        elif source_type == "csv":
            self.data = pd.read_csv(data_source)
        elif source_type == "json":
            self.data = pd.read_json(data_source)
        elif source_type == "sql":
            # data_source seria uma tupla (connection, query)
            conn, query = data_source
            self.data = pd.read_sql_query(query, conn)
        
        print(f"✅ Dados carregados: {self.data.shape[0]} linhas, {self.data.shape[1]} colunas")
        return self.data
    
    def explore_data(self):
        """Análise exploratória inicial dos dados"""
        print("\n🔍 ANÁLISE EXPLORATÓRIA INICIAL")
        print("=" * 40)
        
        if self.data is None:
            print("❌ Nenhum dado carregado!")
            return
        
        # Informações básicas
        print(f"📊 Shape dos dados: {self.data.shape}")
        print(f"💾 Memória utilizada: {self.data.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        # Tipos de dados
        print(f"\n📋 Tipos de dados:")
        type_counts = self.data.dtypes.value_counts()
        for dtype, count in type_counts.items():
            print(f"  • {dtype}: {count} colunas")
        
        # Missing values
        missing_data = self.data.isnull().sum()
        missing_percent = (missing_data / len(self.data)) * 100
        
        if missing_data.sum() > 0:
            print(f"\n⚠️  Missing values:")
            for col in missing_data[missing_data > 0].index:
                print(f"  • {col}: {missing_data[col]} ({missing_percent[col]:.1f}%)")
        else:
            print(f"\n✅ Nenhum missing value encontrado!")
        
        # Duplicatas
        duplicates = self.data.duplicated().sum()
        print(f"\n🔄 Linhas duplicadas: {duplicates}")
        
        # Estatísticas básicas para colunas numéricas
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            print(f"\n📈 Estatísticas das colunas numéricas:")
            print(self.data[numeric_cols].describe())
        
        # Análise de colunas categóricas
        categorical_cols = self.data.select_dtypes(include=['object', 'category']).columns
        if len(categorical_cols) > 0:
            print(f"\n📂 Colunas categóricas:")
            for col in categorical_cols[:5]:  # Mostrar apenas as primeiras 5
                unique_count = self.data[col].nunique()
                print(f"  • {col}: {unique_count} valores únicos")
                if unique_count <= 10:
                    print(f"    Valores: {list(self.data[col].unique())}")
    
    def clean_data(self, strategies=None):
        """Limpeza e tratamento dos dados"""
        print("\n🧹 LIMPEZA DE DADOS")
        print("=" * 25)
        
        if self.data is None:
            print("❌ Nenhum dado carregado!")
            return
        
        self.cleaned_data = self.data.copy()
        
        if strategies is None:
            strategies = {
                'remove_duplicates': True,
                'handle_missing': 'auto',
                'remove_outliers': False,
                'normalize_text': True
            }
        
        # Remover duplicatas
        if strategies.get('remove_duplicates', False):
            initial_size = len(self.cleaned_data)
            self.cleaned_data = self.cleaned_data.drop_duplicates()
            removed = initial_size - len(self.cleaned_data)
            if removed > 0:
                print(f"🗑️  Removidas {removed} linhas duplicadas")
        
        # Tratar missing values
        missing_strategy = strategies.get('handle_missing', 'auto')
        if missing_strategy != 'ignore':
            self._handle_missing_values(missing_strategy)
        
        # Normalizar texto
        if strategies.get('normalize_text', False):
            self._normalize_text_columns()
        
        # Remover outliers
        if strategies.get('remove_outliers', False):
            self._remove_outliers()
        
        print(f"✅ Limpeza concluída: {self.cleaned_data.shape[0]} linhas restantes")
        
    def _handle_missing_values(self, strategy):
        """Trata valores missing baseado na estratégia"""
        numeric_cols = self.cleaned_data.select_dtypes(include=[np.number]).columns
        categorical_cols = self.cleaned_data.select_dtypes(include=['object', 'category']).columns
        
        for col in numeric_cols:
            missing_count = self.cleaned_data[col].isnull().sum()
            if missing_count > 0:
                if strategy == 'auto' or strategy == 'median':
                    fill_value = self.cleaned_data[col].median()
                elif strategy == 'mean':
                    fill_value = self.cleaned_data[col].mean()
                elif strategy == 'mode':
                    fill_value = self.cleaned_data[col].mode().iloc[0] if not self.cleaned_data[col].mode().empty else 0
                
                self.cleaned_data[col].fillna(fill_value, inplace=True)
                print(f"🔧 {col}: {missing_count} valores preenchidos com {fill_value:.2f}")
        
        for col in categorical_cols:
            missing_count = self.cleaned_data[col].isnull().sum()
            if missing_count > 0:
                if strategy == 'auto' or strategy == 'mode':
                    fill_value = self.cleaned_data[col].mode().iloc[0] if not self.cleaned_data[col].mode().empty else 'Unknown'
                else:
                    fill_value = 'Unknown'
                
                self.cleaned_data[col].fillna(fill_value, inplace=True)
                print(f"🔧 {col}: {missing_count} valores preenchidos com '{fill_value}'")
    
    def _normalize_text_columns(self):
        """Normaliza colunas de texto"""
        text_cols = self.cleaned_data.select_dtypes(include=['object']).columns
        
        for col in text_cols:
            # Converter para string e remover espaços extras
            self.cleaned_data[col] = self.cleaned_data[col].astype(str).str.strip()
            # Padronizar case se parecer ser categórico
            if self.cleaned_data[col].nunique() / len(self.cleaned_data) < 0.1:
                self.cleaned_data[col] = self.cleaned_data[col].str.title()
    
    def _remove_outliers(self, method='iqr', threshold=1.5):
        """Remove outliers usando IQR ou Z-score"""
        numeric_cols = self.cleaned_data.select_dtypes(include=[np.number]).columns
        initial_size = len(self.cleaned_data)
        
        for col in numeric_cols:
            if method == 'iqr':
                Q1 = self.cleaned_data[col].quantile(0.25)
                Q3 = self.cleaned_data[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - threshold * IQR
                upper_bound = Q3 + threshold * IQR
                
                outliers = (self.cleaned_data[col] < lower_bound) | (self.cleaned_data[col] > upper_bound)
                
            elif method == 'zscore':
                z_scores = np.abs(stats.zscore(self.cleaned_data[col]))
                outliers = z_scores > threshold
            
            outlier_count = outliers.sum()
            if outlier_count > 0:
                self.cleaned_data = self.cleaned_data[~outliers]
                print(f"🎯 {col}: {outlier_count} outliers removidos")
        
        removed = initial_size - len(self.cleaned_data)
        if removed > 0:
            print(f"📉 Total de {removed} linhas removidas por outliers")
    
    def statistical_analysis(self):
        """Análise estatística aprofundada"""
        print("\n📊 ANÁLISE ESTATÍSTICA")
        print("=" * 30)
        
        if self.cleaned_data is None:
            print("❌ Execute a limpeza dos dados primeiro!")
            return
        
        numeric_cols = self.cleaned_data.select_dtypes(include=[np.number]).columns
        
        # Estatísticas descritivas avançadas
        self.analysis_results['descriptive_stats'] = {}
        
        for col in numeric_cols:
            data = self.cleaned_data[col]
            
            stats_dict = {
                'count': len(data),
                'mean': data.mean(),
                'median': data.median(),
                'mode': data.mode().iloc[0] if not data.mode().empty else None,
                'std': data.std(),
                'var': data.var(),
                'skewness': data.skew(),
                'kurtosis': data.kurtosis(),
                'min': data.min(),
                'max': data.max(),
                'range': data.max() - data.min(),
                'q1': data.quantile(0.25),
                'q3': data.quantile(0.75),
                'iqr': data.quantile(0.75) - data.quantile(0.25)
            }
            
            self.analysis_results['descriptive_stats'][col] = stats_dict
            
            print(f"\n📈 {col}:")
            print(f"  • Média: {stats_dict['mean']:.2f}")
            print(f"  • Mediana: {stats_dict['median']:.2f}")
            print(f"  • Desvio Padrão: {stats_dict['std']:.2f}")
            print(f"  • Assimetria: {stats_dict['skewness']:.2f}")
            print(f"  • Curtose: {stats_dict['kurtosis']:.2f}")
        
        # Análise de correlação
        if len(numeric_cols) > 1:
            correlation_matrix = self.cleaned_data[numeric_cols].corr()
            self.analysis_results['correlation_matrix'] = correlation_matrix
            
            print(f"\n🔗 CORRELAÇÕES MAIS FORTES:")
            # Encontrar correlações mais fortes (excluindo diagonal)
            mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
            correlation_matrix_masked = correlation_matrix.mask(mask)
            
            # Flatten e ordenar por valor absoluto
            correlations = correlation_matrix_masked.unstack().dropna()
            correlations = correlations.reindex(correlations.abs().sort_values(ascending=False).index)
            
            for (var1, var2), corr in correlations.head(5).items():
                print(f"  • {var1} ↔ {var2}: {corr:.3f}")
    
    def create_visualizations(self):
        """Cria visualizações para exploração dos dados"""
        print("\n📊 CRIANDO VISUALIZAÇÕES")
        print("=" * 35)
        
        if self.cleaned_data is None:
            print("❌ Execute a limpeza dos dados primeiro!")
            return
        
        numeric_cols = self.cleaned_data.select_dtypes(include=[np.number]).columns
        categorical_cols = self.cleaned_data.select_dtypes(include=['object', 'category']).columns
        
        # 1. Distribuições das variáveis numéricas
        if len(numeric_cols) > 0:
            n_cols = min(3, len(numeric_cols))
            n_rows = (len(numeric_cols) + n_cols - 1) // n_cols
            
            fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
            if n_rows == 1:
                axes = [axes] if n_cols == 1 else axes
            else:
                axes = axes.flatten()
            
            for i, col in enumerate(numeric_cols):
                if i < len(axes):
                    # Histograma com KDE
                    sns.histplot(data=self.cleaned_data, x=col, kde=True, ax=axes[i])
                    axes[i].set_title(f'Distribuição de {col}')
                    axes[i].grid(True, alpha=0.3)
            
            # Remover subplots vazios
            for i in range(len(numeric_cols), len(axes)):
                fig.delaxes(axes[i])
            
            plt.tight_layout()
            plt.show()
        
        # 2. Matriz de correlação
        if len(numeric_cols) > 1:
            plt.figure(figsize=(10, 8))
            correlation_matrix = self.cleaned_data[numeric_cols].corr()
            
            mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
            sns.heatmap(correlation_matrix, mask=mask, annot=True, cmap='coolwarm', 
                       center=0, square=True, fmt='.2f')
            plt.title('Matriz de Correlação')
            plt.tight_layout()
            plt.show()
        
        # 3. Box plots para detectar outliers
        if len(numeric_cols) > 0:
            n_cols = min(3, len(numeric_cols))
            n_rows = (len(numeric_cols) + n_cols - 1) // n_cols
            
            fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 4*n_rows))
            if n_rows == 1:
                axes = [axes] if n_cols == 1 else axes
            else:
                axes = axes.flatten()
            
            for i, col in enumerate(numeric_cols):
                if i < len(axes):
                    sns.boxplot(data=self.cleaned_data, y=col, ax=axes[i])
                    axes[i].set_title(f'Box Plot - {col}')
                    axes[i].grid(True, alpha=0.3)
            
            # Remover subplots vazios
            for i in range(len(numeric_cols), len(axes)):
                fig.delaxes(axes[i])
            
            plt.tight_layout()
            plt.show()
        
        # 4. Análise de variáveis categóricas
        if len(categorical_cols) > 0:
            for col in categorical_cols[:3]:  # Primeiras 3 categóricas
                plt.figure(figsize=(12, 6))
                
                value_counts = self.cleaned_data[col].value_counts().head(10)
                
                plt.subplot(1, 2, 1)
                value_counts.plot(kind='bar')
                plt.title(f'Frequência - {col}')
                plt.xticks(rotation=45)
                plt.grid(True, alpha=0.3)
                
                plt.subplot(1, 2, 2)
                plt.pie(value_counts.values, labels=value_counts.index, autopct='%1.1f%%')
                plt.title(f'Proporção - {col}')
                
                plt.tight_layout()
                plt.show()
    
    def advanced_analysis(self, target_column=None):
        """Análise avançada incluindo modelagem preditiva"""
        print("\n🎯 ANÁLISE AVANÇADA")
        print("=" * 25)
        
        if self.cleaned_data is None:
            print("❌ Execute a limpeza dos dados primeiro!")
            return
        
        if target_column is None:
            numeric_cols = self.cleaned_data.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                target_column = numeric_cols[0]
                print(f"🎯 Usando '{target_column}' como variável target")
        
        if target_column not in self.cleaned_data.columns:
            print(f"❌ Coluna '{target_column}' não encontrada!")
            return
        
        # Preparar dados para modelagem
        features = self.cleaned_data.select_dtypes(include=[np.number]).columns.tolist()
        if target_column in features:
            features.remove(target_column)
        
        if len(features) == 0:
            print("❌ Nenhuma feature numérica encontrada para modelagem!")
            return
        
        X = self.cleaned_data[features]
        y = self.cleaned_data[target_column]
        
        # Verificar se é problema de classificação ou regressão
        is_classification = (y.dtype == 'object' or y.nunique() < 10)
        
        # Preparar dados
        if is_classification:
            le = LabelEncoder()
            y_encoded = le.fit_transform(y.astype(str))
            X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
            
            # Modelo de classificação
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            
            y_pred = model.predict(X_test)
            
            print(f"📊 RESULTADOS DA CLASSIFICAÇÃO:")
            print(f"  • Acurácia: {model.score(X_test, y_test):.3f}")
            print(f"  • Classes: {list(le.classes_)}")
            
            # Feature importance
            feature_importance = pd.DataFrame({
                'feature': features,
                'importance': model.feature_importances_
            }).sort_values('importance', ascending=False)
            
            print(f"\n🔝 Features mais importantes:")
            for _, row in feature_importance.head().iterrows():
                print(f"  • {row['feature']}: {row['importance']:.3f}")
        
        else:
            # Problema de regressão
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Modelo de regressão
            model = LinearRegression()
            model.fit(X_train, y_train)
            
            y_pred = model.predict(X_test)
            r2 = r2_score(y_test, y_pred)
            
            print(f"📊 RESULTADOS DA REGRESSÃO:")
            print(f"  • R² Score: {r2:.3f}")
            print(f"  • RMSE: {np.sqrt(np.mean((y_test - y_pred)**2)):.3f}")
            
            # Coeficientes
            coefficients = pd.DataFrame({
                'feature': features,
                'coefficient': model.coef_
            }).sort_values('coefficient', key=abs, ascending=False)
            
            print(f"\n📈 Coeficientes mais importantes:")
            for _, row in coefficients.head().iterrows():
                print(f"  • {row['feature']}: {row['coefficient']:.3f}")
        
        self.analysis_results['model'] = model
        self.analysis_results['model_type'] = 'classification' if is_classification else 'regression'
    
    def generate_insights(self):
        """Gera insights automaticamente baseado na análise"""
        print("\n💡 INSIGHTS GERADOS")
        print("=" * 25)
        
        if not self.analysis_results:
            print("❌ Execute as análises primeiro!")
            return
        
        insights = []
        
        # Insights de qualidade dos dados
        if self.data is not None and self.cleaned_data is not None:
            data_quality = (len(self.cleaned_data) / len(self.data)) * 100
            if data_quality < 90:
                insights.append(f"⚠️  Qualidade dos dados: {data_quality:.1f}% dos dados originais foram mantidos após limpeza")
            else:
                insights.append(f"✅ Boa qualidade dos dados: {data_quality:.1f}% dos dados mantidos")
        
        # Insights de correlações
        if 'correlation_matrix' in self.analysis_results:
            corr_matrix = self.analysis_results['correlation_matrix']
            mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
            corr_values = corr_matrix.mask(mask).unstack().dropna()
            
            strong_correlations = corr_values[corr_values.abs() > 0.7]
            if len(strong_correlations) > 0:
                insights.append(f"🔗 Encontradas {len(strong_correlations)} correlações fortes (>0.7)")
                
                strongest = strong_correlations.abs().idxmax()
                insights.append(f"💪 Correlação mais forte: {strongest[0]} ↔ {strongest[1]} ({strong_correlations[strongest]:.3f})")
        
        # Insights estatísticos
        if 'descriptive_stats' in self.analysis_results:
            stats = self.analysis_results['descriptive_stats']
            
            for col, col_stats in stats.items():
                # Assimetria
                if abs(col_stats['skewness']) > 1:
                    direction = "positiva" if col_stats['skewness'] > 0 else "negativa"
                    insights.append(f"📊 {col}: Distribuição com assimetria {direction} acentuada ({col_stats['skewness']:.2f})")
                
                # Variabilidade
                cv = col_stats['std'] / col_stats['mean'] if col_stats['mean'] != 0 else 0
                if cv > 1:
                    insights.append(f"📈 {col}: Alta variabilidade (CV = {cv:.2f})")
        
        # Insights do modelo
        if 'model' in self.analysis_results:
            model_type = self.analysis_results['model_type']
            if model_type == 'classification':
                accuracy = self.analysis_results.get('accuracy', 'N/A')
                insights.append(f"🎯 Modelo de classificação com acurácia de {accuracy}")
            else:
                r2 = self.analysis_results.get('r2_score', 'N/A')
                insights.append(f"📈 Modelo de regressão explica {r2*100:.1f}% da variância")
        
        # Salvar insights
        self.insights = insights
        
        # Mostrar insights
        for i, insight in enumerate(insights, 1):
            print(f"{i:2d}. {insight}")
        
        return insights
    
    def export_report(self, filename="analysis_report.html"):
        """Exporta relatório completo em HTML"""
        print(f"\n📄 EXPORTANDO RELATÓRIO: {filename}")
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Relatório de Análise de Dados - {self.name}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                h1, h2, h3 {{ color: #2c3e50; }}
                .insight {{ background-color: #f8f9fa; padding: 10px; margin: 10px 0; border-left: 4px solid #007bff; }}
                .stats {{ background-color: #ffffff; padding: 15px; border: 1px solid #dee2e6; margin: 10px 0; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>📊 Relatório de Análise de Dados</h1>
            <h2>🔍 Informações Gerais</h2>
            <div class="stats">
                <p><strong>Pipeline:</strong> {self.name}</p>
                <p><strong>Data da Análise:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
        """
        
        if self.data is not None:
            html_content += f"""
                <p><strong>Dados Originais:</strong> {self.data.shape[0]} linhas, {self.data.shape[1]} colunas</p>
            """
        
        if self.cleaned_data is not None:
            html_content += f"""
                <p><strong>Dados Limpos:</strong> {self.cleaned_data.shape[0]} linhas, {self.cleaned_data.shape[1]} colunas</p>
            """
        
        html_content += "</div>"
        
        # Adicionar insights
        if self.insights:
            html_content += "<h2>💡 Principais Insights</h2>"
            for insight in self.insights:
                html_content += f'<div class="insight">{insight}</div>'
        
        # Adicionar estatísticas
        if 'descriptive_stats' in self.analysis_results:
            html_content += "<h2>📊 Estatísticas Descritivas</h2>"
            html_content += "<table><tr><th>Variável</th><th>Média</th><th>Mediana</th><th>Desvio Padrão</th><th>Assimetria</th></tr>"
            
            for col, stats in self.analysis_results['descriptive_stats'].items():
                html_content += f"""
                <tr>
                    <td>{col}</td>
                    <td>{stats['mean']:.2f}</td>
                    <td>{stats['median']:.2f}</td>
                    <td>{stats['std']:.2f}</td>
                    <td>{stats['skewness']:.2f}</td>
                </tr>
                """
            
            html_content += "</table>"
        
        html_content += """
            </body>
            </html>
        """
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Relatório salvo em: {filename}")

def generate_sample_ecommerce_data():
    """Gera dataset de exemplo de e-commerce"""
    print("🛒 Gerando dataset de e-commerce...")
    
    np.random.seed(42)
    n_customers = 5000
    n_orders = 15000
    
    # Dados de clientes
    customers = pd.DataFrame({
        'customer_id': [f"CUST_{i:05d}" for i in range(1, n_customers + 1)],
        'age': np.random.randint(18, 80, n_customers),
        'gender': np.random.choice(['M', 'F'], n_customers),
        'city': np.random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília', 
                                 'Salvador', 'Curitiba', 'Porto Alegre', 'Recife'], n_customers),
        'registration_date': pd.date_range('2020-01-01', '2024-12-31', periods=n_customers),
        'customer_segment': np.random.choice(['Premium', 'Standard', 'Basic'], n_customers, p=[0.2, 0.5, 0.3])
    })
    
    # Dados de pedidos
    orders = pd.DataFrame({
        'order_id': [f"ORD_{i:06d}" for i in range(1, n_orders + 1)],
        'customer_id': np.random.choice(customers['customer_id'], n_orders),
        'order_date': pd.date_range('2021-01-01', '2025-01-01', periods=n_orders),
        'product_category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports'], n_orders),
        'order_value': np.random.exponential(100, n_orders) + 20,  # Distribuição exponencial
        'shipping_cost': np.random.uniform(5, 50, n_orders),
        'discount_applied': np.random.uniform(0, 0.3, n_orders),
        'payment_method': np.random.choice(['Credit Card', 'Debit Card', 'PIX', 'Boleto'], n_orders),
        'delivery_days': np.random.poisson(5, n_orders) + 1
    })
    
    # Adicionar algumas correlações realistas
    # Clientes premium tendem a comprar mais
    premium_mask = orders['customer_id'].isin(
        customers[customers['customer_segment'] == 'Premium']['customer_id']
    )
    orders.loc[premium_mask, 'order_value'] *= 1.5
    
    # Eletrônicos são mais caros
    electronics_mask = orders['product_category'] == 'Electronics'
    orders.loc[electronics_mask, 'order_value'] *= 1.8
    
    # Adicionar alguns missing values
    orders.loc[np.random.choice(orders.index, 100), 'shipping_cost'] = np.nan
    customers.loc[np.random.choice(customers.index, 50), 'age'] = np.nan
    
    # Merge dos dados
    ecommerce_data = orders.merge(customers, on='customer_id', how='left')
    
    print(f"✅ Dataset gerado: {len(ecommerce_data)} registros")
    return ecommerce_data

def demonstrate_complete_pipeline():
    """Demonstra pipeline completo de análise"""
    print("🔄 DEMONSTRAÇÃO: Pipeline Completo de Análise")
    print("=" * 55)
    
    # 1. Gerar dados de exemplo
    data = generate_sample_ecommerce_data()
    
    # 2. Criar pipeline
    pipeline = DataAnalysisPipeline("E-commerce Analysis")
    
    # 3. Carregar dados
    pipeline.load_data(data, "dataframe")
    
    # 4. Exploração inicial
    pipeline.explore_data()
    
    # 5. Limpeza de dados
    cleaning_strategies = {
        'remove_duplicates': True,
        'handle_missing': 'median',
        'remove_outliers': False,
        'normalize_text': True
    }
    pipeline.clean_data(cleaning_strategies)
    
    # 6. Análise estatística
    pipeline.statistical_analysis()
    
    # 7. Visualizações
    pipeline.create_visualizations()
    
    # 8. Análise avançada
    pipeline.advanced_analysis(target_column='order_value')
    
    # 9. Gerar insights
    insights = pipeline.generate_insights()
    
    # 10. Exportar relatório
    pipeline.export_report("ecommerce_analysis_report.html")
    
    return pipeline

if __name__ == "__main__":
    print("📊 AULA 05: Pipeline Completo de Análise de Dados")
    print("=" * 60)
    print("Professor: Vagner Cordeiro")
    print("Curso: Tópicos de Big Data em Python")
    print("=" * 60)
    
    try:
        # Executar demonstração completa
        pipeline = demonstrate_complete_pipeline()
        
        print("\n✅ PIPELINE CONCLUÍDO!")
        print("\n📚 CONCEITOS DEMONSTRADOS:")
        print("  • Carregamento e exploração de dados")
        print("  • Limpeza e tratamento de missing values")
        print("  • Análise estatística descritiva")
        print("  • Visualizações exploratórias")
        print("  • Modelagem preditiva básica")
        print("  • Geração automática de insights")
        print("  • Exportação de relatórios")
        
        print("\n🎯 PRÓXIMA AULA:")
        print("  Aula 06: Introdução e Arquitetura do Hadoop")
        
    except KeyboardInterrupt:
        print("\n⏹️  Análise interrompida pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro durante a análise: {e}")
        import traceback
        traceback.print_exc()
