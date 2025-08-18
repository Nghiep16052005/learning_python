n = int(input('nhap vao so nguyen n:'))
tong = 0 
for i in range(n+1):
    tong += i 

print('tong cua day so tu nhien n la: ',tong)
#cong thuc tinh nhanh
print(int(n*(n+1)/2))