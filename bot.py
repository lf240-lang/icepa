import telebot

# ================= CONFIGURAÇÕES =================

TOKEN = 8584614253:AAHtzkk0VoxqwzoBjh4ByROecLrAxLpv0wI
GRUPO_ATENDIMENTO_ID = 5190305964  # ID do grupo privado

bot = telebot.TeleBot(TOKEN)

# ================= /START =================

@bot.message_handler(commands=['start'])
def start(message):
    texto = (
        "✨ Bem-vindo(a) ✨\n\n"
        "📸 Valores:\n"
        "• R$ 0,50 por Mídia\n"
        "👉 Envie agora o *nome do conteúdo*."
    )
    bot.send_message(
        message.chat.id,
        texto,
        parse_mode="Markdown"
    )

# ================= MENSAGEM DO CLIENTE =================

@bot.message_handler(func=lambda m: m.chat.type == "private")
def receber_cliente(message):
    texto_grupo = (
        "📩 NOVO CLIENTE\n\n"
        f"👤 Usuário: @{message.from_user.username}\n"
        f"🆔 ID: {message.chat.id}\n"
        f"💬 Mensagem: {message.text}"
    )

    # Envia mensagem para o grupo de atendimento
    bot.send_message(GRUPO_ATENDIMENTO_ID, texto_grupo)

    # Confirma para o cliente
    bot.send_message(
        message.chat.id,
        "✔️ Recebi sua mensagem.\nAguarde o retorno ⏳"
    )

# ================= RESPOSTA NO GRUPO (RELAY) =================

@bot.message_handler(
    func=lambda m: m.chat.id == GRUPO_ATENDIMENTO_ID and m.reply_to_message
)
def responder_cliente(message):
    texto_original = message.reply_to_message.text

    if "🆔 ID:" not in texto_original:
        return

    try:
        cliente_id = int(
            texto_original.split("🆔 ID:")[1].split("\n")[0].strip()
        )
    except:
        return

    # Envia sua resposta para o cliente
    bot.send_message(cliente_id, message.text)

# ================= BOT EM EXECUÇÃO =================

bot.polling()
