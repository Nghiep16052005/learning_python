# so smith khong phai la so nguyen to, bang tong cac chu so cua tat ca cac thua so nguyen to 
# cua no 
"""
ex: 
b1: tong cua chu so 666 = 6+6+6 = 18 
b2: phan tich thua so nguyen to
666 = 2*3*3*37 = 2+3+3+3+7 = 18
666 la mot so smith
"""

"""
Bước 1: Tính tổng chữ số ban đầu
sum1 = sum_digit(666) = 6+6+6 = 18
sum2 = 0
tmp = 666

Bước 2: Phân tích thừa số nguyên tố bằng vòng lặp

Ta duyệt i từ 2 → √666 ≈ 25.8 → đến 25.

i = 2:

666 % 2 == 0 → đúng → vào while.

while n % 2 == 0:

sum2 += sum_digit(2) = 0 + 2 = 2

n //= 2 → n = 333

Thoát while (333 % 2 ≠ 0).

sum2 = 2, n = 333.

i = 3:

333 % 3 == 0 → đúng → vào while.

while n % 3 == 0:

sum2 += sum_digit(3) = 2 + 3 = 5

n //= 3 → n = 111

111 % 3 == 0 → tiếp tục while:

sum2 += sum_digit(3) = 5 + 3 = 8

n //= 3 → n = 37

37 % 3 ≠ 0 → thoát while.

 sum2 = 8, n = 37.

i = 4 → 25:

Không chia hết cho 37 nên bỏ qua.

Bước 3: Xử lý n còn lại

Sau vòng for, n = 37 (> 1)

sum2 += sum_digit(37) = 8 + (3+7) = 18

sum2 = 18.

Bước 4: So sánh

sum1 = 18

sum2 = 18

 sum1 == sum2 → return True
"""
import math
def sum_digit(n):
    sum = 0
    while n != 0 :
        sum += n %10 
        n //= 10
    return sum 

def check(n):
    sum1 = sum_digit(n)   # Tổng chữ số của n
    sum2 = 0              # Tổng chữ số của các thừa số nguyên tố
    tmp = n               # Lưu lại n ban đầu

    # Phân tích thừa số nguyên tố
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            while n % i == 0:       # Lặp khi i còn chia hết n
                sum2 += sum_digit(i)
                n //= i             # Giảm n dần

    # Nếu n không thay đổi -> tức là n là số nguyên tố
    if tmp == n:
        return False   # số nguyên tố không phải số Smith

    # Nếu sau vòng lặp n vẫn > 1 -> còn lại một thừa số nguyên tố lớn
    if n > 1:
        sum2 += sum_digit(n)

    # So sánh tổng chữ số của n và tổng chữ số của thừa số nguyên tố
    return sum1 == sum2

if __name__ == '__main__':
    n = int(input('hay nhap vao chu so cua n:'))
    if check(n):
        print("YES")
    else:
        print("NO")