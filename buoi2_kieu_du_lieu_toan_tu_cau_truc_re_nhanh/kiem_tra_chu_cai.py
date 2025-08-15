c = input('hay nhap vao ki tu c: ')
res = ord(c)
#chu in thuong nam trong khoang tu 97 den 122 c.islower()
if(res >= 97 and res <= 122):
    print('LOWER')
#chu in hoa nam trong khoang tu 65 den 90 c.isupper()
elif(res >= 65 and res <= 90):
    print('UPPER')
# chu so nam trong khoang tu 48 den 57 c.isdigit()
elif(res >= 48 and res <=57):
    print('DIGIT')
#ki tu dac biet
else:
    print('SPECIAL')