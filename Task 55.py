try:
    nm_list = tuple(map(int, input("Введите список целых чисел через запятую: ").split(",")))
    print(f"Минимальное число: {min(nm_list)}")
except ValueError:
    print("Неверный формат числа")