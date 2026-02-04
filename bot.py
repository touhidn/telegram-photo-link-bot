from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.photo:
        return

    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    file_url = file.file_path

    await update.message.reply_text(
        f"📸 Image link:\n{file_url}"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.PHOTO, photo_handler))
app.run_polling()
