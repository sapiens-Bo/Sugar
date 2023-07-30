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
terminal = 0
cash = 0
mob_bank = 0
sum = 0

# СУБД
def addSales(total, price, how):
    cursor.execute('INSERT INTO sales VALUES (?, ?, ?)', (int(total), float(price), how))
    sugardb.commit()

def outTable(name):
    table = 'Таблица пустая'
    if name in tables:
        cursor.execute(f'SELECT * FROM {name}')
        table = cursor.fetchall()
        table = [str(i) for i in table]
        table = '\n'.join(table)

    return table

def calcResult():
    global terminal, cash, mob_bank, sum
    cursor.execute('SELECT how, total, price FROM sales')
    sale = cursor.fetchall()
    for how, total, price in sale:
        if how == 't': terminal += price * total
        elif how == 'c': cash += price * total
        elif how == 'mb': mob_bank += price * total
    sum = terminal + cash + mob_bank

def delPos(name):
    cursor.execute(f'DELETE FROM {name}')
    sugardb.commit()