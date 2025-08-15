x,y,z,t = map(float,input('nhap 4 diem cho hoc sinh :').split())
sum = ((x+y)+z*2+t*3)/7
if(sum >= 8):
    print('GIOI')
elif(sum <8 and sum >=6.5):
    print('KHA')
elif(sum <6.5 and sum >= 5):
    print('TRUNG BINH')
else:
    print('YEU')    