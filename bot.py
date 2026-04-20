from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8799004922:AAEBX5QkVVXvh_dDfb5MJHE31VAyjc3o1zY"
ADMIN_ID = 6695574192

# Userdan admin ga
async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text if update.message.text else "📎 media"

    username = f"@{user.username}" if user.username else "yo‘q"
    user_link = f"<a href='tg://user?id={user.id}'>Profilga o‘tish</a>"

    msg = f"""👤 <b>{user.first_name}</b>
Username: {username}
ID:{user.id}

{user_link}

💬 {text}
"""

    await context.bot.send_message(chat_id=ADMIN_ID, text=msg, parse_mode="HTML")

# Admin reply → userga
async def reply_to_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        original = update.message.reply_to_message.text

        if original and "ID:" in original:
            user_id = int(original.split("ID:")[1].split("\n")[0])

            await context.bot.send_message(
                chat_id=user_id,
                text=update.message.text
            )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.REPLY, reply_to_user))
app.add_handler(MessageHandler(filters.ALL, forward_to_admin))

print("Bot ishlayapti...")

app.run_polling()
