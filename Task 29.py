def reverse_str(result):
 if len(result) == 0:
  return result
 else:
  return reverse_str(result[1:]) + result[0]
str1 = input("Введите последовательность символов: ")
reverse_str = reverse_str(str1)
print("Перевернутая строка:", reverse_str)