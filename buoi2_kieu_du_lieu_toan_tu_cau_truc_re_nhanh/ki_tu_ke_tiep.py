c = input('hay nhap vao ki tu : ')
res = ord(c) # chuyen ki tu thanh so vi du a = 97 
# chu in hoa trong khoang 65<= c <= 90
if(res >= 65 and res <= 90):
    print(chr(res+33))
#chu in thuong thi nam trong khoang tu 97 den 122
elif(res >=97 and res <= 122):
    print(chr(res+1))
