ms1 = [24, 36, 48, 60]
ms2 = [12, 18, 24, 36, 72]
def gcd(nm1, nm2):
 while nm2 != 0:
  nm1, nm2 = nm2, nm1 % nm2
  return nm1
def gcd_arr(arr):
 result = arr[0]
 for i in range(1, len(arr)):
  result = gcd(result, arr[i])
  return result
result = ms1 + ms2
result.sort()
result = gcd_arr(result)
print(result)