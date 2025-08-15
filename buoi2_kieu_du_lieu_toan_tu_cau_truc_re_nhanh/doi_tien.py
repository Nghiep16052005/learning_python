n = int(input('nhap so tien: '))
ans1 = n // 100
res1 = n % 100 
ans2 = res1 //20 
res2 = res1 %20
ans3 = res2 //10
res3 = res2 %10 
ans4 = res3 //5 
res4 = res3 %5 
# ans5 = res4 
"""
ans = n//100
n%100
ans += ......
"""
print('tong so to la : ',ans1+ans2+ans3+ans4+res4)


