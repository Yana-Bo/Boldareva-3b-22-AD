from math import sqrt
ms = [(1,2),(3,4),(-1,5),(6,-3)]
sorted = sorted(ms, key=lambda ms: sqrt(ms[0]**2 + ms[1]**2), reverse=True)
print(sorted)