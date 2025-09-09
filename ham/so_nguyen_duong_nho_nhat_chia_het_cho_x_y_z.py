"""
cho 4 so nguyen duong x,y,z,n. tim so nguyen duong nho nhat 
co n chu so chia het cho ca x,y, z"""

"""
Bước 1: Nhập vào
x = 2, y = 3, z = 5, n = 3

Bước 2: Tính bội chung nhỏ nhất (bc)

lcm(2, 3) = 6

lcm(6, 5) = 30
→ bc = 30

Bước 3: Tìm số nhỏ nhất có n chữ số

tmp = 10^(n - 1) = 10^(3 - 1) = 100

Bước 4: Tìm bội của bc ≥ tmp

(tmp + bc - 1) // bc = (100 + 30 - 1) // 30 = 129 // 30 = 4

ans = 4 * 30 = 120

Bước 5: Kiểm tra số chữ số

10^n = 10^3 = 1000

ans = 120 < 1000 → hợp lệ
"""
from math import * 
def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == '__main__':
    x, y, z, n = map(int, input().split())
    bc = lcm(lcm(x, y), z)
    # tim so nho nhat >= 10 ^(n-1) chia het cho boi chung 
    tmp = 10 ** (n - 1)
    ans = (tmp + bc - 1) // bc * bc
    if ans < 10 ** n:
        print(ans)
    else:
        print(-1)
