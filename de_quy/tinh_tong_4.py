# -1 + 2 -3 +4 -5 + .....

def tinh_tong(n):
    if n == 0:
        return 0
    if n % 2 == 0: #n la chan 
        return n + tinh_tong(n-1)
    else:
        return -n + tinh_tong(n-1)
