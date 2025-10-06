"""viet chuong trinh khai bao lop sinh vien gom cac thong tin : masv, hoten,
lop,ngay sinh, gpa. ham khoi tao khong co tham so, gan cac gia tri thuoc
tinh o trang thai mac dinh(xau ki tu rong, gia tri so bang 0).Doc thong tin 1
sinh vien tu ban phim (khong co ma sinh vien) va in ra man hinh.Trong do
ma sinh vien duoc gan la sv001.ngay sinh duoc chuan hoa ve dang dd/mm/yyyy."""

"""
ta có li thuyet ve string rat quan trong phai nho 
1. no co chi so de truy xuat 
2. mac du giong list nhung no khong phai list 
3. trong list co the thay doi duoc gia tri 
3. string khong thay doi duoc gia tri giong list """

"""
 self.ngay_sinh = self.ngay_sinh[0:3] + '0' + self.ngay_sinh[3:] ? 
 slice (cat chuoi) : s[start:end] 
   end : vi tri ket thuc(khong bao gom phan tu nay ), bo trong la lay het chuoi 
   start : vi tri bat dau, bo se lay chi so 0
"""
class SinhVien:
    def __init__(self):
        self.ma = ""         # chuỗi rỗng
        self.ten = ""        # chuỗi rỗng
        self.lop = ""        # chuỗi rỗng
        self.ngay_sinh = ""  # chuỗi rỗng
        self.gpa = 0         # số 0


    def chuan_hoa(self):
        if self.ngay_sinh[1] == '/': # truy xuat den chi cho ngay sinh = 0
            self.ngay_sinh = '0' + self.ngay_sinh
        if self.ngay_sinh[4] == '/':
            self.ngay_sinh = self.ngay_sinh[0:3] + '0' + self.ngay_sinh[3:]

    def __str__(self):
        return f'{self.ma} {self.ten} {self.lop} {self.ngay_sinh} {self.gpa:.1f}'

if __name__ == "__main__":
    s = SinhVien()   # lúc này các thuộc tính đều rỗng/0
    s.ma = "SV001"
    s.ten = input()
    s.lop = input()
    s.ngay_sinh = input()
    s.gpa = float(input())
    s.chuan_hoa()
    print(s)