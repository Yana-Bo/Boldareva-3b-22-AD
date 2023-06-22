f = str(input('Введите имя необходимого файла: '))
try:
    with open(f, 'r') as file:
        print(file.read())
except Exception:
    print("Ошибка")