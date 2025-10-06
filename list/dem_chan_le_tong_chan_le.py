if __name__=='__main__':
    n = int(input('hay nhap gia tri cua mang a : '))
    dem_chan ,dem_le,tong_chan,tong_le = 0,0,0,0
    a = list(map(int,input().split()))
    for i in range(n):
        if(a[i] % 2 == 0):#no la so chan 
            dem_chan += 1
            tong_chan += a[i] 
        else:
            dem_le += 1
            tong_le += a[i]
    
    print(dem_chan,dem_le,tong_chan,tong_le,end=' ')
