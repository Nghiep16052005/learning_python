"""
ắt đầu: decToBin(13)

13 < 2 ❌ → đi xuống else

Gọi tiếp decToBin(13 // 2) = decToBin(6)

Sau đó sẽ print(13 % 2) = print(1)

Gọi tiếp: decToBin(6)

6 < 2 ❌ → đi xuống else

Gọi tiếp decToBin(6 // 2) = decToBin(3)

Sau đó sẽ print(6 % 2) = print(0)

Gọi tiếp: decToBin(3)

3 < 2 ❌ → đi xuống else

Gọi tiếp decToBin(3 // 2) = decToBin(1)

Sau đó sẽ print(3 % 2) = print(1)

Gọi tiếp: decToBin(1)

1 < 2 → in ngay print(1)

Quay ngược trở lại (hàm kết thúc dần):

Từ decToBin(1) in ra 1

Trở về decToBin(3), in tiếp 1

Trở về decToBin(6), in tiếp 0

Trở về decToBin(13), in tiếp 1

Kết quả in ra theo thứ tự:
1101
"""
def dequy(n):
    if n < 2 : 
        print(n, end='')
    else:
        dequy(n // 2)
        print(n %2 , end='')
    
if __name__ == '__main__':
    n = int(input('hay nhap vao n : '))
    dequy(n)

"""
cach 2 : 
Chạy tay với n = 13

F(13)

13 != 0 ✅ → gọi F(6), rồi sẽ in 13 % 2 = 1.

F(6)

6 != 0 ✅ → gọi F(3), rồi sẽ in 6 % 2 = 0.

F(3)

3 != 0 ✅ → gọi F(1), rồi sẽ in 3 % 2 = 1.

F(1)

1 != 0 ✅ → gọi F(0), rồi sẽ in 1 % 2 = 1.

F(0)

n == 0 → không làm gì, quay ngược lại.
noi cbung nghia la f4 chay xong thi den f9 chay xuong duoi cau dieu kien 9 % 2 = 1 
code : 
if n != 0:
    F(n // 2)
    print(n % 2, end='')

    """