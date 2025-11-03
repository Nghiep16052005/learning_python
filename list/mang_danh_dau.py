# cho mang A gom n phan tu, dem xem moi phan tu trong mang xuat hien bao
# nhieu lan va in theo thu tu tu nho den lon 
if __name__=='__main__':
    a = [1,2,3,2,3,1,5,3,2,3,4,3,2,42,3]
    cnt = [0]*10000007
    for x in a : 
        cnt[x] += 1
    l,r = min(a),max(a)
    for i in range(l,r+1):
        print(f"{i} + co tang suat la: {cnt[i]}")
# in theo thu tu xuat hien
if __name__ == '__main__':
    a = [1,2,3,2,3,1,5,3,2,3,4,3,2,42,3]
    cnt = [0]*10000007
    for x in a : 
        cnt[x] += 1
    for i in a 