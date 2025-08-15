# d1 la khoang cach tu nha den cua hang thu nhat
# d2 la khoang cach tu nha den cua hang thu hai
# d3 la khoang cach giua 2 cua hang 
d1,d2,d3 = map(int,input('nhap vao cac khoang cach :').split())
# TH1: nha --> cuahang1 --> cuahang2-->nha
khoangcach1 = d1+d3+d2 
#TH2 : nha --> cuahang1 -->nha -->cuahang2-->nha
khoangcach2 = 2*(d1+d2)
#TH3 : nha --> cuahang1 --> cuahang2 -->cuahang1 -->nha
khoangcach3 = 2*d1 + 2*d3 
#TH4 : nha -->cuahang2 -->cuahang1--> cuahang2 -->nha 
khoangcach4 = 2*d2 + 2*d3 
# quang duong lon nhat: 
quangduong_max = min(khoangcach1,khoangcach2,khoangcach3,khoangcach4)
print(quangduong_max)