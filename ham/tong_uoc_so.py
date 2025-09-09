#tinh tong uoc cua so nguyen duong n
import math 
def sum_divisors(n):
    total = 0 
    for i in range(1,math.isqrt(n)+1):
        if n % i == 0:
            total += i 
            if  i != n//i:
                total += n // i
    return total

if __name__ == '__main__':
    n = int(input("nhap so nguyen duong n: "))
    print("tong uoc cua so nguyen duong n la:",sum_divisors(n))