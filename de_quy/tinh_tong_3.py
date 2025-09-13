# 1 ^3 + 2^3 +..... tinh bang [(n*(n+1) /2]^2
def tinh_tong(n):
    if n ==0:
        return 0
    return n*n*n+tinh_tong(n-1)