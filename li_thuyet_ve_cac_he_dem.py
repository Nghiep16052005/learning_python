"""
1. Hệ nhị phân là gì?

Hệ thập phân: chúng ta thường dùng hằng ngày (0–9).

Hệ nhị phân: chỉ dùng 2 chữ số 0 và 1 để biểu diễn số.

Ví dụ:

Thập phân 5 = Nhị phân 101

Thập phân 10 = Nhị phân 1010

Hệ nhị phân được dùng trong máy tính vì mọi tín hiệu điện chỉ có 2 trạng thái: bật (1) hoặc tắt (0).

2. Công thức chuyển thập phân → nhị phân

Cho một số nguyên dương 
𝑁
N ở hệ thập phân:

Cách làm: chia 
𝑁
N liên tiếp cho 2, ghi lại phần dư, sau đó đọc ngược dãy dư.

Công thức tổng quát:

𝑁
=
𝑎
0
×
2
0
+
𝑎
1
×
2
1
+
𝑎
2
×
2
2
+
⋯
+
𝑎
𝑘
×
2
𝑘
N=a
0
	​

×2
0
+a
1
	​

×2
1
+a
2
	​

×2
2
+⋯+a
k
	​

×2
k

Trong đó mỗi 
𝑎
𝑖
∈
{
0
,
1
}
a
i
	​

∈{0,1} chính là các chữ số nhị phân.

👉 Ví dụ: Thập phân 13 → Nhị phân:

13
÷
2
=
6
13÷2=6, dư 1

6
÷
2
=
3
6÷2=3, dư 0

3
÷
2
=
1
3÷2=1, dư 1

1
÷
2
=
0
1÷2=0, dư 1

→ Đọc ngược các dư: 1101

3. Công thức chuyển nhị phân → thập phân

 Ví dụ: Nhị phân 1101 → Thập phân:

1×23+1×22+0×21+1×20=8+4+01=13

📌 Tóm lại:

Thập phân → Nhị phân: chia liên tiếp cho 2, ghi dư, đọc ngược.

Nhị phân → Thập phân: nhân từng chữ số nhị phân với 
 rồi cộng lại.
"""