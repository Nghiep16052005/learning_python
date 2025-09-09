# so thuan nghich hay con goi la so doi xung
# so thuan nghich la so co gia tri khong doi khi dao nguoc cac chu so
# hay la so thuan nghich khi doc tu trai sang phai hay tu phai sang trai deu giong nhau
# vi du: 121, 12321, 1234321,
# cach nay kho hieu
def check_thuan_nghich(n):
    # chuyen so n thanh chuoi
    s = str(n)
    # dao nguoc chuoi s
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False    
    return True

# cach nay de hieu hon nhieu 
#ham viet so thuan nghich
def tn(n):
    temp = n
    n = 0 
    while n != 0 :
        rev = rev * 10 + n % 10
        n //= 10 
    return rev == temp 
# vi du: check_thuan_nghich(121) = True
if __name__ == "__main__":
    n = int(input("Nhap so nguyen duong n: "))
    if check_thuan_nghich(n):
        print(n, "la so thuan nghich")
    else:
        print(n, "khong phai la so thuan nghich")
# 121 la so thuan nghich
# 123 khong phai la so thuan nghich 