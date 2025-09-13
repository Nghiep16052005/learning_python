"""
Bước 1: Gọi luythua(2,3)

b = 3 ≠ 0 → không vào return 1

Gọi half = luythua(2, 3 // 2) = luythua(2,1)

Bước 2: Gọi luythua(2,1)

b = 1 ≠ 0

Gọi half = luythua(2, 1 // 2) = luythua(2,0)

Bước 3: Gọi luythua(2,0)

b = 0 → return 1
Kết quả: luythua(2,0) = 1

Bước 4: Quay lại luythua(2,1)

half = 1

b = 1 (lẻ)
→ return a * half * half = 2 * 1 * 1 = 2
Kết quả: luythua(2,1) = 2

Bước 5: Quay lại luythua(2,3)

half = 2

b = 3 (lẻ)
→ return a * half * half = 2 * 2 * 2 = 8
Kết quả: luythua(2,3) = 8
"""
from math import *
def luythua(a,b):
    if b == 0 :
        return 1 
    half = luythua(a,b //2)
    if b % 2 == 0 :
        return half * half %(10 ** 9 +7)
    else:
        return a * half*half % (10 ** 9 +7)

if __name__ =='__main__':
    a,b = map(int,input().split())
    print(luythua(a,b))