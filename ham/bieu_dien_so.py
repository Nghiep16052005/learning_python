"""Bạn được cung cấp một số nguyên x. Bạn có thể biểu diễn x bằng cách tổng của các số trong các số 
1,11,111,1111,11111,... (Các số mà bản thân nó chỉ chứa các chữ số 1)?Bạn có thể sử dụng bất kỳ số nào trong 
số chúng bất kỳ số lần nào). Ví dụ, 33 = 11 + 11 + 11  144 = 111 + 11 + 11 + 11
""" 
"""
vasy la chi can kiem tra phuong trinh 
11a + 111b = n co nghiem nguyen khong am
"""

import math

def check(n):
    for i in range(0, n // 111+1): # so chia het cho 111
        if(n -i * 111) % 11 == 0:# so chia het cho 11
            return True 
    return False