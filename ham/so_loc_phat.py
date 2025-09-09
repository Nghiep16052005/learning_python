"""
số lộc phát là số chỉ chứa các chữ số 0,6,8""" 

def locphat(n):
    while n != 0 :
       tmp =  n %10 
       if tmp != 0 and tmp != 6 and tmp != 8 : 
           return 0
       n //= 10 
    return 1 

def new_func():
    n //= 10

if __name__ == '__main__':
    n = int(input('nhap so n: '))
    if locphat(n):
        print('YES')
    else:
        print('NO')
    

