"""
bizon co a1 cup giai nhat, a2 cup giai nhi , a3 cup giai 3 , b1 huy chuong giai nhat
b2 huy chuong giai nhi , b3 huy chuong giai 3 
quy tac : bat ki ke nao cung khong the xep vua cup vua huy chuong,
khong co ke co the chua nhieu them 5 cup 
khong co ke co the chua hon 10 huy chuong 
kiem tra xem Bizon co the dat tat ca cac phan thuong de dap ung dieu kien hay khong 
input : a1,a2,a3 ,b1,b2,b3 
        n : ke 
"""
a1,a2,a3,b1,b2,b3 = map(int,input('nhap gia tri : ').split())
n = int(input('nhap gia tri cho ke : '))
tong_cup = a1 + a2 + a3 
tong_huy_chuong = b1 + b2 + b3 
# tinh gia tri cho tong cup 
if tong_cup %5 == 0 :
    ans = tong_cup //5 
else:
    ans = (tong_cup // 5) +1 
#tinh gia tri cho tong huy chuong 
if tong_huy_chuong % 10 == 0 : 
    ans += tong_huy_chuong % 10 
else:
    ans += (tong_huy_chuong %10)+1
print(ans)

if ans <= n :
    print('YES')
else:
    print('NO')