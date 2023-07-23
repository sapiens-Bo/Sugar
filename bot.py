import telebot
from telebot import types
import time
import database
#import main

bot = telebot.TeleBot('6359616960:AAEGOXYpi0RTpwMYNCKEMogCmJ9rYv4VNuw')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, '''Привет! Это бот продаж, сюда тебе нужно вводить
                     продажу которую ты совершил\n
                     Формат: имя количество цена за еденицу, как\n
                     Если нужна информация по продажам который ты совершил введи команду \out.\n
                     Удачи! Если какие-то проблемы напиши создателю.''')
    
@bot.message_handler(commands=['out'])
def outTable(message):
    bot.send_message(message.from_user.id, database.outTable('sales'))

@bot.message_handler(commands=['result'])
def result(message):
    database.calcResult()
    bot.send_message(message.from_user.id, f'Терминал = {database.terminal}\n \
                    Наличными = {database.cash}\n \
                    Мобильный банк = {database.mob_bank}\n \
                    Общее = {database.sum}')
    
@bot.message_handler(content_types=['text'])
def sale(message):
    a = message.text
    a = a.split(', ')
    database.addSales(a)
    bot.send_message(message.from_user.id, 'Молодец! Продано:\n' + database.outTable('sales'))




# Старый код
# name_table = ''

# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == '/start':
#         keybord = types.InlineKeyboardMarkup()

#         key_sale = types.InlineKeyboardButton(text='Продажа', 
#                                               callback_data='sale')
#         keybord.add(key_sale) # добавляем кнопку в клавиатуру

#         key_out_t = types.InlineKeyboardButton(text='Вывести таблицу', 
#                                                callback_data='out_t')
#         keybord.add(key_out_t)

#         key_add_t = types.InlineKeyboardButton(text='Добавить в таблицу', 
#                                                callback_data='add_t')
#         keybord.add(key_add_t)

#         key_day = types.InlineKeyboardButton(text='Результаты', 
#                                              callback_data='result')
#         keybord.add(key_day)

#         key_delete = types.InlineKeyboardButton(text='Удалить из таблицы',
#                                                 callback_data='delete')
#         keybord.add(key_delete)

#         bot.send_message(message.from_user.id, 'Что от нас требуется?',
#                          reply_markup=keybord)
#     elif message.text == '/end':
#         main.startInRemaindToday()

# @bot.message_handler(content_types=['text'])
# def outputTableBut(message):
#     kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     key_start = types.KeyboardButton('Приход/наличие')
#     key_sales = types.KeyboardButton('Продажи')
#     key_rem = types.KeyboardButton('Остаток')
#     kb.add(key_rem, key_sales, key_start)
#     bot.send_message(message.from_user.id, 'Выберите таблицу которую нужно вывести',
#                      reply_markup=kb)

# @bot.message_handler(content_types=['text'])
# def outputTable(message):
#     name_t = ''
#     if message.text == 'Приход/наличие':
#         name_t = 'start'
#     elif message.text == 'Продажи':
#         name_t = 'sales'
#     elif message.text == 'Остаток':
#         name_t = 'remaind'
#     bot.send_message(message.chat.id, main.outputTable(name_t))

# @bot.message_handler(content_types=['text'])
# def sale(message):
#     if main.outputTable('start'):
#         a = message.text
#         a = a.split(', ')
#         how, name, total = a
#         main.sale(how, name, int(total))
#     else:
#         bot.reply_to(message, 'Void table')

# @bot.message_handler(content_types=['text'])
# def clearTable(message):
#     main.delFromTable(message.text)

# # сделать так что бы пользователь мог вводить несколько значений
# @bot.message_handler(content_types=['text'])
# def addStart(message):
#     a = message.text
#     a = a.split(', ')
#     name, total, price = a
#     main.addInStart(name, int(total), float(price))

# @bot.callback_query_handler(func=lambda call: True)
# def callbackWorker(call):
#     if call.data == 'out_t':
#         # bot.send_message(call.message.chat.id,
#         #                  'Введите название таблицы\n start, sales, remaind, how')
#         bot.register_next_step_handler(call.message, outputTableBut)
#     elif call.data == 'sale':
#         bot.send_message(call.message.chat.id,
#                          'Введите продажу\nформат: чем расплотились, имя позиции, количество\n \
#                             Пример: t, Молочная девочка, 2')
#         bot.register_next_step_handler(call.message, sale)
#     elif call.data == 'result':
#         main.calcHow()
#         sum = main.terminal + main.cash + main.terminal
#         bot.send_message(call.message.chat.id, f'Терминал - {main.terminal}\n \
#                                                 Наличка - {main.cash}\n \
#                                                 Мобильный банк - {main.mob_bank}\n \
#                                                 Общее - {sum}')
#     elif call.data == 'delete':
#         bot.send_message(call.message.chat.id, 'Введите таблицу которую хотите очистить')
#         bot.register_next_step_handler(call.message, clearTable)
#     elif call.data == 'add_t':
#         bot.send_message(call.message.chat.id, 
#                          'Введите данные которые нужно добавить\nпример: молочная девочка, 2, 380')
#         bot.register_next_step_handler(call.message, addStart)

# @bot.message_handler(commands=['stop'])
# def stop(message):
#     print('Ok')
#     bot.stop_polling()

bot.polling(none_stop=True, interval=0)

# while True:
#     try:
#         bot.polling(none_stop=True, interval=0)
#     except Exception:
#         print(Exception)
#         time.sleep(15)

