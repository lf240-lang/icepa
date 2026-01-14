# icepa - Telegram Bot

Este repositório contém um esqueleto mínimo para um bot do Telegram. Você informou que já tem o comando de inicialização do bot pronto e que vai hospedar pelo Railway — este repositório traz apenas os arquivos iniciais para começar.

Arquivos incluídos:
- `README.md` (este arquivo)
- `.gitignore`
- `.env.example`

Como usar
1. Conecte este repositório ao Railway (https://railway.app) ou faça push a partir da sua máquina.
2. No Railway, defina a variável de ambiente `BOT_TOKEN` com o token do BotFather.
3. Configure o "Start Command" do Railway com o comando que você já tem (por exemplo: `npm start` ou `python bot.py`). Substitua abaixo pelo seu comando real.

Start Command (exemplo):
```
# Cole aqui o comando de inicialização que você já tem
# Ex: npm start
```

Deploy localmente
- Clone o repositório e coloque suas fontes no diretório principal.
- Crie um arquivo `.env` local com `BOT_TOKEN=seu_token`

Exemplo de variáveis no `.env`:
```
BOT_TOKEN=seu_token_aqui
```

Railway
- No Railway, clique em "New Project" → "Deploy from GitHub" e selecione `lf240-lang/icepa`.
- Nas Environment Variables, adicione `BOT_TOKEN` com o token do seu bot.
- Em "Settings" do projeto, ajuste o Start Command para o comando que você já tem.

Observações
- Este repositório NÃO inclui código do bot. Coloque seus arquivos (ex: `bot.py`, `index.js`, `package.json`) na raiz e faça push.
- Se quiser, eu posso adicionar um template em Python ou Node.js, um Dockerfile, ou um workflow do GitHub Actions para deploy automático. Diga qual opção prefere.
