#function
"""
cach xay dung ham trong python:
ham can nhung doi so gi --> thong tin ban gui cho ham
ham tra ve gia tri gi , co kieu du lieu la gi 
kiem tra dung hay sai --> ham tra ve True/False
"""
#ham tinh tong 
def tinhtong(a,b):
    res = a+b 
    return res 
print(tinhtong(2,3))

# ham xinchao
def xinchao(name1, name2, name3 = 'nghiepdoan '):
    print("Xin chao cac ban: ", name1, name2, name3)

# ham tinh giai thua
def giaithua(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

#ham tinh a mu b
def amu(a,b):
    res = 1
    for i in range(b):
        res *= a
    return res 

# viet ham in ra dong chu 
def indongchu():
    print('28teach python')
print(xinchao('ti','teo','nam')) # khong co return nen mac dinh la None, keyword argument
#kiem tra 1 so vua chia het cho 3 vua chia het cho 5 dung in YES sai in NO, nhan n tu ban phim
# ham solve qua chi tiet qua cong kenh  ---> sai 
def solve():
    n = int(input("Nhap so n: "))
    if n % 3 == 0 and n % 5 == 0:
        return "YES"
    else:
        return "NO"
def check(n):
    if n % 3 == 0 and n % 5 == 0:
        return True
    else:
        return False
#tinh tong hieu 
def tonghieu(a,b):
    return a+b, a-b
# code de chay chuong trinh 
if __name__ == "__main__":  # dai dien cho ham main 
    #code chay o day
    xinchao(name2 = 'nghiep', name1 = 'tuan' ) # default argument
    x,y = map(int, input("Nhap 2 so a,b cach nhau boi dau cach: ").split())
    tinhtong(2,3) #positionnal argument
    for i in range(1,5):
        for j in range(3):
            print("tong cua lan lap thu nhat la:",i,tinhtong(i,j))
    
    print('giai thua cua 5 la :',giaithua(5)) # goi ham tinh giai thua 
    print('3 mu 3 la :', amu(3,3)) # goi ham tinh a mu b
    print('dong chu la :',indongchu()) # goi ham in dong chu---> khong dung muc dich
    indongchu() # goi ham in dong chu---> dung muc dich
    print(solve()) # goi ham kiem tra so vua chia het cho 3 vua chia het cho 5
    n = int(input("Nhap so n: "))
    if check(n):
        print("YES")
    else:
        print("NO")
    t,h = tonghieu(5,3)
    print("Tong va hieu la: ",t,h)
    print("Tong va hieu la: ",tonghieu(5,3))
    