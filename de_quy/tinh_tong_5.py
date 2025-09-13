# sn = 1/1 + 1/2 + 1/3 +... 
def tong(n):
    if n == 0 :
        return 0
    return 1/n + tong(n-1)