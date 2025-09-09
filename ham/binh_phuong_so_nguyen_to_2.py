"""
khi neu no chia het cho mot so nguyen to nao do 
thi cung phai chia het cho binh phuong cua so nguyen to do """

from math import isqrt   # isqrt(n) = căn bậc hai nguyên của n


def check(n):
    # Duyệt qua tất cả các số từ 2 đến căn bậc hai của n
    for i in range(2, isqrt(n) + 1):
        # Nếu i là ước của n
        if n % i == 0:
            dem = 0   # đếm số mũ của thừa số i trong n
            # Chia n cho i nhiều lần nhất có thể
            while n % i == 0:
                dem += 1
                n //= i
            # Nếu số mũ của i chỉ bằng 1 → không thỏa điều kiện
            if dem == 1:
                return False

    # Sau vòng lặp, nếu n vẫn còn > 1 thì nó là 1 thừa số nguyên tố lớn
    # Trường hợp này, nếu nó xuất hiện mà chỉ bậc 1 → cũng không hợp lệ
    if n != 1:
        return False

    # Nếu qua tất cả kiểm tra thì n thỏa mãn (mọi thừa số nguyên tố có số mũ ≥ 2)
    return True
