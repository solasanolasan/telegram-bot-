import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

nest_asyncio.apply()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salom! Men ishga tushdim! 🚀')

app = ApplicationBuilder().token("7929322570:AAHnuhDbWusPxMITk_lOFVVUGWZhW_WR71A").build()
app.add_handler(CommandHandler("start", start))

print("Bot ishga tushdi...")
asyncio.run(app.run_polling())
