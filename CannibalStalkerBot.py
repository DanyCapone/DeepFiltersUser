from telegram import Update, InputMediaPhoto, InputMediaVideo, InputMediaDocument
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Función para manejar mensajes que contienen medios
def handle_media(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    media_group = update.message.media_group_id

    if media_group:
        # Si el mensaje es parte de un álbum
        media = []
        for msg in context.bot.get_media_group(chat_id, update.message.message_id):
            if msg.photo:
                media.append(InputMediaPhoto(media=msg.photo[-1].file_id))
            elif msg.video:
                media.append(InputMediaVideo(media=msg.video.file_id))
            elif msg.document:
                media.append(InputMediaDocument(media=msg.document.file_id))
        context.bot.send_media_group(chat_id=chat_id, media=media)
    else:
        # Si el mensaje es un solo archivo
        if update.message.photo:
            update.message.reply_photo(photo=update.message.photo[-1].file_id)
        elif update.message.video:
            update.message.reply_video(video=update.message.video.file_id)
        elif update.message.document:
            update.message.reply_document(document=update.message.document.file_id)

def main():
    # Reemplaza 'TU_TOKEN_AQUI' con el token que te dio BotFather
    updater = Updater("7949900927:AAFL_48jph4vPJVZULdtMOLgnpcZJ40Vf_Y", use_context=True)
    dp = updater.dispatcher

    # Manejador para mensajes que contienen medios
    dp.add_handler(MessageHandler(Filters.photo | Filters.video | Filters.document, handle_media))

    # Inicia el bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
