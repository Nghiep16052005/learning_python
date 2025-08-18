n = int(input('nhap so nguyen duong n '))
tong = 0
for i in range(1,n+1):
        tong += 1/(2*i)

print("%.5f"%tong)