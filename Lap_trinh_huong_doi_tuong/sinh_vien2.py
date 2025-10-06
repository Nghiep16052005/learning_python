# khai bao lon thi sinh gom cac thong tin : hoten , ngay sinh ,diem mon 1
# diem mon 2 , diem mon 3 , tong diem , doc thong tin tu ban phim va in ra
#man hinh 3 thong tin : Ho ten, Ngay sinh , tong diem

class SinhVien:
  def __init__(self, HoTen,NgaySinh,DiemMon1,DiemMon2,DiemMon3):
    self.HoTen = HoTen
    self.NgaySinh = NgaySinh
    self.DiemMon1 = DiemMon1
    self.DiemMon2 = DiemMon2
    self.DiemMon3 = DiemMon3
    self.TongDiem = 0
  def Sum(self):
    self.TongDiem = self.DiemMon1 + self.DiemMon2 + self.DiemMon3
  def __str__(self) :
    return f'{self.HoTen},{self.NgaySinh},{self.TongDiem:.1f}'

if __name__ =='__main__':
  HoTen,NgaySinh =input().split()
  DiemMon1,DiemMon2,DiemMon3 = map(int,input().split())
  p = SinhVien(HoTen,NgaySinh,DiemMon1,DiemMon2,DiemMon3)
  p.Sum()
  print(p)