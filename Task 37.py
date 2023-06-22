nm = input("Введите числа через пробел: ").split()
nm = [int(nm) for nm in nm]
min = sorted(nm)
print("Два наименьших числа: ", min[0], min[1])