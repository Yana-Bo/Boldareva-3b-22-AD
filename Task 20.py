import random
ms = []
for i in range(10):
 num = random.randint(1, 100)
 ms.append(num)
print("Массив: ", ms)
max_num = max(ms)
min_num = min(ms)
print("Максимальное число: ", max_num)
print("Минимальное число: ", min_num)