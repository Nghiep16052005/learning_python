a,b,c,n = map(int, input('nhap du lieu ban dau : ').split())
sum = a + b+c+n 
tmp = sum // 3
if sum %3 == 0 and tmp >= a and tmp >= b and tmp >= c : 
    print('YES')
else:
    print('NO')