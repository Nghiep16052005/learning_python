from math import *
"""a =[1,2,4,5,6]
print(type(a))
# trong python list co the luu bat ki doi tuong nao 
a = [1,2,"nghiep doan",True] 
#list constructor 
s = "nghiep doan " # iterable 
a = list(s) #list constructor 
print(a)
# cac phuong phap lam viec voi list 
#tinh xem length cua list a 
print(len(a)) #len(list) 
#truy cap phan tu thong qua chi so 
print(a[0]) # in ra chu n 
print(a[-1])
#duyet list 
# duyet theo chieu xuoi 
for i in range(0,len(a)):
    print(a[i], end=' ') 

#duyet theo chieu nguoc 
for i in range(len(a)-1 , -1,-1):
    print(a[i], end=' ')

# co the su dung for each 
# cach hoat dong vong for thu nhat item = n , ...... cu tiep tuc nhu vay 
for item in a: 
    print(item, end=' ')

o 
"""
#thay doi cac gia tri phan tu thong qua chi s
b = [1,2,3,4,5]
b[2] ="nghiep"
print(b) # thay the 2 bang "nghiep"
#them mot phan tu vao trong list 
# su dung ham append() : them 1 phan tu moi vao cuoi danh sach trong list
b.append(10)# them 10 vao cuoi list b 
print(b) # [1, 2, 'nghiep', 4, 5, 10] 
# su dung ham insert() de them 1 phan tu vao 1 vi tri bat ki trong list 
b.insert(2,"doan") # [1, 2, 'doan', 'nghiep', 4, 5, 10]
print(b) 
print(b[-2]) # chi so duoc danh nguoc lai tu phai sang trai 
# xoa 1 phan tu khoi list 
# su dung ham pop() 
b.pop(2) # xoa phan tu o vi tri 2 
print(b)# [1, 2, 'nghiep', 4, 5, 10]
b.pop()# chi so khong ro rang trong list ----> xoa phan tu cuoi cung va tra ve phan tu bi xoa 
print(b)#[1, 2, 'nghiep', 4, 5]
print(b.pop())# xoa phan tu 5 ra khoi list va tra ve phan tu 5 
#su dung ham del
del b[1]# xoa phan tu 2 ra khoi list luon 
print(b)
#su dung ham remove , neu co nhieu phan tu trung lap thi chi xoa di pt dau tien , neu khong co ham can xoa remove se gay ra loi 
b.remove(1)# xoa 1 ra khoi danh sach , remove la xoa phan tu thong qua gia tri
#su dung clear de xoa moi phan tu trong danh sach list b.clear()
#ta co the sao chep list (nhan ban list )
#ex: ta co the tao ra mang co 1000 phan tu la so 0 
#b = [0]*100 # tao bien b co 100 phan tu la so 0
print(b)
#tim kiem 1 phan tu co nam trong list hay khong su dung ham in ---> su dung toan tu in hoac thuat toan tim kiem tuyen tinh do phuc tap la o(n)
def linear_search(b,x):
    for item in b:
        if item == x:
            return True 
    return False 
# ham linear_search no tuong duong voi ham 
if 5 in b: # do phuc tap  la o(n)
    print('YES')
# ta co the noi list 1 va list 2 lai thanh 1 list moi bang combine list  bang ham extand()
#ex 
a =[1,2,3,54,5]

a.extend(b)# [1, 2, 3, 54, 5, 'nghiep', 4] 
print(a)
# co the su dung a + b luon voi a,b la 2 mang 
a += b
print(a)#[1, 2, 3, 54, 5, 'nghiep', 4, 'nghiep', 4] 
#phuong thuc pho bien cua list 
#1.ham copy : tra ve list moi (khac voi list ban dau) se copy y chang nhu list cu 
c = a.copy()
print(c)# [1, 2, 3, 54, 5, 'nghiep', 4, 'nghiep', 4] ---> copy y chang mang a
#2.count : tra ve so lan xuat hien cua mot phan tu bat ki tron list 
#ex:a = [1, 2, 3, 54, 5, 'nghiep', 4, 'nghiep', 4]
print(a.count("nghiep"))# in ra 2 
#3.index : tra ve chi so phan tu dau tien cua 1 phan tu o trong listo trong list , trong list khong chua phan tu nao thi bao loi 
print(a.index("nghiep")) # tra ve 5
#4.ham reverse(): dung de lat nguoc 1 list do phuc tap o(n)
#ex:a = [1, 2, 3, 54, 5, 'nghiep', 4, 'nghiep', 4]
a.reverse()# lat nguoc thanh [4, 'nghiep', 4, 'nghiep', 5, 54, 3, 2, 1]
print(a)
#5 ham sort : sap xep cac phan tu trong list , do phuc tap nlog(n)
#ex:d = [4, 'nghiep', 4, 'nghiep', 5, 54, 3, 2, 1]
d = [4,4, 5, 54, 3, 2, 1]
d.sort()#sap xep mang theo thu tu tang dan === thuat toan tim sort 
print(d)# neu cung kieu thi moi sai duoc, truong hop nay in ra [1, 2, 3, 4, 4, 5, 54] 

#luu y khi thao tac voi 2 list 
#ex d = [1, 2, 3, 4, 4, 5, 54] 
e = d # list d va e nam tren cung 1 dua chi 
print(d)
print(e)
print(id(d))# dia chi y chang
print(id(e))#dia chi y chang
# tao ra truong hop khi thay doi d ---> cung thay doi luon e dieu nay minh co muon hay khong
#cach khac phuc 
f = d.copy()# se tao ra list moi 
# viet ham thay doi mang a . thực chất, bạn truyền tham chiếu đến list g đó vào tham số arr
def change(arr):
    arr[0] = 1000 # tham chieu den truc tiep vung luu tru du lieu 
    return arr 
g = [1,2,3,4,5,7]
print(change(g)) # none vi khong co return 
change(g)
print(g)
# LIST SLICING : la ki thuat giup truy cap vao 1 khoang cac phan tu trong list thong qua toan tu 
# cu phap: List(start:stop:step), khong co step la 1 , khong co start cat gia tri tu 0 , khong co stop thi cat het , stop + 1 
#ex 
h = [10,20,30,40,50,60]
i = h[2:5:1] # sai duyet chi so bat dau va ket thuc + hay - deu duoc het 
print(i)#[30, 40, 50]
# de lat nguoc list trong list slicing: 
j = h[::-1]# lat nguoc dung rat rat nhieu
print(j)# [60, 50, 40, 30, 20, 10] 
# ham LAMBDA FUNCITON : định nghĩa một hàm định nghĩa hàm vô danh ( không sài tử def va tham số trong hàm đó ) trong python
# xay duong ham ten function voi cu phap dai dong ---> nen qua ham lambda 
def function (n):
    return 2 * n 
function = lambda n : n*2 # tuong duong voi ham o tren va gon hon nhieu, co tham so la x va tra ve x **2   
# lambda khong chua cac cau lenh : return , assest ,pass 
#lambda chi chua mot bieu thuc duy nhat 
#IIFE  (immediately invoked function Expression) bieu thuc lambda co the goi ngay lap tuc , ex 
res = (lambda x : x **2)(10) # ham lambda tra ve binh phuong cua x va 10 la goi ham ten 10 ngay lap tuc 
#tinh tong 
function =( lambda x ,y, z: x+y+z)
print(function(100,200,300))
#truyen doi so cho bieu thuc lambda 
#lambda va map 
k = [1,2,3,4,5,6,7]
l = list(map(lambda x : x **2,k))
print(l)# [1, 4, 9, 16, 25, 36, 49] 
#lambda va filter 
m = [1,2,3,4,5,6,7]
n = list(filter(lambda x : x % 2 == 0,m))# dung de loc nhung phan tu thoa man dieu kien trong function 
print(n)# [2, 4, 6] 
#if else trong lambda
findMax = lambda x, y : x if x > y else y
print(findMax(200,500))# 500 
#LIST COMPREHENTION : la 1 iterable(co the lap lai), ket hop voi dieu kien va vong lap de rut gon cu phap 
o = [1,2,3,4,5,6,7,8]
u =[]
for x in o:
    if x % 2 == 0:
        u.append(x)

print(u)#[2, 4, 6, 8]
#cu phap cua co list comprehention  : [expressiton (su bieu lo) for var in interable (bienlap)]
#p,q,r,stvwxyz
p = [x + 3 for x in o]
print(p)#[4, 5, 6, 7, 8, 9, 10, 11]
# tao so chinh phuong voi ham range
q = [x ** 2 for x in range(1,11)]
print(q)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#tinh tong chu so cua 1 phan tu trong mang a va tao list moi ---> sai comprehention 
r = []
def sum_digit(n):
    tong = 0 
    while n != 0 :
        tong += n%10 
        n //= 10 
    return tong 
# cach nay phen 
#for x in a : 
    #r.append(sum_digit(x))
#print(r)
# su dung cach nay 
r = [sum_digit(x) for x in q]
print(r)#[1, 4, 9, 7, 7, 9, 13, 10, 9, 1]
#list comprehention ket hop voi if : [expressiton (su bieu lo) for var in interable (bienlap) if_clause]
s = [x for x in r if x % 2 == 0]
print(s)#[4,10]
#ham kiem tra so nguyen to
def nt(n):
    if n <2 : return False
    for i in range (2, isqrt(n)+1):
        if n % i == 0: 
            return False 
    return True 

t = [x for x in r if nt(x)]
print(t)#[[7, 7, 13]
# nested(long nhau) list comprehention
v = [[1,2,3],[4,5,6],[7,8,9]]
w = []
for small_list in v : 
    for x in small_list:
        w.append(x)
    
print(w)# [1, 2, 3, 4, 5, 6, 7, 8, 9] 
