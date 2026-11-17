# Lucas Albuquerque — Portfolio

Portfolio estático em português, inglês e espanhol.

Endereço do GitHub Pages: https://lalbuquerque.github.io/portfolio/

## Publicação automática

Cada push na branch `main` executa `.github/workflows/deploy-pages.yml`:

1. Gera as páginas traduzidas e prepara os caminhos para `/portfolio/`.
2. Verifica a sintaxe JavaScript, a seleção de idioma e os links/arquivos locais.
3. Envia o artefato estático para GitHub Pages.

Pull requests executam a validação sem publicar. É possível republicar manualmente por **Actions → Deploy portfolio to GitHub Pages → Run workflow**.

### Ativação inicial

Em **Settings → Pages → Build and deployment → Source**, selecione **GitHub Actions**. Pages precisa estar habilitado antes do primeiro deploy. No GitHub Free, use um repositório público; um repositório privado exige um plano compatível. Não são necessários tokens pessoais ou secrets no workflow.

## Edição

- `content/index.pt.html`: conteúdo principal em português.
- `dist/app.js`: dados dos projetos, filtros e modais.
- `dist/style.css`: identidade visual e layout responsivo.
- `dist/language.js`: seleção inicial de idioma e preferência manual.
- `scripts/build_locales.py`: traduções para inglês e espanhol.
- `dist/assets/`: imagens e currículo original em inglês.

Não edite diretamente os HTMLs gerados em `dist/` nem `dist/app.en.js` e `dist/app.es.js`. Após alterar o conteúdo, execute:

```sh
python3 scripts/build_pages.py
node --test tests/*.test.cjs
python3 scripts/check_pages.py
```

O diretório `_site/` é gerado e não precisa ser versionado.

## Preview local

```sh
python3 scripts/build_locales.py
python3 -m http.server 4173 --directory dist
```

Abra http://localhost:4173/ . A primeira visita considera a preferência salva, os idiomas do navegador e, por último, inglês. As rotas `/pt/`, `/en/` e `/es/` respeitam o idioma explícito. A raiz também contém inglês como fallback sem JavaScript.

## Fontes

Informações profissionais fornecidas por Lucas em seu CV e durante a criação do portfolio. Experiência backend com Java/Spring Boot, BFF em Node.js e .NET associada à Venturus por Lucas. Fontes de imagens oficiais em `dist/assets/sources.json`. As composições ilustrativas estão identificadas no site. Contribuições GitHub verificadas em novembro de 2026.
