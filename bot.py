import telebot


from telebot import types

bot = telebot.TeleBot('1459832039:AAEqDgTuUkzNiukAR8XPrVlD8ktutoguf1k')


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/sticker3.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # KEYBOARD_1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("📚 Учебники есть?")
    item2 = types.KeyboardButton("👨‍💻 На лекцию надо")
    item3 = types.KeyboardButton("🥴 Развиваться")
    item4 = types.KeyboardButton("🥺 Поддержки...")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id,
                     "Бонжур, {0.first_name}!\nТы наверное порядком подустал от учебы\nЯ - <b>{1.first_name}</b> - бот,"
                     " созданный помогать тебе с ней.\nНу по крайней мере с ее систематизацией...\n\n Чем могу помочь?"
                     .format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def talk(message):
    if message.chat.type == 'private':
        if message.text == '📚 Учебники есть?':
            # KEYBORD_2
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("😎 Алгебра", callback_data='algebra')
            item2 = types.InlineKeyboardButton("🧐 Матан", callback_data='calculus')
            item3 = types.InlineKeyboardButton("🤯 Физика", callback_data='physics')
            item4 = types.InlineKeyboardButton("👺 Линал и Ангем", callback_data='linear')
            item5 = types.InlineKeyboardButton("🤖 Дискра", callback_data='discrete')
            markup.add(item1, item2, item3, item4, item5)

            bot.send_message(message.chat.id, "А какие надо?", reply_markup=markup)

        if message.text == '👨‍💻 На лекцию надо':
            # KEYBORD_3
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("🤬 Алгебра/Дискра", callback_data='lection_algebra')
            item2 = types.InlineKeyboardButton("💻 Прога", callback_data='lection_algorithms')
            item3 = types.InlineKeyboardButton("😨 Физика", callback_data='lection_physics')
            item4 = types.InlineKeyboardButton("🥱 Линал/Ангем", callback_data='lection_linear')
            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, "На какую тебе, студент?", reply_markup=markup)

        if message.text == '🥴 Развиваться':
            # KEYBORD_4
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("💪 Математику качаем", callback_data='math')
            item2 = types.InlineKeyboardButton("👾 Прогать хочу", callback_data='programming')
            item3 = types.InlineKeyboardButton("🧐 Может YouTube?", callback_data='you_tube')
            item4 = types.InlineKeyboardButton("💻 Полезные сайты", callback_data='internet')
            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, "О, это похвально\n"
                                              "Как говорил Анашкин - «Вуз - место для самообразования»\n"
                                              "Чего изволите?", reply_markup=markup)

        if message.text == '🥺 Поддержки...':
            bot.send_message(message.chat.id, "Оу, {0.first_name}, я всегда к твоим услугам.\n\n"
                                              "Всем нам иногда нужна поддержка. Сейчас в твоей жизни \nнаступил такой "
                                              "этап, Бывает очень тяжело найти в себе силы и не тильтануть, "
                                              "но нужно всегда"
                                              "продолжать поиск. Нужно искать источникивдохновения, искать то,"
                                              "что помогает \nотвлечься от всей этой суеты. Я вот, например, вам всем помогаю."
                                              "Быть ботом знаешь ли тоже иногда не просто.\nА уж если я нашел что-то,"
                                              "что мне помогает, то и ты сможешь.\nЭто лишь вопрос времени.\n\n"
                                              "Я всегда с тобой, дружище!\n\n"
                                              "Стою на страже твоего учебного процесса".format(message.from_user, bot.get_me()))

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'algebra':
                doc11 = open('books/algebra/[Vinberg_YE.B.]_Kurs_algebrue.pdf', 'rb')
                doc12 = open('books/algebra/Leng_S._Algebra.pdf', 'rb')
                doc13 = open('books/algebra/Вавилов_Конкретная_терия_групп.pdf', 'rb')
                doc14 = open('books/algebra/Глухов_Елизаров_Нечаев_Алгебра.pdf', 'rb')
                doc15 = open('books/algebra/Курош Высшая алгебра.pdf', 'rb')
                doc16 = open('books/algebra/Федоровский_Алгебра_введение_в_теорию_групп.pdf', 'rb')

                bot.send_message(call.message.chat.id, "На здоровье :)")

                bot.send_document(call.message.chat.id, doc11)
                bot.send_document(call.message.chat.id, doc12)
                bot.send_document(call.message.chat.id, doc13)
                bot.send_document(call.message.chat.id, doc14)
                bot.send_document(call.message.chat.id, doc15)
                bot.send_document(call.message.chat.id, doc16)

            elif call.data == 'calculus':
                doc21 = open('books/calculus/Фихтенгольц Том 1.pdf', 'rb')
                doc22 = open('books/calculus/Фихтенгольц Том 2.pdf', 'rb')
                doc23 = open('books/calculus/Фихтенгольц Том 3.pdf', 'rb')
                doc24 = open('books/calculus/Зорич (часть 1).pdf', 'rb')

                bot.send_message(call.message.chat.id, "На здоровье :)")

                bot.send_document(call.message.chat.id, doc21)
                bot.send_document(call.message.chat.id, doc22)
                bot.send_document(call.message.chat.id, doc23)
                bot.send_document(call.message.chat.id, doc24)

            elif call.data == 'physics':
                doc31 = open('books/physics/Первый том Фейнман.pdf', 'rb')
                doc32 = open('books/physics/Второй том Фейнман.pdf', 'rb')
                doc33 = open('books/physics/Третий том Фейнман.pdf', 'rb')
                doc34 = open('books/physics/Четвертый том Фейнман.pdf', 'rb')
                doc35 = open('books/physics/Пятый том Фейнман.pdf', 'rb')
                doc36 = open('books/physics/Шестой том Фейнман.pdf', 'rb')
                doc37 = open('books/physics/Седьмой том Фейнман.pdf', 'rb')
                doc38 = open('books/physics/Восьмой том Фейнман.pdf', 'rb')
                doc39 = open('books/physics/Девятый том Фейнман.pdf', 'rb')
                doc310 = open('books/physics/Десятый том Фейнман.pdf', 'rb')

                bot.send_message(call.message.chat.id, "На здоровье :)")

                bot.send_document(call.message.chat.id, doc31)
                bot.send_document(call.message.chat.id, doc32)
                bot.send_document(call.message.chat.id, doc33)
                bot.send_document(call.message.chat.id, doc34)
                bot.send_document(call.message.chat.id, doc35)
                bot.send_document(call.message.chat.id, doc36)
                bot.send_document(call.message.chat.id, doc37)
                bot.send_document(call.message.chat.id, doc38)
                bot.send_document(call.message.chat.id, doc39)
                bot.send_document(call.message.chat.id, doc310)

            elif call.data == 'linear':
                doc41 = open('books/linear/Беклемишев.Курс аналитичекой геометрии и линейной алгебре.pdf', 'rb')
                doc42 = open('books/linear/линал учебник.pdf', 'rb')
                bot.send_message(call.message.chat.id, "На здоровье :)")
                bot.send_document(call.message.chat.id, doc41)
                bot.send_document(call.message.chat.id, doc42)

            elif call.data == 'discrete':
                doc1 = open('books/discrete/Discrete Mathematics with Applications [2020] Susanna S. Epp.pdf', 'rb')
                doc2 = open('books/discrete/V[1].A.Nosov Kombinatorika i teoriya graphov.pdf', 'rb')
                doc3 = open('books/discrete/Дискретная_математика_и_комбинаторика_2004_Джеймс_А_Андерсон.pdf', 'rb')
                bot.send_message(call.message.chat.id, "На здоровье :)")
                bot.send_document(call.message.chat.id, doc1)
                bot.send_document(call.message.chat.id, doc2)
                bot.send_document(call.message.chat.id, doc3)

            elif call.data == 'lection_algebra':
                bot.send_message(call.message.chat.id, "К Кочету значит... Ну держи:\n\n"
                                                       "https://us04web.zoom.us/j/2371744320?pwd=ei9YeHdtMjkzb2todmdrQWFGTVRBUT09"
                                 .format(call.message.from_user, bot.get_me()))

            elif call.data == 'lection_linear':
                bot.send_message(call.message.chat.id, "Ууууу, Линал... Я бы поспал лучше, но дело твоё:\n\n"
                                                       "https://zoom.us/j/7092630313?pwd"
                                                       "=UG9TdGdHOTZrQWMyT3l4dk5hdVhGdz09 "
                                                       "Код доступа: 914059"
                                 .format(call.message.from_user, bot.get_me()))

            elif call.data == 'lection_physics':
                bot.send_message(call.message.chat.id, "Ну ты жёсткий тип, я понял:\n\n"
                                                       "https://zoom.us/j/6732616551"
                                                       "z09".format(call.message.from_user, bot.get_me()))

            elif call.data == 'lection_algorithms':
                bot.send_message(call.message.chat.id, "Прога? Ни разу там не бывал:\n\n"
                                                       "Семинары: https://zoom.us/j/94668843712"
                                                       "Лекции: https://zoom.us/j/91234806112?pwd=S1hmSXl0eC9VY3JCWTNMLzd6eFluZz09"
                                 .format(call.message.from_user, bot.get_me()))

            elif call.data == 'math':
                doc51 = open('books/for upgrade/Koblitz Введение в эллиптические кривые.pdf', 'rb')
                doc52 = open('books/for upgrade/N_B_Vasilyev_V_L_Gutenmakher_Pryamye_i_krivye.pdf', 'rb')
                doc53 = open('books/for upgrade/Teoria_Galua_2004_Artin.pdf', 'rb')
                doc54 = open(
                    'books/for upgrade/Алгебраическая геометрия и теория чисел. В.В. Острик и М.А. Цфасман.pdf', 'rb')
                doc55 = open('books/for upgrade/Введение в критографию и теорию чисел.pdf', 'rb')
                doc56 = open('books/for upgrade/Кокс-Д. Литтл-Д. ОШи-Д. Идеалы , многообразия и алгоритмы.pdf', 'rb')
                doc59 = open('books/for upgrade/Теория-графов-_2003_-Харари-Ф.-_Harary.pdf', 'rb')

                bot.send_message(call.message.chat.id, "Зачитаешься :)")

                bot.send_document(call.message.chat.id, doc51)
                bot.send_document(call.message.chat.id, doc52)
                bot.send_document(call.message.chat.id, doc53)
                bot.send_document(call.message.chat.id, doc54)
                bot.send_document(call.message.chat.id, doc55)
                bot.send_document(call.message.chat.id, doc56)
                bot.send_document(call.message.chat.id, doc59)

            elif call.data == 'programming':
                doc62 = open('books/programming/CC++_Структурное_и_объектно_ориентированное_программирование_2011.pdf',
                             'rb')
                doc63 = open('books/programming/Django_3_0_Практика_создания_веб_сайтов_на_Python_2021_Владимир.pdf',
                             'rb')
                doc64 = open('books/programming/Learning SQL, 3rd edition [2020] Beaulieu.pdf', 'rb')
                doc65 = open('books/programming/Python_Machine_Learning,_2nd_Edition_2017_Sebastian_Raschka,_Vahid.pdf',
                             'rb')
                doc66 = open('books/programming/Python_для_чайников_2_изд_2020_Мюллер_Джон_Поль.pdf', 'rb')
                doc67 = open('books/programming/Python_и_машинное_обучение_2020_Рашка,_Мирджалили.pdf', 'rb')
                doc68 = open('books/programming/Tiny Python Projects [2020] Ken Youens-Clark.pdf', 'rb')

                bot.send_message(call.message.chat.id, "Держи, мой юный программист :)")

                bot.send_document(call.message.chat.id, doc62)
                bot.send_document(call.message.chat.id, doc63)
                bot.send_document(call.message.chat.id, doc64)
                bot.send_document(call.message.chat.id, doc65)
                bot.send_document(call.message.chat.id, doc66)
                bot.send_document(call.message.chat.id, doc67)
                bot.send_document(call.message.chat.id, doc68)

            elif call.data == 'you_tube':
                bot.send_message(call.message.chat.id, "Ну что ж, как скажешь :)\n\n"
                                                       "Прекрасный плейлист небольших видео по теории групп:\n"
                                                       "https://youtube.com/playlist?list=PLnbH8YQPwKblIpRi0ARO2VadnMwntvF51\n\n"
                                                       "Программирование на Python, МФТИ:\n"
                                                       "https://youtube.com/playlist?list=PLRDzFCPr95fIDJUvFxvzWxg-V9BmZlMMe\n\n"
                                                       "Англоязычный канал об алгоритмах и их реализации с хорошей визуализацией:\n"
                                                       "https://www.youtube.com/channel/UCK8XIGR5kRidIw2fWqwyHRA\n\n"
                                                       "Известный англоязычный канал о математике. Очень советую, отличная визуализация материала:\n"
                                                       "https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw\n\n"
                                                       "Канал о математике с русскими субтитрами, популяризирующий множество математичеких проблем:\n"
                                                       "https://www.youtube.com/channel/UC1_uAIS3r8Vu6JjXWvastJg\n\n"
                                                       "Канал о программировании и геометрии, с точки зрения построения визуальных миров:\n"
                                                       "https://www.youtube.com/c/CodeParade/videos\n\n"
                                                       "Плейлист о теории относительности, тензорном и векторном исчислении, можете найдете\n"
                                                       "связь с вашей физикой\n"
                                                       "https://youtube.com/playlist?list=PLnbH8YQPwKbkVnEMn2qwFZADy-7kgmlNL\n\n")

            elif call.data == 'internet':
                bot.send_message(call.message.chat.id, "Пройдемся по сайтикам\n\n"
                                                       "Если хочешь начать учить Python, то тебе сюда:\n"
                                                       "https://pythontutor.ru/\n\n"
                                                       "А потом советую зайти сюда после предыдущего сайта:\n"
                                                       "https://leetcode.com/\n\n"
                                                       "Полезный ресурс по вузовской математичесой теории\n"
                                                       "http://www.mathprofi.ru/\n\n")

            # REMOVE INLINE BUTTONS
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=None, reply_markup=None)




    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
