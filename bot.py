from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters
)
import os

# Bot token Railway environment variable থেকে নেবে
BOT_TOKEN = os.getenv("BOT_TOKEN")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "📸 I automatically generate image links in groups.\n\n"
        "➕ Add me to your group using the link below:\n"
        "https://t.me/TSfile_bot?startgroup=botstart\n\n"
        "⚠️ After adding, make me admin with:\n"
        "✅ Read messages\n"
        "✅ Send messages"
    )

# Photo handler
async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.photo:
        return

    # highest quality photo
    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)

    await update.message.reply_text(
        f"📸 Image link:\n{file.file_path}"
    )

# App setup
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Handlers (order important)
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

# Run bot
app.run_polling()
