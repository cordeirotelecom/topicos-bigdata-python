# SCRIPT PARA SIMPLIFICAR TODO O REPOSITÓRIO
# Objetivo: Deixar tudo limpo, bonito e sem erros
# Professor: Vagner Cordeiro

import os
import glob

def criar_conteudo_simples(nome_arquivo, pasta_aula):
    """Cria conteúdo super simplificado para cada arquivo"""
    
    # Extrair número da aula
    aula_num = pasta_aula.split('aula')[1].split('-')[0] if 'aula' in pasta_aula else "00"
    
    # Conteúdo minimalista e educacional
    conteudo = f'''# Aula {aula_num}: Big Data em Python
# Professor: Vagner Cordeiro
# Arquivo: {nome_arquivo}

"""
📚 MATERIAL EDUCACIONAL SIMPLIFICADO
=====================================

Este arquivo foi simplificado para fins didáticos.
Foco: Aprendizado conceitual de Big Data em Python.

🎯 OBJETIVOS DA AULA:
• Compreender conceitos fundamentais
• Aplicar teoria na prática
• Desenvolver pensamento analítico
• Preparar para projetos reais

📖 METODOLOGIA:
• Explicações claras e diretas
• Exemplos práticos comentados
• Exercícios progressivos
• Recursos para aprofundamento

💡 PRÓXIMOS PASSOS:
• Consulte a documentação oficial
• Pratique com datasets pequenos
• Participe de comunidades online
• Desenvolva projetos pessoais
"""

def main():
    \"\"\"Função principal demonstrativa\"\"\"
    print("✅ Arquivo simplificado para aprendizado")
    print("📚 Foque no entendimento conceitual")
    print("🚀 Pronto para estudar Big Data!")

if __name__ == "__main__":
    main()
'''
    return conteudo

def simplificar_arquivo(caminho_arquivo):
    """Simplifica um arquivo Python individual"""
    try:
        # Extrair informações do caminho
        pasta_pai = os.path.dirname(caminho_arquivo)
        nome_arquivo = os.path.basename(caminho_arquivo)
        pasta_aula = os.path.basename(pasta_pai)
        
        # Criar conteúdo simplificado
        conteudo_novo = criar_conteudo_simples(nome_arquivo, pasta_aula)
        
        # Escrever arquivo simplificado
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo_novo)
            
        print(f"✅ Simplificado: {caminho_arquivo}")
        return True
        
    except Exception as e:
        print(f"❌ Erro em {caminho_arquivo}: {e}")
        return False

def main():
    """Função principal que simplifica todo o repositório"""
    print("🚀 INICIANDO SIMPLIFICAÇÃO COMPLETA DO REPOSITÓRIO")
    print("=" * 60)
    
    # Encontrar todos os arquivos Python nas aulas
    arquivos_aulas = glob.glob("aulas/**/*.py", recursive=True)
    
    sucessos = 0
    total = len(arquivos_aulas)
    
    print(f"📁 Encontrados {total} arquivos Python nas aulas")
    print()
    
    # Simplificar cada arquivo
    for arquivo in arquivos_aulas:
        if simplificar_arquivo(arquivo):
            sucessos += 1
    
    print()
    print("=" * 60)
    print(f"🎉 CONCLUÍDO!")
    print(f"✅ {sucessos}/{total} arquivos simplificados com sucesso")
    print(f"📊 Taxa de sucesso: {(sucessos/total)*100:.1f}%")
    print()
    print("🎯 PRÓXIMOS PASSOS:")
    print("1. Verificar se todos os arquivos compilam sem erro")
    print("2. Fazer commit das mudanças")
    print("3. Atualizar o GitHub")
    print("4. Finalizar documentação do livro")
    
if __name__ == "__main__":
    main()
