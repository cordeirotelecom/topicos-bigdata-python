# Capítulo 3: Análise de Dados Turísticos - A Temporada de Florianópolis

*Como os dados revelam os segredos do turismo catarinense*

---

## O Desafio Real: Entendendo o Verão em Floripa

A Prefeitura de Florianópolis pediu para **Patrick** analisar um novo desafio: **como prever e se preparar para a temporada de verão?** Com 2,8 milhões de turistas visitando Santa Catarina anualmente, entender os padrões de visitação se tornou crucial para:

- **Hotéis**: Definir preços e capacidade
- **Restaurantes**: Planejar estoque e funcionários  
- **Transporte**: Ajustar rotas e horários
- **Prefeitura**: Organizar serviços públicos

Patrick recebeu dados da **SANTUR** (Santa Catarina Turismo) e começou sua investigação.

---

## O Que os Dados Nos Contam

### 🏖️ **Padrões Sazonais Revelados**

Patrick descobriu que os dados turísticos de Florianópolis seguem padrões bem definidos:

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

Patrick organizou os dados de ocupação hoteleira de 2024 numa planilha simples:

**Dados da Temporada 2024**:
| Mês | Ocupação | Preço Médio | Turistas |
|-----|----------|-------------|----------|
| Janeiro | 92% | R$ 450 | 285.000 |
| Fevereiro | 88% | R$ 420 | 262.000 |
| Março | 78% | R$ 380 | 218.000 |
| Dezembro | 85% | R$ 480 | 295.000 |

**O que Patrick descobriu**:
- **Janeiro**: Pico absoluto (92% ocupação)
- **Dezembro**: Preços mais altos (R$ 480/diária) 
- **Março**: Queda gradual (78% ocupação)

### 📈 **Visualizando Tendências**

Com Python, Patrick criou gráficos simples que revelaram padrões importantes:

**Gráfico 1: Ocupação por Mês**
- Barras azuis mostrando % de ocupação
- Janeiro claramente no topo
- Queda gradual até março

**Gráfico 2: Preços ao Longo do Tempo**  
- Linha vermelha conectando os preços
- Dezembro mais caro que janeiro
- Março com melhor custo-benefício

*Com apenas algumas linhas de código Python, Patrick transformou números em insights visuais!*

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

**Para Hoteleiros - Fórmula Simples de Preços**:

Patrick descobriu uma regra prática para otimizar preços:

**🔍 Lógica de Preços Inteligente**:
- **Ocupação alta** (acima de 80%): Aumente preços em 20%
- **Ocupação baixa** (abaixo de 50%): Reduza preços em 20%  
- **Ocupação normal** (50-80%): Mantenha preço base

**Exemplo prático**:
- Hotel com 65% de ocupação
- Preço base: R$ 350
- **Recomendação**: Manter R$ 350 (está na faixa normal)

*Simples assim! Não precisa de fórmulas complexas para começar.*

---

## Previsão de Demanda: O Próximo Nível

### 🔮 **Prevendo a Próxima Temporada**

Patrick usou uma técnica simples para prever o futuro:

**📊 Dados Históricos de Janeiro**:
- 2022: 265.000 turistas
- 2023: 275.000 turistas  
- 2024: 285.000 turistas

**🧮 Cálculo da Tendência**:
- Crescimento em 2 anos: 20.000 turistas (285k - 265k)
- Crescimento médio anual: 10.000 turistas por ano
- **Previsão 2025**: 285.000 + 10.000 = **295.000 turistas**

**✅ Resultado**: Patrick prevê 295.000 turistas para janeiro de 2025.

### 📊 **Validação do Modelo**

**Fatores que Patrick considera para confirmar a previsão**:
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
- Patrick compartilha dados com hotéis parceiros
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

No **próximo capítulo**, veremos como Patrick evoluiu para usar **Apache Spark** quando os dados cresceram para **terabytes** de informações de todos os municípios de SC.

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

*"Os dados estão por toda parte em Santa Catarina. O segredo é saber onde procurar e como interpretar."* - Patrick, SANTUR
