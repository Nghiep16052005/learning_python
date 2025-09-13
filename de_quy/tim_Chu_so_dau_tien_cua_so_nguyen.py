def tim_chu_so_dau_tien_cua_so_nguyen(n):
    if n <10 : 
        return n
    return tim_chu_so_dau_tien_cua_so_nguyen(n //10) 