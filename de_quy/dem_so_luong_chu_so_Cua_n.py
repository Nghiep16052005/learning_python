def dem_so_luong_chu_so(n):
    if n <10 :
        return 1 
    return 1 + dem_so_luong_chu_so(n // 10)