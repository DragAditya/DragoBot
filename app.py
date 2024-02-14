import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = os.environ.get('TOKEN')  # Retrieve the bot token from environment variables

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

def main() -> None:
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
