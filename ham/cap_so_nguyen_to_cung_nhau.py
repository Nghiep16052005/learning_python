"""
“Liệt kê các cặp số nguyên tố cùng nhau và có giá trị
 khác nhau trong đoạn [a; b] theo thứ tự từ nhỏ đến lớn.”
""" 
from math import * 

#ham kiem tra nguyen to 
def nt (n):
    if n < 2 : 
        return False 
    for i in range(2, isqrt(n)+1): 
        if n % i == 0 : 
            return False 
        return True 

def lcm (a,b):
    return a * b // gcd(a,b)

if __name__ == '__main__':
    a,b = map(int,input('nhap so a va b: '))
    for i in range(a,b):
        for j in range(i+1, b+1):
            if gcd(i,j) == 1: # nguyen to cung nhau thi uoc chung lon nhat la 1 
                print("(",i,",",j,")",sep= '')