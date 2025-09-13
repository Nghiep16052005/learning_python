""""
cấu trúc dữ liệu ngăn xếp : 
cho 1 cái hộp bên dưới bị chặn 
push là đẩy vào ngăn xếp 
còn pop là lấy ra khỏi ngăn xếp --> vào sau ra trước 

stackframe là tập hợp các chương trình liên quan đến chương trình con 
--> xuất hiện khi có lời gọi gọi hàm 
stackframe chỉ tồn tại trong quá trình chương trình thực thi 
thành phần : có thể là biến cục bộ, đối số , địa chỉ trả về """

# ex stackframe 
from math import * 

def A():
    print('A')

def B():
    A()# goi ham A 
    print('B')

def C():
    B()
    print('C') 

#ex2 : tran bo nho stack 
def A():
    A()
    print('A') 

def S(n):
    if n == 0:
        return 0 
    else:
        return n + S(n-1) # de quy 
    
if __name__ == '__main__':
    n = 4
    print(S(4))

