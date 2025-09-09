# so hoan hao va dinh li euclid
# so hoan hao la so bang tong cac uoc so nguyen duong nho hon no
# vi du: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
#dinh li euclid: neu p la so nguyen to va 2^p - 1 
# cung la so nguyen to thi so hoan hao duoc tinh bang cong thuc: n = 2^(p-1) * (2^p - 1)
# vi du: p = 2, 2^2 - 1 = 3 la so nguyen to, n = 2^(2-1) * (2^2 - 1) = 6 la so hoan hao
# p = 3, 2^3 - 1 = 7 la so nguyen to, n = 2^(3-1) * (2^3 - 1) = 28 la so hoan hao
#cach 1: kiem tra so hoan hao bang cach tinh tong cac uoc so, cach nay rat cham
import math
def perfect_number(n):
    tong = 1
    for i in range(1,math.isqrt(n)+1):
        if n % i == 0:
            tong += i
            if i != n //i:
                tong += n // i
    return tong == n

# cach 2: kiem tra so hoan hao bang dinh li euclid, cach nay nhanh hon

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def perfect_number_euclid(p): # neu p la so nguyen to 
    if is_prime(2**p - 1): # va 2^p - 1 la so nguyen to
        return 2**(p-1) * (2**p - 1) # so hoan hao duoc tinh bang cong thuc
    else:
        return -1 # khong phai so hoan hao

# vi du: perfect_number(6) = True, perfect_number(28) = True
if __name__ == "__main__":      
    n = int(input("Nhap so nguyen duong n: "))
    if perfect_number(n):
        print(n, "la so hoan hao")
    else:
        print(n, "khong phai la so hoan hao")
    m = int(input("Nhap so nguyen to p: "))
    hn = perfect_number_euclid(m)
    if hn != -1:
        print("So hoan hao tuong ung voi p =", m, "la:", hn)
    else:
        print(m, "khong phai so nguyen to hoac 2^p - 1 khong phai so nguyen to")
# 6 la so hoan hao
# 28 la so hoan hao
# So hoan hao tuong ung voi p = 2 la: 6
# So hoan hao tuong ung voi p = 3 la: 28