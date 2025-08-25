"""
Aula 01 - Big Data: Trabalhando com Variedade de Dados
Professor: Vagner Cordeiro
"""

import pandas as pd
import numpy as np
import json
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import requests
import sqlite3
import os

class VarietyDataProcessor:
    """
    Classe para processar diferentes tipos de dados (Variedade)
    """
    
    def __init__(self):
        self.processed_data = {}
        
    def processar_csv(self, dados_csv=None):
        """
        Processa dados estruturados em CSV
        """
        print("📊 PROCESSANDO DADOS CSV (Estruturados)")
        print("-" * 40)
        
        if dados_csv is None:
            # Criar dados de exemplo
            dados_csv = {
                'id': range(1, 101),
                'nome_produto': [f'Produto {i}' for i in range(1, 101)],
                'preco': np.random.uniform(10, 1000, 100),
                'categoria': np.random.choice(['Eletrônicos', 'Roupas', 'Casa', 'Livros'], 100),
                'avaliacao': np.random.uniform(1, 5, 100)
            }
        
        df = pd.DataFrame(dados_csv)
        
        print(f"✅ Dados CSV carregados: {df.shape}")
        print(f"📋 Colunas: {list(df.columns)}")
        print(f"📈 Estatísticas básicas:")
        print(df.describe())
        
        self.processed_data['csv'] = df
        return df
    
    def processar_json(self):
        """
        Processa dados semi-estruturados em JSON
        """
        print("\n🌐 PROCESSANDO DADOS JSON (Semi-estruturados)")
        print("-" * 40)
        
        # Simular dados JSON de API de redes sociais
        json_data = []
        for i in range(50):
            post = {
                'id': i + 1,
                'usuario': f'user_{i+1}',
                'texto': f'Este é um post interessante número {i+1} sobre Big Data!',
                'timestamp': datetime.now().isoformat(),
                'curtidas': np.random.randint(0, 1000),
                'comentarios': [
                    {
                        'autor': f'comentarista_{j}',
                        'texto': f'Comentário {j} no post {i+1}',
                        'likes': np.random.randint(0, 50)
                    }
                    for j in range(np.random.randint(0, 5))
                ],
                'hashtags': np.random.choice(
                    ['#bigdata', '#python', '#datascience', '#ai', '#tech'], 
                    size=np.random.randint(1, 4),
                    replace=False
                ).tolist(),
                'localizacao': {
                    'cidade': np.random.choice(['São Paulo', 'Rio de Janeiro', 'Brasília']),
                    'coordenadas': {
                        'lat': np.random.uniform(-25, -5),
                        'lon': np.random.uniform(-60, -35)
                    }
                }
            }
            json_data.append(post)
        
        # Salvar JSON
        with open('dados_social_media.json', 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        
        # Processar JSON para DataFrame
        posts_flat = []
        for post in json_data:
            post_flat = {
                'post_id': post['id'],
                'usuario': post['usuario'],
                'texto': post['texto'],
                'curtidas': post['curtidas'],
                'num_comentarios': len(post['comentarios']),
                'hashtags': ', '.join(post['hashtags']),
                'cidade': post['localizacao']['cidade'],
                'latitude': post['localizacao']['coordenadas']['lat'],
                'longitude': post['localizacao']['coordenadas']['lon']
            }
            posts_flat.append(post_flat)
        
        df_json = pd.DataFrame(posts_flat)
        
        print(f"✅ Dados JSON processados: {df_json.shape}")
        print(f"📋 Estrutura achatada criada")
        print(f"🏷️ Hashtags mais populares:")
        
        # Análise de hashtags
        all_hashtags = []
        for hashtags in df_json['hashtags']:
            all_hashtags.extend(hashtags.split(', '))
        
        hashtag_counts = pd.Series(all_hashtags).value_counts()
        print(hashtag_counts.head())
        
        self.processed_data['json'] = df_json
        return df_json
    
    def processar_texto_nao_estruturado(self):
        """
        Processa dados não estruturados (texto livre)
        """
        print("\n📝 PROCESSANDO TEXTO NÃO ESTRUTURADO")
        print("-" * 40)
        
        # Simular logs de servidor web
        log_entries = []
        ips = ['192.168.1.10', '10.0.0.15', '172.16.0.5', '203.0.113.12']
        methods = ['GET', 'POST', 'PUT', 'DELETE']
        paths = ['/api/users', '/api/products', '/login', '/dashboard', '/admin']
        status_codes = [200, 404, 500, 301, 403]
        
        for i in range(200):
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ip = np.random.choice(ips)
            method = np.random.choice(methods)
            path = np.random.choice(paths)
            status = np.random.choice(status_codes, p=[0.7, 0.1, 0.05, 0.1, 0.05])
            size = np.random.randint(100, 10000)
            
            log_entry = f'{timestamp} {ip} "{method} {path} HTTP/1.1" {status} {size}'
            log_entries.append(log_entry)
        
        # Salvar logs
        with open('server_logs.txt', 'w') as f:
            for entry in log_entries:
                f.write(entry + '\n')
        
        # Processar logs usando regex
        import re
        
        log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\S+) "(\w+) (\S+) HTTP/1.1" (\d+) (\d+)'
        
        parsed_logs = []
        for log in log_entries:
            match = re.match(log_pattern, log)
            if match:
                parsed_logs.append({
                    'timestamp': match.group(1),
                    'ip': match.group(2),
                    'method': match.group(3),
                    'path': match.group(4),
                    'status_code': int(match.group(5)),
                    'response_size': int(match.group(6))
                })
        
        df_logs = pd.DataFrame(parsed_logs)
        
        print(f"✅ Logs processados: {df_logs.shape}")
        print(f"📊 Análise de status codes:")
        print(df_logs['status_code'].value_counts())
        print(f"\n🌐 IPs mais ativos:")
        print(df_logs['ip'].value_counts())
        
        self.processed_data['texto'] = df_logs
        return df_logs
    
    def processar_dados_binarios(self):
        """
        Simula processamento de dados binários (imagens, etc.)
        """
        print("\n🖼️ SIMULANDO DADOS BINÁRIOS (Imagens)")
        print("-" * 40)
        
        # Simular metadados de imagens
        image_metadata = []
        
        for i in range(30):
            metadata = {
                'arquivo': f'image_{i+1:03d}.jpg',
                'tamanho_kb': np.random.randint(500, 5000),
                'resolucao_width': np.random.choice([1920, 1280, 800, 3840]),
                'resolucao_height': np.random.choice([1080, 720, 600, 2160]),
                'formato': np.random.choice(['JPEG', 'PNG', 'TIFF']),
                'data_criacao': datetime.now().isoformat(),
                'camera_marca': np.random.choice(['Canon', 'Nikon', 'Sony', 'iPhone']),
                'tem_flash': np.random.choice([True, False]),
                'localizacao_gps': {
                    'lat': np.random.uniform(-25, -5),
                    'lon': np.random.uniform(-60, -35)
                } if np.random.random() > 0.3 else None
            }
            image_metadata.append(metadata)
        
        # Processar metadados
        df_images = pd.json_normalize(image_metadata)
        
        print(f"✅ Metadados de imagens processados: {df_images.shape}")
        print(f"📊 Distribuição por formato:")
        print(df_images['formato'].value_counts())
        print(f"\n📷 Marcas de câmera:")
        print(df_images['camera_marca'].value_counts())
        
        self.processed_data['binario'] = df_images
        return df_images
    
    def criar_visualizacao_variedade(self):
        """
        Cria visualizações mostrando a variedade de dados
        """
        print("\n📊 CRIANDO VISUALIZAÇÕES DA VARIEDADE")
        print("-" * 40)
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Big Data: Processamento de Variedade de Dados', fontsize=16, fontweight='bold')
        
        # 1. Dados CSV - Categorias de produtos
        if 'csv' in self.processed_data:
            df_csv = self.processed_data['csv']
            categoria_counts = df_csv['categoria'].value_counts()
            axes[0, 0].pie(categoria_counts.values, labels=categoria_counts.index, autopct='%1.1f%%')
            axes[0, 0].set_title('Dados CSV: Produtos por Categoria')
        
        # 2. Dados JSON - Curtidas por cidade
        if 'json' in self.processed_data:
            df_json = self.processed_data['json']
            cidade_curtidas = df_json.groupby('cidade')['curtidas'].mean()
            axes[0, 1].bar(cidade_curtidas.index, cidade_curtidas.values, color='skyblue')
            axes[0, 1].set_title('Dados JSON: Curtidas Médias por Cidade')
            axes[0, 1].set_ylabel('Curtidas Médias')
        
        # 3. Dados de Texto - Status codes
        if 'texto' in self.processed_data:
            df_logs = self.processed_data['texto']
            status_counts = df_logs['status_code'].value_counts()
            axes[1, 0].bar(status_counts.index.astype(str), status_counts.values, color='orange')
            axes[1, 0].set_title('Dados de Texto: Status Codes dos Logs')
            axes[1, 0].set_ylabel('Frequência')
        
        # 4. Dados Binários - Resolução das imagens
        if 'binario' in self.processed_data:
            df_images = self.processed_data['binario']
            df_images['resolucao'] = df_images['resolucao_width'].astype(str) + 'x' + df_images['resolucao_height'].astype(str)
            res_counts = df_images['resolucao'].value_counts()
            axes[1, 1].barh(res_counts.index, res_counts.values, color='green')
            axes[1, 1].set_title('Dados Binários: Resoluções de Imagem')
            axes[1, 1].set_xlabel('Quantidade')
        
        plt.tight_layout()
        plt.savefig('variedade_dados_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✅ Visualizações salvas em 'variedade_dados_analysis.png'")
    
    def consolidar_dados(self):
        """
        Consolida todos os tipos de dados em um relatório final
        """
        print("\n📋 CONSOLIDAÇÃO DE DADOS")
        print("=" * 40)
        
        total_registros = 0
        tipos_dados = []
        
        for tipo, dados in self.processed_data.items():
            registros = len(dados)
            total_registros += registros
            tipos_dados.append({
                'Tipo': tipo.upper(),
                'Registros': registros,
                'Colunas': len(dados.columns) if hasattr(dados, 'columns') else 'N/A',
                'Tamanho_MB': round(dados.memory_usage(deep=True).sum() / 1024**2, 2) if hasattr(dados, 'memory_usage') else 'N/A'
            })
        
        df_consolidado = pd.DataFrame(tipos_dados)
        
        print(f"📊 RESUMO DA VARIEDADE PROCESSADA:")
        print(df_consolidado.to_string(index=False))
        print(f"\n📈 Total de registros processados: {total_registros:,}")
        print(f"🔢 Tipos de dados diferentes: {len(tipos_dados)}")
        
        return df_consolidado

def main():
    """
    Função principal demonstrando conceitos de Variedade em Big Data
    """
    print("🎓 AULA 01 - BIG DATA: CONCEITO DE VARIEDADE")
    print("👨‍🏫 Professor: Vagner Cordeiro")
    print("="*60)
    
    print("\n🎯 OBJETIVOS:")
    print("✅ Entender o conceito de VARIEDADE em Big Data")
    print("✅ Processar dados estruturados (CSV)")
    print("✅ Processar dados semi-estruturados (JSON)")
    print("✅ Processar dados não estruturados (Texto)")
    print("✅ Trabalhar com metadados de arquivos binários")
    print("✅ Consolidar diferentes tipos de dados")
    
    # Inicializar processador
    processor = VarietyDataProcessor()
    
    # Processar diferentes tipos de dados
    print(f"\n🚀 INICIANDO PROCESSAMENTO DE VARIEDADE DE DADOS")
    print("="*60)
    
    # 1. Dados estruturados (CSV)
    df_csv = processor.processar_csv()
    
    # 2. Dados semi-estruturados (JSON)
    df_json = processor.processar_json()
    
    # 3. Dados não estruturados (Texto)
    df_texto = processor.processar_texto_nao_estruturado()
    
    # 4. Dados binários (Metadados)
    df_binario = processor.processar_dados_binarios()
    
    # 5. Criar visualizações
    processor.criar_visualizacao_variedade()
    
    # 6. Consolidar resultados
    df_resumo = processor.consolidar_dados()
    
    # Salvar resultados
    print(f"\n💾 SALVANDO RESULTADOS...")
    df_csv.to_csv('processed_csv_data.csv', index=False)
    df_json.to_csv('processed_json_data.csv', index=False)
    df_texto.to_csv('processed_text_data.csv', index=False)
    df_binario.to_csv('processed_binary_metadata.csv', index=False)
    df_resumo.to_csv('variety_summary.csv', index=False)
    
    print(f"✅ Todos os dados processados salvos!")
    
    print(f"\n🎯 RESUMO DA AULA:")
    print(f"✅ Processamos 4 tipos diferentes de dados")
    print(f"✅ CSV: Dados estruturados tradicionais")
    print(f"✅ JSON: Dados semi-estruturados de APIs")
    print(f"✅ Texto: Logs não estruturados")
    print(f"✅ Binário: Metadados de imagens")
    print(f"✅ Criamos visualizações de cada tipo")
    print(f"✅ Consolidamos tudo em um relatório final")
    
    print(f"\n💡 DICAS IMPORTANTES:")
    print(f"🔹 Pandas é excelente para dados estruturados")
    print(f"🔹 JSON requer normalização para análise")
    print(f"🔹 Regex é crucial para dados não estruturados")
    print(f"🔹 Metadados ajudam a entender dados binários")
    print(f"🔹 Big Data = múltiplos formatos juntos!")

if __name__ == "__main__":
    main()
