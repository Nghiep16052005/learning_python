"""
bạn được cung cấp một bảng hình chữ nhật có kích thước M × N hình vuông đơn vị. Ngoài ra, bạn được cung cấp một số lượng không giới hạn các mảnh domino tiêu chuẩn kích thước 2 × 
1. Bạn được phép xoay các mảnh domino. Bạn được yêu cầu đặt càng nhiều domino càng tốt trên bảng để đáp ứng các điều kiện sau:
Mỗi domino hoàn toàn bao gồm hai hình vuông đơn vị.
Không có hai domino trùng nhau.
Mỗi domino nằm hoàn toàn bên trong bảng. Nó được phép chạm vào các cạnh của bảng.
Tìm số lượng domino tối đa thỏa mãn điều kiện trên
"""

n,m = map(int,input('nhap vao kich thuoc so hang va so cot: ').split())
if(n%2 ==0):
    print((n//2)*m)
elif(n%2 != 0):
    print(((n-1)//2)*m +m//2)

