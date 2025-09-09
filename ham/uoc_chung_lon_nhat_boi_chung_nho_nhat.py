#ap dung giai thuat Euclid de tim uoc chung lon nhat (UCLN) va boi chung nho nhat (BCNN)
# UCLN(a,b) = UCLN(b, a % b) neu b != 0 dung khi b = 0
# UCLN(a,0) = a
# BCNN(a,b) = (a * b) / UCLN(a,b) 
#vi du: UCLN(24,36) = 12, BCNN(24,36) = 72

def gcd(a,b):
    while b != 0:
        r = a % b
        a ,b= b,r # gan gia tri moi cho a va b la b va r
    return a

def lcm(a,b):
    return (a * b) // gcd(a,b)

if __name__ == "__main__":
    a = int(input("Nhap so nguyen duong a: "))
    b = int(input("Nhap so nguyen duong b: "))
    print("UCLN cua", a, "va", b, "la:", gcd(a,b))
    print("BCNN cua", a, "va", b, "la:", lcm(a,b))
# UCLN cua 24 va 36 la: 12
# BCNN cua 24 va 36 la: 72  