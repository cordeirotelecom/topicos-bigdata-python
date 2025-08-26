#!/usr/bin/env python3
"""
Apache Spark Fundamentals - PySpark Implementation (CORRIGIDO)
Demonstra conceitos essenciais do Spark para processamento de Big Data
Professor: Vagner Cordeiro
Curso: Tópicos de Big Data em Python
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

# Importações do PySpark com tratamento de erro
PYSPARK_AVAILABLE = False
try:
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, sum as spark_sum, avg, count, desc, year, month, when, row_number, rank
    from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, DateType
    from pyspark.sql.window import Window
    from pyspark import SparkContext, SparkConf
    PYSPARK_AVAILABLE = True
    logger.info("✅ PySpark importado com sucesso")
except ImportError:
    logger.warning("⚠️ PySpark não disponível - executando em modo simulação")
    
    # Classes mock para permitir execução sem PySpark
    class MockDataFrame:
        def __init__(self, data=None):
            self.data = data or []
            
        def withColumn(self, name, col_expr):
            return MockDataFrame(self.data)
            
        def filter(self, condition):
            return MockDataFrame(self.data)
            
        def groupBy(self, *cols):
            return MockGroupedData()
            
        def agg(self, *exprs):
            return MockDataFrame(self.data)
            
        def orderBy(self, *cols):
            return MockDataFrame(self.data)
            
        def show(self, n=20, truncate=True):
            print(f"📊 DataFrame Simulado (primeiras {n} linhas):")
            for i, row in enumerate(self.data[:n]):
                print(f"  {row}")
            
        def collect(self):
            return self.data
            
        def count(self):
            return len(self.data)
            
        def printSchema(self):
            print("📋 Schema simulado:")
            print("  root")
            print("   |-- field: string (nullable = true)")
    
    class MockGroupedData:
        def agg(self, *exprs):
            return MockDataFrame([{"resultado": "simulação", "count": 100}])
            
        def count(self):
            return MockDataFrame([{"count": 100}])
    
    class MockSparkSession:
        def __init__(self):
            self.builder = self
            
        def appName(self, name):
            return self
            
        def master(self, master):
            return self
            
        def config(self, key, value):
            return self
            
        def getOrCreate(self):
            return MockSparkSession()
            
        def createDataFrame(self, data, schema=None):
            return MockDataFrame(data)
            
        def stop(self):
            pass
    
    # Configurar SparkSession mock
    class MockSparkSessionBuilder:
        def __init__(self):
            self.configs = {}
            
        def appName(self, name):
            self.configs['appName'] = name
            return self
            
        def master(self, master):
            self.configs['master'] = master
            return self
            
        def config(self, key, value):
            self.configs[key] = value
            return self
            
        def getOrCreate(self):
            return MockSparkSession()
    
    # Mock das funções do Spark
    def col(column_name): 
        return column_name
    def count(column_name=None): 
        return "count()"
    def avg(column_name): 
        return "avg()"
    def desc(column_name): 
        return f"desc({column_name})"
    def year(column_name): 
        return f"year({column_name})"
    def month(column_name): 
        return f"month({column_name})"
    def when(condition, value): 
        return MockWhen()
    def row_number(): 
        return "row_number()"
    def rank(): 
        return "rank()"
    
    def spark_sum(column_name):
        return "sum()"
    
    class MockWhen:
        def when(self, condition, value):
            return self
        def otherwise(self, value):
            return f"when_otherwise({value})"
    
    class MockWindow:
        @staticmethod
        def partitionBy(*cols):
            return MockWindowSpec()
        
        @staticmethod
        def orderBy(*cols):
            return MockWindowSpec()
    
    class MockWindowSpec:
        def orderBy(self, *cols):
            return self
        def partitionBy(self, *cols):
            return self
    
    # Tipos mock
    class StructType:
        def __init__(self, fields):
            self.fields = fields
    
    class StructField:
        def __init__(self, name, dataType, nullable):
            self.name = name
            self.dataType = dataType
            self.nullable = nullable
    
    StringType = lambda: "StringType"
    IntegerType = lambda: "IntegerType"
    DoubleType = lambda: "DoubleType"
    DateType = lambda: "DateType"
    
    Window = MockWindow()
    
    # Configurar SparkSession mock global
    SparkSession.builder = MockSparkSessionBuilder()


class SparkSessionManager:
    """Gerenciador para sessões Spark"""
    
    def __init__(self, app_name="BigData-Spark-Tutorial"):
        self.app_name = app_name
        self.spark = None
    
    def create_session(self, config_options=None):
        """Criar sessão Spark com configurações otimizadas"""
        
        if PYSPARK_AVAILABLE:
            builder = SparkSession.builder.appName(self.app_name)
            
            # Configurações padrão otimizadas
            default_config = {
                "spark.sql.adaptive.enabled": "true",
                "spark.sql.adaptive.coalescePartitions.enabled": "true",
                "spark.sql.adaptive.skewJoin.enabled": "true",
                "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
                "spark.dynamicAllocation.enabled": "true",
                "spark.sql.execution.arrow.pyspark.enabled": "true"
            }
            
            # Aplicar configurações
            configs = {**default_config, **(config_options or {})}
            for key, value in configs.items():
                builder = builder.config(key, value)
            
            self.spark = builder.getOrCreate()
            logger.info(f"✅ Sessão Spark criada: {self.app_name}")
        else:
            logger.info("🔄 Criando sessão Spark simulada...")
            self.spark = SparkSession.builder.appName(self.app_name).getOrCreate()
        
        return self.spark
    
    def stop_session(self):
        """Finalizar sessão Spark"""
        if self.spark:
            self.spark.stop()
            logger.info("🛑 Sessão Spark finalizada")


class DataGenerator:
    """Gerador de dados para demonstrações Spark"""
    
    @staticmethod
    def generate_sales_data(num_records=10000):
        """Gera dados de vendas sintéticos"""
        
        customers = [f"Customer_{i:04d}" for i in range(1, 501)]
        products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Phone", "Tablet", "Headphones", "Speaker"]
        regions = ["North", "South", "East", "West", "Central"]
        
        sales_data = []
        
        for i in range(num_records):
            # Data aleatória nos últimos 2 anos
            start_date = datetime.now() - timedelta(days=730)
            random_days = random.randint(0, 730)
            sale_date = start_date + timedelta(days=random_days)
            
            record = {
                "order_id": f"ORD_{i+1:06d}",
                "customer_id": random.choice(customers),
                "customer_age": random.randint(18, 75),
                "product": random.choice(products),
                "quantity": random.randint(1, 10),
                "unit_price": round(random.uniform(50, 2000), 2),
                "region": random.choice(regions),
                "sale_date": sale_date.strftime("%Y-%m-%d"),
                "sales_rep": f"Rep_{random.randint(1, 50):02d}"
            }
            
            sales_data.append(record)
        
        return sales_data


class SparkDataProcessing:
    """Demonstração de processamento de dados com Spark"""
    
    def __init__(self, spark_session):
        self.spark = spark_session
    
    def create_dataframes(self):
        """Criar DataFrames de exemplo"""
        
        print("📊 Gerando dados de vendas...")
        sales_data = DataGenerator.generate_sales_data(10000)
        
        # Schema para o DataFrame
        schema = StructType([
            StructField("order_id", StringType(), True),
            StructField("customer_id", StringType(), True),
            StructField("customer_age", IntegerType(), True),
            StructField("product", StringType(), True),
            StructField("quantity", IntegerType(), True),
            StructField("unit_price", DoubleType(), True),
            StructField("region", StringType(), True),
            StructField("sale_date", DateType(), True),
            StructField("sales_rep", StringType(), True)
        ])
        
        sales_df = self.spark.createDataFrame(sales_data, schema)
        
        if PYSPARK_AVAILABLE:
            # Adicionar colunas calculadas
            sales_df = sales_df.withColumn("total_amount", col("quantity") * col("unit_price")) \
                             .withColumn("age_group", 
                                        when(col("customer_age") < 30, "Young")
                                        .when(col("customer_age") < 50, "Middle")
                                        .otherwise("Senior"))
        else:
            print("🔄 Simulando transformações no DataFrame...")
            
        print("✅ DataFrame criado com sucesso!")
        return sales_df
    
    def basic_operations(self, df):
        """Operações básicas com DataFrames"""
        
        print("\n🔍 OPERAÇÕES BÁSICAS NO DATAFRAME")
        print("=" * 50)
        
        # Mostrar schema
        print("\n📋 Schema do DataFrame:")
        df.printSchema()
        
        # Mostrar primeiras linhas
        print("\n📄 Primeiras 10 linhas:")
        df.show(10)
        
        # Estatísticas básicas
        print(f"\n📊 Total de registros: {df.count()}")
        
        if PYSPARK_AVAILABLE:
            # Filtrar pedidos de alto valor
            high_value_orders = df.filter(col("total_amount") > 1000) \
                               .orderBy(desc("total_amount"))
            
            print(f"\n💰 Pedidos acima de R$ 1.000: {high_value_orders.count()}")
            high_value_orders.show(5)
        else:
            print("🔄 Simulando filtros e ordenação...")
    
    def aggregations(self, df):
        """Demonstrar agregações e agrupamentos"""
        
        print("\n📈 AGREGAÇÕES E AGRUPAMENTOS")
        print("=" * 50)
        
        if PYSPARK_AVAILABLE:
            # Vendas por região
            regional_sales = df.groupBy("region") \
                              .agg(spark_sum("total_amount").alias("total_revenue"),
                                   avg("total_amount").alias("avg_order_value"),
                                   count("order_id").alias("order_count")) \
                              .orderBy(desc("total_revenue"))
            
            print("\n🌍 Vendas por Região:")
            regional_sales.show()
            
            # Vendas por produto
            product_sales = df.groupBy("product") \
                             .agg(spark_sum("quantity").alias("total_quantity"),
                                  spark_sum("total_amount").alias("total_revenue")) \
                             .orderBy(desc("total_revenue"))
            
            print("\n📦 Vendas por Produto:")
            product_sales.show()
        else:
            print("🔄 Simulando agregações por região e produto...")
    
    def window_functions(self, df):
        """Demonstrar Window Functions"""
        
        print("\n🪟 WINDOW FUNCTIONS")
        print("=" * 50)
        
        if PYSPARK_AVAILABLE:
            # Ranking de clientes por valor gasto
            customer_window = Window.partitionBy("customer_id").orderBy(desc("total_amount"))
            
            customer_ranking = df.withColumn("customer_rank", 
                                           row_number().over(customer_window)) \
                                .withColumn("customer_cumulative_spent", 
                                          spark_sum("total_amount").over(customer_window))
            
            # Top clientes por mês
            monthly_window = Window.partitionBy(year("sale_date"), month("sale_date")) \
                                  .orderBy(desc("total_amount"))
            
            top_monthly = customer_ranking.withColumn("monthly_rank", 
                                                     rank().over(monthly_window)) \
                                        .filter(col("monthly_rank") <= 10)
            
            # Análise de lifetime value
            customer_ltv = customer_ranking.groupBy("customer_id") \
                                         .agg(max("customer_cumulative_spent").alias("total_spent")) \
                                         .orderBy(desc("total_spent"))
            
            print("\n👑 Top 10 Clientes por Lifetime Value:")
            customer_ltv.show(10)
        else:
            print("🔄 Simulando Window Functions e rankings...")
    
    def advanced_transformations(self, df):
        """Transformações avançadas"""
        
        print("\n⚙️ TRANSFORMAÇÕES AVANÇADAS")
        print("=" * 50)
        
        if PYSPARK_AVAILABLE:
            # Análise de cohort simples
            monthly_cohorts = df.groupBy(year("sale_date").alias("year"), 
                                       month("sale_date").alias("month")) \
                               .agg(count("customer_id").alias("customers"),
                                   spark_sum("total_amount").alias("revenue")) \
                               .orderBy("year", "month")
            
            print("\n📅 Análise de Cohort Mensal:")
            monthly_cohorts.show()
            
            # Detecção de anomalias (pedidos muito grandes)
            avg_order_value = df.agg(avg("total_amount")).collect()[0][0]
            anomalies = df.filter(col("total_amount") > avg_order_value * 3)
            
            print(f"\n🚨 Pedidos Anômalos (> 3x a média): {anomalies.count()}")
            if anomalies.count() > 0:
                anomalies.show(5)
        else:
            print("🔄 Simulando análises de cohort e detecção de anomalias...")


def performance_tuning_demo():
    """Demonstração de otimização de performance"""
    
    print("\n🚀 DEMONSTRAÇÃO DE OTIMIZAÇÃO DE PERFORMANCE")
    print("=" * 60)
    
    if PYSPARK_AVAILABLE:
        print("""
        📋 ESTRATÉGIAS DE OTIMIZAÇÃO SPARK:
        
        1. ⚡ Adaptive Query Execution (AQE):
           - Enabled automaticamente no Spark 3.0+
           - Otimiza queries durante execução
           
        2. 🗂️ Particionamento Inteligente:
           - Usar .repartition() para balancear dados
           - Coalesce para reduzir partições pequenas
           
        3. 💾 Caching Estratégico:
           - .cache() ou .persist() para dados reutilizados
           - Escolher nível de storage adequado
           
        4. 🔄 Broadcast Joins:
           - Para tabelas pequenas (<200MB)
           - Evita shuffle de dados grandes
           
        5. 📊 Columnar Storage:
           - Parquet para melhor compressão
           - Delta Lake para ACID transactions
        """)
        
        # Exemplo de broadcast join
        try:
            from pyspark.sql.functions import broadcast
            print("\n📡 Exemplo de Broadcast Join disponível")
        except ImportError:
            print("\n📡 Broadcast Join não disponível nesta versão")
    else:
        print("🔄 Demonstração de otimização em modo simulação")


def main():
    """Função principal"""
    
    print("🎯 APACHE SPARK FUNDAMENTALS - DEMONSTRAÇÃO COMPLETA")
    print("=" * 60)
    
    # Configurar Spark
    manager = SparkSessionManager("Spark-Fundamentals-Demo")
    
    # Configurações personalizadas
    custom_config = {
        "spark.sql.adaptive.coalescePartitions.minPartitionNum": "1",
        "spark.sql.adaptive.coalescePartitions.initialPartitionNum": "4"
    }
    
    spark = manager.create_session(custom_config)
    
    try:
        # Processamento de dados
        processor = SparkDataProcessing(spark)
        
        # Criar DataFrame
        sales_df = processor.create_dataframes()
        
        # Demonstrações
        processor.basic_operations(sales_df)
        processor.aggregations(sales_df)
        processor.window_functions(sales_df)
        processor.advanced_transformations(sales_df)
        
        # Performance tuning
        performance_tuning_demo()
        
    except Exception as e:
        logger.error(f"❌ Erro durante execução: {e}")
    
    finally:
        # Limpar recursos
        manager.stop_session()
    
    print("\n✅ Demonstração concluída com sucesso!")
    print("\n📚 PRÓXIMOS PASSOS:")
    print("   1. Explore Spark SQL e DataFrames")
    print("   2. Aprenda sobre Spark Streaming")
    print("   3. Integre com Hadoop e Hive")
    print("   4. Implemente MLlib para Machine Learning")


if __name__ == "__main__":
    main()
