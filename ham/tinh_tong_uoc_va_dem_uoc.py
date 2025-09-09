#tinh tong uoc va dem uoc cua 1 so 
import math
def demuoc(n):
    cnt = 0 
    for i in range(1, math.isqrt(n)+1):
        if n % i == 0:
            cnt += 1 # i la uoc 
            if i != n // i:
                cnt +=1
    return cnt
def tonguoc(n):
    s = 0 
    for i in range(1,math.isqrt(n)+1):
        if n % i == 0:
            s += i #i la uoc
            if i != n // i:
                s += n // i # n//i la uoc  
    return s
if __name__ == '__main__':
    n = int(input("Nhap so n can dem uoc : "))
    print("So uoc cua n la: ", demuoc(n))
print(demuoc(n)) # 1,2,3,6
print(tonguoc(n)) # 1,2,3,6
# 1+2+3+6 = 12