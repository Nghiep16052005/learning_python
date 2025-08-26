import math
n = int(input("Nhap n: "))
a = list(map(int, input("Nhap day so cach nhau boi dau cach: ").split()))
sum = 0
for x in a:
    tong += x
print("Tong cac so trong day la: ", sum)