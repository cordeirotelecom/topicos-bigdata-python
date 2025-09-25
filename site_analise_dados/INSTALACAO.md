# 🎓 Guia de Instalação Completo
## Tópicos de Big Data em Python - Prof. Vagner Cordeiro

---

## 📋 **Pré-requisitos**

### **Sistema Operacional**
- **Windows 10/11** (64-bit)
- **macOS 10.14+**
- **Linux Ubuntu 18.04+**
- **Mínimo**: 8GB RAM, 20GB espaço livre
- **Recomendado**: 16GB RAM, 50GB espaço livre

---

## 🐍 **Passo 1: Instalação do Python**

### **Opção A: Anaconda (Recomendado)**
1. **Download**: https://www.anaconda.com/products/distribution
2. **Instalar** com todas as opções padrão
3. **Verificar**:
   ```bash
   python --version
   conda --version
   ```

### **Opção B: Python Oficial**
1. **Download**: https://python.org/downloads/
2. **Marcar**: "Add Python to PATH"
3. **Verificar**:
   ```bash
   python --version
   pip --version
   ```

---

## 📦 **Passo 2: Dependências do Curso**

### **Instalação Automática**
```bash
# Clonar repositório
git clone https://github.com/cordeirotelecom/topicos-bigdata-python.git
cd topicos-bigdata-python

# Instalar dependências
pip install -r requirements.txt
```

### **Instalação Manual**
```bash
# Análise de dados fundamentais
pip install pandas numpy matplotlib seaborn

# Big Data
pip install pyspark apache-beam

# Machine Learning
pip install scikit-learn tensorflow

# Visualização
pip install plotly bokeh

# Jupyter
pip install jupyter jupyterlab
```

---

## ⚡ **Passo 3: Apache Spark**

### **Windows**
1. **Java 8/11**:
   - Download: https://adoptopenjdk.net/
   - Instalar e configurar JAVA_HOME

2. **Spark**:
   ```bash
   # Download Spark
   # https://spark.apache.org/downloads.html
   
   # Extrair para C:\spark
   
   # Variáveis de ambiente
   SPARK_HOME=C:\spark
   HADOOP_HOME=C:\spark
   PATH=%PATH%;%SPARK_HOME%\bin
   ```

3. **winutils**:
   - Download: https://github.com/steveloughran/winutils
   - Colocar em C:\spark\bin\

### **Linux/macOS**
```bash
# Java
sudo apt install openjdk-8-jdk  # Ubuntu
brew install openjdk@8          # macOS

# Spark
wget https://downloads.apache.org/spark/spark-3.3.0/spark-3.3.0-bin-hadoop3.tgz
tar -xzf spark-3.3.0-bin-hadoop3.tgz
sudo mv spark-3.3.0-bin-hadoop3 /opt/spark

# Variáveis de ambiente (.bashrc)
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin
export PYSPARK_PYTHON=python3
```

---

## 🐳 **Passo 4: Docker (Opcional)**

### **Instalação**
1. **Docker Desktop**: https://docker.com/products/docker-desktop
2. **Verificar**: `docker --version`

### **Ambiente Big Data Completo**
```bash
# Baixar imagem com ambiente completo
docker pull cordeirotelecom/bigdata-python:latest

# Executar
docker run -p 8888:8888 -p 4040:4040 -v $(pwd):/workspace cordeirotelecom/bigdata-python:latest
```

---

## ☁️ **Passo 5: Cloud Platforms**

### **AWS**
```bash
# AWS CLI
pip install awscli boto3

# Configurar
aws configure
```

### **Google Cloud**
```bash
# SDK
curl https://sdk.cloud.google.com | bash

# Bibliotecas Python
pip install google-cloud-storage google-cloud-bigquery
```

### **Azure**
```bash
# CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Bibliotecas Python
pip install azure-storage-blob azure-identity
```

---

## 📊 **Passo 6: Power BI**

### **Power BI Desktop**
1. **Download**: https://powerbi.microsoft.com/desktop/
2. **Instalar** (Windows apenas)
3. **Conta**: Criar conta Microsoft gratuita

### **Python Integration**
1. **Configurar Python** no Power BI:
   - File → Options → Python scripting
   - Apontar para instalação Python

2. **Bibliotecas necessárias**:
   ```bash
   pip install pandas matplotlib seaborn
   ```

---

## 🔧 **Passo 7: Ferramentas de Desenvolvimento**

### **VS Code**
1. **Download**: https://code.visualstudio.com/
2. **Extensões essenciais**:
   - Python
   - Jupyter
   - Python Docstring Generator
   - GitLens

### **Jupyter Lab**
```bash
# Instalar
pip install jupyterlab

# Executar
jupyter lab

# Acessar: http://localhost:8888
```

### **Git**
```bash
# Windows
https://git-scm.com/download/win

# Linux
sudo apt install git

# macOS
brew install git

# Configurar
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@email.com"
```

---

## ✅ **Passo 8: Verificação da Instalação**

### **Script de Teste**
```python
# test_installation.py
import sys
print(f"Python: {sys.version}")

try:
    import pandas as pd
    print(f"✅ Pandas: {pd.__version__}")
except ImportError:
    print("❌ Pandas não instalado")

try:
    import numpy as np
    print(f"✅ NumPy: {np.__version__}")
except ImportError:
    print("❌ NumPy não instalado")

try:
    import matplotlib
    print(f"✅ Matplotlib: {matplotlib.__version__}")
except ImportError:
    print("❌ Matplotlib não instalado")

try:
    import pyspark
    print(f"✅ PySpark: {pyspark.__version__}")
except ImportError:
    print("❌ PySpark não instalado")

try:
    import sklearn
    print(f"✅ Scikit-learn: {sklearn.__version__}")
except ImportError:
    print("❌ Scikit-learn não instalado")

print("\n🎯 Instalação verificada!")
```

### **Executar Teste**
```bash
python test_installation.py
```

---

## 🆘 **Solução de Problemas**

### **Erro: Java não encontrado**
```bash
# Verificar JAVA_HOME
echo $JAVA_HOME  # Linux/macOS
echo %JAVA_HOME% # Windows

# Configurar se necessário
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  # Linux
```

### **Erro: PySpark não funciona**
```bash
# Verificar variáveis
echo $SPARK_HOME
echo $PYSPARK_PYTHON

# Reconfigurar
export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='lab'
```

### **Erro: Módulo não encontrado**
```bash
# Verificar pip
which pip
pip list

# Reinstalar se necessário
pip uninstall pandas
pip install pandas
```

### **Problemas de Memória**
```bash
# Aumentar memória JVM
export SPARK_DRIVER_MEMORY=4g
export SPARK_EXECUTOR_MEMORY=4g
```

---

## 📚 **Recursos Adicionais**

### **Documentação**
- **Python**: https://docs.python.org/3/
- **Pandas**: https://pandas.pydata.org/docs/
- **Spark**: https://spark.apache.org/docs/latest/
- **Jupyter**: https://jupyter.org/documentation

### **Tutoriais**
- **Anaconda**: https://docs.anaconda.com/anaconda/user-guide/
- **Docker**: https://docs.docker.com/get-started/
- **AWS**: https://aws.amazon.com/getting-started/

### **Comunidades**
- **Stack Overflow**: https://stackoverflow.com/questions/tagged/python
- **Reddit**: https://reddit.com/r/Python
- **Discord**: Python Discord Server

---

## 🎯 **Checklist Final**

- [ ] Python instalado e funcionando
- [ ] Pandas, NumPy, Matplotlib funcionando
- [ ] Jupyter Lab funcionando
- [ ] PySpark configurado
- [ ] Java instalado (para Spark)
- [ ] Git configurado
- [ ] VS Code com extensões Python
- [ ] Power BI instalado (Windows)
- [ ] Cloud CLI configurado (opcional)
- [ ] Docker funcionando (opcional)
- [ ] Script de teste executado com sucesso

---

**✨ Parabéns! Seu ambiente está pronto para o curso de Big Data em Python!**

📞 **Suporte**: Em caso de problemas, entre em contato via Discord ou email do curso.
