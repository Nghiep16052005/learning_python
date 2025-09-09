# li thuyet dong du de giai quyet bai toan co so nguyen lon
# cac tinh chat cua phep dong du:
# 1. (a + b) mod m = [(a mod m) + (b mod m)] mod m 
# hay (a+b)% c = ((a % c) + (b % c)) % c
# 2. (a * b) mod m = [(a mod m) * (b mod m)] mod m
# hay (a*b) % c = ((a % c) * (b % c)) % c
# 3. (a^k) mod m = [(a mod m)^k] mod m
# hay (a^k) % c = ((a % c)^k) % c
# vi du: tinh 2^1000 mod 7 = (2 mod 7)^1000 mod 7 = 2^1000 mod 7
# cach tinh 2^1000 mod 7 bang python: pow(2,1000,7) = 2
# cach tinh 2^1000 mod 7 bang li thuyet dong du:
# 2^1 mod 7 = 2
# 2^2 mod 7 = 4 
# 10 ** 9 +7 la so nguyen to lon, dung de tinh dong du 
#khi bai toan yeu cau chia du ket qua cho 1 so nao do --> tinh den dau chia du den do 
#(1.2.3...n) mod p = (1 mod p * 2 mod p * 3 mod p * ... * n mod p) mod p --->

#tinh n! mod p voi n la so nguyen lon va p la so nguyen to
def factorial_mod(n,p):
    res = 1
    for i in range(1,n+1):
        res = (res * (i % p)) % p
    return res

#tinh a **b chia du cho c voi a,b,c la so nguyen lon
def power_mod(a,b,c):
    res = 1
    for i in range(b):
        res *= a
        res %= c
    return res

