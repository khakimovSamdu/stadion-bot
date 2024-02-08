from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import db
def home_keyboard():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton('Stadions ⚽️')],
            [KeyboardButton('ℹ️ About'), KeyboardButton("☎️Contact")]
        ],
        resize_keyboard=True
    )
def stadions_keyboard():
    keyboards_btns = []
    row = []
    for item in db.get_stadions():
        row.append(InlineKeyboardButton(item, callback_data=f'item:{item}'))
        if len(row) == 2:
            keyboards_btns.append(row)
            row = []
    if row:
        keyboards_btns.append(row)
    return InlineKeyboardMarkup(keyboards_btns)

def item_keyboards(item: str):
    stadions = db.get_stadion_by_item(item)
    keyboards_btns = []
    bosh_menu = ["Bosh sahifa 🏠"]
    for item in stadions:
        keyboards_btns.append([KeyboardButton(item['manzil'], resize_keyboard = True)])
    keyboards_btns.append(bosh_menu)
    return ReplyKeyboardMarkup(keyboards_btns)

close =ReplyKeyboardMarkup(
            [
                [KeyboardButton(text="❌ Close")]
            ],
            resize_keyboard=True
        )

replay_izoh = ReplyKeyboardMarkup(
    [
        [KeyboardButton("☺️Menga hamma narsa yoqdi, 5❤️")],
        [KeyboardButton("☺️Yaxshi, 4⭐️⭐️⭐️⭐️")],
        [KeyboardButton("🙂Qoniqarli, 3⭐️⭐️⭐️")],
        [KeyboardButton("☹️Yoqmadi, 2⭐️⭐️")],
        [KeyboardButton("😤Men shikoyat qilmoqchiman👎🏻")],
        [KeyboardButton("Bosh sahifa 🏠")],
    ],
    resize_keyboard=True
)
