from math import *
def nt(n):
    if n < 2:
        return False
    for i in range(2,isqrt(n)+1):
        if n % i == 0:
            return False 
    return True 

if __name__ =='__main__':
    n = int(input('hay nhap vao gia tri cua phan tu a: '))
    a = list(map(int,input().split()))
    cnt,sum = 0,0
    for x in a:
        if nt(x):
            cnt += 1
            sum += x 

    print("trung binh cong cua day so nguyen to la: %.3f"% (sum/cnt))
