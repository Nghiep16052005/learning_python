#tim uoc so nguyen to lon nhat cua mot so nguyen duong
"""Bước chạy tay với n = 36

Ban đầu:

n = 36, ans = -1

math.isqrt(36) = 6

Vòng lặp chạy i = 2 → 6.

i = 2:

36 % 2 == 0 → đúng.

ans = 2

Chạy while 36 % 2 == 0:

n = 36 // 2 = 18

n = 18 // 2 = 9

9 % 2 != 0 → dừng.

Sau khi xử lý xong i = 2:

n = 9, ans = 2.

i = 3:

9 % 3 == 0 → đúng.

ans = 3

Chạy while 9 % 3 == 0:

n = 9 // 3 = 3

n = 3 // 3 = 1

1 % 3 != 0 → dừng.

Sau khi xử lý xong i = 3:

n = 1, ans = 3.

i = 4, 5, 6:

n = 1 rồi → không chia hết nữa.

ans giữ nguyên = 3.

Kết thúc vòng for

Kiểm tra if n > 1: → n = 1 nên không vào.

Trả về ans = 3.
"""
import math 

def solve(n):
    ans = -1
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            ans = i 
            while n % i == 0:
                n //= i
    if n > 1:
        ans = n
    return ans

if __name__ == '__main__':
    n = int(input('nhap so nguyen duong n: '))
    print("uoc so nguyen to lon nhat cua n la: ",solve(n))