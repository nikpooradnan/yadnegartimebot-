import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("TOKEN")

async def start(update, context):
    await update.message.reply_text("ربات فعال شد!")

async def echo(update, context):
    await update.message.reply_text(update.message.text)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, echo))

    app.run_polling()

if __name__ == "__main__":
    main()
