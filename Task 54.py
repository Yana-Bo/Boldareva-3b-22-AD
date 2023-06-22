nm = input("Введите целое число: ")
try:
 nm = int(nm)
 if nm < 1:
  print("")
 else:
  result = list(range(1, nm+1))
  result.reverse()
  summ = sum(result)
  print("Сумма всех чисел до ", nm, " - ", summ)
except ValueError:
  print("Ошибка!")