# S(n) = 1+ 1.2 + 1.2.3 + ... + 1.2.3...n 
n = int(input("Nhap n: "))
sum = 0
giaithua = 1
for i in range(1, n+1):
    giaithua *= i
    sum += giaithua

print("Tong S(n) la: ", sum)