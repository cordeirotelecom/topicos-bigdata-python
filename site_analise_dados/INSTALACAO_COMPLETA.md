# 🛠️ Guia Prático: Instalação e Configuração Completa

*Tutorial passo-a-passo para configurar seu ambiente de Big Data e IA*

---

## 📋 **Pré-requisitos do Sistema**

### **Windows 10/11**
```powershell
# Verificar versão do Windows
winver

# Verificar se tem PowerShell 5.1+
$PSVersionTable.PSVersion
```

### **macOS**
```bash
# Verificar versão do macOS
sw_vers

# Instalar Homebrew (se não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### **Ubuntu/Linux**
```bash
# Verificar versão do Ubuntu
lsb_release -a

# Atualizar sistema
sudo apt update && sudo apt upgrade -y
```

---

## 🐍 **Instalação do Python**

### **Opção 1: Python.org (Recomendado para iniciantes)**

**Windows:**
1. Acesse [python.org/downloads](https://python.org/downloads)
2. Baixe Python 3.11.x (versão mais estável)
3. **IMPORTANTE**: Marque "Add Python to PATH"
4. Execute a instalação
5. Teste no PowerShell:
```powershell
python --version
pip --version
```

**macOS:**
```bash
# Via Homebrew (recomendado)
brew install python@3.11

# Verificar instalação
python3 --version
pip3 --version
```

**Ubuntu:**
```bash
# Instalar Python 3.11
sudo apt install python3.11 python3.11-pip python3.11-venv

# Criar link simbólico (opcional)
sudo ln -sf /usr/bin/python3.11 /usr/bin/python

# Verificar
python --version
```

### **Opção 2: Anaconda (Recomendado para cientistas de dados)**

1. Baixe [Anaconda](https://www.anaconda.com/download)
2. Instale seguindo o assistente
3. Abra Anaconda Navigator ou Anaconda Prompt
4. Teste:
```bash
conda --version
python --version
```

---

## ☕ **Instalação do Java (Essencial para PySpark)**

### **Por que preciso do Java?**
Apache Spark é escrito em Scala (que roda na JVM). PySpark é uma interface Python para Spark, mas ainda precisa do Java.

### **Windows:**
```powershell
# Opção 1: Chocolatey (package manager)
choco install openjdk11

# Opção 2: Download manual
# 1. Acesse https://adoptium.net/
# 2. Baixe OpenJDK 11 LTS
# 3. Instale e configure JAVA_HOME

# Verificar instalação
java -version
echo $env:JAVA_HOME
```

### **macOS:**
```bash
# Via Homebrew
brew install openjdk@11

# Configurar JAVA_HOME no .zshrc ou .bash_profile
echo 'export JAVA_HOME=/opt/homebrew/opt/openjdk@11/libexec/openjdk.jdk/Contents/Home' >> ~/.zshrc
source ~/.zshrc

# Verificar
java -version
echo $JAVA_HOME
```

### **Ubuntu:**
```bash
# Instalar OpenJDK 11
sudo apt install openjdk-11-jdk

# Configurar JAVA_HOME
echo 'export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64' >> ~/.bashrc
source ~/.bashrc

# Verificar
java -version
echo $JAVA_HOME
```

---

## 📦 **Criação do Ambiente Virtual**

### **Por que usar ambiente virtual?**
- Isola dependências do projeto
- Evita conflitos entre bibliotecas
- Facilita reprodução em outros sistemas

### **Criando o ambiente:**

```bash
# 1. Navegar para pasta do projeto
cd "caminho/para/BigData em Python"

# 2. Criar ambiente virtual
python -m venv venv

# 3. Ativar ambiente virtual
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# 4. Verificar se está ativo (deve aparecer (venv) no prompt)
which python  # macOS/Linux
where python   # Windows
```

---

## 📚 **Instalação das Bibliotecas**

### **Passo 1: Instalar dependências básicas**
```bash
# Atualizar pip
python -m pip install --upgrade pip

# Instalar bibliotecas essenciais
pip install pandas numpy matplotlib seaborn

# Verificar instalação
python -c "import pandas as pd; print('✅ Pandas OK!')"
python -c "import numpy as np; print('✅ NumPy OK!')"
python -c "import matplotlib.pyplot as plt; print('✅ Matplotlib OK!')"
```

### **Passo 2: Instalar PySpark**
```bash
# Instalar PySpark
pip install pyspark findspark

# Testar instalação
python -c "
import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Teste').getOrCreate()
print('✅ PySpark funcionando!')
spark.stop()
"
```

### **Passo 3: Machine Learning e IA**
```bash
# Bibliotecas de ML tradicionais
pip install scikit-learn xgboost

# Deep Learning (opcional)
pip install tensorflow torch torchvision

# Processamento de texto (NLP)
pip install nltk spacy transformers

# Verificar ML
python -c "from sklearn.datasets import make_classification; print('✅ Scikit-learn OK!')"
```

### **Passo 4: Jupyter e visualização**
```bash
# Jupyter ecosystem
pip install jupyter jupyterlab ipywidgets

# Visualização avançada
pip install plotly bokeh streamlit

# Iniciar Jupyter Lab
jupyter lab
```

---

## 🔧 **Configuração Avançada**

### **Configurar PySpark no Jupyter**

Criar arquivo `spark_config.py`:
```python
import os
import findspark

# Configurar caminhos (adapte para seu sistema)
os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-11-openjdk-amd64'  # Linux
# os.environ['JAVA_HOME'] = 'C:/Program Files/Java/jdk-11.0.x'  # Windows
# os.environ['JAVA_HOME'] = '/opt/homebrew/opt/openjdk@11/libexec/openjdk.jdk/Contents/Home'  # macOS

findspark.init()

from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

def criar_spark_session(app_name="BigData_SC"):
    """Cria sessão Spark configurada para aprendizado"""
    conf = SparkConf()
    conf.set("spark.sql.adaptive.enabled", "true")
    conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
    
    spark = SparkSession.builder \
        .appName(app_name) \
        .config(conf=conf) \
        .getOrCreate()
    
    return spark

# Usar assim:
# spark = criar_spark_session()
```

### **Configurar GPU para Deep Learning (Opcional)**

**Para NVIDIA GPU:**
```bash
# Verificar se tem GPU NVIDIA
nvidia-smi

# Instalar CUDA toolkit (versão compatível com TensorFlow)
# Windows/Linux: https://developer.nvidia.com/cuda-toolkit
# Verificar compatibilidade: https://www.tensorflow.org/install/source#gpu

# Instalar TensorFlow com GPU
pip install tensorflow[and-cuda]

# Testar GPU
python -c "
import tensorflow as tf
print('GPUs disponíveis:', tf.config.list_physical_devices('GPU'))
"
```

---

## 🧪 **Testes de Validação Completa**

### **Script de teste automático:**

Criar `teste_instalacao.py`:
```python
#!/usr/bin/env python3
"""
Script de validação completa do ambiente Big Data + IA
"""

def teste_bibliotecas_basicas():
    print("🔍 Testando bibliotecas básicas...")
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns
        print("✅ Pandas, NumPy, Matplotlib, Seaborn: OK")
        
        # Teste rápido
        df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
        assert len(df) == 3
        print("✅ Teste funcional Pandas: OK")
        
    except Exception as e:
        print(f"❌ Erro nas bibliotecas básicas: {e}")
        return False
    return True

def teste_pyspark():
    print("\n🔍 Testando PySpark...")
    try:
        import findspark
        findspark.init()
        
        from pyspark.sql import SparkSession
        spark = SparkSession.builder \
            .appName("TesteValidacao") \
            .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
            .getOrCreate()
        
        # Teste com dados
        dados = [("Patrick", 25, "Florianópolis"), ("Ana", 30, "São José")]
        df = spark.createDataFrame(dados, ["nome", "idade", "cidade"])
        
        assert df.count() == 2
        print("✅ PySpark: OK")
        
        spark.stop()
        
    except Exception as e:
        print(f"❌ Erro no PySpark: {e}")
        print("💡 Dica: Verifique se Java está instalado (java -version)")
        return False
    return True

def teste_machine_learning():
    print("\n🔍 Testando Machine Learning...")
    try:
        from sklearn.datasets import make_classification
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score
        
        # Criar dataset sintético
        X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        # Treinar modelo
        model = RandomForestClassifier(n_estimators=10, random_state=42)
        model.fit(X_train, y_train)
        
        # Predizer
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        
        assert acc > 0.7  # Pelo menos 70% de acurácia
        print(f"✅ Scikit-learn: OK (Acurácia: {acc:.3f})")
        
    except Exception as e:
        print(f"❌ Erro no Machine Learning: {e}")
        return False
    return True

def teste_deep_learning():
    print("\n🔍 Testando Deep Learning (opcional)...")
    try:
        import tensorflow as tf
        
        # Verificar GPU
        gpus = tf.config.list_physical_devices('GPU')
        if gpus:
            print(f"✅ TensorFlow com {len(gpus)} GPU(s): OK")
        else:
            print("✅ TensorFlow (CPU apenas): OK")
        
        # Teste simples
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(10, activation='relu', input_shape=(5,)),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        
        # Dados sintéticos
        import numpy as np
        X = np.random.random((100, 5))
        y = np.random.randint(0, 2, (100, 1))
        
        model.compile(optimizer='adam', loss='binary_crossentropy')
        model.fit(X, y, epochs=1, verbose=0)
        
        print("✅ Teste TensorFlow: OK")
        
    except ImportError:
        print("⚠️  TensorFlow não instalado (opcional)")
        return True
    except Exception as e:
        print(f"❌ Erro no TensorFlow: {e}")
        return False
    return True

def teste_jupyter():
    print("\n🔍 Testando Jupyter...")
    try:
        import jupyter
        import jupyterlab
        print("✅ Jupyter Lab: OK")
        print("💡 Para iniciar: jupyter lab")
        
    except Exception as e:
        print(f"❌ Erro no Jupyter: {e}")
        return False
    return True

def relatorio_sistema():
    print("\n📊 Relatório do Sistema:")
    import sys
    import platform
    
    print(f"🐍 Python: {sys.version.split()[0]}")
    print(f"💻 Sistema: {platform.system()} {platform.release()}")
    print(f"🏗️  Arquitetura: {platform.architecture()[0]}")
    
    # Verificar Java
    import subprocess
    try:
        result = subprocess.run(['java', '-version'], 
                              capture_output=True, text=True, stderr=subprocess.STDOUT)
        java_version = result.stdout.split('\n')[0]
        print(f"☕ Java: {java_version}")
    except:
        print("❌ Java: Não encontrado")

if __name__ == "__main__":
    print("🚀 Iniciando validação completa do ambiente Big Data + IA\n")
    
    relatorio_sistema()
    
    testes = [
        teste_bibliotecas_basicas,
        teste_pyspark,
        teste_machine_learning,
        teste_deep_learning,
        teste_jupyter
    ]
    
    resultados = []
    for teste in testes:
        resultado = teste()
        resultados.append(resultado)
    
    print(f"\n📋 Resumo: {sum(resultados)}/{len(resultados)} testes passaram")
    
    if all(resultados):
        print("🎉 Ambiente configurado com sucesso!")
        print("\n📚 Próximos passos:")
        print("1. jupyter lab")
        print("2. Abrir livro/capitulo01-despertar-dos-dados.md")
        print("3. Seguir a jornada de Patrick em Big Data!")
    else:
        print("⚠️  Alguns testes falharam. Verifique a instalação.")
```

### **Executar validação:**
```bash
python teste_instalacao.py
```

---

## 🚨 **Solução de Problemas Comuns**

### **1. "Java not found" no PySpark**
```bash
# Verificar se Java está no PATH
java -version

# Se não encontrar, definir JAVA_HOME
# Windows (PowerShell):
$env:JAVA_HOME = "C:\Program Files\Java\jdk-11.0.x"

# macOS/Linux:
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

### **2. "Permission denied" no macOS/Linux**
```bash
# Dar permissões de execução
chmod +x teste_instalacao.py

# Usar sudo apenas se necessário
sudo pip install nome_biblioteca
```

### **3. Conflitos de versão**
```bash
# Limpar cache do pip
pip cache purge

# Reinstalar tudo
pip uninstall -y -r requirements.txt
pip install -r requirements.txt
```

### **4. Problemas com Jupyter**
```bash
# Recriar kernels
python -m ipykernel install --user --name=venv

# Iniciar Jupyter com configurações padrão
jupyter lab --generate-config
```

---

## 🎯 **Próximos Passos**

1. **✅ Executar teste de validação**
2. **📚 Ler Capítulo 1** - Patrick e os fundamentos de Big Data
3. **💻 Abrir Jupyter Lab** - ambiente interativo
4. **🔬 Experimentar códigos** - cada capítulo tem exemplos
5. **🚀 Criar seu primeiro projeto** - adaptar casos para sua região

**Ambiente configurado? Hora de começar a jornada com Patrick! 🌟**
