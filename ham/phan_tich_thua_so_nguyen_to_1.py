"""
Chạy tay với n = 36

Nhập 36 → gọi print(pt(36)).

Bên trong hàm pt(36):

math.isqrt(36) = 6

Vòng for i in range(2, 7) → i = 2, 3, 4, 5, 6

i = 2

36 % 2 == 0 

mu = 0

36 % 2 == 0 → mu = 1, n = 18

18 % 2 == 0 → mu = 2, n = 9

9 % 2 != 0 → dừng while

In: print(2, 2, sep='^', end='') → màn hình: 2^2

n = 9 ≠ 1 → in thêm dấu *
→ màn hình: 2^2*
"""
import math 

def pt(n):
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            mu = 0
            while n % i == 0:
                mu += 1
                n //= i
            print(i,mu,sep = '^',end = '')
            if n != 1:
                print('*', end = '')
    if n > 1:
        print(n,1,sep = '^')# 1 la so mu 

if __name__ == '__main__':
    n = int(input('hay nhap so nguyen duong n'))
    pt(n)
                