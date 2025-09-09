
# so co so luong uoc le la so chinh phuong 
# vi ex : 16 la so chinh phuong no se di theo cap 
"""
1 -- 16
2 -- 8 
4 khong di duoc voi 4 nen no la uoc le""" 
import math 
def has_odd_divisors_count(n):
    k = math.isqrt(n)
    return k * k  == n

if __name__ == '__main__':
    n = int(input('nhap so n: '))
    if has_odd_divisors_count(n):
        print('YES')
    else:
        print('NO')
