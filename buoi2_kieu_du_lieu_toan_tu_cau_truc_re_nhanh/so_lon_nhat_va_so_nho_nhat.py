"""
cho 2 so nguyen a va b. ban hay tim 2 so sau, so thu nhat la so lon nhat <= a ma chia het
cho b, so thu 2 la so nho nhat >= a ma chia het cho b. khong sai vong lap 
"""
a,b = map(int,input('nhap 2 so nguyen a va b:').split())
print('so lon nhat <=a ma chia het cho b la:',(a//b)*b)
if(a%b ==0):
    print(a)
else:
    print((a//b)*b+b)