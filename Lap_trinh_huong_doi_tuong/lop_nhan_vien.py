"""
một nhân viên làm việc trong công ty  được lưu lại các thông tin sau: 
1. mã nhân viên: được gán giá trị là 00001
2. họ tên : xâu kí tự không quá 50 chữ cái 
3. giới tính : nam hoặc nữ 
4.ngày sinh : đúng theo chuẩn dd/mm/yyyy 
5. địa chỉ : xâu kí tự không quá 100 chữ cái 
6. mã số thuế : dãy số có đúng 10 chữ số 7 
7. ngày kí hợp đồng : đúng theo chuẩn dd/mm/yyyy
viết chương trình nhập một nhân viên(không nhập mã) in ra màn thông tin của nhân viên đó 
"""

class NhanVien:
    def __init__(self,ma_nhan_vien, ho_ten, gioi_tinh,ngay_sinh,dia_chi,ma_so_thue,hop_dong):
        self.ma_nhan_vien = ma_nhan_vien
        self.ho_ten = ho_ten
        self.gioi_tinh = gioi_tinh
        self.ngay_sinh = ngay_sinh
        self.dia_chi = dia_chi
        self.ma_so_thue = ma_so_thue
        self.hop_dong = hop_dong 

    def __str__(self):
        return self.ma_nhan_vien + ' '+self.ho_ten + ' '+self.gioi_tinh +' '+self.ngay_sinh+' '+self.dia_chi+' '+self.ma_so_thue+' '+self.hop_dong
                
if __name__ == '__main__':
    n = NhanVien('00001',input(),input(),input(),input(),input(),input())
    print(n)

            
        
        