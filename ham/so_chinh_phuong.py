import math 
def is_perfect_square(n):
    k = math.isqrt(n)
    return k*k == n

if __name__ == '__main__':
    n = int(input("nhap so nguyen duong n: "))
    if is_perfect_square(n):
        print("n la so chinh phuong")
    else:
        print("n khong la so chinh phuong ")