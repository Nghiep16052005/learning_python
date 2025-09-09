"""theo Goldbach conjecture mot so nguyen duong chan >= 4 deu co the bieu dien
duoi dang cua tong 2 so nguyen to. cho so nguyen to
chan N >=4
hay liet ke cac cap so nguyen to p q co tong dung z
bang N. vi du N = 16 ta co 1 cap so nguyen to z
la 3+3 = 6"""


"""
Chạy từng vòng lặp với n = 10

i = 2
→ n - i = 10 - 2 = 8
is_prime(2) = True, is_prime(8) = False →  không in

i = 3
→ n - i = 10 - 3 = 7
is_prime(3) = True, is_prime(7) = True →  in ra (3, 7)

i = 4
→ n - i = 10 - 4 = 6
is_prime(4) = False →  không in

i = 5
→ n - i = 10 - 5 = 5
is_prime(5) = True, is_prime(5) = True →  in ra (5, 5)
"""
import math

# Hàm kiểm tra số nguyên tố
def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input("hay nhap so luong test case : "))
    for _ in range(t):
        n = int(input())
        for i in range(2, n // 2 + 1):
            if nt(i) and nt(n - i):
                print(i, n - i)

