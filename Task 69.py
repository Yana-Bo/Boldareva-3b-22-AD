import sqlite3

conn = sqlite3.connect('staff.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS staff
(id INTEGER PRIMARY KEY, name TEXT, position INTEGER, zp INTEGER)''')

staff = [('Вика', 'эксперт', 45000),
         ('Андрей', 'бухгалтер', 54000),
         ('Олег', 'менеджер', 34000),
         ('Валентина', 'экономист', 48500),
         ('Дарья', 'руководитель', 85000),
         ('Михаил', 'менеджер', 35000),
         ('Оксана', 'специалист', 45000),
         ('Алена', 'менеджер', 35000)]

cursor.executemany("INSERT INTO staff (name, position, zp) VALUES (?, ?, ?)", staff)
conn.commit()
cursor.execute('SELECT * FROM staff WHERE position = "менеджер"')
rows = cursor.fetchall()

for row in rows:
    print(f'Имя - {row[1]}, должность - {row[2]}, зарплата {row[3]} р.')

conn.close()