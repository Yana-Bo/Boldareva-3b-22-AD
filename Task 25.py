nm = int(input("Введите число: "))
a = 2
b = 0
while nm > a:
    if nm % a == 0:
        b += 1
        break
    a += 1
if b:
    print("Данное число не является простым")
else:
    print("Данное число является простым")