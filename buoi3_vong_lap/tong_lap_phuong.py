n = int(input('nhap nhap vao n : '))

#cong thuc tinh tong lap phuong (n*(n+1)/2)^2
tong = 0 
# su dung ham for 
for i in range(1,n+1):
    tong += i^3

print(tong )