#liet ke nhung so nguyen to nho hon N va co tong chu so cua no 
#mot so trong day so fibonaci 

#ham nguyen to 
from math import * 
def nt(n):
    if n < 2 : 
        return False 
    for i in range(2, isqrt(n)+1):
        if n % i == 0 :
            return False 
    return True 

def check_fibo(n):
    if n == 1 : 
        return True
    fn1 = 1 
    fn2 = 1
    for i in range(2 , n+1):
        fn = fn1 + fn2 
        if fn == n : 
            return True 
        fn2, fn1 = fn1 ,fn 
    return False

def tong (n):
    s = 0 
    while n != 0 : 
        s += n%10 
        n //= 10 
    return s 

if __name__ =='__main__':
    n = int(input('nhap so fibonaci thu n: '))
    for i in range(n):
        if nt(i)and check_fibo(tong(i)):
            print(i,end = ' ')