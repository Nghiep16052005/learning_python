n, u1, d = map(int, input('nhap vao n , u1 va d : ').split())
# tong cac phan tu cua cap so cong la 
s = n*(u1+(u1+(n-1)*d)) // 2 
print('tong cap so cong la: ',s)