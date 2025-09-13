#tinh tong 1 ^2 + 2^2 + 3^3 +.. tinh bang n*(n+1)*(2n+1)/6
def tinh__tong(n):
    if n == 0:
        return 0
    return n*n + tinh__tong(n-1)