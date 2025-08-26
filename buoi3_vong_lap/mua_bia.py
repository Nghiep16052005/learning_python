
n = int(input('Enter the number of coins: '))
# calculate the initial number of beers bought
so_bia_ban_dau = n // 28
# calculate the initial number of bottles
vo = so_bia_ban_dau
so_chai_do_them = 0
while vo >= 3:
    ans = vo // 3  # number of beers exchanged
    so_chai_do_them += ans
    vo = vo % 3 + ans

print(so_bia_ban_dau + so_chai_do_them)
    
