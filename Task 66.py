import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students
(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, average_score REAL)''')

sts_data = [('Виктория', 17, 4.1),
                 ('Алена', 18, 3.9),
                 ('Яна', 22, 4.6),
                 ('Анна', 25, 3.2),
                 ('Олег', 23, 4.0),
                 ('Станислав', 19, 3.8),
                 ('Дмитрий', 21, 4.2),
                 ('Михаил', 24, 4.8)]

cursor.executemany("INSERT INTO students (name, age, average_score) VALUES (?, ?, ?)", sts_data)
conn.commit()
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(f'Имя: {row[1]}, Возраст: {row[2]}, Средний балл: {row[3]}')

conn.close()