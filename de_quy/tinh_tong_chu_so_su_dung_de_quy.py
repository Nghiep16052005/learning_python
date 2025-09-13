"""
bắt đầu: sumDigits(30)

n = 30 ≠ 0 → đi vào else

Trả về (30 % 10) + sumDigits(30 // 10)

(30 % 10) = 0

(30 // 10) = 3
👉 sumDigits(30) = 0 + sumDigits(3)

Gọi tiếp: sumDigits(3)

n = 3 ≠ 0 → đi vào else

Trả về (3 % 10) + sumDigits(3 // 10)

(3 % 10) = 3

(3 // 10) = 0
👉 sumDigits(3) = 3 + sumDigits(0)

Gọi tiếp: sumDigits(0)

n == 0 ✅ → trả về 0

Quay ngược trở lại

sumDigits(3) = 3 + 0 = 3

sumDigits(30) = 0 + 3 = 3

✅ Kết quả cuối cùng:

sumDigits(30) = 3
"""
def sumDigits(n):
    if n < 10: 
        return 0
    else:
        return (n%10)+sumDigits(n//10)