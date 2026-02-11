import telebot
import db 
from telebot import types 

import sqlite3

bot = telebot.TeleBot("8573939809:AAE-sW3ZzmUVpCPX-axSO6ryeoyQFWkXaEM")

name = None

@bot.message_handler(commands=['start'])
def start(message):

    db.create_tables()
    db.products_in()


    bot.send_message(message.chat.id, "Здравствуйте. Это бот проще. Давайте знакомится. Введите ваше имя: ")
    bot.register_next_step_handler(message, main_menu)

def main_menu(message):
    global name
    
    name = message.text.strip()
    user_id = message.from_user.id + 3  


    db.data_in("users", phone = "+73131222813", user_name = name, user_tg_id = user_id)


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

    global current_product

    # bot.answer_callback_query(callback.id)
    # chat_id = callback.message.chat.id
    # msg_id = callback.message.message_id

    # try:
    #     bot.delete_message(chat_id, msg_id)
    # except:
    #     pass



    if callback.data == 'showmenu':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("ЛЕНПОЛИГРАФМАШ", callback_data='101'))
        markup.add(types.InlineKeyboardButton("У КАРАНДАША", callback_data='102'))
        markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))

        bot.send_message(callback.message.chat.id, "Выберите кофейню, а я покажу, что есть для вас в нашем меню", reply_markup=markup)        


    if callback.data == '101':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("САМОВЫВОЗ", callback_data='pickup_len'))
        markup.add(types.InlineKeyboardButton("ДОСТАВКА", callback_data='delivery_len'))
        markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))

        bot.send_message(callback.message.chat.id, "Выберите способ получения вкусняшек", reply_markup=markup)        


    if callback.data == '102':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("САМОВЫВОЗ", callback_data='pickup_kar'))
        #markup.add(types.InlineKeyboardButton("ДОСТАВКА", callback_data='delivery_kar'))
        markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))

        bot.send_message(callback.message.chat.id, "Выберите способ получения вкусняшек", reply_markup=markup)


    if callback.data == 'pickup_len' or callback.data == 'pickup_kar':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("НАПИТКИ", callback_data='showdrink'))
        markup.add(types.InlineKeyboardButton("ЕДА", callback_data='showfood'))
        markup.add(types.InlineKeyboardButton("ДОПОЛНИТЕЛЬНЫЕ ТОВАРЫ", callback_data='showextra'))
        markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))

        bot.send_message(callback.message.chat.id, "Наше меню", reply_markup=markup)

    if callback.data == 'delivery_len':
        with open('delivery.jpg', 'rb') as file:
            bot.send_photo (
                callback.message.chat.id,
                file,
                caption="Внимание! \n \n" \
                "Мы осуществляем доставку только в пределах выделенной зоны.",
            )

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("НАПИТКИ", callback_data='showdrink'))
        markup.add(types.InlineKeyboardButton("ЕДА", callback_data='showfood'))
        markup.add(types.InlineKeyboardButton("ДОПОЛНИТЕЛЬНЫЕ ТОВАРЫ", callback_data='showextra'))
        markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))

        bot.send_message(callback.message.chat.id, "Наше меню", reply_markup=markup)

    if callback.data == 'showdrink':
        markup = types.InlineKeyboardMarkup()

        markup.add(types.InlineKeyboardButton("Американо", callback_data='1'))
        markup.add(types.InlineKeyboardButton("Эспрессо", callback_data='2'))
        markup.add(types.InlineKeyboardButton("Фильтр-кофе", callback_data='3'))
        markup.add(types.InlineKeyboardButton("Капучино", callback_data='4'))
        markup.add(types.InlineKeyboardButton("Латте", callback_data='5'))
        markup.add(types.InlineKeyboardButton("Флэт Уайт", callback_data='6'))
        markup.add(types.InlineKeyboardButton("Раф", callback_data='7'))
        markup.add(types.InlineKeyboardButton("Матча", callback_data='8'))
        markup.add(types.InlineKeyboardButton("Какао", callback_data='9'))
        markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))

        bot.send_message(callback.message.chat.id, "Напитки", reply_markup=markup)


    if callback.data == 'showfood':
        markup = types.InlineKeyboardMarkup()

        markup.add(types.InlineKeyboardButton("Бабка с шоколадом и вишней", callback_data='10'))
        markup.add(types.InlineKeyboardButton("Сэндвич с мясом", callback_data='11'))
        markup.add(types.InlineKeyboardButton("Краффин с соленой карамелью", callback_data='12'))
        markup.add(types.InlineKeyboardButton("Канеле", callback_data='13'))
        markup.add(types.InlineKeyboardButton("Ржаной даниш с брынзой", callback_data='14'))
        markup.add(types.InlineKeyboardButton("Круассан с сыром", callback_data='15'))
        markup.add(types.InlineKeyboardButton("Пан шоколя", callback_data='16'))
        markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))

        bot.send_message(callback.message.chat.id, "Еда", reply_markup=markup)


    # if callback.data == 'showextra':

    #     markup = types.InlineKeyboardMarkup()

    #     markup.add(types.InlineKeyboardButton("Американо", callback_data='a'))
    #     markup.add(types.InlineKeyboardButton("Эспрессо", callback_data='espresso'))
    #     markup.add(types.InlineKeyboardButton("Фильтр-кофе", callback_data='filter_coffee'))
    #     markup.add(types.InlineKeyboardButton("Капучино", callback_data='cappuccino'))
    #     markup.add(types.InlineKeyboardButton("Латте", callback_data='latte'))
    #     markup.add(types.InlineKeyboardButton("Флэт Уайт", callback_data='flat_white'))
    #     markup.add(types.InlineKeyboardButton("Раф", callback_data='raf_coffee'))
    #     markup.add(types.InlineKeyboardButton("Матча", callback_data='matcha'))
    #     markup.add(types.InlineKeyboardButton("Какао", callback_data='cocoa'))
    #     markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))
    #     bot.send_message(callback.message.chat.id, "Дополнительные товары", reply_markup=markup)
  

    if callback.data.isdigit() and callback.data != "101" and callback.data != "102":
        current_product = callback.data

        products = db.get_callback("products", callback.data, "id")
        products_variants = db.get_callback("product_variants", callback.data, "product_id")

        if products and products_variants["variant_name"] != 'onesize':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Размер", callback_data='size'))
            markup.add(types.InlineKeyboardButton("Пропорции", callback_data='ratio'))
            markup.add(types.InlineKeyboardButton("Модификаторы", callback_data='mod'))
            markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))
            
            with open(products['photo_path'], 'rb') as file:
                bot.send_photo(
                    callback.message.chat.id,
                    file,
                    caption=products['product_name'] + "\n\n" + products['desc'],
                    reply_markup=markup
                )

        if products and products_variants["variant_name"] == 'onesize':
            markup = types.InlineKeyboardMarkup()

            if products['category'] == "food":

                markup.add(types.InlineKeyboardButton(f"Добавить в корзину", callback_data='add_food' + callback.data))
                markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))
            if products['category'] == "drinks":

                markup.add(types.InlineKeyboardButton("Пропорции", callback_data='ratio'))
                markup.add(types.InlineKeyboardButton("Модификаторы", callback_data='mod'))
                markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))

            with open(products['photo_path'], 'rb') as file:    
                bot.send_photo(
                    callback.message.chat.id,
                    file,
                    caption=products['product_name'] + "\n\n" + products['desc'] + " " + str(products_variants['price']) + "₽",
                    reply_markup=markup
                )

    if callback.data == 'size': 
        products = db.get_callback("products", current_product, "id")

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Маленький", callback_data='Small'))
        markup.add(types.InlineKeyboardButton("Большой", callback_data='Big'))
        markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))

        with open(products['photo_path'], 'rb') as file:
            bot.send_photo(
                callback.message.chat.id,
                file,
                caption=products['product_name'] + "\n\n" + products['desc'],
                reply_markup=markup
            )

    if callback.data == 'mod':
        products = db.get_callback("products", current_product, "id")

        # бля может отражаться как продукт айдишник
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Сироп карамель", callback_data='1'))
        markup.add(types.InlineKeyboardButton("Сироп ваниль", callback_data='2'))
        markup.add(types.InlineKeyboardButton("Сироп орех", callback_data='3'))
        markup.add(types.InlineKeyboardButton("Овсяное молоко", callback_data='4'))
        markup.add(types.InlineKeyboardButton("Миндальное молоко", callback_data='5'))
        markup.add(types.InlineKeyboardButton("Кокосовое молоко", callback_data='6'))
        markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))

        with open(products['photo_path'], 'rb') as file:
            bot.send_photo(
                callback.message.chat.id,
                file,
                caption=products['product_name'] + "\n\n" + products['desc'],
                reply_markup=markup
            )

    if callback.data == 'ratio':
        products = db.get_callback("products", current_product, "id")

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("50% на 50%", callback_data='fiftyfifty'))

        markup.row (
            types.InlineKeyboardButton("30% на 70%", callback_data='threeseven'),
            types.InlineKeyboardButton("70% на 30%", callback_data='seventhree')
        )

        markup.row (
            types.InlineKeyboardButton("60% на 40%", callback_data='sixfour'),
            types.InlineKeyboardButton("40% на 60%", callback_data='foursix')
        )

        markup.add(types.InlineKeyboardButton("Назад", callback_data='exit'))

        with open(products['photo_path'], 'rb') as file:
            bot.send_photo(
                callback.message.chat.id,
                file,
                caption=products['product_name'] + "\n\n" + products['desc'],
                reply_markup=markup
            )



    if callback.data == 'add_food':
        pass 


    #if callback.data == 'exit':
        #bot.register_next_step_handler(message, user_name)



bot.polling(non_stop=True)