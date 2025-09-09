# no co ham co san trong Python la ham combinations trong thu vien itertools
# ham comb(n,k) tra ve tat ca cac to hop chap k cua cac phan tu trong mot danh sach
import math
def tohop(n,k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))# n! / (k! * (n-k)!)
# vi du: tohop(5,2) = 10
if __name__ == "__main__":
    n = int(input("Nhap so nguyen duong n: "))
    k = int(input("Nhap so nguyen duong k: "))
    print("So to hop chap", k, "cua", n, "la:", tohop(n,k))
# So to hop chap 2 cua 5 la: 10
# so to hop chap 3 cua 5 la: 10
# so to hop chap 4 cua 5 la: 5 