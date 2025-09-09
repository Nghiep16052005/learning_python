"""
Số hoàn hảo (perfect number) là một số nguyên dương bằng đúng tổng các ước số dương của nó
 (không kể chính nó)."""


"""
so hoan hao duoc tinh theo cong thuc 
shh = 2 ^ p-1 *(2^p -1)
"""
import math
def nt(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
 

def check(n):
    for i in range(2, 33):   # duyệt i từ 2 đến 32
        if nt(i) and nt(2 ** i - 1):   # i là số nguyên tố & 2^i - 1 cũng là số nguyên tố (Mersenne prime)
            if (2 ** i - 1) * (2 ** (i - 1)) == n:   # công thức số hoàn hảo
                return True
    return False
