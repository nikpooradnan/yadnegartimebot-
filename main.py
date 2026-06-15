from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "توکن_ربات_تو_اینجا"

def start(update, context):
    update.message.reply_text("ربات فعال شد!")

def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()
