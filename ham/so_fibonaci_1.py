#nhiem vu cua ban la in ra n so fibonaci dau tien 
if __name__ =='__main__':
    n = input('nhap so fibonaci thu 1: ')
    if n == 1 :
        print(1)
    elif n == 2 : 
        print("1 1")
    for i in range(3,n+1):
        fn  = fn1 + fn2 
        print(fn,end = '\n')
        fn2,fn1 = fn1,fn 
        