def F(n):
    if n != 0:
        F(n // 16)
        r = n %16 
        if r < 10:
            print(r,end='')
        else:
            print(chr(r+55),end='') 
if __name__ =='__main__':
    n = int(input('hay nhap so n: '))
    if n == 0 : print('0')
    else:
        F(n)