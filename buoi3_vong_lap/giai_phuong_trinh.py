a,b,n = map(int, input("nhap 3 so nguyen duong a b n :").split())
check = False 
for x in range(0 , n // a+1):
    temp = n -a *x
    print(x,temp %b)
    if temp % b == 0:
        check = True
        break

if check :
    print('YES')
else:
    print('NO')
