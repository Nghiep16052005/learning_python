n = int(input("nhap gia tri tu ban phim: "))
tong  = 0
for i in range(1,n+1):
    if i%2 == 0:
        tong += i
    else:
        tong += -i

print(tong)

# (-1+2)+(-3+4)+(-5+6)+....
# n chan : n/2 ==> n/2
#n le : (n-1)/2 - n