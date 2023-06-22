str1 = input("Введите последовательность символов: ")
str1 = str1.lower()
a = {}
for i in range(len(str1)):
    if str1[i] == " ":
        continue
    if str1[i] in a.keys():
        a[str1[i]] += 1
    else:
        a[str1[i]] = 1
print(a)