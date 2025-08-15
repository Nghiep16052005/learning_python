t,n = map(int,input('nhap vao ngay thang nam').split())
if(t >=1 and t <=12 and n > 0):
    if(t == 1 or t == 3 or t ==5 or t == 7 or t ==8 or t ==10 or t ==12):
        print('31')
    elif(t ==4 or t ==6 or t ==9 or t == 11):
        print('30')
    else:
        if(t == 2 and n%400 == 0 or (n%4 == 0 and n%100 !=0)):
            print('29')
        else:
            print('28')    
else:
    print('INVALID')