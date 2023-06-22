a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = 2
ms = []
while c <= a:
    if a % c == 0:
        ms.append(c)
    c += 1
c = 2
while c <= b:
    if b % c == 0:
        if c in ms:
            break
    c += 1
print(f"Наименьший общий множитель : {c}")