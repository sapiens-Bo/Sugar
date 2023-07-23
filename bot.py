import telebot
import database
import key_autho

# перед тем как добавить в гит удалить Токен!!!!!!!!!!
bot = telebot.TeleBot(key_autho.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, '''Привет! Это бот продаж, сюда тебе нужно вводить
                     продажу которую ты совершил\n
                     Формат: имя, количество, цена за еденицу, как\n
                     Если нужна информация по продажам который ты совершил введи команду /out.\n
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

@bot.message_handler(commands=['end'])
def end(message):
    database.delPos('sales')
    bot.send_message(message.from_user.id, 'Вы молодец! Надеюсь я вам помог)')
    bot.stop_bot()

@bot.message_handler(content_types=['text'])
def sale(message):
    a = message.text
    a = a.split(', ')
    if len(a) != 4:
        bot.reply_to(message, 'Ты что-то забыла. Напомню:\nФормат: имя, количество, цена за еденицу, как')
    else:
        database.addSales(a)
        bot.send_message(message.from_user.id, 'Молодец! Продано:\n' + database.outTable('sales'))



bot.polling(none_stop=True, interval=0)
