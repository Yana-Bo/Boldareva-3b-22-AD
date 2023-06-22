ms1 = [1, 2, 3, 2, 1]
ms2 = ms1.copy()
ms2.reverse()
if ms1 == ms2:
    print('Массив является палиндромом')
else:
    print('Массив не является палиндромом')