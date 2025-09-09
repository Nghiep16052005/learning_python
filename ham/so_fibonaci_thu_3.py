# tim so thuoc dang fibonaci nho nhat lon hon hoac bang n 
# ex: 1, 1,2 ,3 5,8,13 

def check(n):
    fn1 = 1 
    fn2 = 0 
    for i in range(2, 100):
        fn = fn1 + fn2 
        if fn >= n: 
            return fn
        fn2 , fn1 = fn1 ,fn 
    return -1

if __name__ =='__main__':
    n = int(input('hay nhap vao so fibonaci thu n : '))
    print(check(n))