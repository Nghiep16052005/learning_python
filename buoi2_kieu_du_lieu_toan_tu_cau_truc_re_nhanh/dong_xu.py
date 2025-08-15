n,s = map(int, input('nhap vao gia tri lon nhat va tong tien: ').split())
if(s%n == 0):
    print((s//n))
else:
    print((s//n)+1)