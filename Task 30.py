ms_a = set('aeiouy')
ms_b = set('bcdfghjklmnpqrstvwxz')
ms_c = set('аиоуыэ')
ms_d = set('бвгджзйклмнпрстфхцчшщ')
str1 = input('Введите последовательность символов: ')
n1 = 0
n2 = 0
for i in range(len(str1)):
    if str1[i] in ms_a:
        n1 += 1
    if str1[i] in ms_b:
        n2 += 1
    if str1[i] in ms_c:
        n1 += 1
    if str1[i] in ms_d:
        n2 += 1
print(f"В вашей строке {n1} гласных и {n2} согласных")