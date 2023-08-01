import sqlite3

sugardb = sqlite3.connect('sugar.db', check_same_thread=False)
cursor = sugardb.cursor()

# создание таблиц
cursor.execute("""CREATE TABLE IF NOT EXISTS sales (
               total INT,
               price REAL,
               how TEXT
            );
""")

sugardb.commit()

tables = ['sales']
method_pay = ['t', 'c', 'mb']
terminal = 0
cash = 0
mob_bank = 0
sum = 0

# СУБД
def addSales(total, price, how):
    cursor.execute('INSERT INTO sales (total, price, how) VALUES (?, ?, ?)', (total, price, how))
    sugardb.commit()

def outTable(name):
    table = 'Таблица пустая'
    if name in tables:
        cursor.execute(f'SELECT * FROM {name}')
        table = cursor.fetchall()
        table = [str(i) for i in table]
        table = '\n'.join(table)

    return str(table)

def calcResult():
    global terminal, cash, mob_bank, sum
    terminal = 0
    cash = 0
    mob_bank = 0
    cursor.execute('SELECT total, price, how FROM sales')
    sale = cursor.fetchall()
    for total, price, how in sale:
        if how == 't':
            terminal += price * total
        elif how == 'c':
            cash += price * total
        elif how == 'mb':
            mob_bank += price * total
    sum = terminal + cash + mob_bank
    print(terminal, cash, mob_bank, sum)

def delPos(name):
    cursor.execute(f'DELETE FROM {name}')
    global terminal, cash, mob_bank, sum
    terminal = 0
    cash = 0
    mob_bank = 0
    sum = 0
    sugardb.commit()

# addSales(1, 100, 't')

# print(outTable('sales'))
# calcResult()
# print(terminal, cash, mob_bank, sum)