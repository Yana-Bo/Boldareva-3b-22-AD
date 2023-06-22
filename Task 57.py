import os
a = input('Введите путь к директории: ')
b = input('Введите расширение в формате .xlsx: ')
try:
    for root, dirs, files in os.walk(a):
        for filename in files:
            if b in filename:
                print(filename)
except Exception:
    print('Ошибка')