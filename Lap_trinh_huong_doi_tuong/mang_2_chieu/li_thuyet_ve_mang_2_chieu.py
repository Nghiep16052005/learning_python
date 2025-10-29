if __name__=='__main__':
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        b = list(map(int,input().split()))
        a.append(b) 
    for i in range(n):
        for j in range(m):
            print(a[i][j])
