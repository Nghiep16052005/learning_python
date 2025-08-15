n,m = map(int, input('nhap n buoc va so nguyen : ').split())
#b1 tim so buoc toi thieu co the di 
if(n %2 == 0):
    min_step = n//2
else:
    min_step = (n//2)+1
# tim so buoc nho nhat trong doan tu min_step den n 
ans = ((min_step + m-1)//m)*m
if(ans > n):
    print('-1')
else:
    print(ans)

    
