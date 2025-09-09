import math 

def prime(n):
   if n < 2:
       return False
   for i in range(2, math.isqrt(n) + 1):
       if n % i == 0:
           return False
   return True  

    
if __name__ == "__main__":
    n = int(input("Nhap so nguyen duong n: "))
    if prime(n):
        print(n, "la so nguyen to")
    else:
        print(n, "khong phai la so nguyen to")