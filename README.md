# Site de Análise de Dados Científicos

## 📊 Sobre o Projeto

Este é um site completo sobre análise de dados científicos que combina conteúdo educacional de alta qualidade com uma ferramenta interativa de análise. O projeto foi desenvolvido para ser uma referência abrangente para pesquisadores, estudantes e profissionais da área de ciência de dados.

## 🌟 Características Principais

### 📚 Conteúdo Educacional
- **Guia Completo**: Metodologia completa desde preparação de dados até modelagem avançada
- **Rigor Científico**: Conteúdo técnico preciso e atualizado
- **Exemplos Práticos**: Casos de uso reais e aplicações
- **Melhores Práticas**: Padrões da indústria e academia

### 🔧 Ferramenta de Análise Interativa
- **Upload de Dados**: Suporte para CSV, JSON e Excel
- **Análise Automática**: Estatísticas descritivas, correlações, detecção de outliers
- **Visualizações**: Gráficos de distribuição, heatmaps de correlação
- **Qualidade dos Dados**: Métricas de completude e integridade
- **Exportação**: Relatórios e dados processados

### 📖 Biblioteca de Referências
- **30+ Recursos**: Livros, artigos, documentação e cursos
- **Busca Avançada**: Filtros por categoria e texto
- **Citações Automáticas**: Geração de citações formatadas
- **Acesso Direto**: Links para recursos online

## 🚀 Tecnologias Utilizadas

### Frontend
- **HTML5** - Estrutura semântica moderna
- **CSS3** - Design responsivo com CSS Grid e Flexbox
- **Vanilla JavaScript (ES6+)** - Funcionalidade interativa
- **Chart.js** - Visualizações de dados
- **Papa Parse** - Processamento de CSV
- **Font Awesome** - Iconografia

### Bibliotecas de Análise
- **Estatísticas Descritivas**: Média, mediana, desvio padrão
- **Correlações**: Coeficiente de Pearson
- **Detecção de Outliers**: Método IQR
- **Visualizações**: Histogramas, scatter plots, heatmaps

## 📁 Estrutura do Projeto

```
site_analise_dados/
├── index.html              # Página principal (SPA)
├── css/
│   └── style.css           # Estilos completos e responsivos
├── js/
│   ├── main.js            # Funcionalidades principais e utilitários
│   ├── analysis-tool.js   # Ferramenta de análise de dados
│   └── app.js             # Inicialização e referências
├── static/                # Arquivos estáticos (imagens, etc.)
├── templates/             # Templates auxiliares (se necessário)
└── uploads/               # Diretório para uploads (local)
```

## 🌐 Deploy no Netlify

### Pré-requisitos
1. Conta no [Netlify](https://www.netlify.com/)
2. Repositório Git (GitHub, GitLab, ou Bitbucket)

### Opção 1: Deploy via Git (Recomendado)

1. **Prepare o repositório:**
```bash
git init
git add .
git commit -m "Initial commit - DataScience Pro site"
git branch -M main
git remote add origin https://github.com/seu-usuario/site-analise-dados.git
git push -u origin main
```

2. **Configure o Netlify:**
   - Acesse o [Netlify Dashboard](https://app.netlify.com/)
   - Clique em "New site from Git"
   - Conecte seu repositório
   - Configure as opções de build:
     - **Branch to deploy**: `main`
     - **Build command**: (deixe vazio)
     - **Publish directory**: `site_analise_dados`

3. **Deploy automático:**
   - O site será deployado automaticamente
   - Atualizações no repositório triggeram novos deploys

### Opção 2: Deploy Manual

1. **Prepare os arquivos:**
```bash
# Comprima apenas o conteúdo da pasta site_analise_dados
cd "site_analise_dados"
# Selecione todos os arquivos (index.html, css/, js/, etc.)
```

2. **Upload no Netlify:**
   - Acesse [Netlify Drop](https://app.netlify.com/drop)
   - Arraste e solte a pasta ou arquivo ZIP
   - O site será deployado instantaneamente

### Configurações Avançadas

Crie um arquivo `netlify.toml` na raiz do projeto:

```toml
[build]
  publish = "site_analise_dados"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

[[headers]]
  for = "*.js"
  [headers.values]
    Cache-Control = "public, max-age=31536000"

[[headers]]
  for = "*.css"
  [headers.values]
    Cache-Control = "public, max-age=31536000"

[build.environment]
  NODE_VERSION = "18"

# Redirects para SPA
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

## 💡 Funcionalidades Detalhadas

### 📊 Análise de Dados
- **Upload Seguro**: Validação de tipos e tamanhos de arquivo
- **Processamento Inteligente**: Detecção automática de tipos de dados
- **Análise Estatística**: Métricas completas para variáveis numéricas
- **Correlações**: Matriz de correlação visual
- **Qualidade**: Avaliação de completude e duplicatas
- **Outliers**: Detecção usando método IQR

### 📈 Visualizações
- **Distribuições**: Histogramas para dados numéricos
- **Categorias**: Gráficos de barras para dados categóricos
- **Correlações**: Heatmaps interativos
- **Responsive**: Adaptação automática a diferentes telas

### 📚 Conteúdo Educacional
- **Metodologia Científica**: Do planejamento à publicação
- **Ferramentas**: Excel, Python, R, SPSS
- **Técnicas Avançadas**: Machine Learning, Deep Learning
- **Boas Práticas**: Validação, reprodutibilidade, ética

## 🎯 Casos de Uso

### Para Estudantes
- Aprender metodologia de análise de dados
- Praticar com dados reais
- Acessar referências acadêmicas
- Desenvolver projetos de pesquisa

### Para Pesquisadores
- Análise exploratória rápida
- Validação de qualidade dos dados
- Geração de relatórios preliminares
- Referências para metodologia

### Para Profissionais
- Prototipagem de análises
- Apresentações para stakeholders
- Educação de equipes
- Benchmarking de dados

## 🔧 Desenvolvimento Local

1. **Clone o projeto:**
```bash
git clone https://github.com/seu-usuario/site-analise-dados.git
cd site-analise-dados
```

2. **Execute localmente:**
```bash
# Opção 1: Servidor Python
cd site_analise_dados
python -m http.server 8000

# Opção 2: Live Server (VS Code)
# Instale a extensão Live Server e abra index.html

# Opção 3: Node.js serve
npx serve site_analise_dados
```

3. **Acesse:**
```
http://localhost:8000
```

## 📱 Responsividade

O site é totalmente responsivo e funciona perfeitamente em:
- **Desktop**: Layout completo com três colunas
- **Tablet**: Layout adaptado com duas colunas
- **Mobile**: Layout em coluna única com navegação otimizada

## ♿ Acessibilidade

- **WCAG 2.1 AA**: Conformidade com padrões de acessibilidade
- **Navegação por Teclado**: Suporte completo
- **Screen Readers**: Marcação semântica adequada
- **Alto Contraste**: Esquema de cores acessível
- **Reduced Motion**: Respeita preferências de animação

## 🔒 Segurança

- **CSP Headers**: Política de segurança de conteúdo
- **HTTPS Only**: Forçar conexões seguras
- **Input Validation**: Validação de uploads
- **XSS Protection**: Proteção contra scripts maliciosos

## 📈 Performance

- **Otimizado**: CSS e JS minificados
- **Lazy Loading**: Carregamento sob demanda
- **Caching**: Headers de cache apropriados
- **CDN Ready**: Compatível com redes de distribuição

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

Desenvolvido com ❤️ para a comunidade de ciência de dados.

## 🔗 Links Úteis

- **Demo**: [https://seu-site.netlify.app](https://seu-site.netlify.app)
- **Documentação**: [Wiki do Projeto](https://github.com/seu-usuario/site-analise-dados/wiki)
- **Issues**: [Reportar Problemas](https://github.com/seu-usuario/site-analise-dados/issues)
- **Discussions**: [Fórum da Comunidade](https://github.com/seu-usuario/site-analise-dados/discussions)

---

**DataScience Pro** - Transformando dados em conhecimento científico! 🚀📊
