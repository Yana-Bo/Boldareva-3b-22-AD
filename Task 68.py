import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies
(id INTEGER PRIMARY KEY, name TEXT, genre TEXT, rating REAL)''')

movies = [('Клаус', 'мультфильм', 8.2),
          ('Логан', 'боевик', 8.1),
          ('Джокер', 'драма', 8.4),
          ('Паразиты', 'драма', 8.5),
          ('Душа', 'мультфильм', 8.0),
          ('Митчеллы против машин', 'мультфильм', 7.6),
          ('Земля кочевников', 'драма', 7.3)]

cursor.executemany("INSERT INTO movies (name, genre, rating) VALUES (?, ?, ?)", movies)
conn.commit()
cursor.execute('SELECT * FROM movies WHERE genre = "мультфильм"')
rows = cursor.fetchall()

for row in rows:
    print(f'Фильм - {row[1]}, жанр {row[2]}, рейтинг: {row[3]}')

conn.close()