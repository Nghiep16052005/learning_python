"""
kiem tra so nhap vao la chan hay le. cac ban phai tra loi nhieu truong hop .
dong dau tien la so luong truong hop T
T dong tiep theo moi dong la mot so nguyen duong n
can kiem tra n chan hay le

"""
t = int(input("Nhap so luong truong hop: "))
for i in range(t):
    #moi vong lap for --> xu ly 1 truong hop
    n = int(input("Nhap so nguyen duong n: "))
    if n % 2 == 0:
        print(n, "EVEN")
    else:
        print(n, "ODD")