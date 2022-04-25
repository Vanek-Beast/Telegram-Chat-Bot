import telebot
from telebot import types
import logging
import configure

logging.basicConfig(
    level=logging.DEBUG,
    filename="mylog.txt",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )

logging.info('Hello')
bot = telebot.TeleBot(configure.config["token"])


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Информация")
    item2 = types.KeyboardButton("Города")
    item3 = types.KeyboardButton("Как поступить")
    item4 = types.KeyboardButton("Неполный список тем с 1-ого курса")
    item5 = types.KeyboardButton("Неполный список тем со 2-ого курса")

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id,
                     "Добро пожаловать!!!\n"

                     "Меня зовут Yandex bot, я могу рассказать вам про Лицей Академии Яндекса".format(message.from_user,
                                                                                                      bot.get_me()),
                     parse_mode='html', reply_markup=markup)

    bot.send_message(message.chat.id, "Больше информации на официальном сайте Лицея "
                                      "Академии Яндекса: https://academy.yandex.ru/lyceum/"
                     .format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def buttons(message):
    if message.chat.type == 'private':
        if message.text == 'Информация':
            bot.send_message(message.chat.id,
                             "Лицей Академия Яндекса находится  в 162 городах России и Казахстана, "
                             "у нас учащиеся 8-10 классов с нуля за 2 года смогут научиться "
                             "промышленному программированию.".format(
                                 message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=None)

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Чему учат", callback_data='Subject')
            item2 = types.InlineKeyboardButton("Как учат", callback_data='Education')
            item3 = types.InlineKeyboardButton("Кто учит", callback_data='Teachers')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id,
                             "Более подробная информация".format(
                                 message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)

        elif message.text == 'Города':
            img = open('static/image/map.png', 'rb')
            bot.send_photo(message.chat.id, img)

        elif message.text == 'Как поступить':
            bot.send_message(message.chat.id, '1. Проверьте свои силы,'
                                              'решив вступительные задачи прошлых лет\n'
                                              '2. Выберите площадку\n'
                                              '3. Заполните анкету\n'
                                              '4. Пройдите тестирование\n'
                                              '5. Узнайте результаты\n'
                                              '6. Пройдите собеседование\n'
                                              '7. Узнайте итоги)')
        elif message.text == 'Неполный список тем с 1-ого курса':
            bot.send_message(message.chat.id, '1. Знакомство со средой\n'
                                              '2. Условный оператор\n'
                                              '3. Цикл while\n'
                                              '4. Цикл for\n'
                                              '5. True, False, break, continue\n'
                                              '6. Множества\n'
                                              '7. Строки\n'
                                              '8. Словари\n'
                                              '9. Функции\n'
                                              '10. ООП\n'
                                              '11. Классы\n'
                                              '12. Проектирование и разработка классов')
        elif message.text == 'Неполный список тем со 2-ого курса':
            bot.send_message(message.chat.id, '1. Повторение\n'
                                              '2. QT Designer\n'
                                              '3. Введение в репозитории\n'
                                              '4. Pygame\n'
                                              '5. Работа с Git\n'
                                              '6. Совместная работа над проектом\n'
                                              '7. Работа с WEB\n'
                                              '8. Работа в консоли\n'
                                              '9. Алиса(yandex bot)\n'
                                              '10. Чат-бот в ВК\n'
                                              '11. Чат-бот в Телеграмме\n'
                                              '12. Чат-бот в Discord')
        else:
            bot.send_message(message.chat.id, 'Такой команды не существует.')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Subject':
                bot.send_message(call.message.chat.id, 'Промышленному программированию на языке Python. '
                                                       'Это один из самых популярных языков в мире, '
                                                       'который позволяет решать множество задач.')
            elif call.data == 'Education':
                bot.send_message(call.message.chat.id, 'Полный курс длится два года. Нужно пройти конкурсный отбор,'
                                                       'при поступлении можно не уметь программировать. '
                                                       'Обучение бесплатное. '
                                                       'Занятия проходят дважды в неделю на учебных площадках проекта. '
                                                       'Занятия не пересекаются по времени со школьными уроками.')

            elif call.data == 'Teachers':
                bot.send_message(call.message.chat.id, 'Сертифицированные преподаватели. '
                                                       'Занятия ведут местные преподаватели, '
                                                       'прошедшие специальный отбор и обучение.')

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
