from telegram import Update
from telegram.ext import Application, MessageHandler, filters

TOKEN = "7617668499:AAHYoP6UEBMCb9t2axjrYTXkY01Q9bHdfCE"
CHAT_ID = -2259374958  # Reemplaza con el ID de tu grupo o canal

async def forward_message(update: Update, context) -> None:
    user = update.message.from_user
    text = update.message.text

    message_to_send = f"{user.first_name} dice:\n{text}"
    
    await context.bot.send_message(chat_id=CHAT_ID, text=message_to_send)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

    print("Bot iniciado...")
    app.run_polling()

if __name__ == '__main__':
    main()
