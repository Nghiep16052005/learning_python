n =  int(input('nhap so nguyen duong n : '))
#hinh 1
tong = 1
for i in range(1,n+1):
    for j in range(1,n+1):
            print(tong,end=' ')
            tong += 1
    print()
print()
#hinh 2
for i in range(1,n+1):
    tong = i
    for j in range(1,n+1):
            print(tong,end=' ')
            tong += 1
    print()
print()
#hinh 3
for i in range(1, n+1):
      for j in range(1,n+1):
            if j <= n-i:
                print('~',end=' ')
            else:
                print(i,end=' ')
      print()
print()
#hinh 4
for i in range(1,n+1):
      ktao = i
      kc = n-1
      for j in range(i):
            print(ktao,end=' ')
            ktao += kc
            kc -= 1
      print()
print()