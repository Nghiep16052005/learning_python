a,b,c,d = map(int, input('nhap vao 4 so nguyen: ').split())
"""
print('so lon nhat trong 4 so la: ',max(a,b,c,d))
print('so nho nhat trong 4 so la: ',min(a,b,c,d))
"""
min_value, max_value = a, a 
# tim max_value 
if b > max_value : max_value = b 
if c > max_value : max_value = c
if d > max_value : max_value = d 

# tim min_value 
if b <min_value : min_value = b 
if c <min_value : min_value = c
if d <min_value : min_value = d  

print(max_value , min_value)
