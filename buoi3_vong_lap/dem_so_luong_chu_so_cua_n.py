n = int(input('nhap vao n: '))
if n == 0 :
    print(1)
else:
    dem = 0 
    while n != 0 :
        dem += 1
        n //= 10 
    print(dem)
