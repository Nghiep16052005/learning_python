"""
cho 2 so nguyen a va b. ban hay tim 2 so sau, so thu nhat la so lon nhat <= a ma chia het
cho b, so thu 2 la so nho nhat >= a ma chia het cho b. khong sai vong lap 
vi du a =27 b = 25 
so nho hon hoac bang a ma chia het cho b la : (27 /5) * 5 = 25 --> de 
so nho nhat >= a ma chia het cho b 

"""
a,b = map(int,input('nhap 2 so nguyen a va b:').split())
print('so lon nhat <=a ma chia het cho b la:',(a//b)*b)
if(a%b ==0):
    print(a)
else:
    print((a//b)*b+b)