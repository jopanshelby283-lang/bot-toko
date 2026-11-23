from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = "9243615467:AAF_RUcoIj-Px-XD3pwojXK7k1o9mV0NCpY"
ADMIN_ID = 88942177758

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Kirim bukti pembayaran foto ya!")

async def bukti(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        await update.message.reply_text("Bukti terkirim ke admin, tunggu dikonfirmasi ya!")
        try:
            await context.bot.forward_message(chat_id=ADMIN_ID, from_chat_id=update.effective_chat.id, message_id=update.message.message_id)
            await context.bot.send_message(ADMIN_ID, f"Bukti dari @{update.message.from_user.username} ID: {update.message.from_user.id}")
        except Exception as e:
            print(f"Gagal kirim ke admin: {e}")
    else:
        await update.message.reply_text("Kirim foto bukti ya!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, bukti))
print("Bot jalan...")
app.run_polling()
