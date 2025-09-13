# day fibonacci thoa man f1 =0 , f2 =1, fn = fn-1 +fn-2 
"""
Ví dụ cụ thể: fibonacci(5)

fibonacci(5)
= fibonacci(4) + fibonacci(3)

fibonacci(4)
= fibonacci(3) + fibonacci(2)

fibonacci(3)
= fibonacci(2) + fibonacci(1)

fibonacci(2)
= fibonacci(1) + fibonacci(0)
= 1 + 0 = 1

➡ Khi thay ngược trở lên:

fibonacci(2) = 1

fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2

fibonacci(4) = fibonacci(3) + fibonacci(2) = 2 + 1 = 3

fibonacci(5) = fibonacci(4) + fibonacci(3) = 3 + 2 = 5

 Kết quả cuối cùng: fibonacci(5) = 5.
"""
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
        

