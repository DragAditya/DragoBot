from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '6094405994:AAH4OfeICj14Og9qzE9Lrnz9Bbt9QBH5g6A'
ADMIN_ID = '1183272367'

# Define modes
REGULAR_MODE = 0
AI_MODE = 1
CHATTING_MODE = 2

# Initial mode is regular mode
current_mode = REGULAR_MODE

def start(update: Update, context: CallbackContext) -> None:
    user_name = update.message.from_user.username
    update.message.reply_text(f'Hello, {user_name}! I am your Telegram bot.')

def admin_command(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.from_user.id)
    if user_id == ADMIN_ID:
        update.message.reply_text('You are the admin! You have superior access.')
    else:
        update.message.reply_text('You do not have admin access.')

def mode_command(update: Update, context: CallbackContext) -> None:
    global current_mode
    user_id = str(update.message.from_user.id)
    if user_id == ADMIN_ID:
        args = context.args
        if args:
            mode = args[0].lower()
            if mode == 'regular':
                current_mode = REGULAR_MODE
                update.message.reply_text('Switched to Regular Mode.')
            elif mode == 'ai':
                current_mode = AI_MODE
                update.message.reply_text('Switched to AI Mode.')
            elif mode == 'chatting':
                current_mode = CHATTING_MODE
                update.message.reply_text('Switched to Chatting Mode.')
            else:
                update.message.reply_text('Invalid mode. Available modes: Regular, Ai, Chatting.')
        else:
            update.message.reply_text('Please provide a mode. Available modes: Regular, Ai, Chatting.')
    else:
        update.message.reply_text('You do not have admin access.')

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("admin", admin_command))
    dp.add_handler(CommandHandler("mode", mode_command, pass_args=True))

    print("Bot is running! Press Ctrl+C to stop.")
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
