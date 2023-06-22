nm = int(input("Сколько чисел ряда Фибоначчи нужно вывести? -  "))
result = [0, 1]
while len(result) < nm:
 result.append(result[-1] + result[-2])
print(result)