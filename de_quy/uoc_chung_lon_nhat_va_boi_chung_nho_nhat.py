def gcd (a,b):
    if b == 0 :
        return a
    return gcd(b,a%b)
def lcm(a,b):
    return a*b // gcd(a,b)

if __name__ == '__main__':
    a,b = map(int,input('hay nhap vao gia tri a va b: ').split())
    print(gcd(a,b), "la uoc chung lon nhat ")
    print(lcm(a,b),"boi chung nho nhat ")