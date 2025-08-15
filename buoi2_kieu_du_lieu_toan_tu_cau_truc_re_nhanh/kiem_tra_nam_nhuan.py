n = int(input('nhap vao 1 nam nhuan: '))
if(n% 400 or (n%4 ==0 and n% 100 != 0)):{
    print('YES')
}
else:{
    print('NO')
}