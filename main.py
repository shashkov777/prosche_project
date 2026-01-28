import telebot
from telebot import types 

import sqlite3

drinks = {
    # напитки
    'americano': {'name': 'Американо', 'desc': 'Классический чёрный кофе', 'photo': './photo.jpg'},
    'espresso': {'name': 'Эспрессо', 'desc': 'Насыщенный вкус', 'photo': './photo.jpg'},
    'filter_coffee': {'name': 'Фильтр-кофе', 'desc': 'Классический фильтр', 'photo': './photo.jpg'},
    'cappuccino': {'name': 'Капучино', 'desc': 'С молочной пеной', 'photo': './photo.jpg'},
    'latte': {'name': 'Латте', 'desc': 'Нежный и сливочный', 'photo': './photo.jpg'},
    'flat_white': {'name': 'Флэт Уайт', 'desc': 'Микровспенка молока', 'photo': './photo.jpg'},
    'raf_coffee': {'name': 'Раф', 'desc': 'Эспрессо с сливками', 'photo': './photo.jpg'},
    'matcha': {'name': 'Матча', 'desc': 'Зелёный чай', 'photo': './photo.jpg'},
    'cocoa': {'name': 'Какао', 'desc': 'Горячее какао', 'photo': './photo.jpg'},
}

food = {
    # едаfood = {
    'chocolate_cherry_babka': {'name': 'Бабка с шоколадом и вишней', 'desc': 'Сладкая выпечка с шоколадом и вишней', 'price': '100₽', 'photo': './photo2.jpg'},
    'meat_sandwich': {'name': 'Сэндвич с мясом', 'desc': 'Сытный мясной сэндвич','price': '100₽', 'photo': './photo2.jpg'},
    'salted_caramel_croissant': {'name': 'Краффин с соленой карамелью', 'desc': 'Хрустящий краффин с карамелью', 'price': '100₽', 'photo': './photo2.jpg'},
    'canele': {'name': 'Канеле', 'desc': 'Французская выпечка с ромом', 'price': '100₽', 'photo': './photo2.jpg'},
    'rye_danish_with_cheese': {'name': 'Ржаной даниш с брынзой', 'desc': 'Даниш с ржаной мукой и сыром', 'price': '100₽', 'photo': './photo2.jpg'},
    'cheese_croissant': {'name': 'Круассан с сыром', 'desc': 'Классический круассан с плавленым сыром', 'price': '100₽', 'photo': './photo2.jpg'},
    'chocolate_pan': {'name': 'Пан шоколя', 'desc': 'Мягкая булочка с шоколадом', 'price': '100₽', 'photo': './photo2.jpg'},

}


bot = telebot.TeleBot("8573939809:AAE-sW3ZzmUVpCPX-axSO6ryeoyQFWkXaEM")

name = None

@bot.message_handler(commands=['start'])
def start(message):

    conn = sqlite3.connect('userfile.sql')
    cur = conn.cursor() 

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            password TEXT
        )
    """)

    conn.commit()  
    cur.close()  
    conn.close()

    bot.send_message(message.chat.id, "Здравствуйте. Это бот проще. Давайте знакомится. Введите ваше имя: ")
    bot.register_next_step_handler(message, main_menu)

def main_menu(message):
    global name
    name = message.text.strip()

    # register user
    conn = sqlite3.connect('userfile.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name) VALUES ('%s')" % (name))
    conn.commit() 
    cur.close()
    conn.close()


    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton("ЛЕНПОЛИГРАФМАШ", url='https://yandex.ru/maps/org/proshche/211188027241/?ll=30.317764%2C59.968660&utm_source=share&z=16'))
    markup.add(types.InlineKeyboardButton("У КАРАНДАША", url='https://yandex.ru/maps/org/proshche/216836401698/?ll=30.334473%2C59.983504&utm_source=share&z=16')) 
    markup.add(types.InlineKeyboardButton("ПОСМОТРЕТЬ НАШЕ МЕНЮ", callback_data='showmenu'))
    markup.add(types.InlineKeyboardButton("TELEGRAM", url='https://t.me/+ZrS7-0eYuDYwNDMy'))
    markup.add(types.InlineKeyboardButton("INSTAGRAM", url='https://www.instagram.com/proschee__?igsh=MTF4NjdjZ2lzMjQ4MA=='))
    markup.add(types.InlineKeyboardButton("ГРУППА ВКОНТАКТЕ", url='https://vk.com/proshecoffee'))
    markup.add(types.InlineKeyboardButton("ПЛЕЙСЛИСТ ПРОЩЕ", url='https://music.yandex.ru/playlists/e3a190f8-1952-6064-b9b6-8e5da157bcc0?utm_medium=copy_link'))
 
    bot.send_message(message.chat.id, f"Приятно познакомиться, {name}", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'showmenu':
        markup = types.InlineKeyboardMarkup()

        markup.add(types.InlineKeyboardButton("НАПИТКИ", callback_data='showdrink'))
        markup.add(types.InlineKeyboardButton("ЕДА", callback_data='showfood'))
        markup.add(types.InlineKeyboardButton("ДОПОЛНИТЕЛЬНЫЕ ТОВАРЫ", callback_data='showextra'))


        bot.send_message(callback.message.chat.id, "Наше меню", reply_markup=markup)

    if callback.data == 'showdrink':
        markup = types.InlineKeyboardMarkup()

        markup.add(types.InlineKeyboardButton("Американо", callback_data='americano'))
        markup.add(types.InlineKeyboardButton("Эспрессо", callback_data='espresso'))
        markup.add(types.InlineKeyboardButton("Фильтр-кофе", callback_data='filter_coffee'))
        markup.add(types.InlineKeyboardButton("Капучино", callback_data='cappuccino'))
        markup.add(types.InlineKeyboardButton("Латте", callback_data='latte'))
        markup.add(types.InlineKeyboardButton("Флэт Уайт", callback_data='flat_white'))
        markup.add(types.InlineKeyboardButton("Раф", callback_data='raf_coffee'))
        markup.add(types.InlineKeyboardButton("Матча", callback_data='matcha'))
        markup.add(types.InlineKeyboardButton("Какао", callback_data='cocoa'))
        markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))

        bot.send_message(callback.message.chat.id, "Напитки", reply_markup=markup)


    if callback.data == 'showfood':
        markup = types.InlineKeyboardMarkup()

        markup.add(types.InlineKeyboardButton("Бабка с шоколадом и вишней", callback_data='chocolate_cherry_babka'))
        markup.add(types.InlineKeyboardButton("Сэндвич с мясом", callback_data='meat_sandwich'))
        markup.add(types.InlineKeyboardButton("Краффин с соленой карамелью", callback_data='salted_caramel_croissant'))
        markup.add(types.InlineKeyboardButton("Канеле", callback_data='canele'))
        markup.add(types.InlineKeyboardButton("Ржаной даниш с брынзой", callback_data='rye_danish_with_cheese'))
        markup.add(types.InlineKeyboardButton("Круассан с сыром", callback_data='cheese_croissant'))
        markup.add(types.InlineKeyboardButton("Пан шоколя", callback_data='chocolate_pan'))
        markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))

        bot.send_message(callback.message.chat.id, "Еда", reply_markup=markup)


    if callback.data == 'showextra':

        markup = types.InlineKeyboardMarkup()

        markup.add(types.InlineKeyboardButton("Американо", callback_data='americano'))
        markup.add(types.InlineKeyboardButton("Эспрессо", callback_data='espresso'))
        markup.add(types.InlineKeyboardButton("Фильтр-кофе", callback_data='filter_coffee'))
        markup.add(types.InlineKeyboardButton("Капучино", callback_data='cappuccino'))
        markup.add(types.InlineKeyboardButton("Латте", callback_data='latte'))
        markup.add(types.InlineKeyboardButton("Флэт Уайт", callback_data='flat_white'))
        markup.add(types.InlineKeyboardButton("Раф", callback_data='raf_coffee'))
        markup.add(types.InlineKeyboardButton("Матча", callback_data='matcha'))
        markup.add(types.InlineKeyboardButton("Какао", callback_data='cocoa'))
        markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))
        bot.send_message(callback.message.chat.id, "Дополнительные товары", reply_markup=markup)


    if callback.data in drinks:
        p = drinks[callback.data]
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Размер", callback_data='size' + callback.data))
        markup.add(types.InlineKeyboardButton("Пропорции", callback_data='ratio' + callback.data))
        markup.add(types.InlineKeyboardButton("Модификаторы", callback_data='mod' + callback.data))

        with open(p['photo'], 'rb') as file:
            bot.send_photo(
                callback.message.chat.id,
                file,
                caption=p['name'] + "\n\n" + p['desc'],
                reply_markup=markup
            )

    if callback.data in food:
        f = food[callback.data]
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(f"Добавить за {f['price']}", callback_data='add_food' + callback.data))

        with open(f['photo'], 'rb') as file:
            bot.send_photo(
                callback.message.chat.id,
                file,
                caption=f['name'] + "\n\n" + f['desc'],
                reply_markup=markup
            )

    #if callback.data == 'exit':
        #bot.register_next_step_handler(message, user_name)

bot.polling(non_stop=True)