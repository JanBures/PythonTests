import sqlite3

conn = sqlite3.connect("db-diary.db")

cur = conn.cursor()
cur.execute('SELECT * from diar')
print(cur.fetchall())
