import sqlite3

main_db = sqlite3.connect('maindb.db', check_same_thread=False)
cur = main_db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS start(
            name TEXT,
            total INT,
            price REAL
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS sales(
            how TEXT,
            name TEXT,
            total INT,
            sum REAL
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS remaind(
            name TEXT,
            total INT
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS how(
            terminal REAL,
            cash REAL,
            mobile bank, REAL
);""")

main_db.commit()

tables = ['start', 'sales', 'remaind', 'how']

how_list = ['t', 'c', 'mb']

# Добавить новую запись в таблицу старт.
def addInStart(name: str, total: int, price: float):
    pos = (name, total, price)

    cur.execute('SELECT name FROM start WHERE name = ?', (name, ))
    if cur.fetchone() is None:
        cur.execute('INSERT INTO start VALUES (?, ?, ?)', pos)
        main_db.commit()
    else: 
        print('Такая запись уже есть!')

def sale(how: str, name: str, total: int):
    price = 0
    cur.execute('SELECT name FROM start WHERE name = ?', (name, ))
    if cur.fetchone() is None:
        print('Такой записи нет, добавить новую запись?(+ -)')
        if input() == '+':
            # добавить функцию ввода новой позиции в start
            pass
    else:
        if how in how_list:
        # отнимаем количество у name из start
            cur.execute('SELECT total FROM start WHERE name = ?', (name, ))
            old_total = cur.fetchone()
            print(old_total)
            if old_total[0] >= total:
                new_total = old_total[0] - total
                cur.execute('UPDATE start SET total = ? WHERE name = ?', (new_total, name))
                main_db.commit()
                cur.execute('SELECT price FROM start WHERE name = ?', (name, ))
                price_table = cur.fetchone()
                price = price_table[0]

                # вставляем данные в таблицу sales
                cur.execute('SELECT * FROM sales WHERE how = ? AND name = ?', (how, name))
                sales = cur.fetchall()
                print(len(sales), sales)
                *a, t, s = sales[0]
                t += total
                if len(sales) < 1:
                    cur.execute('INSERT INTO sales VALUES(?, ?, ?, ?)', (how, name, total, price * t))
                    main_db.commit()
                else:
                    cur.execute('UPDATE sales SET total = ?, sum = ? WHERE how = ? AND name = ?', (t, price * t, how, name))
                    main_db.commit()
            else:
                # количество < продажи
                pass
        else:
            # Ввели неизвестный способ оплаты
            pass
        

                 
        

def calcRemaind(name: str, sum: float):pass
    

def delFromStart(name: str):
    pass

def outputTable(name: str):
    if name == 'start':
        cur.execute('SELECT * FROM start')
        table = cur.fetchall()
        table = [str(i) for i in table]
        str_table = '\n'.join(table)
        return str_table

# AddInStart('Nano', 10, 380.0)
# AddInStart('Tano', 10, 100.0)
# AddInStart('Vano', 10, 200.0)
# AddInStart('Rano', 10, 320.0)
# AddInStart('Wano', 10, 380.0)


#sale('t', 'Tano', 1)
# cur.execute('SELECT total FROM start WHERE  name = ?', ('Amo', ))

print(outputTable('start'))

# print(a)
# cur.execute('DELETE FROM start')
# main_db.commit()



