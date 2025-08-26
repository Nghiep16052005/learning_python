n = int(input('nhap vao so nguyen duon n: '))
print(int(2*((n*(n+1))/2)))
tong = 0 
# vong lap for 
for i in range(2,n+1,2):
    tong +=i

print(tong) 
