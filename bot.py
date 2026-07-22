import logging
import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# ==========================
# Logging
# ==========================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ==========================
# Bot Config
# ==========================
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 7115355783

# ==========================
# Main Menu
# ==========================
def get_main_keyboard():
    keyboard = [
        [InlineKeyboardButton("🎮 PUBG Mobile Price List", callback_data="pubg")],
        [InlineKeyboardButton("💎 MLBB Diamond Price List", callback_data="mlbb")],
        [InlineKeyboardButton("🛒 Order Now", callback_data="order")],
        [InlineKeyboardButton("💳 Payment Info", callback_data="payment")],
        [InlineKeyboardButton("👨‍💻 Contact Admin", callback_data="admin")],
    ]
    return InlineKeyboardMarkup(keyboard)

# ==========================
# /start
# ==========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "👋 *မင်္ဂလာပါ!*\n\n"
        "🎮 *Bboi_PixZeL's Gameshop* မှ ကြိုဆိုပါတယ်။\n\n"
        "အောက်က Menu မှ လိုရာကို ရွေးချယ်နိုင်ပါတယ်။"
    )

    await update.message.reply_text(
        text=text,
        parse_mode="Markdown",
        reply_markup=get_main_keyboard()
    )

# ==========================
# Button Click
# ==========================
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    back = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔙 Back", callback_data="main_menu")]]
    )    if query.data == "pubg":

        text = (
            "🎮 *PUBG Mobile Price List*\n\n"

            "💎 *UC Price*\n"
            "• 60 UC - 4,614 Ks\n"
            "• 325 UC - 21,128 Ks\n"
            "• 660 UC - 41,755 Ks\n"
            "• 985 UC - 63,097 Ks\n"
            "• 1320 UC - 83,953 Ks\n"
            "• 1800 UC - 103,666 Ks\n"
            "• 2460 UC - 146,550 Ks\n"
            "• 3850 UC - 206,804 Ks\n"
            "• 5650 UC - 313,427 Ks\n"
            "• 8100 UC - 409,000 Ks\n"
            "• 11950 UC - 626,383 Ks\n"
            "• 16200 UC - 825,716 Ks"
        )

        await query.edit_message_text(
            text=text,
            parse_mode="Markdown",
            reply_markup=back
        )

    elif query.data == "mlbb":

        text = (
            "💎 *MLBB Diamond Price List*\n\n"

            "• Weekly Pass - 6,750 Ks\n"
            "• Twilight Pass - 35,000 Ks\n"
            "• WEB Bundle - 3,400 Ks\n"
            "• MEB Bundle - 16,800 Ks\n\n"

            "💠 *Diamond*\n"
            "• 11 Dia - 900 Ks\n"
            "• 22 Dia - 1,850 Ks\n"
            "• 56 Dia - 4,000 Ks\n"
            "• 86 Dia - 5,800 Ks\n"
            "• 172 Dia - 11,000 Ks\n"
            "• 257 Dia - 16,000 Ks\n"
            "• 429 Dia - 27,000 Ks\n"
            "• 514 Dia - 32,500 Ks\n"
            "• 600 Dia - 38,000 Ks\n"
            "• 706 Dia - 42,500 Ks\n"
            "• 878 Dia - 53,500 Ks\n"
            "• 963 Dia - 59,000 Ks\n"
            "• 1049 Dia - 65,000 Ks\n"
            "• 1135 Dia - 70,000 Ks\n"
            "• 1412 Dia - 86,000 Ks\n"
            "• 5532 Dia - 326,000 Ks\n"
            "• 9288 Dia - 542,000 Ks"
        )

        await query.edit_message_text(
            text=text,
            parse_mode="Markdown",
            reply_markup=back
        )

    elif query.data == "payment":

        await query.edit_message_text(
            text=(
                "💳 *Payment Information*\n\n"
                "📱 KPay - 09665528930\n"
                "👤 Name - Aung Khant Kyaw"
            ),
            parse_mode="Markdown",
            reply_markup=back
        )

    elif query.data == "admin":

        await query.edit_message_text(
            text=(
                "👨‍💻 *Contact Admin*\n\n"
                "Telegram - @pixel7k"
            ),
            parse_mode="Markdown",
            reply_markup=back
        )elif query.data == "order":

    context.user_data["step"] = "game"

    await query.edit_message_text(
        "🛒 *Order Form*\n\n"
        "🎮 PUBG / MLBB ဘယ် Game ဝယ်ချင်လဲ?\n\n"
        "ဥပမာ - PUBG",
        parse_mode="Markdown"
    )async def order_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if "step" not in context.user_data:
        return

    step = context.user_data["step"]
    text = update.message.text

    if step == "game":
        context.user_data["game"] = text
        context.user_data["step"] = "package"

        await update.message.reply_text(
            "💎 ဘယ် Package ဝယ်ချင်လဲ?\n\nဥပမာ - 660 UC"
        )

    elif step == "package":
        context.user_data["package"] = text
        context.user_data["step"] = "gameid"

        await update.message.reply_text(
            "🆔 Game ID နဲ့ Server ID ပို့ပါ။"
        )    elif step == "gameid":
        context.user_data["gameid"] = text
        context.user_data["step"] = "screenshot"

        await update.message.reply_text(
            "📸 KPay Screenshot ကို အခုပို့ပေးပါ။"
        )

    elif step == "screenshot":
        await update.message.reply_text(
            "❌ Screenshot ကို Photo အဖြစ်ပို့ပါ။"
        )


async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if context.user_data.get("step") != "screenshot":
        return

    photo = update.message.photo[-1].file_id

    game = context.user_data["game"]
    package = context.user_data["package"]
    gameid = context.user_data["gameid"]

    caption = (
        "🛒 New Order\n\n"
        f"🎮 Game : {game}\n"
        f"💎 Package : {package}\n"
        f"🆔 Game ID : {gameid}\n\n"
        f"👤 Customer : @{update.effective_user.username}"
    )

    await context.bot.send_photo(
        chat_id=ADMIN_ID,
        photo=photo,
        caption=caption
    )

    await update.message.reply_text(
        "✅ Order လက်ခံပြီးပါပြီ။\nAdmin က မကြာခင် ဆက်သွယ်ပေးပါမယ်။"
    )

    context.user_data.clear()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, order_message))
app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

print("Bot is running...")

app.run_polling()
