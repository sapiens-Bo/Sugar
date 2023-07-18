import telebot
from telebot import types
import main

bot = telebot.TeleBot('6359616960:AAEGOXYpi0RTpwMYNCKEMogCmJ9rYv4VNuw')

name_table = ''

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        keybord = types.InlineKeyboardMarkup()
        key_sale = types.InlineKeyboardButton(text='Продажа', callback_data='sale')
        keybord.add(key_sale) # добавляем кнопку в клавиатуру
        key_out_t = types.InlineKeyboardButton(text='Вывести таблицу', callback_data='out_t')
        keybord.add(key_out_t)
        key_add_t = types.InlineKeyboardButton(text='Добавить в таблицу', callback_data='add_t')
        keybord.add(key_add_t)
        key_day = types.InlineKeyboardButton(text='Результаты', callback_data='day')
        keybord.add(key_day)
        bot.send_message(message.from_user.id, 'Что от нас требуется?', reply_markup=keybord)

@bot.message_handler(content_types=['text'])
def outputTable(message):
    if message.text == 'start':
        bot.send_message(message.chat.id, main.outputTable(message.text))

#def whichTable(message)

@bot.callback_query_handler(func=lambda call: True)
def callbackWorker(call):
    if call.data == 'out_t':
        txt = bot.send_message(call.message.chat.id, 'Введите название таблицы')
        bot.register_next_step_handler(call.message, outputTable)

        

# вернуть пользователю обработанную переменную.
def sum(num1: int, num2:int) -> int:
    return num1 + num2

bot.polling(none_stop=True, interval=0)