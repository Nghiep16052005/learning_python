"""dua ra so nguyen to thu k phan tich thua so nguyen
to cua mot so nguyen duong n
n = 28 , k= 3 ta co ket qua la 7 
vi 28 = 2 *2*7"""  
from math import *

def nt(n):
    if n < 2:  
        return False
    for i in range(2, isqrt(n) + 1):  # duyệt từ 2 -> √n
        if n % i == 0:   # nếu chia hết thì không phải số nguyên tố
            return False
    return True   # không chia hết cho số nào thì là số nguyên tố

def solve(n, k):
    dem = 0   # đếm số lượng thừa số nguyên tố
    for i in range(2, isqrt(n) + 1):  # duyệt từ 2 -> √n
        if n % i == 0:   # nếu i là ước của n
            while n % i == 0:   # tách hết các thừa số i
                dem += 1
                if dem == k:   # nếu đạt đến thừa số nguyên tố thứ k
                    return i   # trả về i
                n //= i   # giảm n đi

    if n != 1:   # sau khi chia hết, nếu n vẫn > 1 thì chính nó cũng là số nguyên tố
        dem += 1
    if dem == k:
        return n
    return -1 
        

