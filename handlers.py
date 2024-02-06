from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
import keyboards
import db


def buyurtma(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(
        text=f"{user.full_name.capitalize()} start Buyurtma 🔥",
        reply_markup=keyboards.stadions_keyboard()
    )

def stadions(update: Update, context: CallbackContext):
    item = update.callback_query.data.split(":")[1]
    update.callback_query.message.reply_text(
        text=f'Start Stadions 🔥',
        reply_markup=keyboards.item_keyboards("Stadions")
    )

def stadion(update: Update, context: CallbackContext):
    gazon, gazon_id = update.callback_query.data.split(':')[1].strip('-')
    print(gazon, gazon_id)
    gazon_data = db.get_stadion_by_id(stadion=gazon.strip(), doc_id=gazon_id.strip())
    update.callback_query.message.reply_text(
        text=f'Name: {gazon_data["name"]}\nManzil: {gazon_data["manzil"]}\nIsh vaqti: {gazon_data["ish_vaqt"]}\nTelefon nomer: {gazon_data["phone"]}\n1 soati uchun narx: {gazon_data["narx"]}',
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("❌ Close", callback_data="close")]
            ]
        )
    )
