"""#in ra cac so tu 1 den 20 nhung gap so chia het cho 7 thi dung 
for i in range(1,21):
    print(i, end=' ')
    if i % 7 == 0:
        break 
print('cau lenh ben duoi la: ')

#cau lenh continue
for i in range(5):
    print('nghiep')
    continue
    print('python')


#vong lap for long nhau(Nested loop)|
for i in range(3): # 
    for j in range(2):
        print(i,j)

#liệt kê ước của một số nguyên n 
n =
for i in range(1,101):
    if n%i == 0:
        print('so',i,'chia het cho ',n)
"""
"""
#vong lap while 
while condition:
    #code when condition is True
else:
    #code while condition is False 

# vi du 1
n = 1 
while n <= 5:
    print(n)
    n += 1 
else:
    print('vong lap while ket thuc khi n= 6')

#vi du 2 
n = 20 
i = 1
while i <= n:
    print(i)
    i += 1
else:
    print('vong lap ket thuc khi n bang 21')

# yeu cau nguoi dung nhap 1 so duong neu la so am thi nhap lai !!!
while True:
    n = int(input('nhap n: '))
    if n>0:
        break

#nhap vo hang giua cac so khi nao ra so 2022 thi dung 
while True:
    n = int(input('nhap 1 so nguyen duong n: '))
    if n == 2022:
        break
"""
# chu so cua mot so nguyen --> sài vong while 

#dem so luong chu so cua n 
"""
n = 12345 
dem = 0 
while n != 0 :
    dem += 1 
    n //= 10 

print('dem so chu so cua n: ', dem )
"""
"""
#tinh tong chu so cua mot so nguyen
n = 12345 
tong = 0 
while n!= 0:
    tong += n %10 
    n //= 10

print('tong chu so cua mot so nguyen la:',tong)"""

# lat nguoc mot so nguyen 
"""
n = 1234
lat = 0 
while n!= 0:
    lat = lat*10 + n%10 
    n //= 10 

print('chu so lat nguoc cua n la: ', lat)"""

