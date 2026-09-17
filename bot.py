import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🎓 RUHS", callback_data="ruhs"),
            InlineKeyboardButton("🏥 MMU", callback_data="mmu"),
        ],
        [
            InlineKeyboardButton("📋 Counselling", callback_data="counselling"),
            InlineKeyboardButton("📊 Results", callback_data="results"),
        ],
        [
            InlineKeyboardButton("📝 MCQ", callback_data="mcq"),
            InlineKeyboardButton("📚 Study Material", callback_data="study"),
        ],
        [
            InlineKeyboardButton("💬 Contact Us", callback_data="contact"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome to RUHS WALLAH Bot!\n\n"
        "🎓 RUHS | MMU | AIIMS\n"
        "📝 Exams | Admissions | Counselling | Results\n\n"
        "👇 Choose an option:",
        reply_markup=reply_markup
    )
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 RUHS WALLAH Bot Help\n\n"
        "🎓 /ruhs - RUHS Updates\n"
        "🏥 /mmu - MMU Updates\n"
        "📋 /counselling - Counselling Updates\n"
        "📊 /results - Results & Answer Keys\n"
        "📝 /mcq - Practice MCQs\n"
        "📚 /study - Study Material\n"
        "💬 /contact - Contact RUHS WALLAH"
    )
async def ruhs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎓 RUHS UPDATES\n\n"
        "📢 RUHS CUET\n"
        "📝 Exams & Admissions\n"
        "📋 Counselling & Allotment\n"
        "📊 Results & Answer Keys\n\n"
        "Latest updates ke liye RUHS WALLAH ko follow karein."
    )
async def mmu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏥 MMU UPDATES\n\n"
        "📢 MMU ET\n"
        "📝 Exams & Admissions\n"
        "📋 Counselling & Allotment\n"
        "📊 Results & Answer Keys\n\n"
        "Latest MMU updates ke liye RUHS WALLAH ko follow karein."
    )
async def counselling_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 COUNSELLING UPDATES\n\n"
        "🎓 RUHS Counselling\n"
        "🏥 MMU Counselling\n"
        "📅 Schedule & Dates\n"
        "📢 Registration & Allotment\n\n"
        "Latest counselling updates ke liye RUHS WALLAH ko follow karein."
    )
async def results_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 RESULTS & ANSWER KEYS\n\n"
        "🎓 RUHS Results\n"
        "🏥 MMU Results\n"
        "📝 Answer Keys\n"
        "📄 Result Updates\n\n"
        "Latest updates ke liye RUHS WALLAH ko follow karein."
    )
async def mcq_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📝 MCQ PRACTICE\n\n"
        "🎓 RUHS CUET\n"
        "🏥 MMU ET\n"
        "💊 Pharmacy\n"
        "🩺 Nursing\n"
        "🔬 Paramedical\n\n"
        "Practice MCQs ke liye category choose karein."
    )
async def study_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 STUDY MATERIAL\n\n"
        "🎓 RUHS CUET\n"
        "🏥 MMU ET\n"
        "🩺 Nursing\n"
        "💊 Pharmacy\n"
        "🔬 Paramedical\n\n"
        "Study material category choose karein."
    )
async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💬 CONTACT RUHS WALLAH\n\n"
        "📢 Instagram: @ruhs_wallah\n"
        "📲 Telegram: @ruhswallah\n"
        "📧 Email: ruhswallah@gmail.com\n"
        "🟢 WhatsApp: +919509893335\n\n"
        "Apni query ke liye hume message karein."
    )
RUHS_FILES = {
    "syllabus": "BQACAgUAAxkBAAM0aqp1e3BYlldX6tUbNIfv_syU04UAAh4kAAKOBlFVhR6kcmQG6AABPQQ"
}
async def ruhs_cuet_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📚 Syllabus", callback_data="ruhs_syllabus"),
        ],
        [
            InlineKeyboardButton("📋 Counselling", callback_data="ruhs_cuet_counselling"),
            InlineKeyboardButton("📊 Results", callback_data="ruhs_cuet_results"),
        ],
        [
            InlineKeyboardButton("🔑 Answer Key", callback_data="ruhs_cuet_answer"),
        ],
        [
            InlineKeyboardButton("🔙 RUHS Menu", callback_data="ruhs"),
        ],
    ]

    await update.callback_query.message.reply_text(
        "📝 RUHS CUET\n\n"
        "RUHS CUET se related information ke liye option select karein 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
async def ruhs_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📰 Latest Updates", callback_data="ruhs_latest"),
        ],
        [
            InlineKeyboardButton("📝 RUHS CUET", callback_data="ruhs_cuet"),
            InlineKeyboardButton("📋 Counselling", callback_data="ruhs_counselling"),
        ],
        [
            InlineKeyboardButton("📊 Results", callback_data="ruhs_results"),
            InlineKeyboardButton("🔑 Answer Key", callback_data="ruhs_answer"),
        ],
        [
            InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu"),
        ],
    ]

    await update.callback_query.message.reply_text(
        "🎓 RUHS MENU\n\n"
        "RUHS se related information ke liye option select karein 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
async def document_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document
    file_id = document.file_id

    await update.message.reply_text(
        f"✅ File received!\n\n"
        f"📄 Name: {document.file_name}\n"
        f"🆔 File ID:\n`{file_id}`",
        parse_mode="Markdown"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("ruhs", ruhs_command))
app.add_handler(CommandHandler("mmu", mmu_command))
app.add_handler(CommandHandler("counselling", counselling_command))
app.add_handler(CommandHandler("results", results_command))
app.add_handler(CommandHandler("mcq", mcq_command))
app.add_handler(CommandHandler("study", study_command))
app.add_handler(CommandHandler("contact", contact_command))
app.add_handler(MessageHandler(filters.Document.PDF, document_handler))
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "ruhs":
        await ruhs_menu(update, context)
        return

    elif query.data == "ruhs_cuet":
        await ruhs_cuet_menu(update, context)
        return
    elif query.data == "ruhs_syllabus":
        await query.message.reply_document(
        document=RUHS_FILES["syllabus"],
        caption="📚 RUHS CUET Syllabus\n\n🎓 RUHS WALLAH"
    )
        return
    elif query.data == "mmu":
        text = (
            "🏥 MMU UPDATES\n\n"
            "📢 MMU ET\n"
            "📝 Exams & Admissions\n"
            "📋 Counselling & Allotment\n"
            "📊 Results & Answer Keys"
        )

    elif query.data == "counselling":
        text = (
            "📋 COUNSELLING UPDATES\n\n"
            "🎓 RUHS Counselling\n"
            "🏥 MMU Counselling\n"
            "📅 Schedule & Dates\n"
            "📢 Registration & Allotment"
        )

    elif query.data == "results":
        text = (
            "📊 RESULTS & ANSWER KEYS\n\n"
            "🎓 RUHS Results\n"
            "🏥 MMU Results\n"
            "📝 Answer Keys"
        )

    elif query.data == "mcq":
        text = (
            "📝 MCQ PRACTICE\n\n"
            "🎓 RUHS CUET\n"
            "🏥 MMU ET\n"
            "💊 Pharmacy\n"
            "🩺 Nursing\n"
            "🔬 Paramedical"
        )

    elif query.data == "study":
        text = (
            "📚 STUDY MATERIAL\n\n"
            "🎓 RUHS CUET\n"
            "🏥 MMU ET\n"
            "🩺 Nursing\n"
            "💊 Pharmacy\n"
            "🔬 Paramedical"
        )

    elif query.data == "contact":
        text = (
            "💬 CONTACT RUHS WALLAH\n\n"
            "📢 Instagram: @ruhs_wallah\n"
            "📲 Telegram: @ruhswallah\n"
            "📧 Email: ruhswallah@gmail.com\n"
            "🟢 WhatsApp: +919509893335"
        )

    else:
        text = "❌ Invalid option."

    await query.message.reply_text(text)
app.add_handler(CallbackQueryHandler(button_handler))

print("🤖 RUHS WALLAH Bot is running...")

app.run_polling()
