""""
đề yêu cầu 1 số được coi là đẹp nếu chữ số đầu gấp đôi
chữ số cuối hoặc nguowicj lại đồng thời các chữ số từ
vị trí thứ 2 đến gần cuối thỏa mãn là một số thuận
nghịch """

"""
nghĩa là 
Số đầu gấp đôi số cuối (hoặc ngược lại).

Chuỗi còn lại (bỏ chữ số đầu và cuối) phải là số thuận nghịch."""

def tn(n):
    tmp = n
    rev = 0 
    while n != 0 : 
        rev = rev *10 + n% 10 
        n //= 10 
    return tmp == rev 

def check(n):
    dv = n%10 
    n //= 10
    rev = 0  
    while n >= 10 :
        rev = rev * 10 + n %10 
        n //= 10 
    return (dv == 2 * n or n == 2 * dv ) and tn(rev)

if __name__ == '__main__':
    n = int(input('nhap so nguyen duong n: '))
    if check(n):
        print('YES')
    else:
        print('NO')
       

