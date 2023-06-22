try:
    with open('test.txt', 'r') as file:
        t = file.read()
        print(t)
except FileNotFoundError:
    print('Файл не найден')
