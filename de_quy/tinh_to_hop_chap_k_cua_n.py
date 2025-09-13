# to hop chap k cua n duoc tinh theo cong thuc : kCn = (k-1)C(n-1) + kC(n-1) 
"""
tohop(3,2) 
= tohop(2,1) + tohop(2,2)
Bước 2: Tính tohop(2,1)
Sao chép mã
tohop(2,1) 
= tohop(1,0) + tohop(1,1)
tohop(1,0) = 1 (vì k = 0)

tohop(1,1) = 1 (vì n = k)

tohop(2,1) = 1 + 1 = 2

Bước 3: Tính tohop(2,2)
java
Sao chép mã
tohop(2,2) = 1   (vì n = k)
Bước 4: Quay lại tohop(3,2)
markdown
Sao chép mã
tohop(3,2) = tohop(2,1) + tohop(2,2)
           = 2 + 1

tohop(3,2) = 3
"""
def tohop(n,k):
    if k == 0 or n == k : 
        return 1
    else:
        return tohop(n-1, k-1) + tohop(n-1,k)