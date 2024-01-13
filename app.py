import telebot
from telebot import types
from konf import token
from api import get_price


bot = telebot.TeleBot(token=token)

sp = {
    'рубль':'RUR',
    'евро':'EUR',
    'доллар':'USD'
}

@bot.message_handler(commands=['start'])
def dd(message):
    massag = f"Привет {message.from_user.username}!!!\n"\
    "Для того чтобы сконвертировать валюту необходимо прислать боту сообщение в формате \n"\
    "<имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>\n"\
    "Пример: рубль доллар 100"
    
    bot.send_message(message.chat.id, massag)

@bot.message_handler(commands=['values'])
def dd(message):
    massag = "Доступные валюты для перевода евро, доллар или рубль"
    bot.send_message(message.chat.id, massag)

@bot.message_handler(commands=['help'])
def dd(message):
    massag = "Для того чтобы сконвертировать валюту необходимо прислать боту сообщение в формате \n"\
    "<имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>\n"\
    "Пример: рубль доллар 100\n"\
    "/values для просмотра возможных валют"
    bot.send_message(message.chat.id, massag)

@bot.message_handler()
def dd(message):

    k = message.text.split(' ')
    
    if(len(k) == 3):#проверка на то что как минимум передали 3 аргумента
        if(sp[k[0]] != None):
            if(sp[k[1]] != None):
                if(sp[k[0]] != sp[k[1]]):
                    if(str.isnumeric(k[2]) > 0):
                        jj = get_price(sp[k[0]],sp[k[1]],k[2])
                        if(jj):
                            s = f"Результат равен = {jj['data']['sum_result']}"
                            bot.send_message(message.chat.id, s)
                    else:
                        bot.send_message(message.chat.id,"Нобходимо ввести корректную сумму")        
                else:
                    bot.send_message(message.chat.id,"Введены две одинаковые валюты! Необходимо выбрать разные")
            else:
                bot.send_message(message.chat.id,"Неверное значение первой валюты. Доступные валюты /values")
        else:
            bot.send_message(message.chat.id,"Неверное значение первой валюты. Доступные валюты /values")
    else:
        bot.send_message(message.chat.id,"Передано неверное кол-во аргументов, более подробно в /help")
bot.polling(none_stop=True)