#!/usr/bin/env python3
"""
Hadoop MapReduce Examples - Python Implementation
Demonstra conceitos fundamentais do paradigma MapReduce
"""

import os
import sys
import logging
from collections import defaultdict, Counter
from datetime import datetime
import re
import json

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class HDFSManager:
    """Gerenciador para operações HDFS usando subprocess"""
    
    def __init__(self):
        self.hdfs_cmd = "hdfs dfs"
    
    def upload_file(self, local_path, hdfs_path):
        """Upload arquivo para HDFS"""
        cmd = f"{self.hdfs_cmd} -put {local_path} {hdfs_path}"
        logger.info(f"Uploading: {cmd}")
        return os.system(cmd) == 0
    
    def download_file(self, hdfs_path, local_path):
        """Download arquivo do HDFS"""
        cmd = f"{self.hdfs_cmd} -get {hdfs_path} {local_path}"
        logger.info(f"Downloading: {cmd}")
        return os.system(cmd) == 0
    
    def list_directory(self, hdfs_path):
        """Listar conteúdo de diretório"""
        cmd = f"{self.hdfs_cmd} -ls {hdfs_path}"
        logger.info(f"Listing: {cmd}")
        os.system(cmd)
    
    def create_directory(self, hdfs_path):
        """Criar diretório no HDFS"""
        cmd = f"{self.hdfs_cmd} -mkdir -p {hdfs_path}"
        logger.info(f"Creating directory: {cmd}")
        return os.system(cmd) == 0
    
    def remove_path(self, hdfs_path):
        """Remover arquivo/diretório do HDFS"""
        cmd = f"{self.hdfs_cmd} -rm -r {hdfs_path}"
        logger.info(f"Removing: {cmd}")
        return os.system(cmd) == 0

class MapReduceWordCount:
    """Implementação do clássico Word Count em MapReduce"""
    
    def __init__(self):
        self.intermediate_data = defaultdict(list)
    
    def mapper(self, text_line):
        """
        Função Map: converte linha de texto em pares (palavra, 1)
        """
        # Limpar e dividir texto
        words = re.findall(r'\b\w+\b', text_line.lower())
        
        # Emitir par (palavra, 1) para cada palavra
        pairs = []
        for word in words:
            if len(word) > 2:  # Ignorar palavras muito pequenas
                pairs.append((word, 1))
        
        return pairs
    
    def shuffler(self, mapped_data):
        """
        Função Shuffle: agrupa pares por chave
        """
        shuffled = defaultdict(list)
        
        for pairs in mapped_data:
            for word, count in pairs:
                shuffled[word].append(count)
        
        return shuffled
    
    def reducer(self, word, counts):
        """
        Função Reduce: soma contagens para cada palavra
        """
        total_count = sum(counts)
        return (word, total_count)
    
    def run_mapreduce(self, text_file):
        """
        Executa job MapReduce completo
        """
        logger.info("Iniciando MapReduce Word Count")
        
        # Fase MAP
        mapped_results = []
        with open(text_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                mapped_pairs = self.mapper(line.strip())
                mapped_results.append(mapped_pairs)
                
                if line_num % 1000 == 0:
                    logger.info(f"Processadas {line_num} linhas")
        
        # Fase SHUFFLE
        shuffled_data = self.shuffler(mapped_results)
        logger.info(f"Shuffle concluído: {len(shuffled_data)} palavras únicas")
        
        # Fase REDUCE
        final_results = []
        for word, counts in shuffled_data.items():
            result = self.reducer(word, counts)
            final_results.append(result)
        
        # Ordenar por frequência
        final_results.sort(key=lambda x: x[1], reverse=True)
        
        logger.info(f"MapReduce concluído: {len(final_results)} resultados")
        return final_results

class LogAnalysisMapReduce:
    """MapReduce para análise de logs de servidor web"""
    
    def __init__(self):
        self.log_pattern = re.compile(
            r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"'
        )
    
    def parse_log_line(self, line):
        """Parse linha de log Apache/Nginx"""
        match = self.log_pattern.match(line.strip())
        if match:
            return {
                'ip': match.group(1),
                'timestamp': match.group(2),
                'request': match.group(3),
                'status_code': int(match.group(4)),
                'bytes': int(match.group(5)) if match.group(5) != '-' else 0,
                'referer': match.group(6),
                'user_agent': match.group(7)
            }
        return None
    
    def mapper_top_ips(self, log_line):
        """Mapper para encontrar IPs mais ativos"""
        log_entry = self.parse_log_line(log_line)
        if log_entry:
            return [(log_entry['ip'], 1)]
        return []
    
    def mapper_status_codes(self, log_line):
        """Mapper para análise de códigos de status"""
        log_entry = self.parse_log_line(log_line)
        if log_entry:
            return [(log_entry['status_code'], 1)]
        return []
    
    def mapper_traffic_by_hour(self, log_line):
        """Mapper para análise de tráfego por hora"""
        log_entry = self.parse_log_line(log_line)
        if log_entry:
            try:
                # Parse timestamp: 01/Jan/2024:10:30:45 +0000
                timestamp_str = log_entry['timestamp'].split(' ')[0]
                dt = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S')
                hour = dt.hour
                return [(hour, log_entry['bytes'])]
            except ValueError:
                pass
        return []
    
    def run_log_analysis(self, log_file):
        """Executa análise completa de logs"""
        logger.info("Iniciando análise de logs")
        
        # Contadores para diferentes análises
        ip_counts = defaultdict(int)
        status_counts = defaultdict(int)
        hourly_traffic = defaultdict(int)
        
        with open(log_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                # Análise de IPs
                ip_pairs = self.mapper_top_ips(line)
                for ip, count in ip_pairs:
                    ip_counts[ip] += count
                
                # Análise de status codes
                status_pairs = self.mapper_status_codes(line)
                for status, count in status_pairs:
                    status_counts[status] += count
                
                # Análise de tráfego por hora
                traffic_pairs = self.mapper_traffic_by_hour(line)
                for hour, bytes_transferred in traffic_pairs:
                    hourly_traffic[hour] += bytes_transferred
                
                if line_num % 10000 == 0:
                    logger.info(f"Processadas {line_num} linhas de log")
        
        # Preparar resultados
        results = {
            'top_ips': sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:10],
            'status_distribution': dict(status_counts),
            'hourly_traffic': dict(hourly_traffic)
        }
        
        return results

class HadoopJobManager:
    """Gerenciador para execução de jobs Hadoop"""
    
    def __init__(self):
        self.hdfs = HDFSManager()
    
    def submit_streaming_job(self, mapper_script, reducer_script, input_path, output_path):
        """Submit Hadoop Streaming job"""
        cmd = f"""
        hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
        -files {mapper_script},{reducer_script} \
        -mapper {mapper_script} \
        -reducer {reducer_script} \
        -input {input_path} \
        -output {output_path}
        """
        
        logger.info(f"Submitting Hadoop Streaming job")
        return os.system(cmd) == 0
    
    def monitor_job_status(self, job_id=None):
        """Monitorar status de jobs"""
        if job_id:
            cmd = f"yarn application -status {job_id}"
        else:
            cmd = "yarn application -list"
        
        logger.info("Checking job status")
        os.system(cmd)
    
    def kill_job(self, job_id):
        """Matar job em execução"""
        cmd = f"yarn application -kill {job_id}"
        logger.info(f"Killing job {job_id}")
        return os.system(cmd) == 0

def create_sample_data():
    """Criar dados de exemplo para testes"""
    # Criar arquivo de texto para Word Count
    sample_text = """
    Big Data is a field that treats ways to analyze, systematically extract information from, 
    or otherwise deal with data sets that are too large or complex to be dealt with by traditional 
    data-processing application software. Data with many cases offer greater statistical power, 
    while data with higher complexity may lead to a higher false discovery rate.
    
    Big Data challenges include capturing data, data storage, data analysis, search, sharing, 
    transfer, visualization, querying, updating, information privacy and data source.
    
    Hadoop is an open-source software framework used for distributed storage and processing 
    of Big Data using the MapReduce programming model.
    """ * 100  # Repetir para ter mais dados
    
    with open('sample_text.txt', 'w', encoding='utf-8') as f:
        f.write(sample_text)
    
    # Criar arquivo de logs simulados
    sample_logs = []
    ips = ['192.168.1.1', '10.0.0.5', '172.16.0.10', '203.0.113.1']
    status_codes = [200, 404, 500, 301, 302]
    
    for i in range(10000):
        ip = ips[i % len(ips)]
        status = status_codes[i % len(status_codes)]
        timestamp = f"01/Jan/2024:{10 + (i % 14):02d}:30:45 +0000"
        bytes_sent = 1000 + (i % 5000)
        
        log_line = f'{ip} - - [{timestamp}] "GET /page{i%100} HTTP/1.1" {status} {bytes_sent} "-" "Mozilla/5.0"'
        sample_logs.append(log_line)
    
    with open('sample_logs.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sample_logs))
    
    logger.info("Dados de exemplo criados: sample_text.txt, sample_logs.txt")

def main():
    """Função principal demonstrando uso das classes"""
    
    print("🚀 Hadoop MapReduce Examples")
    print("=" * 50)
    
    # Criar dados de exemplo
    create_sample_data()
    
    # Demonstrar Word Count
    print("\n📊 1. Word Count MapReduce")
    word_count = MapReduceWordCount()
    results = word_count.run_mapreduce('sample_text.txt')
    
    print("\nTop 10 palavras mais frequentes:")
    for word, count in results[:10]:
        print(f"{word}: {count}")
    
    # Salvar resultados
    with open('wordcount_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    # Demonstrar análise de logs
    print("\n📊 2. Log Analysis MapReduce")
    log_analyzer = LogAnalysisMapReduce()
    log_results = log_analyzer.run_log_analysis('sample_logs.txt')
    
    print("\nTop 5 IPs mais ativos:")
    for ip, count in log_results['top_ips'][:5]:
        print(f"{ip}: {count} requests")
    
    print("\nDistribuição de status codes:")
    for status, count in log_results['status_distribution'].items():
        print(f"HTTP {status}: {count}")
    
    print("\nTráfego por hora (bytes):")
    for hour in sorted(log_results['hourly_traffic'].keys()):
        traffic = log_results['hourly_traffic'][hour]
        print(f"{hour:02d}:00 - {traffic:,} bytes")
    
    # Salvar resultados de log
    with open('log_analysis_results.json', 'w') as f:
        json.dump(log_results, f, indent=2, default=str)
    
    # Demonstrar operações HDFS
    print("\n💾 3. HDFS Operations")
    hdfs = HDFSManager()
    
    # Criar diretório no HDFS
    hdfs.create_directory('/user/data/input')
    hdfs.create_directory('/user/data/output')
    
    print("\nOperações HDFS demonstradas (ver logs)")
    
    print("\n✅ Demonstração concluída!")
    print("Arquivos gerados:")
    print("- sample_text.txt: Dados de exemplo para Word Count")
    print("- sample_logs.txt: Logs simulados para análise")
    print("- wordcount_results.json: Resultados do Word Count")
    print("- log_analysis_results.json: Resultados da análise de logs")

if __name__ == "__main__":
    main()
