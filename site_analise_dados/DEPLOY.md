# DataScience Pro - Deploy Guide

## 🚀 Deploy Rápido no Netlify

### Método 1: Drag & Drop (Mais Rápido)

1. **Acesse**: [https://app.netlify.com/drop](https://app.netlify.com/drop)

2. **Prepare os arquivos**: 
   - Comprima a pasta `site_analise_dados` em um ZIP
   - Ou selecione todos os arquivos da pasta

3. **Upload**:
   - Arraste o ZIP ou arquivos para a área do Netlify
   - Aguarde o deploy (1-2 minutos)

4. **Pronto!**: Seu site estará no ar com URL automática

### Método 2: Via Git (Recomendado para Produção)

1. **Crie um repositório no GitHub:**
```bash
# No terminal, na pasta do projeto
git init
git add .
git commit -m "Initial commit: DataScience Pro"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/datascience-pro.git
git push -u origin main
```

2. **Conecte ao Netlify:**
   - Acesse [https://app.netlify.com](https://app.netlify.com)
   - Clique "New site from Git"
   - Escolha GitHub
   - Selecione seu repositório
   - Configure:
     - **Build command**: (deixe vazio)
     - **Publish directory**: `site_analise_dados`
   - Deploy!

### Método 3: Netlify CLI

1. **Instale o CLI:**
```bash
npm install -g netlify-cli
```

2. **Login:**
```bash
netlify login
```

3. **Deploy:**
```bash
cd site_analise_dados
netlify deploy --prod --dir .
```

## ⚙️ Configurações Importantes

### Domínio Personalizado

1. **No Netlify Dashboard:**
   - Site settings → Domain management
   - Add custom domain
   - Configure DNS conforme instruções

### HTTPS Automático

- ✅ Ativado automaticamente
- ✅ Certificado SSL gratuito via Let's Encrypt
- ✅ Redirect HTTP → HTTPS configurado

### Performance

- ✅ CDN global ativo
- ✅ Compressão Gzip/Brotli
- ✅ Cache headers otimizados
- ✅ Assets minificados

## 🔧 Customizações

### Variáveis de Ambiente

Se precisar de configurações:

1. **Site settings → Environment variables**
2. Adicione:
```
SITE_NAME=DataScience Pro
GOOGLE_ANALYTICS_ID=seu-id-aqui
```

### Formulários (Futuro)

Para adicionar formulários de contato:

```html
<form name="contato" method="POST" data-netlify="true">
  <input type="text" name="nome" required>
  <input type="email" name="email" required>
  <textarea name="mensagem" required></textarea>
  <button type="submit">Enviar</button>
</form>
```

### Functions (Avançado)

Para APIs serverless:

```javascript
// netlify/functions/api.js
exports.handler = async (event, context) => {
  return {
    statusCode: 200,
    body: JSON.stringify({ message: "Hello from Netlify Functions!" })
  };
};
```

## 📊 Monitoramento

### Analytics

1. **Site settings → Analytics**
2. Ative o Netlify Analytics (pago) ou configure Google Analytics

### Performance

1. **Deploys → Functions** - Monitore funções
2. **Site settings → Build & deploy** - Logs de build
3. Use ferramentas como:
   - [PageSpeed Insights](https://pagespeed.web.dev/)
   - [GTmetrix](https://gtmetrix.com/)
   - [WebPageTest](https://www.webpagetest.org/)

## 🛠️ Troubleshooting

### Site não carrega

1. Verifique se `index.html` está na raiz do publish directory
2. Confirme que não há erros no console do navegador
3. Verifique os logs de deploy no Netlify

### Arquivos CSS/JS não carregam

1. Confirme que os caminhos estão corretos (relativos)
2. Verifique se não há caracteres especiais nos nomes
3. Force um novo deploy

### Upload de arquivos não funciona

1. O site é estático - uploads são temporários (client-side only)
2. Para uploads persistentes, considere:
   - Netlify Forms
   - Serviços externos (Cloudinary, AWS S3)
   - Netlify Functions com storage

## 🎯 URLs de Exemplo

Após o deploy, seu site estará disponível em:

- **URL automática**: `https://magnificent-unicorn-123456.netlify.app`
- **URL personalizada**: `https://datascience-pro.netlify.app`
- **Domínio próprio**: `https://seudominio.com`

## 📈 Próximos Passos

1. **Configurar domínio personalizado**
2. **Ativar analytics**
3. **Configurar formulário de feedback**
4. **Adicionar PWA features**
5. **Configurar CDN para assets estáticos**

## ⚡ Deploy One-Click

Para deploy instantâneo:

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/SEU-USUARIO/datascience-pro)

---

**Seu site estará no ar em menos de 5 minutos! 🚀**

Precisa de ajuda? Consulte a [documentação oficial do Netlify](https://docs.netlify.com/).
