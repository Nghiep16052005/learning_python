"""
so dep la so thuan nghich 
co it nhat 3 uoc so nguyen to khac nhau"""


""""
Hàm check(585):

dem = 0

Duyệt i từ 2 đến isqrt(585) = 24

i = 2 → 585 % 2 ≠ 0 → bỏ qua.

i = 3 → 585 % 3 = 0

dem = 1

Chia liên tục:

585 // 3 = 195

195 // 3 = 65 (không chia tiếp được)
→ Sau bước này: n = 65

i = 4 → bỏ qua.

i = 5 → 65 % 5 = 0

dem = 2

Chia liên tục:

65 // 5 = 13 (không chia tiếp được)
→ Sau bước này: n = 13

i chạy tiếp đến 24, nhưng lúc này n = 13 rồi.

Sau vòng lặp:

n = 13 (lớn hơn 1) → cộng thêm dem = 3
"""
#viet chuong trinh in ra so dep trong doan tu a va b 
import math 
#ham viet so thuan nghich
def tn(n):
    temp = n
    rev = 0 
    while n != 0 :
        rev = rev * 10 + n % 10
        n //= 10 
    return rev == temp 
 #viet ham kiem tra so dep 
def check(n):
    dem = 0
    for i in range(2, math.isqrt(n) + 1):   # duyệt i từ 2 đến căn bậc 2 của n
        if n % i == 0:                 # nếu i chia hết n
            dem += 1                   # đếm thêm 1 ước số (nguyên tố)
            while n % i == 0:          # chia hết cho i nhiều lần thì cứ chia
                n //= i
    if n != 1:                         # sau khi chia xong, nếu n còn > 1
        dem += 1                       # thì n chính là 1 ước nguyên tố cuối
    return dem >= 3                    # trả về True nếu có ít nhất 3 ước nguyên tố khác nhau

if __name__ =='__main__':
    a,b = map(int,input('nhap trong doan tu a den b: ').split())
    dem = 0 
    for i in range(a,b+1):
        if tn(i) and check(i):
            print(i, end = ' ')
            dem += 1
    if dem == 0:
        print(-1)