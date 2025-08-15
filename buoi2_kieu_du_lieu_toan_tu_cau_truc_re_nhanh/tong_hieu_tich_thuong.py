a,b =map(int,input('nhap vao 2 so xy la: ').split())
print('tong cua x va y: ',a+b)
print('hieu cua x va y la: ',abs(a-b))
print('tich cua a va b la: ',a*b)
if(a == 0 or b == 0):{
    print('INVALID')
}
else:{
    print('thuong cua a va b la:',"%,4f" %abs(a%b))
}
