n = int(input('nhap vao n: '))
dem = 0 
while n!= 0:
   tmp = n % 10
   if tmp == 2 or  tmp == 3 or tmp == 5 or tmp == 7 :
        dem += 1 
   n //= 10 

   
print(dem)



        