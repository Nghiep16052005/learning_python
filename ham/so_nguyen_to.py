# ham kiem tra so nguyen to
# so nguyen to la so lon hon 1 va chi chia het cho 1 va chinh no, 1 khong phai so nguyen to
# Luu y : khi code kiem tra tinh chat dung sai -->nen co gang kiem tra no sai -->ket luan bang return 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Nhap mot so nguyen: "))
    if is_prime(num):
        print(num," la so nguyen to.")
    else:
        print(num," khong phai la so nguyen to.")