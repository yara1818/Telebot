import lambada
import telebot
import open_weather_data

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def print_message(message):
    bot.send_message(message.chat.id, 'Напишите название города:')
    bot.register_next_step_handler(message, get_weather)

@bot.message_handler(func=lambda message: True)
def get_weather(message):
    keyword_city = telebot.types.ReplyKeyboardMarkup(True)
    keyword_city.row(message.text)
    weather_data = open_weather_data.get_open_weather_one_day(message.text)

    if weather_data == 'Напишите название пункта правильно':
        bot.send_message(message.chat.id, weather_data)
    else:
        bot.send_message(message.chat.id, weather_data, reply_markup=keyword_city)
        bot.register_next_step_handler(message, get_weather)


bot.polling(none_stop=True, interval=0)
