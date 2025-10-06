#bai 1 lớp phân số
#viết chương trình khai báo lớp phân số attribute la private tử số và mẫu số
# thực hiện nhập vào phân số và in ra phân số đó tối giản
from math import *
class PhanSo:
  def __init__(self, tu,mau):
    self.__tu = tu
    self.__mau = mau
  def ToiGian(self):
    ucln = gcd(self.__tu ,self.__mau)
    self.__tu //= ucln
    self.__mau //= ucln

  def __str__(self):
    return f'{self.__tu}/{self.__mau}'

if __name__ == '__main__':
  tu,mau = map(int,input().split())
  p = PhanSo(tu,mau)
  p.ToiGian()
  print(p)