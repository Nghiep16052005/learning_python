def tong_even(n):
    if n <10 :
        return n if n % 2 == 0 else 0
    tmp = n %10 
    if tmp % 2 == 0:
        return tmp + tong_even(n //10)
    else:
        return tong_even(n //10 )
    

def tong_odd(n):
    if n <10 :
        return n if n % 2 != 0 else 0
    tmp = n %10 
    if tmp % 2 != 0:
        return tmp + tong_odd(n //10)
    else:
        return tong_odd(n //10 )
    
    
if __name__ =='__main__':
    n = int(input('nhap so nguyen duong n: '))
    print(tong_even(n))
    print(tong_odd(n))

            