a,b,k = map(int,input('nhap gia tri cho  dich phai , dich trai va k buoc nhay va: ').split())
# neu so buoc nhay chan (nghia la nhay a va b)
if(k %2 == 0):
    #toa do x ma ech dich chuyen la
    x = (k//2)*a - (k//2)*b
# neu so buoc nhay le (nghia la nhay ben phai a nhieu hon ben trai 1 lan)
else:
    x = ((k//2)+1)*a -(k//2)*b

print(x)