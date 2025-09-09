"""
so thuan nguyen to la so nguyen to 
tat ca chu so la so nguyen to
tong chu so cua no la 1 so nguyen to

23 là số nguyên tố

Chữ số 2 và 3 đều nguyên tố

Tổng = 2 + 3 = 5 (nguyên tố) → Thoả mãn"""

# cho doan a,b dem co bao nhieu chu thuan nguyen to 
import math 
def nt(n):
    if n < 2 : 
        return False
    for i in range(2,math.isqrt(n)+1 ):
        if n % i == 0:
            return False
    return True 
# cach 1 : cach nay khong ngon 
def check1(n):
    #kiem tra xem ban than n co phai la nguyen to hay khong 
    if not nt(n):
        return False 
    sum = 0 
    while n != 0:
        tmp = n %10 
        # neu tmp khong phai la so nguyen to thi sai luon 
        if not nt(tmp):
            return False
        tong = tmp 
        n //= 10 
    return nt(tong) # tra ve true hoac False 

# cach 2 : cach nay kiem tra chu so 2,3,5,7 
def check2(n):
    tong = 0 
    while n != 0:
        r = n%10 
        if r != 2 and r != 3 and r != 5 and r != 7:
            return False
        tong += r
        n //= 10 
    return nt(tong)
# kiem tra so thuan nguyen to trong doan tu a den b 

if __name__ == '__main__':
    a,b = map(int,input('bat dau tu a va ket thuc o b: ').split())
    for i in range(a , b+1):
        if check1(i):
            print(i, end=' ')
