from math import *
n = int(input('nhap mot so nguyen duong n :'))

# tinh tong uoc tu 1 den sqrt(n)
dem = 0
for i in range(1,n+1):
    if n%i == 0:
        dem += 1
print(dem)
for i in range(1,n+1):
    if n%i == 0:
        print(i,end=" ")