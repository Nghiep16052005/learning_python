# 1+ 2+3+... tinh bang n*(n+1)/2
def tinh_tong(n):
    if n == 0:
        return 0
    return n + tinh_tong(n-1) 

if __name__ =='__main__':
    print(tinh_tong(4))