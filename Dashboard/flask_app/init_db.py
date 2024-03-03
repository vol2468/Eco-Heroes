import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO kids (username, city, latitude, longitude) VALUES (?, ?, ?, ?)", ('john', 'Kelowna', 0, 0))
cur.execute("INSERT INTO kids (username, city, latitude, longitude) VALUES (?, ?, ?, ?)", ('arnold', 'Vancouver', 0, 0))

connection.commit()
connection.close()