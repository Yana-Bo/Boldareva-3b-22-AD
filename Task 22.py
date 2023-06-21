import random
ms = []
for i in range(10):
 ms.append(random.randint(1, 10))
print("Массив: ", ms)
ms_sum = sum(ms)
print("Сумма всех элементов массива: ", ms_sum)