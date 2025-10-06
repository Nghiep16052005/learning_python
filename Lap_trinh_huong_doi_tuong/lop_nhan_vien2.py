from math import *
class NhanVien:
    def __init__(self,ma_nhan_vien,ho_ten,gioi_tinh,ngay_sinh,dia_chi,ma_thue,hop_dong):
        self.ma_nhan_vien = ma_nhan_vien
        self.ho_ten = ho_ten
        self.gioi_tinh = gioi_tinh 
        self.ngay_sinh = ngay_sinh
        self.dia_chi = dia_chi
        self.ma_thue = ma_thue 
        self.hop_dong = hop_dong
    # chuan hoa ten va ngay sinh 
    def chuan_hoa(self):
        if self.ngay_sinh[1] == '/': # truy xuat den chi cho ngay sinh = 0
            self.ngay_sinh = '0' + self.ngay_sinh
        if self.ngay_sinh[4] == '/':
            self.ngay_sinh = self.ngay_sinh[0:3] + '0' + self.ngay_sinh[3:]
        #chuan hoa ten 
        tmp = self.ten.split()    # Bước 1: Tách tên thành list các từ,tach theo khoang trang 
        res = ' '.join(tmp)       # Bước 2: Nối lại với 1 dấu cách giữa các từ
        res = res.title()         # Bước 3: Viết hoa chữ cái đầu mỗi từ
        self.ten = res            # Bước 4: Gán lại tên đã chuẩn hóa

    def __str__(self):
        return self.ma_nhan_vien + ' ' + self.ho_ten + ' '+ self.gioi_tinh + ' ' +self.ngay_sinh+ ' ' + self.dia_chi+ ' ' + self.ma_thue+ ' ' + self.hop_dong

if __name__ =='__main__':
    n = NhanVien('00001',input(), input(), input(), input(), input(), input())
    print(n)