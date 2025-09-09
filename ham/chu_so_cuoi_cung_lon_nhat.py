"""
nhap vao n va liet ke cac so nguyen to thoa man
nho hon hoac bang n va co chu so cuoi cung lon nhat
co bao nhieu so nhu vay  """
import math 
def nt(n):
    if n < 2:
        return False
    for i in range(2,math.isqrt(n)+1):
        if n % i ==0 : 
            return False 
    return True 

def check(n):
    tmp = n%10 
    while n != 0 : 
        if n% 10 > tmp :
            return False 
        n //= 10 
    return True 

if __name__ =='__main__':
    n = int(input('nhap n: '))
    count = 0 
    for i in range(n):
        if nt(i) and check(i):
            count += 1 
            print(i,end = ' ')
    
    print()
    print(count)