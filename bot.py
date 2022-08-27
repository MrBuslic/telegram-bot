import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    #sti = open('static/welcome.webp', 'rb')
    #bot.send_sticker(message.chat.id, sti)

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item5 = types.KeyboardButton("Что такое Boardingclub33?")
    item2 = types.KeyboardButton("Прайс на катание")
    item3 = types.KeyboardButton("Свободные даты")
    #item4 = types.KeyboardButton("Сотрудничество")
    item4 = types.KeyboardButton("Контакты")

    markup.add(item2, item3, item4, item5)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

    #voice = open('sounds/vsem_zdorova.ogg', 'rb')
    #bot.send_voice(message.chat.id, voice)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        #if message.text == '🎲 Рандомное число':
            #bot.send_message(message.chat.id, str(random.randint(0,100)))
        #if message.text == '😊 Как дела?':
            #voice = open('sounds/masjanja-jepizod-10-p.ogg', 'rb')
            #bot.send_voice(message.chat.id, voice)
            #bot.send_message(message.chat.id, 'Отлично, сам как?')
        price_pic = open('pict/price.jpg', 'rb')
        if message.text == 'Что такое Boardingclub33?':
            bot.send_message(message.chat.id, 'Boardingclub33 - это сообщество любителей и профессионалов, занимающихся спортивными видами отдыха, как летом на воде, так и зимой. В Вашем распоряжении летом услуги вейк-парка на базе отдыха «Горшиха» или аренда катера на Кольчугинском водохранилище. А как же быть зимой?Всё очень просто… Cноукайтинг! Берём сноуборд или горные лыжи, кайт и покоряем бескрайние снежные просторы. Мы предлагаем услуги по обучению вейкбордингу и сноукайтингу, а также прокат оборудования – досок и гидрокостюмов.')
        if message.text == 'Прайс на катание':
            bot.send_message(message.chat.id, 'Прайс: - катание за катером: 5000р/час, любое снаряжение кроме гидрокостюм (оплачиваются отдельно - 200р/час) входит в стоимость (вейкборд, сёрфинг, гидрофойл, водные лыжи, ватрушка) - катание на Горшихе:')
            bot.send_photo(message.chat.id, price_pic)
        if message.text == 'Свободные даты':
            bot.send_message(message.chat.id, '')
        if message.text == 'Контакты':
            bot.send_message(message.chat.id, '@studentova24')
        #if message.text == 'Связь с руководством клуба':
        #    bot.send_message(message.chat.id, '@studentova24')
# RUN
bot.polling(none_stop=True)
