#!/usr/bin/env python3
"""
Apache Spark Fundamentals - PySpark Implementation
Demonstra conceitos essenciais do Spark para processamento de Big Data
"""

import os
import sys
import logging
import json
from datetime import datetime, timedelta
import random

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import *
    from pyspark.sql.types import *
    from pyspark.sql.window import Window
    from pyspark import SparkContext, SparkConf
except ImportError:
    logger.error("PySpark não instalado. Execute: pip install pyspark")
    sys.exit(1)

class SparkSessionManager:
    """Gerenciador para sessões Spark"""
    
    def __init__(self, app_name="BigData-Spark-Tutorial"):
        self.app_name = app_name
        self.spark = None
    
    def create_session(self, config_options=None):
        """Criar sessão Spark com configurações otimizadas"""
        
        builder = SparkSession.builder.appName(self.app_name)
        
        # Configurações padrão otimizadas
        default_config = {
            "spark.sql.adaptive.enabled": "true",
            "spark.sql.adaptive.coalescePartitions.enabled": "true",
            "spark.sql.adaptive.skewJoin.enabled": "true",
            "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
            "spark.sql.execution.arrow.pyspark.enabled": "true",
            "spark.executor.memory": "2g",
            "spark.driver.memory": "2g",
            "spark.executor.cores": "2",
            "spark.sql.shuffle.partitions": "200"
        }
        
        if config_options:
            default_config.update(config_options)
        
        for key, value in default_config.items():
            builder = builder.config(key, value)
        
        self.spark = builder.getOrCreate()
        self.spark.sparkContext.setLogLevel("WARN")
        
        logger.info(f"Spark Session criada: {self.spark.version}")
        return self.spark
    
    def stop_session(self):
        """Parar sessão Spark"""
        if self.spark:
            self.spark.stop()
            logger.info("Spark Session finalizada")

class RDDOperations:
    """Demonstrações de operações com RDDs"""
    
    def __init__(self, spark_session):
        self.spark = spark_session
        self.sc = spark_session.sparkContext
    
    def basic_rdd_operations(self):
        """Operações básicas com RDDs"""
        logger.info("🔥 Demonstrando operações básicas com RDDs")
        
        # Criar RDD a partir de lista
        numbers = self.sc.parallelize(range(1, 1000001))  # 1 milhão de números
        
        # Transformações (lazy evaluation)
        even_numbers = numbers.filter(lambda x: x % 2 == 0)
        squared_numbers = even_numbers.map(lambda x: x ** 2)
        
        # Ações (trigger computation)
        count = squared_numbers.count()
        first_10 = squared_numbers.take(10)
        sum_result = squared_numbers.reduce(lambda a, b: a + b)
        
        logger.info(f"Números pares encontrados: {count:,}")
        logger.info(f"Primeiros 10 quadrados: {first_10}")
        logger.info(f"Soma total: {sum_result:,}")
        
        return {
            'count': count,
            'first_10': first_10,
            'sum': sum_result
        }
    
    def text_processing_rdd(self, text_file="sample_text.txt"):
        """Processamento de texto com RDDs"""
        logger.info("📝 Processamento de texto com RDDs")
        
        # Criar arquivo de exemplo se não existir
        if not os.path.exists(text_file):
            self.create_sample_text_file(text_file)
        
        # Ler arquivo como RDD
        text_rdd = self.sc.textFile(text_file)
        
        # Pipeline de transformações
        words_rdd = text_rdd.flatMap(lambda line: line.lower().split()) \
                           .filter(lambda word: len(word) > 3) \
                           .map(lambda word: (word, 1)) \
                           .reduceByKey(lambda a, b: a + b) \
                           .sortBy(lambda x: x[1], ascending=False)
        
        # Cache para múltiplas ações
        words_rdd.cache()
        
        # Ações
        word_count = words_rdd.count()
        top_10_words = words_rdd.take(10)
        
        logger.info(f"Total de palavras únicas: {word_count}")
        logger.info("Top 10 palavras:")
        for word, count in top_10_words:
            logger.info(f"  {word}: {count}")
        
        return {
            'word_count': word_count,
            'top_words': top_10_words
        }
    
    def create_sample_text_file(self, filename):
        """Criar arquivo de texto de exemplo"""
        sample_text = """
        Apache Spark is a unified analytics engine for large-scale data processing.
        Spark provides high-level APIs in Java, Scala, Python and R, and an optimized 
        engine that supports general execution graphs. It also supports a rich set of 
        higher-level tools including Spark SQL for SQL and structured data processing, 
        MLlib for machine learning, GraphX for graph processing, and Structured Streaming 
        for incremental computation and stream processing.
        
        Spark runs on Hadoop, Apache Mesos, Kubernetes, standalone, or in the cloud. 
        It can access diverse data sources including HDFS, Alluxio, Apache Cassandra, 
        Apache HBase, Apache Hive, and hundreds of other data sources.
        """ * 1000  # Repetir para criar arquivo maior
        
        with open(filename, 'w') as f:
            f.write(sample_text)

class DataFrameOperations:
    """Demonstrações de operações com DataFrames"""
    
    def __init__(self, spark_session):
        self.spark = spark_session
    
    def create_sample_dataframes(self):
        """Criar DataFrames de exemplo"""
        logger.info("📊 Criando DataFrames de exemplo")
        
        # Schema para dados de vendas
        sales_schema = StructType([
            StructField("order_id", StringType(), True),
            StructField("customer_id", StringType(), True),
            StructField("product_id", StringType(), True),
            StructField("product_name", StringType(), True),
            StructField("category", StringType(), True),
            StructField("quantity", IntegerType(), True),
            StructField("unit_price", DoubleType(), True),
            StructField("order_date", DateType(), True),
            StructField("customer_age", IntegerType(), True),
            StructField("customer_city", StringType(), True)
        ])
        
        # Gerar dados sintéticos
        sample_data = []
        categories = ["Electronics", "Clothing", "Books", "Home", "Sports"]
        cities = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília", "Salvador"]
        
        for i in range(100000):  # 100k registros
            order_date = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))
            
            record = (
                f"ORD-{i:06d}",
                f"CUST-{random.randint(1, 10000):05d}",
                f"PROD-{random.randint(1, 1000):04d}",
                f"Product {random.randint(1, 1000)}",
                random.choice(categories),
                random.randint(1, 10),
                round(random.uniform(10.0, 500.0), 2),
                order_date.date(),
                random.randint(18, 70),
                random.choice(cities)
            )
            sample_data.append(record)
        
        # Criar DataFrame
        sales_df = self.spark.createDataFrame(sample_data, sales_schema)
        
        # Adicionar colunas calculadas
        sales_df = sales_df.withColumn("total_amount", col("quantity") * col("unit_price")) \
                          .withColumn("year", year("order_date")) \
                          .withColumn("month", month("order_date")) \
                          .withColumn("age_group", 
                                    when(col("customer_age") < 30, "Young")
                                    .when(col("customer_age") < 50, "Middle")
                                    .otherwise("Senior"))
        
        # Cache para performance
        sales_df.cache()
        
        logger.info(f"DataFrame criado com {sales_df.count():,} registros")
        sales_df.printSchema()
        sales_df.show(10)
        
        return sales_df
    
    def basic_dataframe_operations(self, df):
        """Operações básicas com DataFrames"""
        logger.info("🔍 Operações básicas com DataFrames")
        
        # Estatísticas descritivas
        logger.info("Estatísticas descritivas:")
        df.describe().show()
        
        # Filtros e seleções
        high_value_orders = df.filter(col("total_amount") > 1000) \
                             .select("order_id", "customer_id", "product_name", "total_amount")
        
        logger.info(f"Pedidos de alto valor: {high_value_orders.count():,}")
        high_value_orders.show(10)
        
        # Agregações
        category_sales = df.groupBy("category") \
                          .agg(
                              sum("total_amount").alias("total_revenue"),
                              avg("total_amount").alias("avg_order_value"),
                              count("order_id").alias("order_count")
                          ) \
                          .orderBy(desc("total_revenue"))
        
        logger.info("Vendas por categoria:")
        category_sales.show()
        
        return {
            'high_value_count': high_value_orders.count(),
            'category_sales': category_sales.collect()
        }
    
    def advanced_analytics(self, df):
        """Analytics avançados com Window Functions"""
        logger.info("📈 Analytics avançados com Window Functions")
        
        # Window specifications
        customer_window = Window.partitionBy("customer_id").orderBy("order_date")
        monthly_window = Window.partitionBy("year", "month").orderBy("total_amount")
        
        # Customer analytics
        customer_analytics = df.withColumn("order_number", 
                                         row_number().over(customer_window)) \
                              .withColumn("customer_cumulative_spent", 
                                        sum("total_amount").over(customer_window))
        
        # Monthly rankings
        monthly_rankings = df.withColumn("monthly_rank", 
                                       rank().over(monthly_window)) \
                            .filter(col("monthly_rank") <= 10)
        
        logger.info("Top customers por valor acumulado:")
        top_customers = customer_analytics.groupBy("customer_id") \
                                        .agg(max("customer_cumulative_spent").alias("total_spent")) \
                                        .orderBy(desc("total_spent")) \
                                        .limit(10)
        top_customers.show()
        
        logger.info("Sample de rankings mensais:")
        monthly_rankings.select("year", "month", "order_id", "total_amount", "monthly_rank") \
                       .show(20)
        
        return {
            'top_customers': top_customers.collect(),
            'monthly_rankings_count': monthly_rankings.count()
        }
    
    def sql_operations(self, df):
        """Operações usando Spark SQL"""
        logger.info("🗃️ Operações com Spark SQL")
        
        # Registrar DataFrame como view temporária
        df.createOrReplaceTempView("sales")
        
        # Consultas SQL complexas
        queries = {
            'monthly_trends': """
                SELECT 
                    year, month,
                    COUNT(*) as order_count,
                    SUM(total_amount) as revenue,
                    AVG(total_amount) as avg_order_value
                FROM sales 
                GROUP BY year, month 
                ORDER BY year, month
            """,
            
            'customer_segmentation': """
                WITH customer_stats AS (
                    SELECT 
                        customer_id,
                        COUNT(*) as order_frequency,
                        SUM(total_amount) as total_spent,
                        AVG(total_amount) as avg_order_value,
                        MAX(order_date) as last_order_date
                    FROM sales 
                    GROUP BY customer_id
                )
                SELECT 
                    CASE 
                        WHEN total_spent > 5000 AND order_frequency > 10 THEN 'VIP'
                        WHEN total_spent > 2000 AND order_frequency > 5 THEN 'Premium'
                        WHEN order_frequency > 3 THEN 'Regular'
                        ELSE 'New'
                    END as customer_segment,
                    COUNT(*) as customer_count,
                    AVG(total_spent) as avg_spent,
                    AVG(order_frequency) as avg_frequency
                FROM customer_stats 
                GROUP BY customer_segment
                ORDER BY avg_spent DESC
            """,
            
            'product_performance': """
                SELECT 
                    category,
                    product_name,
                    SUM(quantity) as total_quantity,
                    SUM(total_amount) as total_revenue,
                    COUNT(DISTINCT customer_id) as unique_customers
                FROM sales 
                GROUP BY category, product_name
                HAVING total_revenue > 10000
                ORDER BY total_revenue DESC
                LIMIT 20
            """
        }
        
        results = {}
        for query_name, query in queries.items():
            logger.info(f"Executando: {query_name}")
            result_df = self.spark.sql(query)
            result_df.show()
            results[query_name] = result_df.collect()
        
        return results

class PerformanceTuning:
    """Técnicas de otimização de performance"""
    
    def __init__(self, spark_session):
        self.spark = spark_session
    
    def partitioning_demo(self, df):
        """Demonstração de estratégias de particionamento"""
        logger.info("⚡ Demonstração de particionamento")
        
        # Verificar particionamento atual
        logger.info(f"Partições atuais: {df.rdd.getNumPartitions()}")
        
        # Repartition por coluna para otimizar joins
        partitioned_df = df.repartition(col("category"))
        logger.info(f"Partições após repartition: {partitioned_df.rdd.getNumPartitions()}")
        
        # Coalesce para reduzir partições
        coalesced_df = df.coalesce(4)
        logger.info(f"Partições após coalesce: {coalesced_df.rdd.getNumPartitions()}")
        
        # Demonstrar impacto de cache
        import time
        
        # Primeira execução (sem cache)
        start_time = time.time()
        result1 = df.groupBy("category").count().collect()
        time1 = time.time() - start_time
        
        # Segunda execução (com cache)
        df.cache()
        start_time = time.time()
        result2 = df.groupBy("category").count().collect()
        time2 = time.time() - start_time
        
        logger.info(f"Tempo sem cache: {time1:.2f}s")
        logger.info(f"Tempo com cache: {time2:.2f}s")
        logger.info(f"Speedup: {time1/time2:.2f}x")
        
        return {
            'original_partitions': df.rdd.getNumPartitions(),
            'time_without_cache': time1,
            'time_with_cache': time2,
            'speedup': time1/time2
        }
    
    def broadcast_demo(self, large_df):
        """Demonstração de broadcast variables"""
        logger.info("📡 Demonstração de broadcast variables")
        
        # Criar DataFrame pequeno para broadcast
        category_mapping = self.spark.createDataFrame([
            ("Electronics", "Tech"),
            ("Clothing", "Fashion"),
            ("Books", "Education"),
            ("Home", "Lifestyle"),
            ("Sports", "Recreation")
        ], ["category", "category_group"])
        
        # Join regular
        regular_join = large_df.join(category_mapping, "category")
        
        # Broadcast join
        from pyspark.sql.functions import broadcast
        broadcast_join = large_df.join(broadcast(category_mapping), "category")
        
        logger.info("Join regular vs broadcast join configurado")
        logger.info(f"Resultado join: {broadcast_join.count():,} registros")
        
        return {
            'regular_join_count': regular_join.count(),
            'broadcast_join_count': broadcast_join.count()
        }

def main():
    """Função principal demonstrando funcionalidades do Spark"""
    
    print("🚀 Apache Spark Fundamentals")
    print("=" * 50)
    
    # Criar sessão Spark
    spark_manager = SparkSessionManager()
    spark = spark_manager.create_session()
    
    try:
        # 1. Demonstrações com RDDs
        print("\n🔥 1. RDD Operations")
        rdd_ops = RDDOperations(spark)
        
        # Operações básicas
        basic_results = rdd_ops.basic_rdd_operations()
        
        # Processamento de texto
        text_results = rdd_ops.text_processing_rdd()
        
        # 2. Demonstrações com DataFrames
        print("\n📊 2. DataFrame Operations")
        df_ops = DataFrameOperations(spark)
        
        # Criar dados de exemplo
        sales_df = df_ops.create_sample_dataframes()
        
        # Operações básicas
        basic_df_results = df_ops.basic_dataframe_operations(sales_df)
        
        # Analytics avançados
        advanced_results = df_ops.advanced_analytics(sales_df)
        
        # Operações SQL
        sql_results = df_ops.sql_operations(sales_df)
        
        # 3. Performance Tuning
        print("\n⚡ 3. Performance Tuning")
        perf_tuning = PerformanceTuning(spark)
        
        # Demonstrações de particionamento
        partition_results = perf_tuning.partitioning_demo(sales_df)
        
        # Demonstrações de broadcast
        broadcast_results = perf_tuning.broadcast_demo(sales_df)
        
        # Salvar resultados consolidados
        all_results = {
            'rdd_operations': {
                'basic': basic_results,
                'text_processing': text_results
            },
            'dataframe_operations': {
                'basic': basic_df_results,
                'advanced': advanced_results,
                'sql': sql_results
            },
            'performance': {
                'partitioning': partition_results,
                'broadcast': broadcast_results
            },
            'spark_info': {
                'version': spark.version,
                'app_name': spark.sparkContext.appName
            }
        }
        
        # Salvar para arquivo JSON
        with open('spark_demo_results.json', 'w') as f:
            json.dump(all_results, f, indent=2, default=str)
        
        # Salvar DataFrame como arquivo Parquet
        output_path = "sales_data_output"
        sales_df.write.mode("overwrite").parquet(output_path)
        
        print("\n✅ Demonstração Spark concluída!")
        print("Arquivos gerados:")
        print("- spark_demo_results.json: Resultados das operações")
        print("- sales_data_output/: DataFrame em formato Parquet")
        print("- sample_text.txt: Dados de exemplo para RDD")
        
        # Estatísticas finais
        print(f"\n📊 Estatísticas da sessão:")
        print(f"- Spark Version: {spark.version}")
        print(f"- DataFrames processados: {sales_df.count():,} registros")
        print(f"- Partições utilizadas: {sales_df.rdd.getNumPartitions()}")
        
    except Exception as e:
        logger.error(f"Erro durante execução: {e}")
        raise
    
    finally:
        # Finalizar sessão Spark
        spark_manager.stop_session()

if __name__ == "__main__":
    main()
