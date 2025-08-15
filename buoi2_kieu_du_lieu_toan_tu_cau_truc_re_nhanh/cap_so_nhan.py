a,b,c,d = map(int,input('nhap vao 4 so nguyen a b c d : ').split())
# cong boi  
if b%a == 0 :
    q = b //a 
#kiem tra xem day a b c d co tao thanh cap so nhan hay khong 
if b *q == c and c *q == d:
    print('YES')
else:
    print('NO')