# kiem tra 1 so co phai la so fibonaci hay khong 
#ban phai tra loi nhieu truong hop 
def check_fibo(n):
    if n == 1 : 
        return True
    fn1 = 1 
    fn2 = 1
    for i in range(2 , 100):
        fn = fn1 + fn2 
        if fn == n : 
            return True 
        fn2, fn1 = fn1 ,fn 
    return False 

if __name__ == '__main__':
    t = int(input('nhap so luong can kiem tra so fibonaci: '))
    for _ in range(t):
        n = int (input("hay nhap so fibonaci: "))
        if check_fibo(n):
            print('YES')
        else:
            print('NO')