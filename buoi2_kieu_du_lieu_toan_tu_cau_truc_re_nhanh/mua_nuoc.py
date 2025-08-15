n,a,b = map(int,input('nhap 3 gia tri cho de bai: ').split())
#tinh so xu trung binh lit a
res1 = a//1
#tinh so xu trung binh lit b
res2 = a//2

if(res1 <res2 ):
    print('gia toi thieu can phai tra la: ',n*a)
else:
    if(res2 <res1 and n%2 == 0):
        print('gia toi thieu can phai tra la: ',(n//2)*b)
    else:
        print('gia toi thieu can phai tra la: ',(n//2)*b+(n%2)*a)
