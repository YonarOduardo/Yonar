import telebot

bot = telebot.TeleBot("5245520800:AAHX_-CrokrwGb1oot5I_R8GQjAvMnn43oc", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hola, yonar cómo estás?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()