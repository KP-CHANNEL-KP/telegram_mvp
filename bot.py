from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7955233621:AAEgDL9_3FHVoSztzBMOKIqpHtaT5Ud-2O4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"မင်္ဂလာပါ {user.first_name} 👋\n"
        "ဒီ Channel ကို join လုပ်ပြီး အသစ်အသစ်တွေ ရယူပါ 🚀"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
