#!/usr/bin/env python3
"""
Machine Learning with Big Data - Spark MLlib Implementation
Sistema completo de ML distribuído para análise de grandes volumes de dados
"""

import os
import sys
import logging
import json
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
from typing import List, Dict, Tuple, Any

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import *
    from pyspark.sql.types import *
    from pyspark.ml import Pipeline
    from pyspark.ml.feature import *
    from pyspark.ml.classification import *
    from pyspark.ml.regression import *
    from pyspark.ml.clustering import *
    from pyspark.ml.recommendation import *
    from pyspark.ml.evaluation import *
    from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
    from pyspark.mllib.stat import Statistics
except ImportError:
    logger.error("PySpark MLlib não encontrado. Execute: pip install pyspark")
    sys.exit(1)

class BigDataMLPlatform:
    """Plataforma de Machine Learning para Big Data"""
    
    def __init__(self, app_name="BigData-ML-Platform"):
        self.spark = self._create_spark_session(app_name)
        self.models = {}
        self.pipelines = {}
        self.evaluation_results = {}
    
    def _create_spark_session(self, app_name):
        """Criar sessão Spark otimizada para ML"""
        return SparkSession.builder \
            .appName(app_name) \
            .config("spark.sql.adaptive.enabled", "true") \
            .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
            .config("spark.ml.cache.enabled", "true") \
            .config("spark.executor.memory", "4g") \
            .config("spark.driver.memory", "2g") \
            .config("spark.executor.cores", "4") \
            .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
            .getOrCreate()
    
    def create_synthetic_datasets(self):
        """Criar datasets sintéticos para demonstração"""
        logger.info("🔄 Criando datasets sintéticos...")
        
        # 1. Dataset de Transações Financeiras (Detecção de Fraude)
        fraud_data = self._create_fraud_detection_dataset()
        
        # 2. Dataset de Ratings (Sistema de Recomendação)
        ratings_data = self._create_recommendation_dataset()
        
        # 3. Dataset de Reviews (Análise de Sentimento)
        reviews_data = self._create_sentiment_analysis_dataset()
        
        return {
            'fraud_detection': fraud_data,
            'recommendations': ratings_data,
            'sentiment_analysis': reviews_data
        }
    
    def _create_fraud_detection_dataset(self):
        """Criar dataset para detecção de fraudes"""
        logger.info("📊 Gerando dataset de transações financeiras...")
        
        # Schema
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
        np.random.seed(42)
        n_samples = 1000000  # 1 milhão de transações
        
        data = []
        categories = ["grocery", "gas", "restaurant", "retail", "online", "atm"]
        merchants = [f"merchant_{i}" for i in range(1000)]
        
        for i in range(n_samples):
            # Características normais vs fraudulentas
            is_fraud = np.random.choice([0, 1], p=[0.99, 0.01])  # 1% fraude
            
            if is_fraud:
                # Transações fraudulentas tendem a ter características específicas
                amount = np.random.lognormal(6, 2)  # Valores maiores
                hour = np.random.choice(range(24), p=[0.02]*6 + [0.03]*6 + [0.06]*12)  # Mais comuns à noite
                transaction_count_today = np.random.poisson(8)  # Mais transações
                time_since_last = np.random.exponential(0.5)  # Transações mais frequentes
            else:
                # Transações normais
                amount = np.random.lognormal(3.5, 1.2)
                hour = np.random.choice(range(24), p=[0.01]*6 + [0.05]*6 + [0.08]*12)  # Padrão normal
                transaction_count_today = np.random.poisson(2)
                time_since_last = np.random.exponential(8)
            
            day_of_week = np.random.randint(1, 8)
            is_weekend = day_of_week >= 6
            
            record = [
                f"txn_{i:07d}",
                f"user_{np.random.randint(1, 100000)}",
                round(amount, 2),
                np.random.choice(merchants),
                np.random.choice(categories),
                hour,
                day_of_week,
                is_weekend,
                np.random.randint(18, 80),  # user age
                np.random.randint(1, 3650),  # account age in days
                round(np.random.lognormal(4, 1), 2),  # avg amount last 30 days
                transaction_count_today,
                round(time_since_last, 2),
                is_fraud
            ]
            data.append(record)
        
        df = self.spark.createDataFrame(data, schema)
        df.cache()
        
        logger.info(f"Dataset de fraude criado: {df.count():,} transações")
        return df
    
    def _create_recommendation_dataset(self):
        """Criar dataset para sistema de recomendação"""
        logger.info("📊 Gerando dataset de ratings...")
        
        n_users = 10000
        n_items = 5000
        n_ratings = 500000
        
        # Gerar ratings com padrões realísticos
        data = []
        np.random.seed(42)
        
        for _ in range(n_ratings):
            user_id = np.random.randint(1, n_users + 1)
            item_id = np.random.randint(1, n_items + 1)
            
            # Simular preferências de usuários
            base_rating = np.random.normal(3.5, 1.2)
            rating = max(1, min(5, round(base_rating)))
            
            timestamp = datetime.now() - timedelta(days=np.random.randint(0, 365))
            
            data.append([user_id, item_id, float(rating), int(timestamp.timestamp())])
        
        schema = StructType([
            StructField("user_id", IntegerType(), True),
            StructField("item_id", IntegerType(), True),
            StructField("rating", DoubleType(), True),
            StructField("timestamp", IntegerType(), True)
        ])
        
        df = self.spark.createDataFrame(data, schema)
        df.cache()
        
        logger.info(f"Dataset de ratings criado: {df.count():,} ratings")
        return df
    
    def _create_sentiment_analysis_dataset(self):
        """Criar dataset para análise de sentimento"""
        logger.info("📊 Gerando dataset de reviews...")
        
        # Templates de reviews
        positive_reviews = [
            "This product is amazing! I love it so much and would definitely recommend it.",
            "Excellent quality and fast shipping. Very satisfied with this purchase.",
            "Outstanding customer service and great product quality. Five stars!",
            "Perfect item, exactly as described. Will buy again from this seller.",
            "Fantastic experience overall. The product exceeded my expectations."
        ]
        
        negative_reviews = [
            "Terrible quality, broke after one use. Complete waste of money.",
            "Poor customer service and delayed shipping. Very disappointed.",
            "Product doesn't match description. Requesting a refund immediately.",
            "Cheaply made and overpriced. Would not recommend to anyone.",
            "Worst purchase ever. Save your money and buy elsewhere."
        ]
        
        neutral_reviews = [
            "Product is okay, nothing special but does what it's supposed to do.",
            "Average quality for the price. Could be better but acceptable.",
            "It's fine, meets basic expectations but nothing extraordinary.",
            "Decent product, some pros and cons but overall satisfactory.",
            "Standard quality item, works as expected without any surprises."
        ]
        
        data = []
        n_reviews = 100000
        
        for i in range(n_reviews):
            sentiment = np.random.choice([0, 1, 2], p=[0.3, 0.5, 0.2])  # negative, positive, neutral
            
            if sentiment == 0:
                text = np.random.choice(negative_reviews)
                label = 0.0
            elif sentiment == 1:
                text = np.random.choice(positive_reviews)
                label = 1.0
            else:
                text = np.random.choice(neutral_reviews)
                label = 0.5
            
            data.append([f"review_{i}", text, label])
        
        schema = StructType([
            StructField("review_id", StringType(), True),
            StructField("text", StringType(), True),
            StructField("sentiment", DoubleType(), True)
        ])
        
        df = self.spark.createDataFrame(data, schema)
        df.cache()
        
        logger.info(f"Dataset de reviews criado: {df.count():,} reviews")
        return df

class FraudDetectionPipeline:
    """Pipeline de detecção de fraudes usando Spark MLlib"""
    
    def __init__(self, spark_session):
        self.spark = spark_session
        self.pipeline = None
        self.model = None
        self.feature_cols = [
            "amount", "hour", "day_of_week", "user_age", "account_age_days",
            "avg_amount_last_30_days", "transaction_count_today", 
            "time_since_last_transaction_hours"
        ]
    
    def create_features(self, df):
        """Criar features para o modelo"""
        logger.info("🔧 Criando features para detecção de fraudes...")
        
        # Feature engineering
        df_features = df.withColumn("amount_log", log(col("amount") + 1)) \
                       .withColumn("is_high_amount", (col("amount") > 1000).cast("double")) \
                       .withColumn("is_night_transaction", 
                                 ((col("hour") >= 22) | (col("hour") <= 6)).cast("double")) \
                       .withColumn("transaction_frequency", 
                                 col("transaction_count_today") / 24.0)
        
        # Adicionar features categóricas
        category_indexer = StringIndexer(inputCol="category", outputCol="category_index")
        merchant_indexer = StringIndexer(inputCol="merchant", outputCol="merchant_index")
        
        # One-hot encoding
        category_encoder = OneHotEncoder(inputCol="category_index", outputCol="category_vec")
        merchant_encoder = OneHotEncoder(inputCol="merchant_index", outputCol="merchant_vec")
        
        # Assembler para features numéricas
        numeric_features = self.feature_cols + ["amount_log", "is_high_amount", 
                                               "is_night_transaction", "transaction_frequency"]
        
        feature_assembler = VectorAssembler(
            inputCols=numeric_features + ["category_vec", "merchant_vec"],
            outputCol="features"
        )
        
        # Scaler para normalização
        scaler = StandardScaler(inputCol="features", outputCol="scaled_features", 
                              withStd=True, withMean=True)
        
        # Pipeline de feature engineering
        feature_pipeline = Pipeline(stages=[
            category_indexer, merchant_indexer,
            category_encoder, merchant_encoder,
            feature_assembler, scaler
        ])
        
        return feature_pipeline, df_features
    
    def train_model(self, df):
        """Treinar modelo de detecção de fraudes"""
        logger.info("🎯 Treinando modelo de detecção de fraudes...")
        
        # Criar features
        feature_pipeline, df_features = self.create_features(df)
        
        # Dividir dados
        train_df, test_df = df_features.randomSplit([0.8, 0.2], seed=42)
        
        # Múltiplos algoritmos para ensemble
        rf_classifier = RandomForestClassifier(
            featuresCol="scaled_features",
            labelCol="is_fraud",
            numTrees=100,
            maxDepth=10,
            seed=42
        )
        
        gbt_classifier = GBTClassifier(
            featuresCol="scaled_features",
            labelCol="is_fraud",
            maxIter=100,
            maxDepth=8,
            seed=42
        )
        
        lr_classifier = LogisticRegression(
            featuresCol="scaled_features",
            labelCol="is_fraud",
            maxIter=100,
            regParam=0.01
        )
        
        # Pipeline completo
        self.pipeline = Pipeline(stages=feature_pipeline.getStages() + [rf_classifier])
        
        # Treinar modelo
        self.model = self.pipeline.fit(train_df)
        
        # Avaliar modelo
        predictions = self.model.transform(test_df)
        
        # Métricas de avaliação
        evaluator_auc = BinaryClassificationEvaluator(
            labelCol="is_fraud", rawPredictionCol="rawPrediction", metricName="areaUnderROC"
        )
        
        evaluator_pr = BinaryClassificationEvaluator(
            labelCol="is_fraud", rawPredictionCol="rawPrediction", metricName="areaUnderPR"
        )
        
        auc = evaluator_auc.evaluate(predictions)
        pr_auc = evaluator_pr.evaluate(predictions)
        
        # Matriz de confusão
        confusion_matrix = predictions.groupBy("is_fraud", "prediction") \
                                    .count() \
                                    .orderBy("is_fraud", "prediction")
        
        logger.info(f"🎯 Métricas do modelo:")
        logger.info(f"   AUC-ROC: {auc:.4f}")
        logger.info(f"   AUC-PR: {pr_auc:.4f}")
        
        logger.info("📊 Matriz de Confusão:")
        confusion_matrix.show()
        
        # Feature importance (para Random Forest)
        if hasattr(self.model.stages[-1], 'featureImportances'):
            feature_importance = self.model.stages[-1].featureImportances
            logger.info("🔍 Top Features:")
            for i, importance in enumerate(feature_importance.toArray()[:10]):
                logger.info(f"   Feature {i}: {importance:.4f}")
        
        return {
            'auc_roc': auc,
            'auc_pr': pr_auc,
            'confusion_matrix': confusion_matrix.collect(),
            'test_predictions': predictions
        }
    
    def predict_fraud_probability(self, df):
        """Predizer probabilidade de fraude"""
        if self.model is None:
            raise ValueError("Modelo não foi treinado ainda!")
        
        predictions = self.model.transform(df)
        
        # Extrair probabilidades
        prob_udf = udf(lambda v: float(v[1]), DoubleType())
        predictions_with_prob = predictions.withColumn(
            "fraud_probability", 
            prob_udf(col("probability"))
        )
        
        return predictions_with_prob.select(
            "transaction_id", "amount", "merchant", "category",
            "prediction", "fraud_probability"
        )

class RecommendationSystem:
    """Sistema de recomendação usando ALS (Alternating Least Squares)"""
    
    def __init__(self, spark_session):
        self.spark = spark_session
        self.model = None
    
    def train_als_model(self, ratings_df):
        """Treinar modelo ALS"""
        logger.info("🎯 Treinando sistema de recomendação com ALS...")
        
        # Dividir dados
        train_df, test_df = ratings_df.randomSplit([0.8, 0.2], seed=42)
        
        # Configurar ALS
        als = ALS(
            maxIter=10,
            regParam=0.1,
            rank=50,
            userCol="user_id",
            itemCol="item_id",
            ratingCol="rating",
            coldStartStrategy="drop",
            seed=42
        )
        
        # Treinar modelo
        self.model = als.fit(train_df)
        
        # Avaliar modelo
        predictions = self.model.transform(test_df)
        evaluator = RegressionEvaluator(
            metricName="rmse",
            labelCol="rating",
            predictionCol="prediction"
        )
        
        rmse = evaluator.evaluate(predictions)
        logger.info(f"🎯 RMSE do modelo: {rmse:.4f}")
        
        return {'rmse': rmse, 'predictions': predictions}
    
    def get_user_recommendations(self, user_id, num_recommendations=10):
        """Obter recomendações para um usuário"""
        if self.model is None:
            raise ValueError("Modelo não foi treinado!")
        
        # Criar DataFrame com o usuário
        user_df = self.spark.createDataFrame([(user_id,)], ["user_id"])
        
        # Gerar recomendações
        recommendations = self.model.recommendForUserSubset(user_df, num_recommendations)
        
        return recommendations
    
    def get_item_recommendations(self, item_id, num_recommendations=10):
        """Obter usuários que podem gostar de um item"""
        if self.model is None:
            raise ValueError("Modelo não foi treinado!")
        
        item_df = self.spark.createDataFrame([(item_id,)], ["item_id"])
        recommendations = self.model.recommendForItemSubset(item_df, num_recommendations)
        
        return recommendations

class SentimentAnalysisPipeline:
    """Pipeline de análise de sentimento usando NLP"""
    
    def __init__(self, spark_session):
        self.spark = spark_session
        self.pipeline = None
        self.model = None
    
    def create_nlp_pipeline(self, df):
        """Criar pipeline de NLP"""
        logger.info("🔧 Criando pipeline de NLP...")
        
        # Tokenização
        tokenizer = Tokenizer(inputCol="text", outputCol="words")
        
        # Remover stop words
        remover = StopWordsRemover(inputCol="words", outputCol="filtered_words")
        
        # TF-IDF
        hashing_tf = HashingTF(inputCol="filtered_words", outputCol="raw_features", numFeatures=10000)
        idf = IDF(inputCol="raw_features", outputCol="features")
        
        # Classificador
        lr = LogisticRegression(
            featuresCol="features",
            labelCol="sentiment",
            maxIter=100,
            regParam=0.01
        )
        
        # Pipeline completo
        self.pipeline = Pipeline(stages=[tokenizer, remover, hashing_tf, idf, lr])
        
        return self.pipeline
    
    def train_sentiment_model(self, df):
        """Treinar modelo de análise de sentimento"""
        logger.info("🎯 Treinando modelo de análise de sentimento...")
        
        # Criar pipeline
        pipeline = self.create_nlp_pipeline(df)
        
        # Dividir dados
        train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)
        
        # Treinar modelo
        self.model = pipeline.fit(train_df)
        
        # Avaliar modelo
        predictions = self.model.transform(test_df)
        
        evaluator = MulticlassClassificationEvaluator(
            labelCol="sentiment",
            predictionCol="prediction",
            metricName="accuracy"
        )
        
        accuracy = evaluator.evaluate(predictions)
        logger.info(f"🎯 Acurácia do modelo: {accuracy:.4f}")
        
        return {
            'accuracy': accuracy,
            'predictions': predictions
        }
    
    def analyze_sentiment_batch(self, texts):
        """Analisar sentimento de um lote de textos"""
        if self.model is None:
            raise ValueError("Modelo não foi treinado!")
        
        # Criar DataFrame temporário
        text_df = self.spark.createDataFrame(
            [(i, text) for i, text in enumerate(texts)],
            ["id", "text"]
        )
        
        predictions = self.model.transform(text_df)
        
        return predictions.select("id", "text", "prediction").collect()

def run_complete_ml_demo():
    """Executar demonstração completa de ML com Big Data"""
    
    print("🚀 Machine Learning with Big Data - Complete Demo")
    print("=" * 60)
    
    # Inicializar plataforma
    ml_platform = BigDataMLPlatform()
    
    try:
        # Criar datasets sintéticos
        datasets = ml_platform.create_synthetic_datasets()
        
        # 1. Detecção de Fraudes
        print("\n🔍 1. FRAUD DETECTION PIPELINE")
        print("-" * 40)
        
        fraud_pipeline = FraudDetectionPipeline(ml_platform.spark)
        fraud_results = fraud_pipeline.train_model(datasets['fraud_detection'])
        
        # Exemplo de predição
        sample_transactions = datasets['fraud_detection'].limit(100)
        fraud_predictions = fraud_pipeline.predict_fraud_probability(sample_transactions)
        
        print("🚨 Top transações suspeitas:")
        fraud_predictions.filter(col("fraud_probability") > 0.5) \
                        .orderBy(desc("fraud_probability")) \
                        .show(10)
        
        # 2. Sistema de Recomendação
        print("\n📚 2. RECOMMENDATION SYSTEM")
        print("-" * 40)
        
        rec_system = RecommendationSystem(ml_platform.spark)
        rec_results = rec_system.train_als_model(datasets['recommendations'])
        
        # Exemplo de recomendações
        user_recs = rec_system.get_user_recommendations(user_id=123, num_recommendations=5)
        print("🎯 Recomendações para usuário 123:")
        user_recs.show(truncate=False)
        
        # 3. Análise de Sentimento
        print("\n😊 3. SENTIMENT ANALYSIS")
        print("-" * 40)
        
        sentiment_pipeline = SentimentAnalysisPipeline(ml_platform.spark)
        sentiment_results = sentiment_pipeline.train_sentiment_model(datasets['sentiment_analysis'])
        
        # Exemplo de análise
        sample_texts = [
            "This product is absolutely amazing!",
            "Terrible quality, very disappointed.",
            "It's okay, nothing special."
        ]
        
        sentiment_predictions = sentiment_pipeline.analyze_sentiment_batch(sample_texts)
        print("📝 Análise de sentimento:")
        for pred in sentiment_predictions:
            sentiment_label = "Positive" if pred['prediction'] > 0.5 else "Negative" if pred['prediction'] < 0.5 else "Neutral"
            print(f"   '{pred['text'][:50]}...' -> {sentiment_label}")
        
        # Salvar resultados
        results_summary = {
            'fraud_detection': {
                'auc_roc': fraud_results['auc_roc'],
                'auc_pr': fraud_results['auc_pr']
            },
            'recommendation_system': {
                'rmse': rec_results['rmse']
            },
            'sentiment_analysis': {
                'accuracy': sentiment_results['accuracy']
            },
            'timestamp': datetime.now().isoformat()
        }
        
        with open('ml_demo_results.json', 'w') as f:
            json.dump(results_summary, f, indent=2)
        
        print("\n✅ Demo completo finalizado!")
        print("📊 Resultados salvos em 'ml_demo_results.json'")
        
        # Estatísticas finais
        print(f"\n📈 RESUMO DOS RESULTADOS:")
        print(f"🔍 Fraud Detection AUC-ROC: {fraud_results['auc_roc']:.4f}")
        print(f"📚 Recommendation RMSE: {rec_results['rmse']:.4f}")
        print(f"😊 Sentiment Analysis Accuracy: {sentiment_results['accuracy']:.4f}")
        
    except Exception as e:
        logger.error(f"Erro durante execução: {e}")
        raise
    
    finally:
        # Limpar recursos
        ml_platform.spark.stop()

def main():
    """Função principal"""
    
    print("🚀 Machine Learning with Big Data")
    print("=" * 50)
    
    print("\nEscolha uma opção:")
    print("1. Demo Completo de ML")
    print("2. Apenas Detecção de Fraudes")
    print("3. Apenas Sistema de Recomendação")
    print("4. Apenas Análise de Sentimento")
    
    choice = input("\nOpção (1-4): ").strip()
    
    if choice == '1':
        run_complete_ml_demo()
    
    elif choice == '2':
        ml_platform = BigDataMLPlatform()
        datasets = ml_platform.create_synthetic_datasets()
        fraud_pipeline = FraudDetectionPipeline(ml_platform.spark)
        fraud_pipeline.train_model(datasets['fraud_detection'])
        ml_platform.spark.stop()
    
    elif choice == '3':
        ml_platform = BigDataMLPlatform()
        datasets = ml_platform.create_synthetic_datasets()
        rec_system = RecommendationSystem(ml_platform.spark)
        rec_system.train_als_model(datasets['recommendations'])
        ml_platform.spark.stop()
    
    elif choice == '4':
        ml_platform = BigDataMLPlatform()
        datasets = ml_platform.create_synthetic_datasets()
        sentiment_pipeline = SentimentAnalysisPipeline(ml_platform.spark)
        sentiment_pipeline.train_sentiment_model(datasets['sentiment_analysis'])
        ml_platform.spark.stop()
    
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
