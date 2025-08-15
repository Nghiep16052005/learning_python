"""
Quảng trường Nhà hát ở thủ đô Berland có hình chữ nhật với kích thước n × m mét.
 Nhân dịp kỷ niệm thành phố, một quyết định đã được đưa ra để lát Quảng trường
   bằng những viên bằng đá granit vuông. Mỗi viên đá hình vuông có kích thước a × a. 
   Số lượng viên đá ít nhất cần thiết để lát Quảng trường là bao nhiêu? 
   Nó được phép che phủ bề mặt lớn hơn Quảng trường Nhà hát. 
   Nó không được phép phá vỡ các viên đá. Các cạnh của viên đá phải song song 
   với các cạnh của Quảng trường.
"""
m,n,a = map(int,input('nhap vao doc va ngang va kich thuoc da ').split())
#so vien gach chieu ngang co the them vao la 
if(m%a == 0):
    res1 = m//a
else:
    res1 = m//a +1

# so vien gach chieu doc co the them vao duoc la 
if(n%a == 0):
    res2 = n //a
else:
    res2 = m //a +1 

# so vien gach can them vao la 
sum = res1 * res2 
print(sum)