# so fibonaci la so trong day fibonaci
# day fibonaci bat dau bang 0 va 1, so tiep theo la tong cua hai so truoc do
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# so fibonaci thu n duoc tinh bang cong so fibonaci thu n-1 va n-2
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) neu n >= 2
# vi du: F(5) = F(4) + F(3) .... 

def fibonaci(n):
    print("0 1", end = " ")
    fn1,fn2 = 1,0 # fn1 la F(n-1), fn2 la F(n-2)
    for i in range(2,n):
        fn = fn1 + fn2
        print(fn, end = " ")
        fn2 = fn1
        fn1 = fn
    print() # xuong dong
    return fn1 # tra ve so fibonaci thu n

def check_fibonaci(n):
    if n == 0 or n == 1:
        return True # 0 va 1 la so fibonaci
    fn1,fn2 = 1,0
    while fn1 < n:
        fn = fn1 + fn2 # tinh so fibonaci tiep theo
        fn2 = fn1# cap nhat fn2 la so fibonaci truoc do
        fn1 = fn# cap nhat fn1 la so fibonaci hien tai
    return fn1 == n

# vi du: fibonaci(5) = 5
if __name__ == "__main__":
    n = int(input("Nhap so fibonaci thu n: "))
    print("So fibonaci thu", n, "la:", fibonaci(n))
    m = int(input("Nhap so nguyen duong m: "))
    if check_fibonaci(m):
        print(m, "la so fibonaci")
    else:
        print(m, "khong phai la so fibonaci")
# So fibonaci thu 5 la: 5
# So fibonaci thu 10 la: 34