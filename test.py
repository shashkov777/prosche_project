import sqlite3
import db

conn = sqlite3.connect('userfile.db')
cur = conn.cursor()

cur.execute("SELECT * FROM users")
users = cur.fetchall()

info = ''

for el in users:
    info += f'Телефон: {el[1]}, имя: {el[2]}, айдишник: {el[3]}\n'

cur.close()
conn.close()    

print(info)