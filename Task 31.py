from calculator import Calculator
cl1 = Calculator()
n1=int(input('Введите первое число'))
n2=int(input('Введите второе число'))
print(cl1.add(n1, n2))
print(cl1.sub(n1, n2))
print(cl1.multiply(n1, n2))
print(cl1.divide(n1,n2))