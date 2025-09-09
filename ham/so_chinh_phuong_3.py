#in ra cac so chinh phuong trong doan tu a den b
import math
a,b = map(int,input('hay nhap a va b: ').split())
can1, can2 = math.isqrt(a),math.isqrt(b)
#kiem tra xem can co lay dung hay khong 
if can1 * can2 != a:
    can1 += 1
if (can2 + 1) *(can2 + 1) == b:
    can2 += 1
print(can2 - can1 + 1)