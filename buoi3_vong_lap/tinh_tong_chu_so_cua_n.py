n = int(input('nhap vao n: '))
if n == 0 :
    print(0)
else:
    tong = 0 
    while n!= 0 :
        tong += n%10 
        n //= 10
    print(tong)