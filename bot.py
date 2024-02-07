from flask import Flask, request
from telegram import Bot
from config import get_token
import keyboards
import db

app = Flask(__name__)
TOKEN = get_token()
bot = Bot(TOKEN)
url = "https://xakimov.pythonanywhere.com/"

def start(user: str):
    bot.send_message(
        chat_id = user['id'],
        text=f'Assalomu aleykum {user["first_name"].capitalize()}.\nBu bot sizga Samarqand shaharidagi stadionlar haqida ma\'lumot olishingiz mumkin.',
        reply_markup=keyboards.home_keyboard()
    )

@app.route('/', methods=["POST"])
def main():
    data = request.get_json()
    user = data['message']['chat']
    if data['message'].get('text')!=None:
        if data['message']['text'] == '/start' or data['message']['text']=="Bosh sahifa 🏠" :
            start(user)
        elif data['message']['text']=="Stadions ⚽️" or data['message']['text']=="❌ Close":
            bot.send_message(
                chat_id = user['id'],
                text = f'Start Stadions 🔥',
                reply_markup=keyboards.item_keyboards("Stadions")
            )
        else:
            text = data['message']['text']
            gazon_data = db.get_stadion_malumot(text)[0]
            if gazon_data!=[]:
                bot.send_message(
                    chat_id=user['id'],
                    text=f'👤 Name: {gazon_data["name"]}\n📍 Manzil: {gazon_data["manzil"]}\n⏰ Ish vaqti: {gazon_data["ish_vaqt"]}\n📲 Telefon nomer: {gazon_data["phone"]}\n💰 1 soati uchun narx: {gazon_data["narx"]}',
                    reply_markup=keyboards.close
                )
                bot.send_location(
                    chat_id=user['id'],
                    latitude = gazon_data['location']['latitude'],
                    longitude = gazon_data['location']['longitude'],
                )
            else:
                bot.send_message(chat_id=user['id'], text = "Ikkinchi ")
            
    else:
        bot.send_message(chat_id=user['id'], text = "Birinchi ")

    return "Hello programmer"

if __name__=="__main__":
    app.run(debug=True)
