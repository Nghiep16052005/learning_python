from math import *
x,y,z,t = map(int, input().split())
result = sqrt(pow(abs(x-z),2) + pow(abs(y-t),2))
print('khoang cach euclid giua 2 diem trong oxy:',"%.2f" %result)
