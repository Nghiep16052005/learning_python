"""de bai tinh so thao tac nho nhat : 
ta co cac thao tac sau 
neu n chia het cho 2 --> thao tac
n chia het cho 3 --> thao tac 
n tru di 1 don vi --->thao tac 
can lam thao tac nho nhat de bien doi gan 1 nhat"""

def f(n):
    # khi n = 1 thi khong can thao tac gi de bien doi no ve 1
    if n == 1: 
        return 0
    tt1,tt2,tt3 = 10 **9 ,10 **9 ,10 ** 9 # li do la khi tra ve 3 so dam bao dieu kien lay so nho nhat 
    if n %2 == 0:
        tt1 = 1+ f(n //2) # tinh 1 lan thao tac 

    if n % 3 == 0:
        tt2 = 1 +f(n //3) # tinh mot lan thao tac 
    if n > 1 : 
        tt3 = 1 + f(n-1)
    return min(tt1,tt2,tt3)

    