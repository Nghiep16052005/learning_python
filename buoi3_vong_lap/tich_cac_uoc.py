# Ước của số nguyên dương n là những số nguyên dương chia hết vào n.
n = int(input('nhap vao so nguyen n: '))
tich = 1
for i in range(1,n+1):
    if n% i == 0 :
        tich *= i

print(tich)
