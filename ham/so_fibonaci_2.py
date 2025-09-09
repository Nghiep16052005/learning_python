# nhap vao so fibonaci dau tien  luu y so 0 la so fibonaci nha 
def check(n):
    if n == 0 or n == 1 : 
        return True 
    fn1 = 1 
    fn2 = 0 
    for i in range(2, 100):
        fn = fn1 + fn2 
        print(fn, end="\n")
        if fn == n: 
            return True 
        fn2 , fn1 = fn1 ,fn 
    return False 

if __name__ =='__main__':
    n = int(input('hay nhap vao so fibonaci thu n : '))
    if check(n):
        print('YES')
    else:
        print('NO')