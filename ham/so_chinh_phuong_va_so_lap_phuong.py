# cach thanh so chinh phuong va so lap phuong
# ta chi can can bac 2 va bac 3 cua so do roi so sanh nhan nguoc lai 

import math
# ham kiem tra so chinh phuong
def square(n):
    r = math.isqrt(n)# r la can bac 2 cua n
    return r * r == n
# ham kiem tra so lap phuong
def cube(n):
    r = round(n ** (1/3)) # r la can bac 3 cua n
    return r * r * r == n

if __name__ == "__main__":
    n = int(input("Nhap so nguyen duong n: "))
    if square(n):
        print(n, "la so chinh phuong")
    else:
        print(n, "khong phai la so chinh phuong")
    if cube(n):
        print(n, "la so lap phuong")
    else:
        print(n, "khong phai la so lap phuong")