n = int(input('hay nhap vao so ngay: '))
result1= n//365
result2 = n%365
result3 = result2//7
result4 = result2-result3*7
print(result1,result3,result4)

"""
nam = n // 365
n = n %365
tuan = n // 7
n = n%7 
"""