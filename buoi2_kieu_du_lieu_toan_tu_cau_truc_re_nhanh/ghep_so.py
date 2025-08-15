"""
co k2 chu so 2 , co k3 chu so 3 , co k5 chu so 5 ,k6 chu so 6 
so yeu thich cua anh ta la 32 va 256 
anh ta quyet dinh soan tu cac so ma anh ta co 
de lam cho tong so nguyen cang som cang tot
chu y: 
moi chu so co the duoc su dung khong qua 1 lan 
"""
k2,k3,k5,k6 = map(int,input('nhap gia tri: ').split())
k256 = min(k2,k5,k6)
k32 = min(k3,k2-k256)
print(k32 *32 + k256)
