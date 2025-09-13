def kiem_tra_chu_so_chan(n):
    if n < 10 :
        if n % 2 == 0:
            return True
        else:
            return False 
    else:
        if n % 2 != 0 :
            return False 
        else:
            return kiem_tra_chu_so_chan(n //10 )

if __name__ =='__main__':
    n = int(input('nhap so nguyen duong n: '))
    if kiem_tra_chu_so_chan(n):
        print('YES')
    else:
        print('NO')

    
