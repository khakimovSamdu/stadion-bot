from flask import Flask, request
from telegram import Bot
import db
from config import get_token
import keyboards

app = Flask(__name__)
TOKEN = get_token()
bot = Bot(TOKEN)

def start(user: str):
    bot.send_message(
        chat_id = user['id'],
        text=f'Assalomu aleykum {user["id"].capitalize()}.\nBu bot sizga Samarqand shaharidagi stadionlar haqida ma\'lumot olishingiz mumkin.',
        reply_markup=keyboards.home_keyboard()
    )

@app.route('/', methods=["POST"])
def main():
    data = request.get_json()
    user = data['message']['chat']
    if data['message'].get('text')!=None:
        if data['message']['text'] == '/start':
            start(user)
        elif data['message']['text']=="Stadions ⚽️":
            bot.send_message(
                chat_id = user['id'],
                text = f'Start Stadions 🔥',
                reply_markup=keyboards.item_keyboards("Stadions")
            )
        else:
            bot.send_message(chat_id=user['id'], text = "Ikkinchi ")
    else:
        bot.send_message(chat_id=user['id'], text = "Birinchi ")

    return "Hello programmer"
if __name__=="__main__":
    app.run(debug=True)
