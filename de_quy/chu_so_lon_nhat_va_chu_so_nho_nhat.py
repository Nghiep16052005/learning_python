"""
Bước 1: Gọi find_max_digit(237)

237 < 10 ❌ → vào else

last = 237 % 10 = 7

Gọi tiếp find_max_digit(237 // 10) = find_max_digit(23)

Kết quả cuối cùng: max(7, find_max_digit(23))

Bước 2: Gọi find_max_digit(23)

23 < 10 ❌

last = 23 % 10 = 3

Gọi tiếp find_max_digit(23 // 10) = find_max_digit(2)

Kết quả: max(3, find_max_digit(2))

Bước 3: Gọi find_max_digit(2)

2 < 10 ✅ → trả về 2

Quay ngược lại:

find_max_digit(23) = max(3, 2) = 3

find_max_digit(237) = max(7, 3) = 7

✅ Kết quả cuối cùng:

find_max_digit(237) = 7

"""
def digital_max(n):
    if n < 10 : 
        return n 
    else: 
        return max(n%10,digital_max(n //10))
    
def digital_min(n):
    if n < 10 : 
        return n 
    else: 
        return min(n%10,digital_min(n //10))