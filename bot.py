import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
from telegram.ext import MessageHandler, filters
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ==========================
# Logging
# ==========================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ==========================
# BOT TOKEN
# (နောက်ပိုင်း Render မှာ Environment Variable သုံးပါမယ်)
# ==========================
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 7115355783

# ==========================
# Main Menu
# ==========================
def get_main_keyboard():

    keyboard = [
        [
            InlineKeyboardButton(
                "🎮 PUBG Mobile Price List",
                callback_data="pubg"
            )
        ],
        [
            InlineKeyboardButton(
                "💎 MLBB Diamond Price List",
                callback_data="mlbb"
            )
        ],
        [
            InlineKeyboardButton(
                "🛒 Order Now",
                callback_data="order"
            )
        ],
        [
            InlineKeyboardButton(
                "💳 Payment Info",
                callback_data="payment"
            )
        ],
        [
            InlineKeyboardButton(
                "👨‍💻 Contact Admin",
                callback_data="admin"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


# ==========================
# Start Command
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
        [
            [
                InlineKeyboardButton(
                    "🔙 Back",
                    callback_data="main_menu"
                )
            ]
        ]
    )

# Part 2 မှာ ဒီနေရာကနေ PUBG / MLBB / Order / Payment / Admin ကို ဆက်ထည့်မယ်
    if query.data == "pubg":

        text = (
            "🎮 *PUBG Mobile Price List (MMK)*\n\n"
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
            "• 56 Dia - 4,000 Ks\n"
            "• 172 Dia - 11,000 Ks\n"
            "• 257 Dia - 16,000 Ks\n"
            "• 429 Dia - 27,000 Ks\n"
            "• 514 Dia - 32,500 Ks\n"
            "• 878 Dia - 53,500 Ks\n"
            "• 1412 Dia - 86,000 Ks\n"
            "• 5532 Dia - 326,000 Ks\n"
            "• 9288 Dia - 542,000 Ks"
        )

        await query.edit_message_text(
            text=text,
            parse_mode="Markdown",
            reply_markup=back
        )


    elif query.data == "order":

        text = (
            "🛒 *Order ပြုလုပ်နည်း*\n\n"
            "1. PUBG / MLBB Item ရွေးပါ\n"
            "2. Game ID & Server ID ပို့ပါ\n"
            "3. Payment ပြီး Screenshot ပို့ပါ\n"
            "4. Admin ထံ Order တင်ပါ"
        )

        await query.edit_message_text(
            text=text,
            parse_mode="Markdown",
            reply_markup=back
        )


    elif query.data == "payment":

        text = (
            "💳 *Payment Info*\n\n"
            "KPay 📱\n"
            "09665528930\n\n"
            "Name - AungKhantkyaw"
        )

        await query.edit_message_text(
            text=text,
            parse_mode="Markdown",
            reply_markup=back
        )


    elif query.data == "admin":

        text = (
            "👨‍💻 *Contact Admin*\n\n"
            "Order တင်ရန် ဆက်သွယ်ပါ👇\n"
            "@pixel7k"
        )

        await query.edit_message_text(
            text=text,
            parse_mode="Markdown",
            reply_markup=back
        )


    elif query.data == "main_menu":

        await query.edit_message_text(
            text="🎮 *Bboi_PixZeL's Gameshop*",
parse_mode="Markdown",
            reply_markup=get_main_keyboard()
        )


# ==========================
# Run Bot
# ==========================
if __name__ == "__main__":

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("Bot is running...")

    app.run_polling()


