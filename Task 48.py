ms = [5,7,11,13,15,20,25]
result = []
while ms:
 nm = ms.pop()
 if nm > 10:
  result.append(nm)
result1 = sum(result)/len(result)
print(result1)