try:
 f1 = input("Введите имя файла с расширением:  ")
 with open(f1, "r") as file:
  words = file.read().split()
  result = [word[::-1] for word in words]
  result1= max(set(result), key=result.count)
  often_word = result1[::-1]
  print(often_word)
except FileNotFoundError:
  print("Ошибка!")