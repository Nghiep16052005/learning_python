# Sphenic là tích của ba số nguyên tố khác nhau 
# 30 = 2 × 3 × 5 (có 3 thừa số nguyên tố khác nhau: 2, 3, 5).
# 42 = 2 × 3 × 7 (có 3 thừa số nguyên tố khác nhau: 2, 3, 7).
# 100 = 2² × 5² (không phải số Sphenic vì thừa số 2 và 5 lặp lại với lũy thừa > 1).

"""
Tư duy của code:

Khởi tạo: cnt = 0 để đếm số lượng thừa số nguyên tố khác nhau.

Vòng lặp for: duyệt từ 2 đến căn bậc hai của n.

Nếu i là ước của n → kiểm tra số mũ mu.

Dùng vòng while để chia nhiều lần, nếu mu ≥ 2 → loại (vì Sphenic yêu cầu mũ = 1).

Nếu hợp lệ thì tăng cnt lên 1.

Sau vòng lặp: nếu còn dư n > 1 thì đây là 1 thừa số nguyên tố lớn (lớn hơn √n), tăng cnt.

Kết quả cuối: chỉ trả về True nếu cnt == 3.
"""
#kha nang la bi timelimit khi code bang vong for 
import math
def sphenic(n):
    cnt = 0
    for i in range(2,math.isqrt(n)+1 ):
        if n % i == 0:
            mu = 0 
            while n % i == 0:
                mu += 1
                n //= i 
            if mu >= 2:
                return False
            cnt += 1
    if n > 1: 
        cnt += 1
    return cnt == 3

from math import *

def sphenic1(n):
    cnt = 0   # đếm số lượng thừa số nguyên tố khác nhau
    for i in range(2, isqrt(n) + 1):   # duyệt từ 2 đến √n
        if n % i == 0:   # nếu i chia hết n → i là thừa số
            mu = 0       # biến mu đếm số mũ của i
            while n % i == 0:   # chia hết bao nhiêu lần thì đếm
                mu += 1
                n //= i
            if mu >= 2:   # nếu có mũ ≥ 2 → không phải Sphenic
                return False
            cnt += 1      # có 1 thừa số nguyên tố hợp lệ
    if n > 1:   # còn lại 1 thừa số nguyên tố lớn hơn √n
        cnt += 1
    return cnt == 3   # chỉ đúng nếu có đúng 3 thừa số nguyên tố khác nhau

if __name__ == '__main__':
    n = int(input('hay nhap so nguyen dung n:'))
    if sphenic1(n):
        print(n , "la so sphenic.")
    else:
        print(n,"khong phai la so sphenic.")

