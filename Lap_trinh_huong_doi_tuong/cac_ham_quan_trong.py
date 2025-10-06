#các hàm quan trọng trong python
# 1. hàm init
# 2. hàm hủy __del__
#3. hàm in __str__
class person:
  def __init__(self, name,brith):
    self.name = name
    self.brith = brith

  def __str__(self):
    return f'{self.name} {self.brith}'

if __name__ =='__main__':
  p = person('nghiep','7/07/2777')
  print(p.__str__())   # gọi trực tiếp __str__
  print(str(p))        # gọi built-in str()
  print(repr(p))       # gọi built-in repr()
#hàm __repr__: trả về chuỗi kí tự đại diện cho đối tượng
#   khi không có hàm __str__ thì print(p) ra sẽ default lấy hàm __repr__ đai diện