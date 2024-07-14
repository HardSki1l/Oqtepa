import sqlite3

connect = sqlite3.connect('oqtepa.db')
cursor = connect.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY AUTOINCREMENT, product_name TEXT,img TEXT,  price INTEGER, tavsif TEXT, count_1 INTEGER)")

cursor.execute(
    "CREATE TABLE IF NOT EXISTS savat (id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER , product_name TEXT,count INTEGER)")



cursor.execute('DROP TABLE IF EXISTS counts')
cursor.execute('''CREATE TABLE IF NOT EXISTS counts (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    user_id INTEGER UNIQUE, 
    count_1 INTEGER DEFAULT 0
)''')
connect.commit()


async def check_count(user_id):
    result = cursor.execute('SELECT * FROM counts WHERE user_id = ?', (user_id,)).fetchone()
    if not result:
        cursor.execute('INSERT INTO counts (user_id, count_1) VALUES (?, ?)', (user_id, 0))
        connect.commit()


def add_in_savat(user_id, product_name, count):
    cursor.execute("INSERT INTO savat (user_id, product_name, count) VALUES (?, ?, ?)", (user_id, product_name, count))
    connect.commit()