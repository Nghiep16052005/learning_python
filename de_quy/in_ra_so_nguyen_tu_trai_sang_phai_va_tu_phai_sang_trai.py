"""
Ý tưởng

In từ phải sang trái:

Lấy n % 10 để in chữ số cuối cùng.

Gọi lại hàm với n // 10.

Điều kiện dừng: n < 10, in luôn n.

In từ trái sang phải:

Gọi lại hàm với n // 10 trước (đi sâu đến chữ số đầu tiên).

Sau đó in n % 10.

Điều kiện dừng: n < 10, in luôn n.
"""
def phai_sang_trai(n):
    if n <10 : 
        print(n,end=' ')
    else:
        print(n%10,end=' ')
        return phai_sang_trai(n //10)

def trai_sang_phai(n):
    if n <10 :
        print(n,end=' ')
    else:
        trai_sang_phai(n //10)
        print(n%10,end=' ')
        
if __name__=='__main__':
    n = int(input('nhap vao n: '))
    phai_sang_trai(n)
    print()
    trai_sang_phai(n)
