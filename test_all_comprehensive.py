
# Imports de fallback para compatibilidade
try:
    from typing import Any, Dict, List, Optional, Union
except ImportError:
    # Python < 3.5
    Any = object
    Dict = dict
    List = list
    Optional = object
    Union = object

#!/usr/bin/env python3
"""
Teste Abrangente - Verifica se todos os arquivos executam sem erros críticos
"""

import os
import sys
import subprocess
from pathlib import Path

def test_all_python_files():
    """Testa todos os arquivos Python do projeto"""
    print("🧪 TESTE ABRANGENTE DO PROJETO")
    print("=" * 50)
    
    base_dir = Path(__file__).parent
    python_files = list(base_dir.rglob("*.py"))
    
    # Exclui este próprio arquivo
    python_files = [f for f in python_files if f.name != "test_all_comprehensive.py"]
    
    print(f"📁 Testando {len(python_files)} arquivos...")
    
    passed = 0
    failed = 0
    
    for file_path in python_files:
        try:
            # Tenta executar o arquivo
            result = subprocess.run(
                [sys.executable, str(file_path)], 
                capture_output=True, 
                text=True, 
                timeout=30  # Timeout de 30 segundos
            )
            
            if result.returncode == 0:
                print(f"✅ {file_path.name}")
                passed += 1
            else:
                print(f"❌ {file_path.name} - Exit code: {result.returncode}")
                failed += 1
                
        except subprocess.TimeoutExpired:
            print(f"⏰ {file_path.name} - Timeout")
            failed += 1
        except Exception as e:
            print(f"💥 {file_path.name} - Erro: {e}")
            failed += 1
    
    print(f"\n📊 RESULTADOS:")
    print(f"✅ Passou: {passed}")
    print(f"❌ Falhou: {failed}")
    print(f"📈 Taxa de sucesso: {passed/(passed+failed)*100:.1f}%")
    
    if failed == 0:
        print("\n🎉 TODOS OS ARQUIVOS PASSARAM NO TESTE!")
    else:
        print(f"\n⚠️ {failed} arquivos ainda têm problemas")

if __name__ == "__main__":
    test_all_python_files()
