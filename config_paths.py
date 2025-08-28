#!/usr/bin/env python3
"""
Configuração de Paths e Imports para Big Data em Python
Adicione este import no início dos seus notebooks/scripts
"""

import sys
import os
from pathlib import Path

# Adiciona paths do projeto
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "aulas"))
sys.path.insert(0, str(project_root / "notebooks"))
sys.path.insert(0, str(project_root / "livro"))

# Configurações para PySpark
os.environ.setdefault('PYSPARK_PYTHON', sys.executable)
os.environ.setdefault('PYSPARK_DRIVER_PYTHON', sys.executable)

# Suprime warnings desnecessários
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)

# Configuração de logging
import logging
logging.getLogger("py4j").setLevel(logging.WARN)

print("✅ Configuração de paths carregada com sucesso!")
print(f"📁 Projeto root: {project_root}")
print(f"🐍 Python executable: {sys.executable}")
