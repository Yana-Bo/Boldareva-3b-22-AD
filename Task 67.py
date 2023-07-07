import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS books
(id INTEGER PRIMARY KEY, name TEXT, author TEXT, year INTEGER)''')

books = [('Мемуары Гейши', 'Артур Голден', 1997),
         ('Цвет волшебства', 'Терри Пратчетт', 1983),
         ('Американские боги', 'Нил Гейман', 2001),
         ('Мы', 'Евгений Замятин', 1924),
         ('1984', 'Джордж Оруэлл', 1949),
         ('Есть, молиться, любить', 'Элизабет Гилберт', 2006),
         ('Понедельник начинается в субботу', 'братья Стругацкие', 1965),
         ('Благие знамения', 'Терри Пратчетт', 1990)]

cursor.executemany("INSERT INTO books (name, author, year) VALUES (?, ?, ?)", books)
conn.commit()
cursor.execute('SELECT * FROM books WHERE year > 2000')
rows = cursor.fetchall()

for row in rows:
    print(f'Книга - {row[1]}, автор {row[2]}, год издания - {row[3]}')
conn.close()