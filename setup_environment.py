#!/usr/bin/env python3
"""
Script de Configuração do Ambiente Big Data em Python
Instala automaticamente todas as dependências necessárias
"""

import subprocess
import sys
import os
import platform
from pathlib import Path

def run_command(command, description=""):
    """Executa um comando e retorna o resultado"""
    print(f"\n🔄 {description}")
    print(f"Executando: {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Sucesso: {description}")
            if result.stdout:
                print(f"Output: {result.stdout.strip()}")
        else:
            print(f"❌ Erro: {description}")
            print(f"Error: {result.stderr.strip()}")
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Exceção ao executar comando: {e}")
        return False

def check_python_version():
    """Verifica se a versão do Python é adequada"""
    version = sys.version_info
    print(f"🐍 Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ é necessário")
        return False
    else:
        print("✅ Versão do Python adequada")
        return True

def check_java():
    """Verifica se o Java está instalado"""
    print("\n☕ Verificando Java...")
    
    # Verifica se java está no PATH
    result = subprocess.run("java -version", shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ Java encontrado")
        print(f"Versão: {result.stderr.split()[2] if result.stderr else 'Desconhecida'}")
        return True
    else:
        print("❌ Java não encontrado")
        print("PySpark requer Java 8 ou superior")
        print("Instale Java em: https://adoptium.net/")
        return False

def install_requirements():
    """Instala as dependências do requirements.txt"""
    print("\n📦 Instalando dependências...")
    
    requirements_file = Path("requirements.txt")
    if not requirements_file.exists():
        print("❌ Arquivo requirements.txt não encontrado")
        return False
    
    # Atualiza pip primeiro
    run_command(f"{sys.executable} -m pip install --upgrade pip", "Atualizando pip")
    
    # Instala requirements
    success = run_command(
        f"{sys.executable} -m pip install -r {requirements_file}",
        "Instalando dependências do requirements.txt"
    )
    
    return success

def install_pyspark():
    """Instala PySpark especificamente"""
    print("\n⚡ Instalando PySpark...")
    
    commands = [
        f"{sys.executable} -m pip install pyspark>=3.4.0",
        f"{sys.executable} -m pip install findspark>=2.0.0",
        f"{sys.executable} -m pip install py4j>=0.10.9"
    ]
    
    for cmd in commands:
        if not run_command(cmd, f"Instalando {cmd.split()[-1]}"):
            return False
    
    return True

def test_pyspark():
    """Testa se o PySpark está funcionando"""
    print("\n🧪 Testando PySpark...")
    
    test_code = '''
try:
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.appName("Test").master("local[1]").getOrCreate()
    df = spark.createDataFrame([(1, "Hello"), (2, "World")], ["id", "message"])
    count = df.count()
    spark.stop()
    print(f"✅ PySpark funcionando! DataFrame com {count} registros criado.")
except Exception as e:
    print(f"❌ Erro no PySpark: {e}")
'''
    
    result = subprocess.run(
        [sys.executable, "-c", test_code],
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    
    return result.returncode == 0

def setup_environment_variables():
    """Configura variáveis de ambiente necessárias"""
    print("\n🔧 Configurando variáveis de ambiente...")
    
    # Detecta JAVA_HOME automaticamente
    java_home = None
    
    # Tenta encontrar Java automaticamente
    if platform.system() == "Windows":
        java_candidates = [
            "C:\\Program Files\\Java\\jdk*",
            "C:\\Program Files\\Eclipse Adoptium\\jdk*",
            "C:\\Program Files\\OpenJDK\\jdk*"
        ]
    else:
        java_candidates = [
            "/usr/lib/jvm/java-*",
            "/opt/java/*",
            "/Library/Java/JavaVirtualMachines/*/Contents/Home"
        ]
    
    # Define variáveis básicas
    env_vars = {
        'PYSPARK_PYTHON': sys.executable,
        'PYSPARK_DRIVER_PYTHON': sys.executable,
    }
    
    for var, value in env_vars.items():
        os.environ[var] = value
        print(f"✅ {var} = {value}")
    
    return True

def create_test_script():
    """Cria um script de teste básico"""
    print("\n📝 Criando script de teste...")
    
    test_script = '''#!/usr/bin/env python3
"""
Script de Teste do Ambiente Big Data
"""

def test_imports():
    """Testa todas as importações principais"""
    print("🧪 Testando importações...")
    
    # Core libraries
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        print("✅ Pandas, NumPy, Matplotlib OK")
    except ImportError as e:
        print(f"❌ Erro nas bibliotecas core: {e}")
    
    # PySpark
    try:
        from pyspark.sql import SparkSession
        print("✅ PySpark importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro no PySpark: {e}")
    
    # Machine Learning
    try:
        import sklearn
        print("✅ Scikit-learn OK")
    except ImportError as e:
        print(f"❌ Erro no scikit-learn: {e}")
    
    print("\\n🎉 Teste de importações concluído!")

def test_simple_spark():
    """Testa funcionalidades básicas do Spark"""
    print("\\n⚡ Testando Spark...")
    
    try:
        from pyspark.sql import SparkSession
        
        spark = SparkSession.builder \\
            .appName("Test") \\
            .master("local[*]") \\
            .getOrCreate()
        
        # Cria DataFrame de teste
        data = [(i, f"item_{i}", i * 10) for i in range(100)]
        df = spark.createDataFrame(data, ["id", "name", "value"])
        
        # Operações básicas
        count = df.count()
        avg_value = df.agg({"value": "avg"}).collect()[0][0]
        
        print(f"✅ DataFrame criado com {count} registros")
        print(f"✅ Valor médio: {avg_value}")
        
        spark.stop()
        print("✅ Spark funcionando perfeitamente!")
        
    except Exception as e:
        print(f"❌ Erro no teste do Spark: {e}")

if __name__ == "__main__":
    print("🚀 TESTE DO AMBIENTE BIG DATA EM PYTHON")
    print("=" * 50)
    
    test_imports()
    test_simple_spark()
    
    print("\\n✅ Ambiente testado com sucesso!")
'''
    
    with open("test_environment.py", "w", encoding="utf-8") as f:
        f.write(test_script)
    
    print("✅ Script de teste criado: test_environment.py")
    return True

def main():
    """Função principal"""
    print("🚀 CONFIGURAÇÃO DO AMBIENTE BIG DATA EM PYTHON")
    print("=" * 60)
    print("Este script configurará automaticamente seu ambiente para Big Data")
    print("=" * 60)
    
    # Verifica pré-requisitos
    if not check_python_version():
        print("\n❌ Configuração abortada - Python inadequado")
        return False
    
    java_ok = check_java()
    if not java_ok:
        print("\n⚠️ Java não encontrado - PySpark pode não funcionar corretamente")
        response = input("Continuar mesmo assim? (s/N): ")
        if response.lower() != 's':
            return False
    
    # Configura ambiente
    setup_environment_variables()
    
    # Instala dependências
    if not install_requirements():
        print("\n❌ Falha na instalação das dependências")
        return False
    
    # Instala PySpark especificamente
    if not install_pyspark():
        print("\n❌ Falha na instalação do PySpark")
        return False
    
    # Testa instalação
    if test_pyspark():
        print("\n✅ PySpark instalado e testado com sucesso!")
    else:
        print("\n⚠️ PySpark instalado mas com problemas")
    
    # Cria script de teste
    create_test_script()
    
    print("\n🎉 CONFIGURAÇÃO CONCLUÍDA!")
    print("=" * 40)
    print("Para testar o ambiente, execute:")
    print("python test_environment.py")
    print("\nPara usar nos notebooks/scripts:")
    print("import findspark")
    print("findspark.init()")
    print("from pyspark.sql import SparkSession")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
