n = int(input('nhap so tu nhien n:\n'))
"""#in ra cac so tu 1 den n
for i in range(1,n+1):
    print(i, end=' ')

print()
#in ra cac so tu n ve 0 
for i in range(n,-1,-1):
    print(i,end=' ')
print()
#in ra cac so chan nho hon hoac bang n 
for i in range(n+1):
    if i % 2 == 0:
        print(i,end=' ')

#in ra cac so le nho hon hoac bang n 
for i in range(0 , n+1):
    if i %2 != 0:
        print(i, end=' ')
#in ra cac boi cua so 4 nho hon n 
for i in range(n):
    if i %4 == 0:
        print(i,end=" ")"""
#in ra n chu cai in thuong dau tien 
for i in range(n+1):
    print(chr(97+i),end=' ')

print()
#in ra n chu cai in thuong theo thu tu tang dan 

for i in range(122-n+1,123):
    if i <= 122:
        print(chr(i),end=" ")
