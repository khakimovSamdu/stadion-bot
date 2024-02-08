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
        elif data['message']['text']=="ℹ️ About":
            bot.send_message(
                chat_id=user['id'],
                text = """"
                ✅ Stadions loyihasini tanlaganingiz uchun rahmat.
Bizning xizmatlarimiz sifatini yaxshilashga yordam bersangiz juda xursand bo’lar edik :)
Buning uchun 5 ballik tizim asosida bizni baholang yoki o'z tilaklaringizni yozib jo'nating.
""",
                reply_markup=keyboards.replay_izoh
            )
        elif data['message']['text']=="☺️Menga hamma narsa yoqdi, 5❤️":
            bot.send_message(
                chat_id = user['id'],
                text = """Mamnun qolganingizdan xursandmiz 😊. Siz va yaqinlaringizni har doim xursand qilishga harakat qilamiz 🤗""",
                reply_markup=keyboards.home_keyboard()
            )
        elif data['message']['text'] == "☺️Yaxshi, 4⭐️⭐️⭐️⭐️":
            bot.send_message(
                chat_id=user['id'],
                text = """Sizga yoqqanidan xursandmiz 😊. Bot ishlashini yaxshilash uchun qanday maslahatlaringiz bor?👇🏻""",
                reply_markup=keyboards.home_keyboard()
            )
        elif data['message']['text'] == "🙂Qoniqarli, 3⭐️⭐️⭐️":
            bot.send_message(
                chat_id=user['id'],
                text="""Botimiz sizni qoniqtirmaganidan afsusdamiz 😔. 
Bizni yaxshilashga yordam bering, 
sharh va takliflaringizni qoldiring👇🏻. 
Yaxshilashga harakat qilamiz🙏🏻.""",
                reply_markup=keyboards.home_keyboard()
            )
        elif data['message']['text']== "☹️Yoqmadi, 2⭐️⭐️":
            bot.send_message(
                chat_id=user['id'],
                text="""Botimiz sizni qoniqtirmaganidan afsusdamiz 😔. Bizni yaxshilashga yordam bering, sharh va takliflaringizni qoldiring👇🏻. Yaxshilashga harakat qilamiz🙏🏻""",
                reply_markup=keyboards.home_keyboard()
            )
        elif data['message']['text']=="😤Men shikoyat qilmoqchiman👎🏻":
            bot.send_message(
                chat_id=user['id'],
                text="""Botimiz sizni qoniqtirmaganidan afsusdamiz 😔. Bizni yaxshilashga yordam bering, sharh va takliflaringizni qoldiring👇🏻. Yaxshilashga harakat qilamiz🙏🏻""",
                reply_markup=keyboards.home_keyboard()
            )
        elif data['message']['text']=="☎️Contact":
            bot.send_contact(chat_id=user['id'], phone_number="+998938554640", first_name="Allamurod")
        else:
            text = data['message']['text']
            try:
                gazon_data = db.get_stadion_malumot(text)[0]
                print(gazon_data)
                if gazon_data!=[]:
                    bot.send_message(
                        chat_id=user['id'],
                        text=f'📍 Manzil: {gazon_data["manzil"]}\n⏰ Ish vaqti: {gazon_data["ish_vaqt"]}\n💰 1 soati uchun narx: {gazon_data["narx"]}\n📲 Telefon nomer: {gazon_data["phone"]}',
                        reply_markup=keyboards.close
                    )
                    bot.send_location(
                        chat_id=user['id'],
                        latitude = gazon_data['location']['latitude'],
                        longitude = gazon_data['location']['longitude'],
                    )
            except:
                    bot.send_message(chat_id=user['id'], text = f"Kechirasiz {user['first_name']} siz gazon nomini xato kiritdingiz. Iltimos so'rovlarni to'gri kiriting. Tushinish uchun quyi qismidagi keyboardlardan foydalaning 🔥")      
    else:
        bot.send_message(chat_id=user['id'], text = f"Kechirasiz {user['first_name']} siz text yubormadingiz. Iltimos so'rovlarni to'gri kiriting. Tushinish uchun quyi qismidagi keyboardlardan foydalaning 🔥")

    return "Hello programmer"

if __name__=="__main__":
    app.run(debug=True)
