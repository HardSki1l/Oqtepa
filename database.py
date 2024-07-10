import sqlite3

connect = sqlite3.connect('oqtepa.db')
cursor = connect.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS savat (id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER , product_name TEXT,count INTEGER)")

connect.commit()





cursor.execute('INSERT INTO products VALUES(?,?,?,?)', ())