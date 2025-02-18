from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

TOKEN = "7617668499:AAHYoP6UEBMCb9t2axjrYTXkY01Q9bHdfCE"
CHAT_ID = -2259374958  # Reemplaza con el ID de tu grupo o canal

def forward_message(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    text = update.message.text

    # Formateamos el mensaje con el nombre del usuario
    message_to_send = f"{user.first_name} dice:\n{text}"
    
    # Enviar el mensaje al grupo/canal
    context.bot.send_message(chat_id=CHAT_ID, text=message_to_send)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Manejar todos los mensajes de los usuarios
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
