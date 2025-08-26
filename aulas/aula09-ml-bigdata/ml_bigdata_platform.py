#!/usr/bin/env python3
"""
Aula 09: Machine Learning com Big Data
Professor: Vagner Cordeiro
Curso: Tópicos de Big Data em Python

Plataforma completa de Machine Learning para Big Data usando PySpark
e técnicas avançadas de processamento distribuído.
"""

import os
import sys
import random
import json
import time
import math
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
import warnings
warnings.filterwarnings('ignore')

# Importações com tratamento de erros
try:
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, when, isnan, isnull, count, mean, stddev, max as spark_max, min as spark_min
    from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, BooleanType
    from pyspark.ml.feature import VectorAssembler, StandardScaler, StringIndexer, OneHotEncoder
    from pyspark.ml.classification import LogisticRegression, RandomForestClassifier, GBTClassifier
    from pyspark.ml.regression import LinearRegression, RandomForestRegressor
    from pyspark.ml.clustering import KMeans
    from pyspark.ml.recommendation import ALS
    from pyspark.ml.evaluation import BinaryClassificationEvaluator, RegressionEvaluator, ClusteringEvaluator
    from pyspark.ml import Pipeline
    PYSPARK_AVAILABLE = True
    print("✅ PySpark disponível")
except ImportError:
    print("⚠️ PySpark não está instalado. Usando simulação de conceitos.")
    PYSPARK_AVAILABLE = False

try:
    import pandas as pd
    import numpy as np
    PANDAS_AVAILABLE = True
    print("✅ Pandas e NumPy disponíveis")
except ImportError:
    print("⚠️ Pandas/NumPy não disponível. Funcionalidades limitadas.")
    PANDAS_AVAILABLE = False

try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    MATPLOTLIB_AVAILABLE = True
    print("✅ Matplotlib e Seaborn disponíveis")
except ImportError:
    print("⚠️ Matplotlib/Seaborn não disponível. Visualizações serão simuladas.")
    MATPLOTLIB_AVAILABLE = False

class BigDataMLPlatform:
    """Plataforma de Machine Learning para Big Data"""
    
    def __init__(self, app_name: str = "BigData ML Platform"):
        """Inicializa a plataforma"""
        self.app_name = app_name
        self.spark = None
        self.models = {}
        self.datasets = {}
        self.results = {}
        
        if PYSPARK_AVAILABLE:
            self._initialize_spark()
        else:
            print("🎭 Modo simulação: PySpark não disponível")
    
    def _initialize_spark(self) -> None:
        """Inicializa sessão Spark"""
        try:
            self.spark = SparkSession.builder \
                .appName(self.app_name) \
                .config("spark.sql.adaptive.enabled", "true") \
                .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
                .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
                .getOrCreate()
            
            self.spark.sparkContext.setLogLevel("WARN")
            print(f"✅ Spark inicializado: {self.spark.version}")
            
        except Exception as e:
            print(f"❌ Erro ao inicializar Spark: {e}")
            self.spark = None
    
    def generate_fraud_detection_data(self, num_transactions: int = 100000) -> Any:
        """Gera dataset sintético para detecção de fraude"""
        print(f"📊 Gerando {num_transactions:,} transações para detecção de fraude...")
        
        if not PYSPARK_AVAILABLE:
            return self._simulate_fraud_data(num_transactions)
        
        # Schema dos dados
        schema = StructType([
            StructField("transaction_id", StringType(), True),
            StructField("user_id", StringType(), True),
            StructField("amount", DoubleType(), True),
            StructField("merchant", StringType(), True),
            StructField("category", StringType(), True),
            StructField("hour", IntegerType(), True),
            StructField("day_of_week", IntegerType(), True),
            StructField("is_weekend", BooleanType(), True),
            StructField("user_age", IntegerType(), True),
            StructField("account_age_days", IntegerType(), True),
            StructField("avg_amount_last_30_days", DoubleType(), True),
            StructField("transaction_count_today", IntegerType(), True),
            StructField("time_since_last_transaction_hours", DoubleType(), True),
            StructField("is_fraud", IntegerType(), True)  # Target variable
        ])
        
        # Gerar dados sintéticos
        data = []
        merchants = ['Amazon', 'Walmart', 'Target', 'Costco', 'Gas Station', 'Restaurant', 'ATM']
        categories = ['Shopping', 'Groceries', 'Fuel', 'Dining', 'Cash', 'Entertainment']
        
        for i in range(num_transactions):
            # Probabilidade de fraude: 2%
            is_fraud = 1 if random.random() < 0.02 else 0
            
            # Transações fraudulentas têm padrões diferentes
            if is_fraud:
                amount = random.uniform(1000, 10000)  # Valores altos
                hour = random.choice([2, 3, 4, 23])  # Horários suspeitos
                user_age = random.randint(18, 80)
                account_age = random.randint(1, 30)  # Contas novas
                avg_amount = random.uniform(50, 200)
                tx_count_today = random.randint(5, 20)  # Muitas transações
                time_since_last = random.uniform(0.1, 2)  # Transações rápidas
            else:
                amount = math.exp(random.gauss(4, 1.5))  # Distribuição lognormal simulada
                hour = random.randint(6, 22)  # Horários normais
                user_age = random.randint(18, 80)
                account_age = random.randint(30, 2000)  # Contas estabelecidas
                avg_amount = math.exp(random.gauss(4, 1))  # Lognormal simulada
                tx_count_today = random.randint(1, 5)
                time_since_last = random.uniform(2, 48)
            
            data.append((
                f"tx_{i:08d}",
                f"user_{random.randint(1, 10000):06d}",
                round(amount, 2),
                random.choice(merchants),
                random.choice(categories),
                hour,
                random.randint(0, 6),  # 0=Sunday
                hour in [0, 6],  # Weekend
                user_age,
                account_age,
                round(avg_amount, 2),
                tx_count_today,
                round(time_since_last, 2),
                is_fraud
            ))
        
        if self.spark:
            df = self.spark.createDataFrame(data, schema)
            print(f"✅ Dataset criado: {df.count():,} linhas, {len(df.columns)} colunas")
            return df
        else:
            print("✅ Schema definido para dados simulados")
            return data
    
    def _simulate_fraud_data(self, num_transactions: int) -> Dict[str, List]:
        """Simula dados de fraude quando PySpark não está disponível"""
        print("🎭 Simulando dados de detecção de fraude...")
        
        data = {
            'transaction_id': [f"tx_{i:08d}" for i in range(num_transactions)],
            'amount': [math.exp(random.gauss(4, 1.5)) for _ in range(num_transactions)],
            'is_fraud': [1 if random.random() < 0.02 else 0 for _ in range(num_transactions)],
            'hour': [random.randint(6, 22) for _ in range(num_transactions)],
            'merchant': [random.choice(['Amazon', 'Walmart', 'Target']) for _ in range(num_transactions)]
        }
        
        fraud_count = sum(data['is_fraud'])
        print(f"✅ Dados simulados: {num_transactions:,} transações, {fraud_count} fraudes ({fraud_count/num_transactions*100:.2f}%)")
        
        return data
    
    def generate_recommendation_data(self, num_users: int = 10000, num_items: int = 1000, num_ratings: int = 100000) -> Any:
        """Gera dataset sintético para sistema de recomendação"""
        print(f"📊 Gerando dados de recomendação: {num_users} usuários, {num_items} itens, {num_ratings} avaliações...")
        
        if not PYSPARK_AVAILABLE:
            return self._simulate_recommendation_data(num_users, num_items, num_ratings)
        
        # Gerar ratings com base em preferências dos usuários
        data = []
        
        for _ in range(num_ratings):
            user_id = random.randint(1, num_users)
            item_id = random.randint(1, num_items)
            
            # Simular preferências: alguns usuários gostam de categorias específicas
            user_preference = user_id % 5  # 5 tipos de usuários
            item_category = item_id % 5    # 5 categorias de itens
            
            if user_preference == item_category:
                # Usuário gosta desta categoria
                base_rating = random.uniform(3.5, 5.0)
            else:
                # Rating neutro/baixo
                base_rating = random.uniform(1.0, 3.5)
            
            rating = max(1, min(5, round(base_rating)))
            data.append((user_id, item_id, float(rating)))
        
        # Schema
        schema = StructType([
            StructField("user_id", IntegerType(), True),
            StructField("item_id", IntegerType(), True),
            StructField("rating", DoubleType(), True),
        ])
        
        if self.spark:
            df = self.spark.createDataFrame(data, schema)
            print(f"✅ Dataset de recomendação criado: {df.count():,} avaliações")
            return df
        else:
            print("✅ Dados de recomendação simulados")
            return data
    
    def _simulate_recommendation_data(self, num_users: int, num_items: int, num_ratings: int) -> Dict[str, List]:
        """Simula dados de recomendação"""
        print("🎭 Simulando dados de recomendação...")
        
        data = {
            'user_id': [random.randint(1, num_users) for _ in range(num_ratings)],
            'item_id': [random.randint(1, num_items) for _ in range(num_ratings)],
            'rating': [random.uniform(1, 5) for _ in range(num_ratings)]
        }
        
        print(f"✅ Dados simulados: {num_ratings:,} avaliações")
        return data
    
    def fraud_detection_pipeline(self, data: Any) -> Dict[str, Any]:
        """Pipeline de detecção de fraude"""
        print("\n🔍 PIPELINE DE DETECÇÃO DE FRAUDE")
        print("=" * 50)
        
        if not PYSPARK_AVAILABLE:
            return self._simulate_fraud_detection()
        
        try:
            # 1. Análise exploratória
            print("📊 Análise exploratória dos dados...")
            self._analyze_fraud_data(data)
            
            # 2. Preparação dos dados
            print("🔧 Preparando features...")
            prepared_data = self._prepare_fraud_features(data)
            
            # 3. Divisão treino/teste
            train_data, test_data = prepared_data.randomSplit([0.8, 0.2], seed=42)
            
            print(f"📊 Dados de treino: {train_data.count():,} registros")
            print(f"📊 Dados de teste: {test_data.count():,} registros")
            
            # 4. Treinar modelos
            models_results = {}
            
            # Logistic Regression
            lr_result = self._train_fraud_logistic_regression(train_data, test_data)
            models_results['logistic_regression'] = lr_result
            
            # Random Forest
            rf_result = self._train_fraud_random_forest(train_data, test_data)
            models_results['random_forest'] = rf_result
            
            # GBT
            gbt_result = self._train_fraud_gbt(train_data, test_data)
            models_results['gradient_boosting'] = gbt_result
            
            # 5. Comparar modelos
            best_model = self._compare_fraud_models(models_results)
            
            return {
                'models': models_results,
                'best_model': best_model,
                'train_count': train_data.count(),
                'test_count': test_data.count()
            }
            
        except Exception as e:
            print(f"❌ Erro no pipeline de fraude: {e}")
            return self._simulate_fraud_detection()
    
    def _simulate_fraud_detection(self) -> Dict[str, Any]:
        """Simula resultados de detecção de fraude"""
        print("🎭 Simulando detecção de fraude...")
        
        results = {
            'logistic_regression': {'auc': 0.92, 'precision': 0.85, 'recall': 0.78},
            'random_forest': {'auc': 0.95, 'precision': 0.89, 'recall': 0.83},
            'gradient_boosting': {'auc': 0.96, 'precision': 0.91, 'recall': 0.85}
        }
        
        print("📈 Resultados simulados:")
        for model, metrics in results.items():
            print(f"   {model}: AUC={metrics['auc']:.3f}, Precision={metrics['precision']:.3f}, Recall={metrics['recall']:.3f}")
        
        return {'models': results, 'best_model': 'gradient_boosting'}
    
    def _analyze_fraud_data(self, data: Any) -> None:
        """Analisa dados de fraude"""
        print("🔍 Analisando distribuição de fraudes...")
        
        # Contagem de fraudes
        fraud_stats = data.groupBy("is_fraud").count().collect()
        for row in fraud_stats:
            fraud_type = "Fraude" if row['is_fraud'] == 1 else "Normal"
            print(f"   {fraud_type}: {row['count']:,} transações")
        
        # Estatísticas por valor
        print("💰 Análise por valor de transação...")
        data.groupBy("is_fraud").agg(
            mean("amount").alias("avg_amount"),
            stddev("amount").alias("std_amount")
        ).show()
    
    def _prepare_fraud_features(self, data: Any) -> Any:
        """Prepara features para detecção de fraude"""
        
        # Selecionar features numéricas
        feature_cols = [
            "amount", "hour", "day_of_week", "user_age", "account_age_days",
            "avg_amount_last_30_days", "transaction_count_today", 
            "time_since_last_transaction_hours"
        ]
        
        # Assembler
        assembler = VectorAssembler(
            inputCols=feature_cols,
            outputCol="features"
        )
        
        # Scaler
        scaler = StandardScaler(
            inputCol="features",
            outputCol="scaled_features",
            withStd=True,
            withMean=True
        )
        
        # Pipeline de preparação
        prep_pipeline = Pipeline(stages=[assembler, scaler])
        prep_model = prep_pipeline.fit(data)
        
        return prep_model.transform(data)
    
    def _train_fraud_logistic_regression(self, train_data: Any, test_data: Any) -> Dict[str, float]:
        """Treina modelo de regressão logística"""
        print("🤖 Treinando Regressão Logística...")
        
        lr = LogisticRegression(
            featuresCol="scaled_features",
            labelCol="is_fraud",
            maxIter=100
        )
        
        lr_model = lr.fit(train_data)
        predictions = lr_model.transform(test_data)
        
        # Avaliação
        evaluator = BinaryClassificationEvaluator(
            labelCol="is_fraud",
            rawPredictionCol="rawPrediction",
            metricName="areaUnderROC"
        )
        
        auc = evaluator.evaluate(predictions)
        print(f"   AUC: {auc:.4f}")
        
        return {'auc': auc, 'model': lr_model}
    
    def _train_fraud_random_forest(self, train_data: Any, test_data: Any) -> Dict[str, float]:
        """Treina modelo Random Forest"""
        print("🌳 Treinando Random Forest...")
        
        rf = RandomForestClassifier(
            featuresCol="scaled_features",
            labelCol="is_fraud",
            numTrees=100
        )
        
        rf_model = rf.fit(train_data)
        predictions = rf_model.transform(test_data)
        
        evaluator = BinaryClassificationEvaluator(
            labelCol="is_fraud",
            rawPredictionCol="rawPrediction",
            metricName="areaUnderROC"
        )
        
        auc = evaluator.evaluate(predictions)
        print(f"   AUC: {auc:.4f}")
        
        return {'auc': auc, 'model': rf_model}
    
    def _train_fraud_gbt(self, train_data: Any, test_data: Any) -> Dict[str, float]:
        """Treina modelo Gradient Boosting"""
        print("⚡ Treinando Gradient Boosting...")
        
        gbt = GBTClassifier(
            featuresCol="scaled_features",
            labelCol="is_fraud",
            maxIter=100
        )
        
        gbt_model = gbt.fit(train_data)
        predictions = gbt_model.transform(test_data)
        
        evaluator = BinaryClassificationEvaluator(
            labelCol="is_fraud",
            rawPredictionCol="rawPrediction",
            metricName="areaUnderROC"
        )
        
        auc = evaluator.evaluate(predictions)
        print(f"   AUC: {auc:.4f}")
        
        return {'auc': auc, 'model': gbt_model}
    
    def _compare_fraud_models(self, models_results: Dict) -> str:
        """Compara modelos de fraude"""
        print("\n📊 COMPARAÇÃO DOS MODELOS")
        print("-" * 30)
        
        best_auc = 0
        best_model = ""
        
        for model_name, result in models_results.items():
            auc = result['auc']
            print(f"{model_name:20}: AUC = {auc:.4f}")
            
            if auc > best_auc:
                best_auc = auc
                best_model = model_name
        
        print(f"\n🏆 Melhor modelo: {best_model} (AUC = {best_auc:.4f})")
        return best_model
    
    def recommendation_pipeline(self, data: Any) -> Dict[str, Any]:
        """Pipeline de sistema de recomendação"""
        print("\n🎯 PIPELINE DE SISTEMA DE RECOMENDAÇÃO")
        print("=" * 50)
        
        if not PYSPARK_AVAILABLE:
            return self._simulate_recommendation_system()
        
        try:
            # 1. Análise dos dados
            print("📊 Análise dos dados de rating...")
            self._analyze_recommendation_data(data)
            
            # 2. Dividir dados
            train_data, test_data = data.randomSplit([0.8, 0.2], seed=42)
            
            # 3. Treinar modelo ALS
            print("🤖 Treinando modelo de Collaborative Filtering (ALS)...")
            
            als = ALS(
                maxIter=10,
                regParam=0.1,
                userCol="user_id",
                itemCol="item_id",
                ratingCol="rating",
                coldStartStrategy="drop"
            )
            
            als_model = als.fit(train_data)
            
            # 4. Fazer predições
            predictions = als_model.transform(test_data)
            
            # 5. Avaliar modelo
            evaluator = RegressionEvaluator(
                metricName="rmse",
                labelCol="rating",
                predictionCol="prediction"
            )
            
            rmse = evaluator.evaluate(predictions)
            print(f"📈 RMSE: {rmse:.4f}")
            
            # 6. Gerar recomendações
            print("🎯 Gerando recomendações...")
            user_recs = als_model.recommendForAllUsers(10)
            item_recs = als_model.recommendForAllItems(10)
            
            print(f"✅ Recomendações geradas para {user_recs.count()} usuários")
            
            return {
                'model': als_model,
                'rmse': rmse,
                'user_recommendations': user_recs,
                'item_recommendations': item_recs
            }
            
        except Exception as e:
            print(f"❌ Erro no pipeline de recomendação: {e}")
            return self._simulate_recommendation_system()
    
    def _simulate_recommendation_system(self) -> Dict[str, Any]:
        """Simula sistema de recomendação"""
        print("🎭 Simulando sistema de recomendação...")
        
        rmse = 0.87
        print(f"📈 RMSE simulado: {rmse:.4f}")
        print("✅ Recomendações simuladas para 8000 usuários")
        
        return {'rmse': rmse, 'users_with_recs': 8000}
    
    def _analyze_recommendation_data(self, data: Any) -> None:
        """Analisa dados de recomendação"""
        print("📊 Estatísticas dos ratings:")
        
        data.describe("rating").show()
        
        print("👥 Usuários mais ativos:")
        data.groupBy("user_id").count().orderBy(col("count").desc()).limit(5).show()
        
        print("📱 Itens mais avaliados:")
        data.groupBy("item_id").count().orderBy(col("count").desc()).limit(5).show()
    
    def clustering_pipeline(self, data: Any, k: int = 5) -> Dict[str, Any]:
        """Pipeline de clustering de usuários"""
        print(f"\n🎯 PIPELINE DE CLUSTERING (K={k})")
        print("=" * 50)
        
        if not PYSPARK_AVAILABLE:
            return self._simulate_clustering(k)
        
        try:
            # Preparar features para clustering
            # Vamos usar estatísticas dos usuários como features
            print("🔧 Preparando features de usuário...")
            
            user_features = data.groupBy("user_id").agg(
                count("rating").alias("num_ratings"),
                mean("rating").alias("avg_rating"),
                stddev("rating").alias("std_rating")
            ).fillna(0)
            
            # Preparar features para clustering
            feature_cols = ["num_ratings", "avg_rating", "std_rating"]
            assembler = VectorAssembler(
                inputCols=feature_cols,
                outputCol="features"
            )
            
            user_features_assembled = assembler.transform(user_features)
            
            # Aplicar K-Means
            print(f"🤖 Aplicando K-Means com {k} clusters...")
            kmeans = KMeans(k=k, seed=42)
            kmeans_model = kmeans.fit(user_features_assembled)
            
            # Fazer predições
            clustered_users = kmeans_model.transform(user_features_assembled)
            
            # Analisar clusters
            print("📊 Análise dos clusters:")
            cluster_analysis = clustered_users.groupBy("prediction").agg(
                count("user_id").alias("num_users"),
                mean("num_ratings").alias("avg_num_ratings"),
                mean("avg_rating").alias("avg_avg_rating")
            ).orderBy("prediction")
            
            cluster_analysis.show()
            
            # Calcular métricas
            evaluator = ClusteringEvaluator()
            silhouette = evaluator.evaluate(clustered_users)
            print(f"📈 Silhouette Score: {silhouette:.4f}")
            
            return {
                'model': kmeans_model,
                'clustered_data': clustered_users,
                'silhouette_score': silhouette,
                'num_clusters': k
            }
            
        except Exception as e:
            print(f"❌ Erro no clustering: {e}")
            return self._simulate_clustering(k)
    
    def _simulate_clustering(self, k: int) -> Dict[str, Any]:
        """Simula clustering"""
        print("🎭 Simulando clustering de usuários...")
        
        silhouette = 0.65
        print(f"📈 Silhouette Score simulado: {silhouette:.4f}")
        print(f"✅ {k} clusters criados")
        
        # Simular distribuição dos clusters
        for i in range(k):
            users_in_cluster = random.randint(1500, 2500)
            avg_ratings = random.uniform(2.5, 4.5)
            print(f"   Cluster {i}: {users_in_cluster} usuários, rating médio: {avg_ratings:.2f}")
        
        return {'silhouette_score': silhouette, 'num_clusters': k}
    
    def run_complete_demo(self):
        """Executa demonstração completa da plataforma"""
        print("🚀 DEMONSTRAÇÃO COMPLETA: Big Data ML Platform")
        print("=" * 60)
        
        try:
            # 1. Detecção de Fraude
            print("\n1️⃣ DETECÇÃO DE FRAUDE")
            fraud_data = self.generate_fraud_detection_data(50000)
            fraud_results = self.fraud_detection_pipeline(fraud_data)
            self.results['fraud_detection'] = fraud_results
            
            # 2. Sistema de Recomendação
            print("\n2️⃣ SISTEMA DE RECOMENDAÇÃO")
            rec_data = self.generate_recommendation_data(5000, 500, 50000)
            rec_results = self.recommendation_pipeline(rec_data)
            self.results['recommendation'] = rec_results
            
            # 3. Clustering de Usuários
            print("\n3️⃣ CLUSTERING DE USUÁRIOS")
            clustering_results = self.clustering_pipeline(rec_data, k=5)
            self.results['clustering'] = clustering_results
            
            # 4. Relatório Final
            self._generate_final_report()
            
        except Exception as e:
            print(f"❌ Erro na demonstração: {e}")
        
        finally:
            self.stop()
    
    def _generate_final_report(self):
        """Gera relatório final"""
        print("\n📋 RELATÓRIO FINAL")
        print("=" * 50)
        
        if 'fraud_detection' in self.results:
            fraud_res = self.results['fraud_detection']
            if 'best_model' in fraud_res:
                print(f"🔍 Detecção de Fraude: Melhor modelo = {fraud_res['best_model']}")
        
        if 'recommendation' in self.results:
            rec_res = self.results['recommendation']
            if 'rmse' in rec_res:
                print(f"🎯 Recomendação: RMSE = {rec_res['rmse']:.4f}")
        
        if 'clustering' in self.results:
            cluster_res = self.results['clustering']
            if 'silhouette_score' in cluster_res:
                print(f"🎯 Clustering: Silhouette = {cluster_res['silhouette_score']:.4f}")
        
        print(f"\n✅ Demonstração concluída com sucesso!")
        
        # Salvar resultados
        self._save_results()
    
    def _save_results(self):
        """Salva resultados em arquivo JSON"""
        try:
            results_summary = {
                'timestamp': datetime.now().isoformat(),
                'platform': self.app_name,
                'results': {}
            }
            
            for task, result in self.results.items():
                # Extrair apenas métricas (não objetos Spark)
                if isinstance(result, dict):
                    summary = {}
                    for key, value in result.items():
                        if isinstance(value, (int, float, str, bool)):
                            summary[key] = value
                    results_summary['results'][task] = summary
            
            filename = f"ml_bigdata_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(results_summary, f, indent=2, ensure_ascii=False)
            
            print(f"💾 Resultados salvos em: {filename}")
            
        except Exception as e:
            print(f"⚠️ Erro ao salvar resultados: {e}")
    
    def stop(self):
        """Para a sessão Spark"""
        if self.spark:
            self.spark.stop()
            print("🔒 Sessão Spark finalizada")

def demonstrate_ml_concepts():
    """Demonstra conceitos fundamentais de ML com Big Data"""
    print("\n📚 CONCEITOS FUNDAMENTAIS: ML + BIG DATA")
    print("=" * 60)
    
    concepts = {
        "🤖 Machine Learning Distribuído": [
            "Paralelização: Divisão de dados e processamento em clusters",
            "Algoritmos escaláveis: Gradient Descent distribuído",
            "Feature Engineering: Transformações em larga escala",
            "Model Training: Treinamento paralelo e iterativo",
            "Hyperparameter Tuning: Busca distribuída de parâmetros"
        ],
        
        "📊 Tipos de Problemas": [
            "Classificação: Detecção de fraude, spam, categorização",
            "Regressão: Predição de preços, demanda, valores",
            "Clustering: Segmentação de clientes, anomalias",
            "Recomendação: Sistemas de recomendação colaborativos",
            "Processamento de Linguagem: Análise de sentimentos"
        ],
        
        "⚡ Desafios de Escala": [
            "Volume: Terabytes/Petabytes de dados de treinamento",
            "Velocidade: Treinamento e inferência em tempo real",
            "Variedade: Dados estruturados, texto, imagens, streams",
            "Memória: Modelos que não cabem em uma máquina",
            "Distribuição: Coordenação entre múltiplos nós"
        ],
        
        "🛠️ Ferramentas e Frameworks": [
            "Apache Spark MLlib: ML distribuído integrado",
            "TensorFlow: Deep learning distribuído",
            "Horovod: Treinamento distribuído para DL",
            "Ray: ML distribuído moderno",
            "Dask: Computação paralela em Python"
        ]
    }
    
    for category, items in concepts.items():
        print(f"\n{category}")
        print("-" * 50)
        for item in items:
            print(f"  • {item}")

def main():
    """Função principal"""
    print("🎯 AULA 09: Machine Learning com Big Data")
    print("Autor: Professor Vagner Cordeiro")
    print("=" * 60)
    
    # Demonstrar conceitos
    demonstrate_ml_concepts()
    
    # Executar demonstração prática
    platform = BigDataMLPlatform("Aula09_ML_BigData")
    
    try:
        platform.run_complete_demo()
    except KeyboardInterrupt:
        print("\n⚠️ Demonstração interrompida pelo usuário")
    except Exception as e:
        print(f"❌ Erro na demonstração: {e}")
    finally:
        platform.stop()
    
    print("\n✅ Aula concluída! Conceitos de ML com Big Data demonstrados.")

if __name__ == "__main__":
    main()
