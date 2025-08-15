c = input('nhap vao ki tu : ')
res = ord(c)

if(res >= 65 and res <= 90):
    print(chr(res+32))
elif(res >= 97 and res <= 122):
    print(chr(res -32))
else:
    print(chr(res))