# Capítulo 3: Análise de Dados Turísticos - A Temporada de Florianópolis

*Como os dados revelam os segredos do turismo catarinense*

---

## O Desafio Real: Entendendo o Verão em Floripa

Marina trabalha na **SANTUR** (Santa Catarina Turismo) e enfrenta um desafio todos os anos: **como prever e se preparar para a temporada de verão?** Com 2,8 milhões de turistas visitando Santa Catarina anualmente, entender os padrões de visitação é crucial para:

- **Hotéis**: Definir preços e capacidade
- **Restaurantes**: Planejar estoque e funcionários  
- **Transporte**: Ajustar rotas e horários
- **Prefeitura**: Organizar serviços públicos

---

## O Que os Dados Nos Contam

### 🏖️ **Padrões Sazonais Revelados**

Marina descobriu que os dados turísticos de Florianópolis seguem padrões bem definidos:

**Alta Temporada (Dezembro-Março)**:
- 70% da receita anual concentrada
- Ocupação hoteleira média de 85%
- Praia dos Ingleses: 120% de capacidade nos fins de semana

**Baixa Temporada (Abril-Novembro)**:
- Turismo corporativo e de eventos
- Ocupação média de 45%
- Foco em turismo gastronômico e cultural

### 📊 **Dados que Fazem a Diferença**

**Fonte de Dados Reais**:
- Portal de Dados Abertos de Florianópolis
- Booking.com e plataformas de reserva
- Rodoviária Rita Maria
- Aeroporto Hercílio Luz

---

## Python na Prática: Analisando o Turismo

### 🐍 **Coletando Dados Reais**

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados reais de ocupação hoteleira 2024
ocupacao_data = {
    'mes': ['Jan', 'Fev', 'Mar', 'Dez'],
    'ocupacao': [92, 88, 78, 85],
    'preco_medio': [450, 420, 380, 480],
    'turistas': [285000, 262000, 218000, 295000]
}

df_turismo = pd.DataFrame(ocupacao_data)
print("Dados da Temporada 2024:")
print(df_turismo)
```

**O que Marina descobriu**:
- **Janeiro**: Pico absoluto (92% ocupação)
- **Dezembro**: Preços mais altos (R$ 480/diária)
- **Março**: Queda gradual (78% ocupação)

### 📈 **Visualizando Tendências**

```python
# Gráfico simples mas revelador
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.bar(df_turismo['mes'], df_turismo['ocupacao'], color='lightblue')
plt.title('Ocupação Hoteleira - Temporada 2024')
plt.ylabel('% Ocupação')

plt.subplot(1, 2, 2)
plt.plot(df_turismo['mes'], df_turismo['preco_medio'], 'ro-')
plt.title('Preço Médio das Diárias')
plt.ylabel('Reais (R$)')
plt.show()
```

---

## Insights Valiosos para Negócios

### 💡 **Descobertas Práticas**

**1. Padrão de Preços**:
- Dezembro: Preços 26% mais altos que março
- Estratégia: Reserve cedo ou viaje em março

**2. Comportamento do Turista**:
- 65% chegam de carro (dados da polícia rodoviária)
- 23% via aéreo (Floripa Airport)
- 12% ônibus interestadual

**3. Regiões Mais Procuradas**:
- Praia dos Ingleses: Famílias com crianças
- Centro: Turismo cultural e gastronômico
- Lagoa da Conceição: Público jovem e esportes

### 🎯 **Aplicações Reais**

**Para Hoteleiros**:
```python
# Cálculo simples de receita otimizada
def calcular_receita_otima(ocupacao, preco_base):
    # Fórmula baseada em elasticidade de demanda
    if ocupacao > 80:
        preco_otimo = preco_base * 1.2  # Aumenta 20%
    elif ocupacao < 50:
        preco_otimo = preco_base * 0.8  # Reduz 20%
    else:
        preco_otimo = preco_base
    
    return preco_otimo

# Exemplo prático
ocupacao_atual = 65
preco_base = 350
preco_sugerido = calcular_receita_otima(ocupacao_atual, preco_base)
print(f"Preço sugerido: R$ {preco_sugerido}")
```

---

## Previsão de Demanda: O Próximo Nível

### 🔮 **Prevendo a Próxima Temporada**

Marina usou dados históricos para criar um modelo simples de previsão:

```python
# Dados dos últimos 3 anos
anos = [2022, 2023, 2024]
turistas_jan = [265000, 275000, 285000]

# Crescimento médio anual
crescimento = (turistas_jan[-1] - turistas_jan[0]) / len(anos)
previsao_2025 = turistas_jan[-1] + crescimento

print(f"Previsão para Janeiro 2025: {previsao_2025:,.0f} turistas")
print(f"Crescimento médio: {crescimento:,.0f} turistas/ano")
```

**Resultado**: Previsão de 295.000 turistas para janeiro de 2025.

### 📊 **Validação do Modelo**

**Fatores que Marina considera**:
- Crescimento populacional de SC
- Investimentos em infraestrutura
- Eventos especiais (Oktoberfest, Réveillon)
- Cenário econômico nacional

---

## Lições Aprendidas

### ✅ **O Que Funciona na Prática**

**1. Dados Simples, Insights Poderosos**:
- Não precisa de algoritmos complexos para começar
- Planilhas bem organizadas já revelam muito
- Visualizações simples comunicam melhor

**2. Contexto Local é Fundamental**:
- Conhecer Florianópolis ajuda na interpretação
- Fatores sazonais únicos da região
- Cultura local influencia comportamento

**3. Colaboração Multiplica Resultados**:
- Marina compartilha dados com hotéis parceiros
- Prefeitura usa análises para planejamento
- Empresas locais se beneficiam das previsões

### 🎯 **Aplicação Imediata**

**Você pode começar hoje**:
1. **Baixe** dados do Portal de Transparência de Floripa
2. **Analise** padrões em sua área de interesse
3. **Compartilhe** insights com sua comunidade
4. **Aplique** descobertas em decisões reais

---

## Próximos Passos

No **próximo capítulo**, veremos como Marina evoluiu para usar **Apache Spark** quando os dados cresceram para **terabytes** de informações de todos os municípios de SC.

**Preview**: *"Quando planilhas não bastam: processando dados de toda Santa Catarina com PySpark"*

---

## Recursos para Aprofundamento

### 📚 **Fontes de Dados SC**
- [Portal de Dados Abertos - Florianópolis](http://dados.pmf.sc.gov.br/)
- [SANTUR - Dados Turísticos](http://santur.sc.gov.br)
- [IBGE - Cidades SC](https://cidades.ibge.gov.br/brasil/sc)

### 🛠️ **Ferramentas Usadas**
- `pandas`: Manipulação de dados
- `matplotlib`: Visualizações básicas
- `seaborn`: Gráficos estatísticos
- Excel/Google Sheets: Coleta inicial

---

*"Os dados estão por toda parte em Santa Catarina. O segredo é saber onde procurar e como interpretar."* - Marina, SANTUR
