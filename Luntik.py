import telebot
from telebot import types

token = '5098116058:AAGc55adHadDynJH8K6iHRX_mDQSzvAva48'
bot = telebot.TeleBot(token=token)

pictures = {
    1: "https://ibb.co/L047ttw",
    2: "https://ibb.co/7QqtkKg",
    3: "https://ibb.co/H2Hz8B3",
    4: "https://ibb.co/H7bSJz3",
    5: "https://ibb.co/3f7CYMc",
    6: "https://ibb.co/KD7DzPM",
    7: "https://ibb.co/w7DFtGZ",
    8: "https://ibb.co/JjcfWgn",
    9: "https://ibb.co/qC7H2bb",
    10: "https://ibb.co/gw0zYPx",
    11: "https://ibb.co/brrkjcF",
    12: "https://ibb.co/10g9x0J",
    13: "https://ibb.co/89vJhyb",
    14: "https://ibb.co/9VwG3Pk",
    15: "https://ibb.co/WV14kXb",
    16: "https://ibb.co/SNNTCGR",
    17: "https://ibb.co/mTkh3KX",
    18: "https://ibb.co/8P5rCZw",
    19: "https://ibb.co/b6hDgRf",
    20: "https://ibb.co/Jq8s3Fc",
    21: "https://ibb.co/jbsgHPq",
    22: "https://ibb.co/svQHQsr",
    23: "https://ibb.co/L9JmZH1",
    24: "https://ibb.co/m0J9wbF",
    25: "https://ibb.co/JFGHXBs",
    26: "https://ibb.co/b7NSzF5",
    27: "https://ibb.co/T4XdCQY",
    28: "https://ibb.co/HH9TgZK",
    29: "https://ibb.co/Htxfpd1",
    30: "https://ibb.co/RvkpjMf",
    31: "https://ibb.co/92KY2NX",
    32: "https://ibb.co/17CXbS7",
    33: "https://ibb.co/f8v250x",
    34: "https://ibb.co/n6Br11Q",
    35: "https://ibb.co/T2Yg7ZQ",
    36: "https://ibb.co/kQQR8mH",
    37: "https://ibb.co/X4Cp3T3",
    38: "https://ibb.co/F3TYqpy",
    39: "https://ibb.co/4j6mZSy",
    40: "https://ibb.co/g6WnBwW",
    41: "https://ibb.co/F6NjR21"

}

states = {}
inventories = {}
user_markup = types.ReplyKeyboardMarkup(True)


@bot.message_handler(commands=["start"])
def start_game(message):
    user = message.chat.id

    states[user] = 1
    inventories[user] = []

    process_state(user, states[user], inventories[user])


def process_state(user, state, inventory):
    kb = types.ReplyKeyboardMarkup(True)

    bot.send_photo(user, pictures[state])
    if state == 1:
        kb.add(types.KeyboardButton(text="Начать!"))

        bot.send_message(user, 'Начать!', reply_markup=kb)

    if state == 2:
        kb.add(types.KeyboardButton(text="Меня зовут..."))

        bot.send_message(user, 'Как тебя зовут?', reply_markup=kb)

    if state == 3:
        kb.add(types.KeyboardButton(text="Предложить помощь"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 4:
        kb.add(types.KeyboardButton(text="Узнать, что произошло дальше"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 5:
        kb.add(types.KeyboardButton(text="Внимательно слушать программу"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 6:
        kb.add(types.KeyboardButton(text="так-так..."))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 7:
        kb.add(types.KeyboardButton(text="..."))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 8:
        kb.add(types.KeyboardButton(text="..."))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 9:
        kb.add(types.KeyboardButton(text="Что же это могло значить?"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 10:
        kb.add(types.KeyboardButton(text="Посмотреть на реакцию родителей"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 11:
        kb.add(types.KeyboardButton(text="Рассказать всем об этой новости"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 12:
        kb.add(types.KeyboardButton(text="Рассказать Миле"))
        kb.add(types.KeyboardButton(text="Побежать к Кузе"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 13:
        kb.add(types.KeyboardButton(text="Что же думает Мила?"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 14:
        kb.add(types.KeyboardButton(text="Дать слово Лунтику"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 15:
        kb.add(types.KeyboardButton(text="Почему Мила сомневается?"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 16:
        kb.add(types.KeyboardButton(text="..."))

        bot.send_message(user, 'Лунтик удивлён:', reply_markup=kb)

    if state == 17:
        kb.add(types.KeyboardButton(text="Узнать, что такое фейк"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 18:
        kb.add(types.KeyboardButton(text="Что отвечает Кузя?"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 19:
        kb.add(types.KeyboardButton(text="..."))

        bot.send_message(user, 'Лунтик в ответ:', reply_markup=kb)

    if state == 20:
        kb.add(types.KeyboardButton(text="Почему он так смотрит?"))

        bot.send_message(user, 'Кузя осуждающе смотрит на Лунтика', reply_markup=kb)

    if state == 21:
        kb.add(types.KeyboardButton(text="..."))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 22:
        kb.add(types.KeyboardButton(text="Лунтик в недоумении"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 23:
        kb.add(types.KeyboardButton(text="Узнать, что такое фейк"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 24:
        kb.add(types.KeyboardButton(text="..."))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 25:
        kb.add(types.KeyboardButton(text="..."))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 25:
        kb.add(types.KeyboardButton(text="..."))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 26:
        kb.add(types.KeyboardButton(text="оххх"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 27:
        kb.add(types.KeyboardButton(text="..."))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 28:
        kb.add(types.KeyboardButton(text="..."))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 29:
        kb.add(types.KeyboardButton(text="..."))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 30:
        kb.add(types.KeyboardButton(text="Вперёд!"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 31:
        kb.add(types.KeyboardButton(text="Фейк"))
        kb.add(types.KeyboardButton(text="Не фейк"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 32:
        kb.add(types.KeyboardButton(text="Ещё!"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 33:
        kb.add(types.KeyboardButton(text="Ещё!"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 34:
        kb.add(types.KeyboardButton(text="Фейк"))
        kb.add(types.KeyboardButton(text="Не фейк"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 35:
        kb.add(types.KeyboardButton(text="..."))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 36:
        kb.add(types.KeyboardButton(text="..."))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 37:
        kb.add(types.KeyboardButton(text="..."))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 38:
        kb.add(types.KeyboardButton(text="Как бороться с фейками?"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 39:
        kb.add(types.KeyboardButton(text="Понятно!"))

        bot.send_message(user, '...', reply_markup=kb)

    if state == 40:
        kb.add(types.KeyboardButton(text="Урааа!"))

        bot.send_message(user, '...', reply_markup=kb)


@bot.message_handler(content_types=['text'])
def send_text(message):
    user = message.chat.id

    if states[user] == 1:
        if message.text == 'Начать!':
            states[user] = 2

    if states[user] == 2:
        if message.text == 'Меня зовут...':
            states[user] = 3

    if states[user] == 3:
        if message.text == 'Предложить помощь':
            states[user] = 4

    if states[user] == 4:
        if message.text == 'Узнать, что произошло дальше':
            states[user] = 5

    if states[user] == 5:
        if message.text == 'Внимательно слушать программу':
            states[user] = 6

    if states[user] == 6:
        if message.text == 'так-так...':
            states[user] = 7

    if states[user] == 7:
        if message.text == '...':
            states[user] = 8

    if states[user] == 8:
        if message.text == '...':
            states[user] = 9

    if states[user] == 9:
        if message.text == 'Что же это могло значить?':
            states[user] = 10

    if states[user] == 10:
        if message.text == 'Посмотреть на реакцию родителей':
            states[user] = 11

    if states[user] == 11:
        if message.text == 'Рассказать всем об этой новости':
            states[user] = 12

    if states[user] == 12:
        if message.text == 'Рассказать Миле':
            states[user] = 13
        elif message.text == 'Побежать к Кузе':
            states[user] = 18

    if states[user] == 13:
        if message.text == 'Что же думает Мила?':
            states[user] = 14

    if states[user] == 14:
        if message.text == 'Дать слово Лунтику':
            states[user] = 15

    if states[user] == 15:
        if message.text == 'Почему Мила сомневается?':
            states[user] = 16

    if states[user] == 16:
        if message.text == '...':
            states[user] = 17

    if states[user] == 17:
        if message.text == 'Узнать, что такое фейк':
            states[user] = 24

    if states[user] == 18:
        if message.text == 'Что отвечает Кузя?':
            states[user] = 19

    if states[user] == 19:
        if message.text == '...':
            states[user] = 20

    if states[user] == 20:
        if message.text == 'Почему он так смотрит?':
            states[user] = 21

    if states[user] == 21:
        if message.text == '...':
            states[user] = 22

    if states[user] == 22:
        if message.text == 'Лунтик в недоумении':
            states[user] = 23

    if states[user] == 23:
        if message.text == 'Узнать, что такое фейк':
            states[user] = 24

    if states[user] == 24:
        if message.text == '...':
            states[user] = 25

    if states[user] == 25:
        if message.text == '...':
            states[user] = 26

    if states[user] == 26:
        if message.text == 'оххх':
            states[user] = 27

    if states[user] == 27:
        if message.text == '...':
            states[user] = 28

    if states[user] == 28:
        if message.text == '...':
            states[user] = 29

    if states[user] == 29:
        if message.text == '...':
            states[user] = 30

    if states[user] == 30:
        if message.text == 'Вперёд!':
            states[user] = 31

    if states[user] == 31:
        if message.text == 'Фейк':
            states[user] = 32
        elif message.text == 'Не фейк':
            states[user] = 33

    if states[user] == 32:
        if message.text == 'Ещё!':
            states[user] = 34

    if states[user] == 33:
        if message.text == 'Ещё!':
            states[user] = 34

    if states[user] == 34:
        if message.text == 'Фейк':
            states[user] = 35
        elif message.text == 'Не фейк':
            states[user] = 36

    if states[user] == 35:
        if message.text == '...':
            states[user] = 36

    if states[user] == 36:
        if message.text == '...':
            states[user] = 37

    if states[user] == 37:
        if message.text == '...':
            states[user] = 38

    if states[user] == 38:
        if message.text == 'Как бороться с фейками?':
            states[user] = 39

    if states[user] == 39:
        if message.text == 'Понятно!':
            states[user] = 40

    if states[user] == 40:
        if message.text == 'Урааа!':
            states[user] = 1

    process_state(user, states[user], inventories[user])


bot.polling(none_stop=True)
