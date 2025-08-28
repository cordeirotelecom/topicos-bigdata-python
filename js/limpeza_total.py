# LIMPEZA TOTAL E DEFINITIVA - APENAS O ESSENCIAL
# Objetivo: Deixar SOMENTE arquivos educacionais necessários
# Professor: Vagner Cordeiro

import os
import shutil

def remover_pastas_desnecessarias():
    """Remove pastas que não são essenciais para o projeto educacional"""
    print("🗑️ REMOVENDO PASTAS DESNECESSÁRIAS")
    print("=" * 50)
    
    pastas_remover = [
        "home",           # Pasta com arquivos pessoais
        "datasets",       # Datasets vazios
        "notebooks",      # Pasta vazia
        "projetos",       # Pasta vazia  
        "simulados",      # Pasta vazia
        "trabalho-final", # Não essencial para aulas
        "materiais",      # Redundante
        ".vscode",        # Configurações do editor
        ".venv"           # Ambiente virtual local
    ]
    
    for pasta in pastas_remover:
        if os.path.exists(pasta):
            try:
                shutil.rmtree(pasta)
                print(f"🗑️ Removida pasta: {pasta}/")
            except Exception as e:
                print(f"❌ Erro ao remover {pasta}: {e}")

def remover_arquivos_desnecessarios():
    """Remove arquivos que não são essenciais"""
    print("\n🗑️ REMOVENDO ARQUIVOS DESNECESSÁRIOS")
    print("=" * 50)
    
    arquivos_remover = [
        "contato.md",
        "cronograma-expandido.md", 
        "cronograma.md",
        "index.md",
        "INSTALACAO.md",
        "INSTRUCOES-GITHUB-PROFILE.md",
        "materiais.md",
        "projetos.md", 
        "README-expandido.md",
        "README-GITHUB-PROFILE.md",
        "snake-github-action.yml",
        "_config.yml",
        ".gitignore"
    ]
    
    for arquivo in arquivos_remover:
        if os.path.exists(arquivo):
            try:
                os.remove(arquivo)
                print(f"🗑️ Removido: {arquivo}")
            except Exception as e:
                print(f"❌ Erro ao remover {arquivo}: {e}")

def manter_apenas_essencial():
    """Mantém apenas o que é realmente necessário"""
    print("\n✅ MANTENDO APENAS O ESSENCIAL")
    print("=" * 50)
    
    # Arquivos essenciais que devem permanecer
    essenciais = [
        "README.md",           # Documentação principal
        "requirements.txt",    # Dependências Python
        "aulas/",             # Conteúdo das aulas
        "livro/",             # Material do livro
        "assets/",            # Recursos visuais
        ".github/"            # Configurações do GitHub
    ]
    
    print("📋 ARQUIVOS/PASTAS ESSENCIAIS MANTIDOS:")
    for item in essenciais:
        if os.path.exists(item.rstrip('/')):
            print(f"✅ {item}")
        else:
            print(f"❌ {item} (não encontrado)")

def criar_estrutura_final():
    """Cria estrutura final limpa e organizada"""
    print("\n📁 ESTRUTURA FINAL DO PROJETO")
    print("=" * 50)
    
    # Listar estrutura final
    print("📊 PROJETO: Tópicos de Big Data em Python")
    print("├── 📄 README.md")
    print("├── 📄 requirements.txt") 
    print("├── 📁 .github/")
    print("├── 📁 assets/")
    print("├── 📁 aulas/")
    
    # Contar aulas
    if os.path.exists("aulas"):
        aulas = [d for d in os.listdir("aulas") if os.path.isdir(f"aulas/{d}") and d.startswith("aula")]
        print(f"│   ├── 📚 {len(aulas)} aulas organizadas")
        for aula in sorted(aulas)[:3]:  # Mostrar apenas 3 primeiras
            print(f"│   ├── 📂 {aula}/")
        if len(aulas) > 3:
            print(f"│   └── ... e mais {len(aulas)-3} aulas")
    
    print("└── 📁 livro/")
    
    if os.path.exists("livro"):
        livro_files = [f for f in os.listdir("livro") if f.endswith('.md')]
        print(f"    └── 📖 {len(livro_files)} capítulos do livro")

def main():
    """Executa limpeza total e definitiva"""
    print("🧹 LIMPEZA TOTAL E DEFINITIVA")
    print("🎯 Objetivo: Manter apenas arquivos educacionais essenciais")
    print("=" * 60)
    
    remover_pastas_desnecessarias()
    remover_arquivos_desnecessarios() 
    manter_apenas_essencial()
    criar_estrutura_final()
    
    print("\n" + "=" * 60)
    print("🎉 LIMPEZA TOTAL CONCLUÍDA!")
    print("✅ Projeto 100% focado em educação")
    print("✅ Sem arquivos desnecessários")
    print("✅ Estrutura profissional e limpa")
    print("✅ Pronto para uso acadêmico")
    print("=" * 60)

if __name__ == "__main__":
    main()
