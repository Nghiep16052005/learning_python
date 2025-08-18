from math import *
n = int(input('nhap so nguyen duong n: '))
# so chinh phuong (so hinh nguyen ) duoc tao thanh tu binh phuong 1 so nguyen 
# ta co bpt 1 <= p**2(la so chinh phuong) <= n 
for i in range(1,isqrt(n)+1):
    print(i**2,end=" ")
