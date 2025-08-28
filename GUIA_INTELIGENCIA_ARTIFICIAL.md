# 🤖 Guia Completo: Inteligência Artificial com Big Data

*Como Patrick descobriu o poder da IA aplicada a grandes volumes de dados em Santa Catarina*

---

## 🧠 **Fundamentos de IA e Big Data**

### **O que é Inteligência Artificial?**
IA é a capacidade de máquinas executarem tarefas que tradicionalmente requerem inteligência humana:

- **Machine Learning**: Aprendizado através de dados
- **Deep Learning**: Redes neurais profundas
- **NLP**: Processamento de linguagem natural
- **Computer Vision**: Reconhecimento de imagens
- **Reinforcement Learning**: Aprendizado por recompensas

### **Por que IA + Big Data?**
```python
# Exemplo prático: Análise de sentimentos no turismo de SC
import pandas as pd
from textblob import TextBlob

# Comentários de turistas sobre Florianópolis
comentarios = [
    "Floripa é incrível! Praias lindas e vida noturna agitada",
    "Ponte Hercílio Luz é um cartão postal maravilhoso",
    "Trânsito muito ruim na temporada, mas vale a pena",
    "Lagoa da Conceição é mágica, lugar perfeito para relaxar"
]

# Análise automática de sentimentos
resultados = []
for comentario in comentarios:
    blob = TextBlob(comentario)
    sentimento = blob.sentiment.polarity  # -1 (negativo) a 1 (positivo)
    resultados.append({
        'comentario': comentario,
        'sentimento': 'Positivo' if sentimento > 0 else 'Negativo' if sentimento < 0 else 'Neutro',
        'polaridade': sentimento
    })

df_sentimentos = pd.DataFrame(resultados)
print(df_sentimentos)
```

---

## 🔬 **Machine Learning Aplicado aos Casos de SC**

### **Caso 1: Predição de Tráfego na Ponte Hercílio Luz**

```python
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Dados históricos da ponte (simulados baseados em padrões reais)
def gerar_dados_ponte():
    np.random.seed(42)
    
    # 1 ano de dados (8760 horas)
    horas = range(8760)
    dados = []
    
    for h in horas:
        # Padrões temporais
        hora_dia = h % 24
        dia_semana = (h // 24) % 7
        mes = (h // (24 * 30)) % 12
        
        # Padrão base por hora do dia
        if 6 <= hora_dia <= 9:  # Rush manhã
            base = 800 + np.random.normal(0, 100)
        elif 17 <= hora_dia <= 20:  # Rush tarde
            base = 900 + np.random.normal(0, 120)
        elif 22 <= hora_dia or hora_dia <= 5:  # Madrugada
            base = 50 + np.random.normal(0, 20)
        else:  # Outros horários
            base = 300 + np.random.normal(0, 80)
        
        # Ajuste por dia da semana
        if dia_semana in [5, 6]:  # Final de semana
            base *= 0.7 if hora_dia < 10 else 1.3
        
        # Ajuste sazonal (verão em SC)
        if mes in [11, 0, 1, 2]:  # Verão
            base *= 1.4
        
        # Clima (simulado)
        chuva = np.random.choice([0, 1], p=[0.7, 0.3])
        if chuva:
            base *= 0.6
        
        dados.append({
            'hora_dia': hora_dia,
            'dia_semana': dia_semana,
            'mes': mes,
            'chuva': chuva,
            'veiculos': max(0, int(base))
        })
    
    return pd.DataFrame(dados)

# Gerar e dividir dados
df_ponte = gerar_dados_ponte()

# Features e target
features = ['hora_dia', 'dia_semana', 'mes', 'chuva']
X = df_ponte[features]
y = df_ponte['veiculos']

# Divisão treino/teste (80/20)
split = int(0.8 * len(df_ponte))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Treinar modelo
modelo_ponte = RandomForestRegressor(n_estimators=100, random_state=42)
modelo_ponte.fit(X_train, y_train)

# Predições
y_pred = modelo_ponte.predict(X_test)

# Avaliação
mae = mean_absolute_error(y_test, y_pred)
print(f"Erro médio absoluto: {mae:.0f} veículos")

# Importância das features
importancias = pd.DataFrame({
    'feature': features,
    'importancia': modelo_ponte.feature_importances_
}).sort_values('importancia', ascending=False)

print("\nImportância dos fatores:")
for _, row in importancias.iterrows():
    print(f"{row['feature']}: {row['importancia']:.3f}")

# Visualização
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(y_test.values[:168], label='Real', alpha=0.7)  # 1 semana
plt.plot(y_pred[:168], label='Predito', alpha=0.7)
plt.title('Predição vs Realidade - Ponte Hercílio Luz')
plt.legend()

plt.subplot(1, 2, 2)
plt.bar(importancias['feature'], importancias['importancia'])
plt.title('Importância dos Fatores')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### **Caso 2: Classificação de Imóveis em Florianópolis**

```python
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder

# Dados de imóveis em Floripa (características + categoria de preço)
def gerar_dados_imoveis():
    np.random.seed(42)
    
    bairros = ['Centro', 'Lagoa da Conceição', 'Ingleses', 'Canasvieiras', 
               'Trindade', 'Córrego Grande', 'Campeche', 'Barra da Lagoa']
    
    dados = []
    for _ in range(1000):
        bairro = np.random.choice(bairros)
        
        # Características baseadas no bairro
        if bairro in ['Centro', 'Lagoa da Conceição']:
            area_base = np.random.normal(80, 20)
            preco_m2_base = np.random.normal(9000, 1500)
        elif bairro in ['Ingleses', 'Canasvieiras']:
            area_base = np.random.normal(70, 15)
            preco_m2_base = np.random.normal(6500, 1000)
        else:
            area_base = np.random.normal(90, 25)
            preco_m2_base = np.random.normal(5500, 800)
        
        area = max(30, area_base)
        quartos = min(4, max(1, int(area / 30)))
        banheiros = min(3, max(1, int(quartos * 0.8)))
        vagas = np.random.choice([0, 1, 2, 3], p=[0.1, 0.4, 0.4, 0.1])
        idade = np.random.exponential(8)  # Maioria dos imóveis é nova
        
        # Preço total
        preco_total = area * preco_m2_base * (1 - idade/100)  # Depreciação
        
        # Categoria de preço
        if preco_total < 400000:
            categoria = 'Econômico'
        elif preco_total < 800000:
            categoria = 'Médio'
        else:
            categoria = 'Alto padrão'
        
        dados.append({
            'bairro': bairro,
            'area': area,
            'quartos': quartos,
            'banheiros': banheiros,
            'vagas': vagas,
            'idade': idade,
            'categoria': categoria
        })
    
    return pd.DataFrame(dados)

# Gerar dados
df_imoveis = gerar_dados_imoveis()

# Preprocessamento
le_bairro = LabelEncoder()
df_imoveis['bairro_encoded'] = le_bairro.fit_transform(df_imoveis['bairro'])

# Features e target
features_imoveis = ['bairro_encoded', 'area', 'quartos', 'banheiros', 'vagas', 'idade']
X_imoveis = df_imoveis[features_imoveis]
y_imoveis = df_imoveis['categoria']

# Modelo de classificação
modelo_imoveis = GradientBoostingClassifier(n_estimators=100, random_state=42)

# Validação cruzada
scores = cross_val_score(modelo_imoveis, X_imoveis, y_imoveis, cv=5)
print(f"Acurácia média: {scores.mean():.3f} (+/- {scores.std() * 2:.3f})")

# Treinar modelo final
modelo_imoveis.fit(X_imoveis, y_imoveis)

# Função para predizer categoria de um imóvel
def predizer_categoria_imovel(bairro, area, quartos, banheiros, vagas, idade):
    bairro_encoded = le_bairro.transform([bairro])[0]
    features = [[bairro_encoded, area, quartos, banheiros, vagas, idade]]
    categoria = modelo_imoveis.predict(features)[0]
    probabilidades = modelo_imoveis.predict_proba(features)[0]
    
    return categoria, probabilidades

# Exemplo de uso
categoria, probs = predizer_categoria_imovel('Lagoa da Conceição', 100, 2, 2, 1, 5)
print(f"\nImóvel na Lagoa da Conceição (100m², 2/2, 1 vaga, 5 anos):")
print(f"Categoria predita: {categoria}")
print(f"Probabilidades: {dict(zip(modelo_imoveis.classes_, probs))}")
```

---

## 🧠 **Deep Learning para Dados de SC**

### **Caso 3: Predição de Ocupação Hoteleira com Redes Neurais**

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Dados de ocupação hoteleira em Floripa
def gerar_dados_ocupacao():
    np.random.seed(42)
    
    # 3 anos de dados diários
    dias = 365 * 3
    dados = []
    
    for d in range(dias):
        # Sazonalidade anual
        mes = (d // 30) % 12
        if mes in [10, 11, 0, 1, 2]:  # Alta temporada
            ocupacao_base = 0.85
        elif mes in [5, 6, 7]:  # Baixa temporada  
            ocupacao_base = 0.45
        else:  # Média temporada
            ocupacao_base = 0.65
        
        # Sazonalidade semanal
        dia_semana = d % 7
        if dia_semana in [4, 5, 6]:  # Sexta, sábado, domingo
            ocupacao_base *= 1.2
        elif dia_semana in [0, 1]:  # Segunda, terça
            ocupacao_base *= 0.8
        
        # Eventos especiais (simplificado)
        if d % 365 in [1, 100, 200, 300]:  # 4 eventos por ano
            ocupacao_base *= 1.5
        
        # Ruído
        ocupacao = min(1.0, max(0.1, ocupacao_base + np.random.normal(0, 0.1)))
        
        dados.append({
            'dia': d,
            'ocupacao': ocupacao,
            'mes': mes,
            'dia_semana': dia_semana
        })
    
    return pd.DataFrame(dados)

# Gerar dados
df_ocupacao = gerar_dados_ocupacao()

# Preparar dados para LSTM
def preparar_dados_lstm(dados, look_back=30):
    """Preparar dados em sequências para LSTM"""
    scaler = MinMaxScaler()
    dados_scaled = scaler.fit_transform(dados[['ocupacao']].values)
    
    X, y = [], []
    for i in range(look_back, len(dados_scaled)):
        X.append(dados_scaled[i-look_back:i, 0])
        y.append(dados_scaled[i, 0])
    
    return np.array(X), np.array(y), scaler

# Preparar dados
look_back = 30  # Usar 30 dias anteriores para predizer o próximo
X, y, scaler = preparar_dados_lstm(df_ocupacao, look_back)

# Reshape para LSTM [amostras, timesteps, features]
X = X.reshape((X.shape[0], X.shape[1], 1))

# Dividir em treino/teste
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Criar modelo LSTM
modelo_lstm = Sequential([
    LSTM(50, return_sequences=True, input_shape=(look_back, 1)),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(25),
    Dense(1)
])

# Compilar modelo
modelo_lstm.compile(optimizer='adam', loss='mean_squared_error')

# Treinar
print("Treinando modelo LSTM...")
historia = modelo_lstm.fit(
    X_train, y_train,
    batch_size=32,
    epochs=50,
    validation_data=(X_test, y_test),
    verbose=0
)

# Predições
y_pred_scaled = modelo_lstm.predict(X_test)

# Desnormalizar
y_test_original = scaler.inverse_transform(y_test.reshape(-1, 1))
y_pred_original = scaler.inverse_transform(y_pred_scaled)

# Avaliar modelo
mse = tf.keras.metrics.mean_squared_error(y_test_original, y_pred_original)
rmse = np.sqrt(mse)
print(f"RMSE: {rmse:.3f}")

# Visualizar resultados
plt.figure(figsize=(15, 10))

# 1. Histórico de treinamento
plt.subplot(2, 2, 1)
plt.plot(historia.history['loss'], label='Treino')
plt.plot(historia.history['val_loss'], label='Validação')
plt.title('Histórico de Treinamento')
plt.legend()

# 2. Predições vs Real
plt.subplot(2, 2, 2)
plt.plot(y_test_original[:100], label='Real', alpha=0.7)
plt.plot(y_pred_original[:100], label='Predito', alpha=0.7)
plt.title('Predições vs Realidade (100 dias)')
plt.legend()

# 3. Dados originais
plt.subplot(2, 2, 3)
plt.plot(df_ocupacao['ocupacao'])
plt.title('Ocupação Hoteleira - Série Temporal Completa')
plt.ylabel('Taxa de Ocupação')

# 4. Distribuição de erros
plt.subplot(2, 2, 4)
erros = y_test_original.flatten() - y_pred_original.flatten()
plt.hist(erros, bins=30, alpha=0.7)
plt.title('Distribuição dos Erros')
plt.xlabel('Erro')

plt.tight_layout()
plt.show()

# Função para predizer próximos dias
def predizer_ocupacao(modelo, ultimos_dados, scaler, dias_futuros=7):
    """Predizer ocupação para próximos dias"""
    # Normalizar últimos dados
    dados_scaled = scaler.transform(ultimos_dados.reshape(-1, 1))
    
    predicoes = []
    entrada = dados_scaled[-look_back:].reshape(1, look_back, 1)
    
    for _ in range(dias_futuros):
        pred = modelo.predict(entrada, verbose=0)
        predicoes.append(pred[0, 0])
        
        # Atualizar entrada para próxima predição
        entrada = np.append(entrada[:, 1:, :], pred.reshape(1, 1, 1), axis=1)
    
    # Desnormalizar predições
    predicoes = scaler.inverse_transform(np.array(predicoes).reshape(-1, 1))
    return predicoes.flatten()

# Exemplo de uso
ultimos_30_dias = df_ocupacao['ocupacao'].values[-30:]
predicoes_futuras = predizer_ocupacao(modelo_lstm, ultimos_30_dias, scaler, 14)

print(f"\nPredições para próximos 14 dias:")
for i, pred in enumerate(predicoes_futuras, 1):
    print(f"Dia +{i}: {pred:.1%} de ocupação")
```

---

## 🔍 **Processamento de Linguagem Natural (NLP)**

### **Caso 4: Análise de Comentários sobre Turismo em SC**

```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from wordcloud import WordCloud
import re
from collections import Counter

# Download de recursos necessários (executar uma vez)
# nltk.download('vader_lexicon')
# nltk.download('punkt')

def analisar_comentarios_turismo():
    """Análise completa de comentários sobre turismo em SC"""
    
    # Comentários simulados (em um projeto real, viriam de APIs, redes sociais, etc.)
    comentarios = [
        "Florianópolis é simplesmente maravilhosa! As praias são lindas e a cidade tem uma energia incrível",
        "Visitei a Ponte Hercílio Luz durante o pôr do sol, que experiência emocionante!",
        "O trânsito em Floripa é um caos na alta temporada, muito estressante",
        "Lagoa da Conceição é mágica, perfeita para relaxar e curtir a natureza",
        "Os preços dos restaurantes estão muito altos, dificulta o turismo",
        "Praia de Jurerê Internacional é top, mas muito elitizada",
        "Mercado Público de Florianópolis tem uma variedade incrível de produtos locais",
        "Ilha da Magia faz jus ao nome, lugar encantador demais!",
        "Barra da Lagoa tem um astral único, adorei a vibe local",
        "Centro histórico bem preservado, cultura e história de Santa Catarina",
        "Campeche beach é perfeita para surfar, ondas consistentes",
        "Ingleses do Rio Vermelho, praia família, excelente infraestrutura",
        "Canasvieiras à noite é muito agitada, vida noturna animada",
        "Trilha da Lagoinha do Leste é desafiadora mas vale cada passo",
        "Santo Antônio de Lisboa, charmoso vilarejo de pescadores"
    ]
    
    # Preparar analisador de sentimentos
    sia = SentimentIntensityAnalyzer()
    
    # Análise completa
    resultados = []
    todas_palavras = []
    
    for i, comentario in enumerate(comentarios):
        # Limpeza do texto
        texto_limpo = re.sub(r'[^\w\s]', '', comentario.lower())
        palavras = texto_limpo.split()
        todas_palavras.extend(palavras)
        
        # Análise de sentimento com VADER
        scores_vader = sia.polarity_scores(comentario)
        
        # Análise com TextBlob
        blob = TextBlob(comentario)
        sentimento_textblob = blob.sentiment.polarity
        
        # Extrair locais mencionados (simplificado)
        locais_sc = ['florianópolis', 'floripa', 'ponte', 'lagoa', 'jurerê', 'barra', 
                     'mercado', 'centro', 'campeche', 'ingleses', 'canasvieiras', 
                     'lagoinha', 'santo antônio']
        
        locais_encontrados = [local for local in locais_sc if local in texto_limpo]
        
        resultados.append({
            'comentario': comentario,
            'sentimento_vader': scores_vader['compound'],
            'sentimento_textblob': sentimento_textblob,
            'classificacao': 'Positivo' if scores_vader['compound'] > 0.05 else 
                           'Negativo' if scores_vader['compound'] < -0.05 else 'Neutro',
            'locais_mencionados': locais_encontrados,
            'palavras_count': len(palavras)
        })
    
    # Converter para DataFrame
    df_analise = pd.DataFrame(resultados)
    
    # Estatísticas gerais
    print("📊 ANÁLISE DE SENTIMENTOS - TURISMO SC")
    print("=" * 50)
    print(f"Total de comentários analisados: {len(comentarios)}")
    print(f"Sentimentos:")
    print(df_analise['classificacao'].value_counts())
    print(f"\nSentimento médio (VADER): {df_analise['sentimento_vader'].mean():.3f}")
    print(f"Sentimento médio (TextBlob): {df_analise['sentimento_textblob'].mean():.3f}")
    
    # Palavras mais frequentes
    palavras_comuns = Counter(todas_palavras).most_common(10)
    print(f"\n🔤 Palavras mais mencionadas:")
    for palavra, freq in palavras_comuns:
        if len(palavra) > 3:  # Filtrar palavras muito pequenas
            print(f"{palavra}: {freq} vezes")
    
    # Locais mais mencionados
    todos_locais = []
    for locais in df_analise['locais_mencionados']:
        todos_locais.extend(locais)
    
    if todos_locais:
        locais_comuns = Counter(todos_locais).most_common(5)
        print(f"\n📍 Locais mais mencionados:")
        for local, freq in locais_comuns:
            print(f"{local.title()}: {freq} vezes")
    
    # Comentários mais positivos e negativos
    mais_positivo = df_analise.loc[df_analise['sentimento_vader'].idxmax()]
    mais_negativo = df_analise.loc[df_analise['sentimento_vader'].idxmin()]
    
    print(f"\n😊 Comentário mais positivo (score: {mais_positivo['sentimento_vader']:.3f}):")
    print(f"'{mais_positivo['comentario']}'")
    
    print(f"\n😞 Comentário mais negativo (score: {mais_negativo['sentimento_vader']:.3f}):")
    print(f"'{mais_negativo['comentario']}'")
    
    # Visualização
    plt.figure(figsize=(15, 10))
    
    # 1. Distribuição de sentimentos
    plt.subplot(2, 3, 1)
    df_analise['classificacao'].value_counts().plot(kind='bar')
    plt.title('Distribuição de Sentimentos')
    plt.xticks(rotation=45)
    
    # 2. Sentimentos por método
    plt.subplot(2, 3, 2)
    plt.scatter(df_analise['sentimento_vader'], df_analise['sentimento_textblob'], alpha=0.7)
    plt.xlabel('VADER')
    plt.ylabel('TextBlob')
    plt.title('Comparação de Métodos')
    
    # 3. Palavras mais comuns
    plt.subplot(2, 3, 3)
    palavras_filtradas = [(p, f) for p, f in palavras_comuns if len(p) > 3][:8]
    if palavras_filtradas:
        palavras, freqs = zip(*palavras_filtradas)
        plt.bar(palavras, freqs)
        plt.title('Palavras Mais Frequentes')
        plt.xticks(rotation=45)
    
    # 4. Locais mencionados
    plt.subplot(2, 3, 4)
    if todos_locais:
        locais_df = pd.Series(todos_locais).value_counts()[:8]
        locais_df.plot(kind='bar')
        plt.title('Locais Mais Mencionados')
        plt.xticks(rotation=45)
    
    # 5. Distribuição de scores
    plt.subplot(2, 3, 5)
    plt.hist(df_analise['sentimento_vader'], bins=20, alpha=0.7, label='VADER')
    plt.hist(df_analise['sentimento_textblob'], bins=20, alpha=0.7, label='TextBlob')
    plt.title('Distribuição de Scores')
    plt.legend()
    
    # 6. Tamanho dos comentários vs sentimento
    plt.subplot(2, 3, 6)
    plt.scatter(df_analise['palavras_count'], df_analise['sentimento_vader'], alpha=0.7)
    plt.xlabel('Número de Palavras')
    plt.ylabel('Sentimento')
    plt.title('Tamanho vs Sentimento')
    
    plt.tight_layout()
    plt.show()
    
    return df_analise

# Executar análise
df_sentimentos = analisar_comentarios_turismo()

# Função para analisar novos comentários
def analisar_novo_comentario(comentario):
    """Analisar sentimento de um novo comentário"""
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(comentario)
    blob = TextBlob(comentario)
    
    print(f"Comentário: '{comentario}'")
    print(f"Sentimento VADER: {scores['compound']:.3f}")
    print(f"Sentimento TextBlob: {blob.sentiment.polarity:.3f}")
    print(f"Classificação: {'Positivo' if scores['compound'] > 0.05 else 'Negativo' if scores['compound'] < -0.05 else 'Neutro'}")

# Exemplo de uso
analisar_novo_comentario("Adorei minha viagem para Florianópolis, cidade incrível!")
```

---

## 🚀 **IA Aplicada ao Planejamento Urbano**

### **Caso 5: Otimização de Rotas com Algoritmos Genéticos**

```python
import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations
import random

class OtimizadorRotas:
    """Otimizador de rotas para problemas urbanos usando Algoritmos Genéticos"""
    
    def __init__(self, pontos, nomes_pontos=None):
        self.pontos = np.array(pontos)
        self.n_pontos = len(pontos)
        self.nomes_pontos = nomes_pontos or [f"Ponto {i}" for i in range(self.n_pontos)]
        self.matriz_distancias = self._calcular_matriz_distancias()
    
    def _calcular_matriz_distancias(self):
        """Calcular matriz de distâncias entre todos os pontos"""
        matriz = np.zeros((self.n_pontos, self.n_pontos))
        for i in range(self.n_pontos):
            for j in range(self.n_pontos):
                if i != j:
                    matriz[i, j] = np.sqrt(
                        (self.pontos[i, 0] - self.pontos[j, 0])**2 + 
                        (self.pontos[i, 1] - self.pontos[j, 1])**2
                    )
        return matriz
    
    def calcular_distancia_rota(self, rota):
        """Calcular distância total de uma rota"""
        distancia = 0
        for i in range(len(rota) - 1):
            distancia += self.matriz_distancias[rota[i], rota[i + 1]]
        # Voltar ao ponto inicial
        distancia += self.matriz_distancias[rota[-1], rota[0]]
        return distancia
    
    def gerar_populacao_inicial(self, tamanho_populacao):
        """Gerar população inicial de rotas"""
        populacao = []
        for _ in range(tamanho_populacao):
            rota = list(range(self.n_pontos))
            random.shuffle(rota)
            populacao.append(rota)
        return populacao
    
    def selecao_torneio(self, populacao, fitness, tamanho_torneio=3):
        """Seleção por torneio"""
        selecionados = []
        for _ in range(len(populacao)):
            torneio = random.sample(range(len(populacao)), tamanho_torneio)
            vencedor = min(torneio, key=lambda x: fitness[x])
            selecionados.append(populacao[vencedor][:])
        return selecionados
    
    def crossover_ordenado(self, pai1, pai2):
        """Crossover ordenado (OX)"""
        size = len(pai1)
        start, end = sorted(random.sample(range(size), 2))
        
        filho1 = [-1] * size
        filho1[start:end] = pai1[start:end]
        
        pointer = end
        for city in pai2[end:] + pai2[:end]:
            if city not in filho1:
                filho1[pointer % size] = city
                pointer += 1
        
        return filho1
    
    def mutacao_swap(self, rota, taxa_mutacao=0.02):
        """Mutação por troca de posições"""
        if random.random() < taxa_mutacao:
            i, j = random.sample(range(len(rota)), 2)
            rota[i], rota[j] = rota[j], rota[i]
        return rota
    
    def algoritmo_genetico(self, tamanho_populacao=100, geracoes=500, 
                          taxa_mutacao=0.02, elitismo=0.1):
        """Algoritmo genético principal"""
        
        # População inicial
        populacao = self.gerar_populacao_inicial(tamanho_populacao)
        melhor_historico = []
        media_historico = []
        
        num_elite = int(elitismo * tamanho_populacao)
        
        for geracao in range(geracoes):
            # Calcular fitness (distância - quanto menor, melhor)
            fitness = [self.calcular_distancia_rota(rota) for rota in populacao]
            
            # Estatísticas
            melhor_fitness = min(fitness)
            media_fitness = np.mean(fitness)
            melhor_historico.append(melhor_fitness)
            media_historico.append(media_fitness)
            
            if geracao % 50 == 0:
                print(f"Geração {geracao}: Melhor = {melhor_fitness:.2f}, Média = {media_fitness:.2f}")
            
            # Elitismo - manter os melhores
            indices_ordenados = sorted(range(len(fitness)), key=lambda x: fitness[x])
            nova_populacao = [populacao[i][:] for i in indices_ordenados[:num_elite]]
            
            # Seleção e reprodução
            selecionados = self.selecao_torneio(populacao, fitness)
            
            while len(nova_populacao) < tamanho_populacao:
                pai1, pai2 = random.sample(selecionados, 2)
                filho = self.crossover_ordenado(pai1, pai2)
                filho = self.mutacao_swap(filho, taxa_mutacao)
                nova_populacao.append(filho)
            
            populacao = nova_populacao
        
        # Melhor solução final
        fitness_final = [self.calcular_distancia_rota(rota) for rota in populacao]
        melhor_indice = fitness_final.index(min(fitness_final))
        melhor_rota = populacao[melhor_indice]
        
        return melhor_rota, melhor_historico, media_historico
    
    def plotar_rota(self, rota, titulo="Rota Otimizada"):
        """Plotar rota no mapa"""
        plt.figure(figsize=(10, 8))
        
        # Plotar pontos
        for i, (x, y) in enumerate(self.pontos):
            plt.scatter(x, y, s=200, c='red' if i == 0 else 'blue', 
                       alpha=0.7, edgecolors='black')
            plt.annotate(self.nomes_pontos[i], (x, y), xytext=(5, 5), 
                        textcoords='offset points', fontsize=8)
        
        # Plotar rota
        rota_completa = rota + [rota[0]]  # Voltar ao início
        for i in range(len(rota_completa) - 1):
            p1 = self.pontos[rota_completa[i]]
            p2 = self.pontos[rota_completa[i + 1]]
            plt.arrow(p1[0], p1[1], p2[0] - p1[0], p2[1] - p1[1], 
                     head_width=0.5, head_length=0.3, fc='green', ec='green', alpha=0.7)
        
        plt.title(f"{titulo}\nDistância total: {self.calcular_distancia_rota(rota):.2f}")
        plt.grid(True, alpha=0.3)
        plt.axis('equal')
        plt.show()

# Exemplo: Otimização de rota de coleta de lixo em Florianópolis
pontos_floripa = [
    (0, 0),    # Centro (base)
    (3, 4),    # Trindade
    (6, 2),    # Córrego Grande
    (8, 7),    # Lagoa da Conceição
    (5, 9),    # Ingleses
    (2, 8),    # Canasvieiras
    (9, 4),    # Barra da Lagoa
    (4, 1),    # Campeche
    (7, 6)     # Jurerê
]

nomes_bairros = [
    "Centro", "Trindade", "Córrego Grande", "Lagoa da Conceição",
    "Ingleses", "Canasvieiras", "Barra da Lagoa", "Campeche", "Jurerê"
]

# Criar otimizador
otimizador = OtimizadorRotas(pontos_floripa, nomes_bairros)

print("🚛 OTIMIZAÇÃO DE ROTA DE COLETA - FLORIANÓPOLIS")
print("=" * 50)

# Solução força bruta para comparação (apenas para problemas pequenos)
if len(pontos_floripa) <= 8:
    print("Calculando solução ótima (força bruta)...")
    melhor_distancia_fb = float('inf')
    melhor_rota_fb = None
    
    for rota in permutations(range(1, len(pontos_floripa))):  # Fixar centro como início
        rota_completa = [0] + list(rota)
        distancia = otimizador.calcular_distancia_rota(rota_completa)
        if distancia < melhor_distancia_fb:
            melhor_distancia_fb = distancia
            melhor_rota_fb = rota_completa
    
    print(f"Solução ótima encontrada: {melhor_distancia_fb:.2f}")

# Algoritmo genético
print("\nExecutando algoritmo genético...")
melhor_rota_ag, historico_melhor, historico_media = otimizador.algoritmo_genetico(
    tamanho_populacao=100, 
    geracoes=300,
    taxa_mutacao=0.02
)

print(f"\nMelhor rota encontrada (AG): {otimizador.calcular_distancia_rota(melhor_rota_ag):.2f}")
print(f"Sequência de bairros:")
for i, ponto in enumerate(melhor_rota_ag):
    print(f"{i+1}. {nomes_bairros[ponto]}")

# Visualizações
plt.figure(figsize=(15, 5))

# 1. Evolução do algoritmo
plt.subplot(1, 3, 1)
plt.plot(historico_melhor, label='Melhor')
plt.plot(historico_media, label='Média', alpha=0.7)
plt.title('Evolução do Algoritmo Genético')
plt.xlabel('Geração')
plt.ylabel('Distância')
plt.legend()
plt.grid(True, alpha=0.3)

# 2. Comparação de soluções
plt.subplot(1, 3, 2)
if 'melhor_distancia_fb' in locals():
    solucoes = ['Força Bruta\n(Ótima)', 'Algoritmo\nGenético']
    distancias = [melhor_distancia_fb, otimizador.calcular_distancia_rota(melhor_rota_ag)]
    cores = ['green', 'orange']
    
    bars = plt.bar(solucoes, distancias, color=cores, alpha=0.7)
    plt.title('Comparação de Soluções')
    plt.ylabel('Distância Total')
    
    # Adicionar valores nas barras
    for bar, dist in zip(bars, distancias):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                f'{dist:.2f}', ha='center', va='bottom')

# 3. Mapa da rota
plt.subplot(1, 3, 3)
otimizador.plotar_rota(melhor_rota_ag, "Rota Otimizada - Florianópolis")

plt.tight_layout()
plt.show()

# Função para analisar impacto de mudanças
def analisar_impacto_novo_ponto(otimizador, novo_ponto, nome_ponto):
    """Analisar impacto de adicionar um novo ponto na rota"""
    print(f"\n🔍 Analisando impacto de adicionar: {nome_ponto}")
    
    # Criar novo otimizador com ponto adicional
    novos_pontos = np.vstack([otimizador.pontos, novo_ponto])
    novos_nomes = otimizador.nomes_pontos + [nome_ponto]
    novo_otimizador = OtimizadorRotas(novos_pontos, novos_nomes)
    
    # Otimizar nova rota
    nova_rota, _, _ = novo_otimizador.algoritmo_genetico(
        tamanho_populacao=50, geracoes=100
    )
    
    distancia_original = otimizador.calcular_distancia_rota(melhor_rota_ag)
    nova_distancia = novo_otimizador.calcular_distancia_rota(nova_rota)
    
    print(f"Distância original: {distancia_original:.2f}")
    print(f"Nova distância: {nova_distancia:.2f}")
    print(f"Impacto: +{nova_distancia - distancia_original:.2f} ({((nova_distancia/distancia_original - 1)*100):.1f}%)")

# Exemplo: Impacto de adicionar Santo Antônio de Lisboa
analisar_impacto_novo_ponto(otimizador, (1, 6), "Santo Antônio")
```

---

## 📚 **Próximos Passos em IA + Big Data**

### **1. Tópicos Avançados para Explorar**

- **Reinforcement Learning**: Otimização de semáforos em tempo real
- **Computer Vision**: Análise de imagens de satélite para planejamento urbano
- **AutoML**: Automatização da criação de modelos
- **Federated Learning**: ML distribuído preservando privacidade
- **Explainable AI**: Interpretabilidade de modelos complexos

### **2. Ferramentas e Frameworks**

```python
# MLOps e produção
import mlflow        # Tracking de experimentos
import dvc          # Versionamento de dados
import prefect      # Orquestração de pipelines

# AutoML
import auto-sklearn  # AutoML para classificação/regressão
import h2o          # Platform de ML automático

# Deep Learning avançado
import pytorch_lightning  # Framework para PyTorch
import transformers      # Modelos de linguagem (BERT, GPT)
```

### **3. Projetos Práticos Sugeridos**

1. **Sistema de Recomendação Turística**
   - Recomendar pontos turísticos baseado no perfil do visitante
   - Usar collaborative filtering e content-based filtering

2. **Detecção de Anomalias no Trânsito**
   - Identificar padrões anômalos de tráfego usando autoencoders
   - Alertas automáticos para gestores de trânsito

3. **Chatbot para Turismo em SC**
   - Processamento de linguagem natural para responder dúvidas
   - Integração com dados reais de turismo

4. **Previsão de Demanda Energética**
   - Usar dados meteorológicos e históricos para prever consumo
   - Otimização da geração de energia renovável

### **4. Recursos para Continuar Aprendendo**

- **Cursos Online**: Coursera Deep Learning, Fast.ai, Udacity AI Nanodegree
- **Papers**: arXiv.org, Papers With Code
- **Competições**: Kaggle, DrivenData
- **Comunidades**: Stack Overflow, Reddit r/MachineLearning

**Com estes fundamentos e exemplos práticos, você está pronto para aplicar IA em projetos reais de Big Data! 🚀**
