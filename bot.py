import telebot

TOKEN = "8769822799:AAHV6H1BAfh-Re59VBHUsIvIRrDQejY9SsE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Bot ishlayapti ✅")

bot.polling()
