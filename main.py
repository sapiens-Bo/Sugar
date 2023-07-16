import sqlite3

main_db = sqlite3.connect('maindb.db')
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

how_list = ['t', 'c', 'mb']

# Добавить новую запись в таблицу старт.
def AddInStart(name: str, total: int, price: float):
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
            if how in how_list:
                cur.execute('SELECT * FROM sales WHERE how = ? AND name = ?', (how, name))
                sales = cur.fetchall()
                print(len(sales), sales)
                *a, t, s = sales[0]
                t += total
                print(total, t)
                if len(sales) < 1:
                    cur.execute('INSERT INTO sales VALUES(?, ?, ?, ?)', (how, name, total, price * t))
                    main_db.commit()
                else:
                    # цена не изменяется тк не проходит проверку на количество в start
                    cur.execute('UPDATE sales SET total = ?, sum = ? WHERE how = ? AND name = ?', (t, price * t, how, name))
                    main_db.commit()
            else:
                print('Продажа > Наличия')

        # берем цену за еденицу
        
                 
        

def CalcRemaind():
    pass

def delFromStart(name: str):
    pass

# AddInStart('Nano', 10, 380.0)
# AddInStart('Tano', 10, 100.0)
# AddInStart('Vano', 10, 200.0)
# AddInStart('Rano', 10, 320.0)
# AddInStart('Wano', 10, 380.0)


sale('t', 'Tano', 1)
# cur.execute('SELECT total FROM start WHERE  name = ?', ('Amo', ))

# print(a)
# cur.execute('DELETE FROM start')
# main_db.commit()



