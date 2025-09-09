# uoc chung lon nhat
#gcd(a,b)×lcm(a,b)=a×b 

def GCD(a,b):
    while b != 0:
        a,b = b, a % b 
    return a 
def LCM(a,b):
    return a * b / GCD(a,b)

if __name__ =='__main__':
    a,b = int(input('nhap vao a va b: '))
    print(GCD(a,b))