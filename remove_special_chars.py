# Script para remover emojis e caracteres especiais que causam erros de linter
# Execução: python remove_special_chars.py

import os
import glob
import re

def clean_special_characters(content):
    """Remove emojis e caracteres especiais problemáticos"""
    
    # Remover emojis (Unicode ranges)
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
        "]+", flags=re.UNICODE)
    
    # Substituir caracteres problemáticos
    replacements = {
        # Emojis específicos que ficaram
        '📚': 'MATERIAL',
        '🔸': '*',
        '👨‍🏫': 'Professor:',
        '📊': 'DADOS:',
        '⚡': 'VELOCIDADE:',
        '🎨': 'VARIEDADE:',
        '🌐': 'IOT:',
        '📡': 'CONCEITOS:',
        '🏭': 'INDUSTRIA:',
        '🌊': 'EDGE:',
        '☁️': 'CLOUD:',
        '🔄': 'PROCESSAMENTO:',
        '🔐': 'SEGURANCA:',
        '📈': 'ANALYTICS:',
        '🎯': 'OBJETIVO:',
        '📝': 'EXERCICIOS:',
        '🚀': 'FUTURO:',
        '⚠️': 'ATENCAO:',
        '✅': 'OK:',
        '❌': 'ERRO:',
        '🎉': 'SUCESSO:',
        # Caracteres especiais
        '•': '-',
        '→': '->',
        '…': '...',
        '"': '"',
        '"': '"',
        ''': "'",
        ''': "'",
        '–': '-',
        '—': '-',
        '═': '=',
        '║': '|',
        '╔': '+',
        '╗': '+',
        '╚': '+',
        '╝': '+',
        '╠': '+',
        '╣': '+',
        '╦': '+',
        '╩': '+',
        '╬': '+',
    }
    
    # Aplicar substituições
    cleaned = content
    for old, new in replacements.items():
        cleaned = cleaned.replace(old, new)
    
    # Remover emojis restantes
    cleaned = emoji_pattern.sub('', cleaned)
    
    # Limpar linhas vazias extras
    cleaned = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned)
    
    return cleaned

def main():
    """Função principal que limpa todos os arquivos"""
    
    base_dir = r"c:\Users\corde\OneDrive\Desktop\BigData em Python\aulas"
    python_files = glob.glob(os.path.join(base_dir, "**", "*.py"), recursive=True)
    
    print("🧹 LIMPANDO CARACTERES ESPECIAIS E EMOJIS...")
    print("=" * 60)
    
    cleaned_count = 0
    
    for file_path in python_files:
        try:
            # Ler arquivo
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # Limpar caracteres especiais
            cleaned_content = clean_special_characters(original_content)
            
            # Se houve mudanças, salvar
            if cleaned_content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                print(f"✅ Limpo: {os.path.basename(file_path)}")
                cleaned_count += 1
            else:
                print(f"⚪ Já limpo: {os.path.basename(file_path)}")
                
        except Exception as e:
            print(f"❌ Erro: {file_path} - {e}")
    
    print("=" * 60)
    print(f"🎉 LIMPEZA COMPLETA!")
    print(f"📊 Arquivos processados: {len(python_files)}")
    print(f"🧹 Arquivos limpos: {cleaned_count}")
    print(f"🎯 Erros de caracteres especiais: ELIMINADOS!")

if __name__ == "__main__":
    main()
