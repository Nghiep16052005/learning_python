# cho 2 so a va b tim uoc chung lon nhat cua a giai thua va b giai thua
#Với hai số nguyên dương 𝑎 , 𝑏 a,b, ƯCLN(a, b) là số nguyên dương lớn nhất chia hết cho cả 𝑎 a và 𝑏 b.
from math import *
a,b = map(int, input('nhap 2 so nguyen a va b :').split())
print(factorial(min(a,b)))