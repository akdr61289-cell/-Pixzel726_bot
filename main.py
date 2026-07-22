import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
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
TOKEN = "YOUR_BOT_TOKEN"


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
