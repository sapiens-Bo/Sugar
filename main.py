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

main_db.commit()

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
    pass

def CalcRemaind():
    pass

def delFromStart(name: str):
    pass

AddInStart('Amo', 10, 380.0)
cur.execute('SELECT * FROM start')
print(cur.fetchall())
# cur.execute('DELETE FROM start')
# main_db.commit()




