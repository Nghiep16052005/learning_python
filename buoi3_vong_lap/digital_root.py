n = int(input("Nhap so nguyen duong: "))

while n>= 10 :
   #tinh tong cac chu so cua n >= gan lai cho n
    sum = 0
    while n > 0 :
        sum += n%10
        n //=10 
    n = sum

print("Digital root la: ", n)

   