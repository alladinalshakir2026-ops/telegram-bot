import telebot

TOKEN = "8769822799:AAHZFBsAo-0-iYCqcrY0fd_Y7T8fSZp8-bQ"
ADMIN_ID = 7781703083

bot = telebot.TeleBot(TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Assalomu alaykum!\nIsmingizni kiriting:")
    user_data[message.chat.id] = {}

@bot.message_handler(func=lambda message: True)
def handle(message):
    chat_id = message.chat.id

    if 'name' not in user_data[chat_id]:
        user_data[chat_id]['name'] = message.text
        bot.send_message(chat_id, "Telefon raqamingizni kiriting:")
    
    elif 'phone' not in user_data[chat_id]:
        user_data[chat_id]['phone'] = message.text
        bot.send_message(chat_id, "Muammoingizni yozing:")
    
    elif 'problem' not in user_data[chat_id]:
        user_data[chat_id]['problem'] = message.text

        text = f"📩 Yangi murojaat:\n\n👤 Ism: {user_data[chat_id]['name']}\n📞 Tel: {user_data[chat_id]['phone']}\n📝 Muammo: {user_data[chat_id]['problem']}"

        bot.send_message(ADMIN_ID, text)
        bot.send_message(chat_id, "✅ Murojaatingiz yuborildi!")

        user_data.pop(chat_id)

bot.polling()
