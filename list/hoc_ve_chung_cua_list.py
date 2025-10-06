# liet ke trong list thoa man tinh chat gi do 
from math import *
def nt(n):
    if n <2 : 
        return False
    for i in range(isqrt(n)+1):
        if n % i == 0 :
            return False 
    return True 

if __name__ =='__main__':
    n = int(input())
    a = list(map(int,input.split()))
    for x in a : 
        if nt(x):
            print(x,end=' ')
