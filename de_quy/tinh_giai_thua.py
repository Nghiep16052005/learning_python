def giai_thua(n):
    if n == 0:
        return 1
    return n *giai_thua(n-1)