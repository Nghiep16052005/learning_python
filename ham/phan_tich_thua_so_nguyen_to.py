# phan tich thua so nguyen to
# 30 = 2 * 3 * 5
# 60 = 2 * 2 * 3 * 5
import math
# ham phan tich thua so nguyen to
def pt(n):
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            # i la thua so nguyen to
            while n % i == 0:
                print(i, end = ' ')
                n //= i
        # neu n con lai lon hon 1 thi no la so nguyen to
    if n > 1:
        print(n)

if __name__ =="__main__":
    n = int(input("Nhap so n can phan tich: "))
    pt(n)

#neu da co phan tich thua so nguyen to roi thi co the tinh so uoc cua n
# neu n = p1^a1 * p2^a2 * ... * pk^ak
# so uoc cua n = (a1 + 1) * (a2 + 1) * ... * (ak + 1)
# so uoc cua 60 = (2+1) * (1+1) * (1+1)
