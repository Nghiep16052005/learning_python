from math import *
n = int(input('nhap vao so nguyen duong n : '))
"""#cach 1 --> cach ngu 
n = int(input('nhap vao so nguyen duong n : '))
tong = 0
for i in range(1,n+1):
    if(n%i == 0):
        tong += i

print(tong)"""
# cach 2: cach khon 
"""
a = 1
b = 60 
1 <60 
nghia la neu i la uoc cua n thi n/ i cung la uoc cua n vay thoi 
"""
tong = 0
for i in range(1,isqrt(n)+1):
    if n%i ==0 :
        tong += i
        if n//i != i:
            tong += n//i

print(tong)
