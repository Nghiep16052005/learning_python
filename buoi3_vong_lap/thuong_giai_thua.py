import math
n = int(input('nhap so nguyen duong n : '))
res = 0
for i in range(n):
    res += 1/ math.factorial(i)

print("%.4f"%res)