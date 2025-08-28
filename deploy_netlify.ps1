# 🚀 Deploy Automático no Netlify - BigData Analytics Pro
Write-Host "🚀 INICIANDO DEPLOY AUTOMÁTICO NO NETLIFY..." -ForegroundColor Green
Write-Host ""

# Verificar se estamos no diretório correto
$currentDir = Get-Location
Write-Host "📁 Diretório atual: $currentDir" -ForegroundColor Yellow

# Verificar arquivos essenciais
$files = @("netlify.toml", "_redirects", "index.html", "site_analise_dados/index.html")
foreach ($file in $files) {
    if (Test-Path $file) {
        Write-Host "✅ $file encontrado" -ForegroundColor Green
    } else {
        Write-Host "❌ $file não encontrado" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "🌐 ABRINDO NETLIFY DEPLOY..." -ForegroundColor Cyan

# Abrir URLs necessárias
Start-Process "https://app.netlify.com/start"
Start-Sleep 2
Start-Process "https://github.com/cordeirotelecom/topicos-bigdata-python"

Write-Host ""
Write-Host "📋 INSTRUÇÕES AUTOMÁTICAS:" -ForegroundColor Yellow
Write-Host "1. ✅ No Netlify: Clique 'GitHub'" -ForegroundColor White
Write-Host "2. ✅ Selecione: topicos-bigdata-python" -ForegroundColor White
Write-Host "3. ✅ Branch: main" -ForegroundColor White
Write-Host "4. ✅ Build command: (deixe vazio)" -ForegroundColor White
Write-Host "5. ✅ Publish directory: ." -ForegroundColor White
Write-Host "6. ✅ Clique 'Deploy site'" -ForegroundColor White

Write-Host ""
Write-Host "🎯 LINKS DE TESTE IMEDIATOS:" -ForegroundColor Magenta
Write-Host "RawGit: https://raw.githack.com/cordeirotelecom/topicos-bigdata-python/main/site_analise_dados/index.html" -ForegroundColor Cyan
Write-Host "GitHub: https://cordeirotelecom.github.io/topicos-bigdata-python/site_analise_dados/" -ForegroundColor Cyan

Write-Host ""
Write-Host "⏱️  Deploy estimado: 2-3 minutos" -ForegroundColor Yellow
Write-Host "🎉 SEU SITE ESTARÁ ONLINE EM BREVE!" -ForegroundColor Green
