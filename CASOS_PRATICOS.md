# 🎯 Casos Práticos: Aplicações Reais de Big Data em SC

*Exemplos prontos para executar e adaptar para sua realidade*

---

## 📊 **Caso 1: Dashboard de Monitoramento Urbano**

### **Objetivo**: Criar dashboard interativo para monitorar indicadores urbanos de Florianópolis

```python
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configurar página do Streamlit
st.set_page_config(
    page_title="Monitor Urbano - Florianópolis",
    page_icon="🏙️",
    layout="wide"
)

@st.cache_data
def gerar_dados_urbanos():
    """Gerar dados simulados de monitoramento urbano"""
    np.random.seed(42)
    
    # Últimos 30 dias
    datas = pd.date_range(
        start=datetime.now() - timedelta(days=30),
        end=datetime.now(),
        freq='H'
    )
    
    dados = []
    for i, data in enumerate(datas):
        hora = data.hour
        dia_semana = data.weekday()
        
        # Tráfego na Ponte Hercílio Luz
        if 6 <= hora <= 9 or 17 <= hora <= 20:  # Rush hours
            trafego_base = 800
        elif 22 <= hora or hora <= 5:  # Madrugada
            trafego_base = 100
        else:
            trafego_base = 400
            
        if dia_semana >= 5:  # Fim de semana
            trafego_base *= 0.7
            
        trafego = max(0, trafego_base + np.random.normal(0, 100))
        
        # Qualidade do ar (PM2.5)
        pm25_base = 25 + (trafego / 100) * 0.5  # Correlação com tráfego
        pm25 = max(0, pm25_base + np.random.normal(0, 5))
        
        # Temperatura
        temp_base = 22 + 8 * np.sin((hora - 6) * 2 * np.pi / 24)
        temperatura = temp_base + np.random.normal(0, 2)
        
        # Ocupação hoteleira
        if dia_semana >= 5:  # Fim de semana
            ocupacao_base = 75
        else:
            ocupacao_base = 55
        ocupacao = min(100, max(0, ocupacao_base + np.random.normal(0, 15)))
        
        # Consumo energético
        consumo_base = 150 + 50 * np.sin((hora - 12) * 2 * np.pi / 24)
        if temperatura > 25:  # Ar condicionado
            consumo_base *= 1.3
        consumo = max(0, consumo_base + np.random.normal(0, 20))
        
        dados.append({
            'datetime': data,
            'trafego_ponte': int(trafego),
            'pm25': round(pm25, 1),
            'temperatura': round(temperatura, 1),
            'ocupacao_hoteis': round(ocupacao, 1),
            'consumo_energia': round(consumo, 1)
        })
    
    return pd.DataFrame(dados)

def main():
    st.title("🏙️ Monitor Urbano - Florianópolis")
    st.markdown("*Dashboard em tempo real dos indicadores urbanos da Ilha da Magia*")
    
    # Carregar dados
    df = gerar_dados_urbanos()
    
    # Métricas em tempo real (última hora)
    st.header("📊 Indicadores Atuais")
    ultimo_registro = df.iloc[-1]
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            "🚗 Tráfego Ponte",
            f"{ultimo_registro['trafego_ponte']:,} veículos/h",
            delta=f"{ultimo_registro['trafego_ponte'] - df.iloc[-2]['trafego_ponte']:+.0f}"
        )
    
    with col2:
        pm25_atual = ultimo_registro['pm25']
        cor_pm25 = "🟢" if pm25_atual <= 25 else "🟡" if pm25_atual <= 50 else "🔴"
        st.metric(
            f"{cor_pm25} Qualidade do Ar",
            f"{pm25_atual} μg/m³",
            delta=f"{pm25_atual - df.iloc[-2]['pm25']:+.1f}"
        )
    
    with col3:
        st.metric(
            "🌡️ Temperatura",
            f"{ultimo_registro['temperatura']:.1f}°C",
            delta=f"{ultimo_registro['temperatura'] - df.iloc[-2]['temperatura']:+.1f}"
        )
    
    with col4:
        st.metric(
            "🏨 Ocupação Hotéis",
            f"{ultimo_registro['ocupacao_hoteis']:.1f}%",
            delta=f"{ultimo_registro['ocupacao_hoteis'] - df.iloc[-2]['ocupacao_hoteis']:+.1f}"
        )
    
    with col5:
        st.metric(
            "⚡ Consumo Energia",
            f"{ultimo_registro['consumo_energia']:.0f} MW",
            delta=f"{ultimo_registro['consumo_energia'] - df.iloc[-2]['consumo_energia']:+.0f}"
        )
    
    # Gráficos temporais
    st.header("📈 Tendências (Últimos 7 dias)")
    
    # Filtrar últimos 7 dias
    df_7d = df[df['datetime'] >= df['datetime'].max() - timedelta(days=7)]
    
    # Tráfego e Qualidade do Ar
    col1, col2 = st.columns(2)
    
    with col1:
        fig_trafego = px.line(
            df_7d, x='datetime', y='trafego_ponte',
            title='🚗 Tráfego na Ponte Hercílio Luz',
            labels={'trafego_ponte': 'Veículos/hora', 'datetime': 'Data/Hora'}
        )
        fig_trafego.update_layout(height=400)
        st.plotly_chart(fig_trafego, use_container_width=True)
    
    with col2:
        # Colorir pontos baseado na qualidade do ar
        df_7d['qualidade'] = df_7d['pm25'].apply(
            lambda x: 'Boa' if x <= 25 else 'Moderada' if x <= 50 else 'Ruim'
        )
        
        fig_pm25 = px.scatter(
            df_7d, x='datetime', y='pm25', color='qualidade',
            title='🌬️ Qualidade do Ar (PM2.5)',
            labels={'pm25': 'PM2.5 (μg/m³)', 'datetime': 'Data/Hora'},
            color_discrete_map={'Boa': 'green', 'Moderada': 'orange', 'Ruim': 'red'}
        )
        fig_pm25.add_hline(y=25, line_dash="dash", line_color="orange", annotation_text="Limite Recomendado")
        fig_pm25.update_layout(height=400)
        st.plotly_chart(fig_pm25, use_container_width=True)
    
    # Correlações
    st.header("🔗 Análise de Correlações")
    
    # Calcular correlações
    correlacoes = df[['trafego_ponte', 'pm25', 'temperatura', 'ocupacao_hoteis', 'consumo_energia']].corr()
    
    fig_corr = px.imshow(
        correlacoes,
        title='Matriz de Correlações dos Indicadores Urbanos',
        color_continuous_scale='RdBu',
        aspect="auto"
    )
    fig_corr.update_layout(height=500)
    st.plotly_chart(fig_corr, use_container_width=True)
    
    # Insights automáticos
    st.header("💡 Insights Automáticos")
    
    # Calcular algumas estatísticas
    media_trafego = df['trafego_ponte'].mean()
    trafego_atual = ultimo_registro['trafego_ponte']
    
    media_pm25 = df['pm25'].mean()
    pm25_atual = ultimo_registro['pm25']
    
    ocupacao_atual = ultimo_registro['ocupacao_hoteis']
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"""
        **🚦 Situação do Tráfego**
        
        • Tráfego atual: {'Acima da média' if trafego_atual > media_trafego else 'Abaixo da média'}
        • Diferença: {((trafego_atual/media_trafego - 1) * 100):+.1f}%
        • Recomendação: {'Considere rotas alternativas' if trafego_atual > media_trafego * 1.2 else 'Fluxo normal'}
        """)
        
        st.info(f"""
        **🏨 Turismo**
        
        • Ocupação atual: {ocupacao_atual:.1f}%
        • Status: {'Alta demanda' if ocupacao_atual > 70 else 'Demanda moderada' if ocupacao_atual > 50 else 'Baixa demanda'}
        • Tendência: {'Temporada alta' if ocupacao_atual > 60 else 'Temporada baixa'}
        """)
    
    with col2:
        st.info(f"""
        **🌬️ Qualidade do Ar**
        
        • PM2.5 atual: {pm25_atual} μg/m³
        • Classificação: {'Boa' if pm25_atual <= 25 else 'Moderada' if pm25_atual <= 50 else 'Ruim'}
        • Tendência: {'Melhorando' if pm25_atual < media_pm25 else 'Piorando'}
        """)
        
        # Correlação tráfego x PM2.5
        corr_trafego_pm25 = df['trafego_ponte'].corr(df['pm25'])
        st.info(f"""
        **🔬 Correlação Tráfego x Poluição**
        
        • Correlação: {corr_trafego_pm25:.3f}
        • Interpretação: {'Forte correlação positiva' if corr_trafego_pm25 > 0.7 else 'Correlação moderada' if corr_trafego_pm25 > 0.3 else 'Correlação fraca'}
        • Impacto: Cada 100 veículos/h pode aumentar PM2.5 em ~{(corr_trafego_pm25 * 2):.1f} μg/m³
        """)
    
    # Download dos dados
    st.header("📥 Download dos Dados")
    
    csv = df.to_csv(index=False)
    st.download_button(
        label="💾 Baixar dados completos (CSV)",
        data=csv,
        file_name=f"monitor_urbano_floripa_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

if __name__ == "__main__":
    main()
```

### **Como executar o dashboard:**
```bash
# Instalar Streamlit se não tiver
pip install streamlit plotly

# Salvar código acima como 'dashboard_floripa.py'
# Executar dashboard
streamlit run dashboard_floripa.py
```

---

## 🤖 **Caso 2: Sistema de Predição de Demanda Turística**

### **Objetivo**: Prever ocupação hoteleira usando machine learning

```python
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class PreditorTurismo:
    """Sistema completo de predição de demanda turística para Florianópolis"""
    
    def __init__(self):
        self.modelo = None
        self.scaler = StandardScaler()
        self.feature_names = None
        
    def gerar_dados_historicos(self, anos=3):
        """Gerar dados históricos de turismo com padrões realistas"""
        np.random.seed(42)
        
        # Gerar datas
        inicio = datetime.now() - timedelta(days=365 * anos)
        datas = pd.date_range(start=inicio, periods=365 * anos, freq='D')
        
        dados = []
        for data in datas:
            # Features temporais
            mes = data.month
            dia_ano = data.timetuple().tm_yday
            dia_semana = data.weekday()
            
            # Sazonalidade de SC
            if mes in [12, 1, 2]:  # Verão
                sazonalidade = 1.5
            elif mes in [6, 7]:  # Inverno
                sazonalidade = 0.6
            elif mes in [10, 11, 3]:  # Primavera/fim verão
                sazonalidade = 1.2
            else:  # Outono
                sazonalidade = 0.8
            
            # Efeito fim de semana
            if dia_semana >= 5:  # Sábado e domingo
                efeito_fds = 1.3
            elif dia_semana == 4:  # Sexta
                efeito_fds = 1.1
            else:
                efeito_fds = 0.9
            
            # Feriados simulados (aproximados)
            feriados_importantes = [1, 60, 120, 180, 240, 300, 359]  # Aproximação
            eh_feriado = any(abs(dia_ano - f) <= 1 for f in feriados_importantes)
            efeito_feriado = 1.4 if eh_feriado else 1.0
            
            # Eventos especiais (simulados)
            eventos_especiais = [45, 105, 165, 225, 285, 345]  # 6 eventos por ano
            eh_evento = any(abs(dia_ano - e) <= 3 for e in eventos_especiais)
            efeito_evento = 1.6 if eh_evento else 1.0
            
            # Condições climáticas (simuladas)
            temperatura = 20 + 8 * np.sin((dia_ano - 15) * 2 * np.pi / 365) + np.random.normal(0, 3)
            chuva_prob = 0.3 + 0.2 * np.sin((dia_ano - 15) * 2 * np.pi / 365)
            eh_chuva = np.random.random() < chuva_prob
            efeito_clima = 0.8 if eh_chuva else 1.0 if temperatura > 25 else 0.9
            
            # Calcular ocupação base
            ocupacao_base = 55  # Base 55%
            ocupacao = ocupacao_base * sazonalidade * efeito_fds * efeito_feriado * efeito_evento * efeito_clima
            
            # Adicionar ruído realista
            ocupacao += np.random.normal(0, 8)
            ocupacao = max(10, min(98, ocupacao))  # Limitar entre 10% e 98%
            
            # Variáveis econômicas (simuladas)
            preco_medio_diaria = 150 + 50 * sazonalidade + np.random.normal(0, 20)
            taxa_cambio = 5.0 + np.random.normal(0, 0.5)  # USD/BRL
            
            dados.append({
                'data': data,
                'ocupacao': round(ocupacao, 1),
                'mes': mes,
                'dia_semana': dia_semana,
                'dia_ano': dia_ano,
                'eh_feriado': int(eh_feriado),
                'eh_evento': int(eh_evento),
                'eh_fim_semana': int(dia_semana >= 5),
                'temperatura': round(temperatura, 1),
                'eh_chuva': int(eh_chuva),
                'preco_medio': round(preco_medio_diaria, 0),
                'taxa_cambio': round(taxa_cambio, 2)
            })
        
        return pd.DataFrame(dados)
    
    def preparar_features(self, df):
        """Preparar features para o modelo"""
        df = df.copy()
        
        # Features cíclicas para capturar sazonalidade
        df['mes_sin'] = np.sin(2 * np.pi * df['mes'] / 12)
        df['mes_cos'] = np.cos(2 * np.pi * df['mes'] / 12)
        df['dia_ano_sin'] = np.sin(2 * np.pi * df['dia_ano'] / 365)
        df['dia_ano_cos'] = np.cos(2 * np.pi * df['dia_ano'] / 365)
        df['dia_semana_sin'] = np.sin(2 * np.pi * df['dia_semana'] / 7)
        df['dia_semana_cos'] = np.cos(2 * np.pi * df['dia_semana'] / 7)
        
        # Features de lag (valores passados)
        df = df.sort_values('data')
        df['ocupacao_lag_1'] = df['ocupacao'].shift(1)
        df['ocupacao_lag_7'] = df['ocupacao'].shift(7)  # Semana anterior
        df['ocupacao_lag_30'] = df['ocupacao'].shift(30)  # Mês anterior
        
        # Médias móveis
        df['ocupacao_ma_7'] = df['ocupacao'].rolling(window=7).mean()
        df['ocupacao_ma_30'] = df['ocupacao'].rolling(window=30).mean()
        
        # Remover linhas com NaN (devido aos lags)
        df = df.dropna()
        
        # Features para o modelo
        feature_cols = [
            'mes_sin', 'mes_cos', 'dia_ano_sin', 'dia_ano_cos',
            'dia_semana_sin', 'dia_semana_cos', 'eh_feriado', 'eh_evento',
            'eh_fim_semana', 'temperatura', 'eh_chuva', 'preco_medio', 'taxa_cambio',
            'ocupacao_lag_1', 'ocupacao_lag_7', 'ocupacao_lag_30',
            'ocupacao_ma_7', 'ocupacao_ma_30'
        ]
        
        return df, feature_cols
    
    def treinar_modelo(self, df):
        """Treinar modelo de predição"""
        df_prep, feature_cols = self.preparar_features(df)
        
        X = df_prep[feature_cols]
        y = df_prep['ocupacao']
        
        # Dividir dados
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, shuffle=False  # Não embaralhar dados temporais
        )
        
        # Normalizar features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Treinar diferentes modelos
        modelos = {
            'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
            'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
        }
        
        resultados = {}
        for nome, modelo in modelos.items():
            # Treinar
            modelo.fit(X_train_scaled, y_train)
            
            # Predizer
            y_pred_train = modelo.predict(X_train_scaled)
            y_pred_test = modelo.predict(X_test_scaled)
            
            # Métricas
            mae_train = mean_absolute_error(y_train, y_pred_train)
            mae_test = mean_absolute_error(y_test, y_pred_test)
            rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
            
            # Validação cruzada
            cv_scores = cross_val_score(modelo, X_train_scaled, y_train, cv=5, scoring='neg_mean_absolute_error')
            
            resultados[nome] = {
                'modelo': modelo,
                'mae_train': mae_train,
                'mae_test': mae_test,
                'rmse_test': rmse_test,
                'cv_mean': -cv_scores.mean(),
                'cv_std': cv_scores.std(),
                'y_pred_test': y_pred_test,
                'y_test': y_test
            }
        
        # Escolher melhor modelo
        melhor_modelo_nome = min(resultados.keys(), key=lambda x: resultados[x]['mae_test'])
        self.modelo = resultados[melhor_modelo_nome]['modelo']
        self.feature_names = feature_cols
        
        print("🤖 RESULTADOS DO TREINAMENTO")
        print("=" * 50)
        for nome, res in resultados.items():
            print(f"\n{nome}:")
            print(f"  MAE Treino: {res['mae_train']:.2f}%")
            print(f"  MAE Teste: {res['mae_test']:.2f}%")
            print(f"  RMSE Teste: {res['rmse_test']:.2f}%")
            print(f"  CV Score: {res['cv_mean']:.2f} (±{res['cv_std']:.2f})")
            
        print(f"\n🏆 Melhor modelo: {melhor_modelo_nome}")
        print(f"Erro médio absoluto: {resultados[melhor_modelo_nome]['mae_test']:.2f}%")
        
        return resultados, X_test, y_test, df_prep
    
    def predizer_ocupacao(self, data_futura, **kwargs):
        """Predizer ocupação para uma data específica"""
        if self.modelo is None:
            raise ValueError("Modelo ainda não foi treinado!")
        
        # Criar DataFrame com a data
        df_pred = pd.DataFrame([{
            'data': data_futura,
            'mes': data_futura.month,
            'dia_semana': data_futura.weekday(),
            'dia_ano': data_futura.timetuple().tm_yday,
            'eh_feriado': kwargs.get('eh_feriado', 0),
            'eh_evento': kwargs.get('eh_evento', 0),
            'eh_fim_semana': int(data_futura.weekday() >= 5),
            'temperatura': kwargs.get('temperatura', 25),
            'eh_chuva': kwargs.get('eh_chuva', 0),
            'preco_medio': kwargs.get('preco_medio', 200),
            'taxa_cambio': kwargs.get('taxa_cambio', 5.0),
            'ocupacao': 0  # Placeholder
        }])
        
        # Adicionar valores de lag (em um sistema real, viria do histórico)
        df_pred['ocupacao_lag_1'] = kwargs.get('ocupacao_ontem', 60)
        df_pred['ocupacao_lag_7'] = kwargs.get('ocupacao_semana_passada', 60)
        df_pred['ocupacao_lag_30'] = kwargs.get('ocupacao_mes_passado', 60)
        df_pred['ocupacao_ma_7'] = kwargs.get('media_7d', 60)
        df_pred['ocupacao_ma_30'] = kwargs.get('media_30d', 60)
        
        # Preparar features
        df_pred, _ = self.preparar_features(df_pred)
        
        if len(df_pred) == 0:
            raise ValueError("Não foi possível preparar features para predição")
        
        # Predizer
        X_pred = df_pred[self.feature_names]
        X_pred_scaled = self.scaler.transform(X_pred)
        predicao = self.modelo.predict(X_pred_scaled)[0]
        
        return max(0, min(100, predicao))  # Garantir que esteja entre 0-100%

# Demonstração do sistema
def main():
    print("🏖️ SISTEMA DE PREDIÇÃO TURÍSTICA - FLORIANÓPOLIS")
    print("=" * 60)
    
    # Criar preditor
    preditor = PreditorTurismo()
    
    # Gerar dados históricos
    print("\n📊 Gerando dados históricos...")
    df_historico = preditor.gerar_dados_historicos(anos=3)
    print(f"Dados gerados: {len(df_historico)} dias")
    
    # Estatísticas descritivas
    print(f"\n📈 Estatísticas da ocupação:")
    print(f"Média: {df_historico['ocupacao'].mean():.1f}%")
    print(f"Desvio padrão: {df_historico['ocupacao'].std():.1f}%")
    print(f"Mínimo: {df_historico['ocupacao'].min():.1f}%")
    print(f"Máximo: {df_historico['ocupacao'].max():.1f}%")
    
    # Treinar modelo
    print("\n🤖 Treinando modelos...")
    resultados, X_test, y_test, df_prep = preditor.treinar_modelo(df_historico)
    
    # Visualizações
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # 1. Série temporal da ocupação
    axes[0, 0].plot(df_historico['data'], df_historico['ocupacao'], alpha=0.7)
    axes[0, 0].set_title('Histórico de Ocupação Hoteleira')
    axes[0, 0].set_ylabel('Ocupação (%)')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Sazonalidade por mês
    ocupacao_mensal = df_historico.groupby('mes')['ocupacao'].mean()
    axes[0, 1].bar(ocupacao_mensal.index, ocupacao_mensal.values)
    axes[0, 1].set_title('Ocupação Média por Mês')
    axes[0, 1].set_xlabel('Mês')
    axes[0, 1].set_ylabel('Ocupação (%)')
    
    # 3. Ocupação por dia da semana
    dias_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
    ocupacao_dia_semana = df_historico.groupby('dia_semana')['ocupacao'].mean()
    axes[0, 2].bar(range(7), ocupacao_dia_semana.values)
    axes[0, 2].set_title('Ocupação por Dia da Semana')
    axes[0, 2].set_xticks(range(7))
    axes[0, 2].set_xticklabels(dias_semana)
    axes[0, 2].set_ylabel('Ocupação (%)')
    
    # 4. Predições vs Real
    melhor_resultado = min(resultados.values(), key=lambda x: x['mae_test'])
    axes[1, 0].scatter(melhor_resultado['y_test'], melhor_resultado['y_pred_test'], alpha=0.6)
    axes[1, 0].plot([0, 100], [0, 100], 'r--', lw=2)
    axes[1, 0].set_xlabel('Ocupação Real (%)')
    axes[1, 0].set_ylabel('Ocupação Predita (%)')
    axes[1, 0].set_title('Predições vs Realidade')
    
    # 5. Distribuição dos erros
    erros = melhor_resultado['y_test'] - melhor_resultado['y_pred_test']
    axes[1, 1].hist(erros, bins=30, alpha=0.7, edgecolor='black')
    axes[1, 1].set_xlabel('Erro (Real - Predito)')
    axes[1, 1].set_ylabel('Frequência')
    axes[1, 1].set_title('Distribuição dos Erros')
    axes[1, 1].axvline(x=0, color='red', linestyle='--')
    
    # 6. Importância das features
    if hasattr(preditor.modelo, 'feature_importances_'):
        importancias = pd.DataFrame({
            'feature': preditor.feature_names,
            'importancia': preditor.modelo.feature_importances_
        }).sort_values('importancia', ascending=True)
        
        axes[1, 2].barh(range(len(importancias)), importancias['importancia'])
        axes[1, 2].set_yticks(range(len(importancias)))
        axes[1, 2].set_yticklabels(importancias['feature'], fontsize=8)
        axes[1, 2].set_xlabel('Importância')
        axes[1, 2].set_title('Importância das Features')
    
    plt.tight_layout()
    plt.show()
    
    # Exemplos de predição
    print("\n🔮 EXEMPLOS DE PREDIÇÕES")
    print("=" * 40)
    
    # Predição para fim de semana de verão
    data_verao = datetime(2025, 1, 11)  # Sábado de janeiro
    ocupacao_verao = preditor.predizer_ocupacao(
        data_verao,
        eh_feriado=0,
        eh_evento=0,
        temperatura=28,
        eh_chuva=0,
        preco_medio=250,
        ocupacao_ontem=75,
        ocupacao_semana_passada=70,
        media_7d=72
    )
    print(f"Fim de semana de verão (11/01/2025): {ocupacao_verao:.1f}%")
    
    # Predição para dia de semana no inverno
    data_inverno = datetime(2025, 7, 15)  # Terça de julho
    ocupacao_inverno = preditor.predizer_ocupacao(
        data_inverno,
        eh_feriado=0,
        eh_evento=0,
        temperatura=18,
        eh_chuva=1,
        preco_medio=120,
        ocupacao_ontem=45,
        ocupacao_semana_passada=50,
        media_7d=48
    )
    print(f"Dia de semana no inverno (15/07/2025): {ocupacao_inverno:.1f}%")
    
    # Predição para evento especial
    data_evento = datetime(2025, 10, 20)  # Durante Oktoberfest
    ocupacao_evento = preditor.predizer_ocupacao(
        data_evento,
        eh_feriado=0,
        eh_evento=1,  # Evento especial
        temperatura=24,
        eh_chuva=0,
        preco_medio=300,
        ocupacao_ontem=85,
        ocupacao_semana_passada=80,
        media_7d=82
    )
    print(f"Durante evento especial (20/10/2025): {ocupacao_evento:.1f}%")
    
    return preditor, df_historico

if __name__ == "__main__":
    preditor, dados = main()
```

---

## 🌐 **Caso 3: API de Dados Urbanos em Tempo Real**

### **Objetivo**: Criar API RESTful para servir dados urbanos de Florianópolis

```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import sqlite3
import uvicorn
from contextlib import asynccontextmanager

# Modelos Pydantic para validação de dados
class SensorData(BaseModel):
    timestamp: datetime
    sensor_id: str
    location: str = Field(..., description="Localização do sensor")
    pm25: float = Field(..., ge=0, le=500, description="PM2.5 em μg/m³")
    temperature: float = Field(..., ge=-10, le=50, description="Temperatura em °C")
    humidity: float = Field(..., ge=0, le=100, description="Umidade em %")

class TrafficData(BaseModel):
    timestamp: datetime
    location: str
    vehicles_count: int = Field(..., ge=0, description="Número de veículos")
    average_speed: float = Field(..., ge=0, le=120, description="Velocidade média km/h")

class TourismData(BaseModel):
    date: datetime
    hotel_occupancy: float = Field(..., ge=0, le=100, description="Ocupação hoteleira em %")
    tourist_count: int = Field(..., ge=0, description="Estimativa de turistas")
    average_price: float = Field(..., ge=0, description="Preço médio diária em R$")

class DashboardMetrics(BaseModel):
    timestamp: datetime
    air_quality_status: str
    traffic_status: str
    tourism_status: str
    alerts: List[str]

# Database manager
class DatabaseManager:
    def __init__(self, db_path: str = "floripa_urban_data.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Inicializar tabelas do banco de dados"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Tabela de dados de sensores
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            sensor_id TEXT,
            location TEXT,
            pm25 REAL,
            temperature REAL,
            humidity REAL
        )
        """)
        
        # Tabela de dados de tráfego
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS traffic_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            location TEXT,
            vehicles_count INTEGER,
            average_speed REAL
        )
        """)
        
        # Tabela de dados de turismo
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tourism_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATETIME,
            hotel_occupancy REAL,
            tourist_count INTEGER,
            average_price REAL
        )
        """)
        
        conn.commit()
        conn.close()
        
        # Inserir dados simulados se as tabelas estiverem vazias
        self.populate_sample_data()
    
    def populate_sample_data(self):
        """Popular com dados simulados para demonstração"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Verificar se já temos dados
        cursor.execute("SELECT COUNT(*) FROM sensor_data")
        if cursor.fetchone()[0] > 0:
            conn.close()
            return
        
        # Gerar dados dos últimos 7 dias
        end_time = datetime.now()
        start_time = end_time - timedelta(days=7)
        
        np.random.seed(42)
        
        # Localizações dos sensores
        locations = [
            "Centro - Praça XV",
            "Ponte Hercílio Luz",
            "Lagoa da Conceição",
            "Ingleses",
            "Trindade - UFSC"
        ]
        
        # Dados de sensores (a cada hora)
        current_time = start_time
        while current_time <= end_time:
            for i, location in enumerate(locations):
                # Simular variação diária
                hour = current_time.hour
                base_pm25 = 20 + 10 * np.sin((hour - 6) * np.pi / 12)
                if 7 <= hour <= 9 or 17 <= hour <= 19:  # Rush hours
                    base_pm25 += 15
                
                pm25 = max(5, base_pm25 + np.random.normal(0, 5))
                temp = 22 + 8 * np.sin((hour - 6) * np.pi / 12) + np.random.normal(0, 2)
                humidity = 65 + 20 * np.sin((hour - 12) * np.pi / 12) + np.random.normal(0, 5)
                
                cursor.execute("""
                INSERT INTO sensor_data (timestamp, sensor_id, location, pm25, temperature, humidity)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (current_time, f"SENSOR_{i:03d}", location, round(pm25, 1), 
                     round(temp, 1), round(max(20, min(95, humidity)), 1)))
            
            current_time += timedelta(hours=1)
        
        # Dados de tráfego
        traffic_locations = [
            "Ponte Hercílio Luz",
            "SC-401 - Ingleses",
            "SC-404 - Jurerê",
            "Av. Beira-Mar Norte",
            "Túnel Antonieta de Barros"
        ]
        
        current_time = start_time
        while current_time <= end_time:
            for location in traffic_locations:
                hour = current_time.hour
                day_of_week = current_time.weekday()
                
                # Padrão de tráfego
                if 6 <= hour <= 9 or 17 <= hour <= 20:  # Rush hours
                    base_vehicles = 800
                    base_speed = 25
                elif 22 <= hour or hour <= 5:  # Madrugada
                    base_vehicles = 50
                    base_speed = 60
                else:
                    base_vehicles = 300
                    base_speed = 45
                
                # Ajuste fim de semana
                if day_of_week >= 5:
                    base_vehicles *= 0.7
                    base_speed *= 1.2
                
                vehicles = max(10, int(base_vehicles + np.random.normal(0, 100)))
                speed = max(5, base_speed + np.random.normal(0, 10))
                
                cursor.execute("""
                INSERT INTO traffic_data (timestamp, location, vehicles_count, average_speed)
                VALUES (?, ?, ?, ?)
                """, (current_time, location, vehicles, round(speed, 1)))
            
            current_time += timedelta(hours=1)
        
        # Dados de turismo (diários)
        current_date = start_time.date()
        end_date = end_time.date()
        
        while current_date <= end_date:
            # Sazonalidade
            month = current_date.month
            if month in [12, 1, 2]:  # Verão
                base_occupancy = 80
            elif month in [6, 7]:  # Inverno
                base_occupancy = 45
            else:
                base_occupancy = 60
            
            # Fim de semana
            weekday = current_date.weekday()
            if weekday >= 5:
                base_occupancy += 15
            
            occupancy = max(10, min(95, base_occupancy + np.random.normal(0, 10)))
            tourists = int(occupancy * 1000 + np.random.normal(0, 5000))
            avg_price = 150 + (occupancy - 50) * 3 + np.random.normal(0, 30)
            
            cursor.execute("""
            INSERT INTO tourism_data (date, hotel_occupancy, tourist_count, average_price)
            VALUES (?, ?, ?, ?)
            """, (current_date, round(occupancy, 1), max(0, tourists), round(max(80, avg_price), 0)))
            
            current_date += timedelta(days=1)
        
        conn.commit()
        conn.close()
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)

# Instância global do gerenciador de banco
db_manager = DatabaseManager()

# Dependência para injeção do banco
def get_db():
    conn = db_manager.get_connection()
    try:
        yield conn
    finally:
        conn.close()

# Criar aplicação FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Iniciando API de Dados Urbanos - Florianópolis")
    yield
    # Shutdown
    print("🛑 Encerrando API")

app = FastAPI(
    title="API Dados Urbanos - Florianópolis",
    description="API para monitoramento de dados urbanos da Ilha da Magia",
    version="1.0.0",
    lifespan=lifespan
)

# CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints da API

@app.get("/")
async def root():
    return {
        "message": "API de Dados Urbanos - Florianópolis",
        "version": "1.0.0",
        "endpoints": {
            "sensor_data": "/sensors/",
            "traffic_data": "/traffic/",
            "tourism_data": "/tourism/",
            "dashboard": "/dashboard/",
            "health": "/health/"
        }
    }

@app.get("/health/")
async def health_check():
    """Verificação de saúde da API"""
    return {
        "status": "healthy",
        "timestamp": datetime.now(),
        "database": "connected"
    }

@app.get("/sensors/", response_model=List[SensorData])
async def get_sensor_data(
    hours: int = 24,
    location: Optional[str] = None,
    conn = Depends(get_db)
):
    """Obter dados dos sensores de qualidade do ar"""
    
    cursor = conn.cursor()
    
    # Construir query
    query = """
    SELECT timestamp, sensor_id, location, pm25, temperature, humidity 
    FROM sensor_data 
    WHERE timestamp >= datetime('now', '-{} hours')
    """.format(hours)
    
    params = []
    if location:
        query += " AND location = ?"
        params.append(location)
    
    query += " ORDER BY timestamp DESC"
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    if not rows:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado")
    
    # Converter para modelo Pydantic
    data = []
    for row in rows:
        data.append(SensorData(
            timestamp=datetime.fromisoformat(row[0]),
            sensor_id=row[1],
            location=row[2],
            pm25=row[3],
            temperature=row[4],
            humidity=row[5]
        ))
    
    return data

@app.get("/traffic/", response_model=List[TrafficData])
async def get_traffic_data(
    hours: int = 24,
    location: Optional[str] = None,
    conn = Depends(get_db)
):
    """Obter dados de tráfego"""
    
    cursor = conn.cursor()
    
    query = """
    SELECT timestamp, location, vehicles_count, average_speed 
    FROM traffic_data 
    WHERE timestamp >= datetime('now', '-{} hours')
    """.format(hours)
    
    params = []
    if location:
        query += " AND location = ?"
        params.append(location)
    
    query += " ORDER BY timestamp DESC"
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    if not rows:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado")
    
    data = []
    for row in rows:
        data.append(TrafficData(
            timestamp=datetime.fromisoformat(row[0]),
            location=row[1],
            vehicles_count=row[2],
            average_speed=row[3]
        ))
    
    return data

@app.get("/tourism/", response_model=List[TourismData])
async def get_tourism_data(
    days: int = 30,
    conn = Depends(get_db)
):
    """Obter dados de turismo"""
    
    cursor = conn.cursor()
    
    query = """
    SELECT date, hotel_occupancy, tourist_count, average_price 
    FROM tourism_data 
    WHERE date >= date('now', '-{} days')
    ORDER BY date DESC
    """.format(days)
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    if not rows:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado")
    
    data = []
    for row in rows:
        data.append(TourismData(
            date=datetime.fromisoformat(row[0]),
            hotel_occupancy=row[1],
            tourist_count=row[2],
            average_price=row[3]
        ))
    
    return data

@app.get("/dashboard/", response_model=DashboardMetrics)
async def get_dashboard_metrics(conn = Depends(get_db)):
    """Obter métricas consolidadas para dashboard"""
    
    cursor = conn.cursor()
    
    # Dados mais recentes de qualidade do ar
    cursor.execute("""
    SELECT AVG(pm25) as avg_pm25 
    FROM sensor_data 
    WHERE timestamp >= datetime('now', '-1 hour')
    """)
    avg_pm25 = cursor.fetchone()[0] or 0
    
    # Status da qualidade do ar
    if avg_pm25 <= 25:
        air_status = "Boa"
    elif avg_pm25 <= 50:
        air_status = "Moderada"
    else:
        air_status = "Ruim"
    
    # Dados de tráfego
    cursor.execute("""
    SELECT AVG(vehicles_count) as avg_traffic 
    FROM traffic_data 
    WHERE timestamp >= datetime('now', '-1 hour')
    """)
    avg_traffic = cursor.fetchone()[0] or 0
    
    # Status do tráfego
    if avg_traffic < 200:
        traffic_status = "Fluindo"
    elif avg_traffic < 500:
        traffic_status = "Moderado"
    else:
        traffic_status = "Congestionado"
    
    # Dados de turismo (último dia)
    cursor.execute("""
    SELECT hotel_occupancy 
    FROM tourism_data 
    ORDER BY date DESC 
    LIMIT 1
    """)
    occupancy = cursor.fetchone()
    occupancy = occupancy[0] if occupancy else 50
    
    # Status do turismo
    if occupancy > 80:
        tourism_status = "Alta demanda"
    elif occupancy > 60:
        tourism_status = "Demanda moderada"
    else:
        tourism_status = "Baixa demanda"
    
    # Gerar alertas
    alerts = []
    if avg_pm25 > 50:
        alerts.append(f"Qualidade do ar ruim (PM2.5: {avg_pm25:.1f} μg/m³)")
    if avg_traffic > 600:
        alerts.append(f"Tráfego intenso ({avg_traffic:.0f} veículos/h)")
    if occupancy > 90:
        alerts.append(f"Ocupação hoteleira crítica ({occupancy:.1f}%)")
    
    if not alerts:
        alerts.append("Todos os indicadores normais")
    
    return DashboardMetrics(
        timestamp=datetime.now(),
        air_quality_status=air_status,
        traffic_status=traffic_status,
        tourism_status=tourism_status,
        alerts=alerts
    )

@app.post("/sensors/", response_model=dict)
async def add_sensor_data(data: SensorData, conn = Depends(get_db)):
    """Adicionar novos dados de sensor"""
    
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO sensor_data (timestamp, sensor_id, location, pm25, temperature, humidity)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (data.timestamp, data.sensor_id, data.location, data.pm25, data.temperature, data.humidity))
    
    conn.commit()
    
    return {"message": "Dados do sensor adicionados com sucesso", "id": cursor.lastrowid}

# Endpoint para estatísticas
@app.get("/stats/")
async def get_statistics(conn = Depends(get_db)):
    """Obter estatísticas gerais dos dados"""
    
    cursor = conn.cursor()
    
    # Estatísticas de sensores
    cursor.execute("SELECT COUNT(*) FROM sensor_data")
    sensor_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT AVG(pm25), MIN(pm25), MAX(pm25) FROM sensor_data WHERE timestamp >= datetime('now', '-24 hours')")
    pm25_stats = cursor.fetchone()
    
    # Estatísticas de tráfego
    cursor.execute("SELECT COUNT(*) FROM traffic_data")
    traffic_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT AVG(vehicles_count) FROM traffic_data WHERE timestamp >= datetime('now', '-24 hours')")
    avg_traffic_24h = cursor.fetchone()[0]
    
    # Estatísticas de turismo
    cursor.execute("SELECT COUNT(*) FROM tourism_data")
    tourism_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT AVG(hotel_occupancy) FROM tourism_data WHERE date >= date('now', '-7 days')")
    avg_occupancy_7d = cursor.fetchone()[0]
    
    return {
        "total_records": {
            "sensor_data": sensor_count,
            "traffic_data": traffic_count,
            "tourism_data": tourism_count
        },
        "last_24h": {
            "avg_pm25": round(pm25_stats[0] or 0, 1),
            "min_pm25": round(pm25_stats[1] or 0, 1),
            "max_pm25": round(pm25_stats[2] or 0, 1),
            "avg_traffic": round(avg_traffic_24h or 0, 0)
        },
        "last_7d": {
            "avg_hotel_occupancy": round(avg_occupancy_7d or 0, 1)
        }
    }

if __name__ == "__main__":
    uvicorn.run(
        "api_floripa:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
```

### **Como executar a API:**

```bash
# Instalar dependências
pip install fastapi uvicorn sqlite3

# Salvar código como 'api_floripa.py'
# Executar API
python api_floripa.py

# Ou usando uvicorn diretamente
uvicorn api_floripa:app --reload --host 0.0.0.0 --port 8000
```

### **Exemplos de uso da API:**

```bash
# Obter dados dos sensores (últimas 24h)
curl http://localhost:8000/sensors/

# Obter dados de tráfego da Ponte Hercílio Luz
curl "http://localhost:8000/traffic/?location=Ponte Hercílio Luz"

# Obter métricas do dashboard
curl http://localhost:8000/dashboard/

# Obter estatísticas gerais
curl http://localhost:8000/stats/

# Documentação automática (Swagger)
# Acesse: http://localhost:8000/docs
```

---

## 📝 **Resumo dos Casos Práticos**

### **🎯 O que cada caso ensina:**

1. **Dashboard Streamlit**: Interface visual interativa para dados
2. **Sistema ML**: Predição usando algoritmos de machine learning  
3. **API REST**: Arquitetura de microsserviços para dados urbanos

### **🛠️ Tecnologias aplicadas:**
- **Visualização**: Streamlit, Plotly, Matplotlib
- **Machine Learning**: Scikit-learn, feature engineering, validação
- **APIs**: FastAPI, Pydantic, SQLite, documentação automática
- **Dados**: Pandas, NumPy, séries temporais, correlações

### **📚 Próximos passos:**
1. Implementar autenticação na API
2. Adicionar cache Redis para performance
3. Integrar com dados reais (APIs governamentais)
4. Deploy em cloud (AWS, Google Cloud, Azure)
5. Adicionar testes automatizados

**Estes casos práticos mostram aplicações reais de Big Data que podem ser adaptadas para qualquer região ou contexto! 🚀**
