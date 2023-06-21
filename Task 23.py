ms = [i for i in range(10)]
num = int(input('Введите число: '))
print(ms)
if num in ms:
    print("Число", num, "найдено в массиве")
else:
    print("Число", num, "не найдено в массиве")