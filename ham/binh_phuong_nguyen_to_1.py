"""
viet chuong trinh kiem tra 1 so n khi no dong thoi vua
chia het cho 1 so nguyen to vua chia het cho binh phuong 
cua so nguyen to do """

"""
 trong số nếu n chia hết cho b mũ m thì với mọi số mũ
 nhỏ hơn k < m , ta cung có n chia hết cho b mũ k """

import math 
def nt(n):
    if n <2 :
        return False 
    for i in range(i , math.isqrt(n)+1):
        if n % i == 0 : 
            return False
    return True 

def check(n):
    for i in range ( 2,math.isqrt(n)+1):
        if n % i == 0: # tim duoc uoc so cua i
            dem = 0 
            while n % i ==0 :
                dem += 1 
                n //= i
            if dem >= 2:
                return True 
    return False 

if __name__ =='__main__':
    a,b = map(int,input('nhap so a va b: ').split())
    for i in range (a, b+1):
        if check(i):
            print(i,end = ' ')