"""
một số được coi là số đẹp nếu nó là số thuận nghich
có chứa ít nhất 1 số 6, và tổng các chữ số của nó có
chữ số cuối cùng là 8.Viết chương trình liệt kê các số
đẹp trong đoạn giữa 2 số nguyên cho trước, các số cách
nhau 1 dấu cách """


from math import *

def check(n):
    temp = n        # Lưu lại giá trị ban đầu của n để so sánh sau
    rev = 0         # Biến lưu số đảo ngược
    tong = 0        # Biến lưu tổng các chữ số
    ok = False      # Cờ (flag) để kiểm tra có chứa số 6 hay không

    while n != 0:
        rev = rev * 10 + n % 10   # Tạo số đảo ngược (lấy chữ số cuối rồi thêm vào rev)
        
        if n % 10 == 6:           # Nếu chữ số cuối = 6
            ok = True             # Đánh dấu là có chứa số 6
        
        tong += n % 10            # Cộng chữ số cuối vào tổng
        n //= 10                  # Bỏ đi chữ số cuối

    # Trả về True nếu:
    # - ok == True (có ít nhất 1 số 6)
    # - temp == rev (số ban đầu bằng số đảo ngược => thuận nghịch)
    # - tong % 10 == 8 (tổng các chữ số có tận cùng bằng 8)
    return ok and (temp == rev) and (tong % 10 == 8)

if __name__ == '__main__':
    a,b = map(int,input('nhap a va b: ').split())
    for i in range(a,b+1):
        if check(i):
            print(i,end = ' ')