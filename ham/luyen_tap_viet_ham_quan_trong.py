#cau 1:kiem tra n co phai so nguyen to khong 
import math
def is_prime(n):
    if n < 2: 
        return 0
    else:
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return 0
            
    return 1

#cau 2:in tong chu so cua n
def print_sum_of_digits(n):
    sum = 0
    while n >0:
        sum += n % 10
        n //=10 
    return sum
#cau 3:in tong chu so chan cua n 
def print_sum_of_even_digits(n):
    sum = 0
    while n >0 :
        if n % 2 == 0:
            sum += n % 10
        n //=10 
    return sum

#cau 4 : in tong chu so cua n la so nguyen to
def print_sum_of_digits_if_prime(n):
    sum = 0
    while n > 0:
        tmp = n % 10
        if is_prime(tmp):
            sum += n % 10
        n //= 10
    return sum
#cau 5 in so lat nguoc cua n vi du 123 -> 321 , reverse nghia la dao nguoc 
def print_reverse_number(n):
    reverse = 0
    while n > 0 :
        reverse = reverse * 10 + n % 10
        n //= 10
    return reverse

#cau 6: in so luong uoc cua n la nguyen to (lam tuong tu phan tich thua so nguyen to)
def count_prime_factors(n):
    count = 0 
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            if is_prime(i):
                count += 1
            if i != n // i and is_prime(n // i):
                count += 1
    return count

# cau 7: in uoc nguyen to lon nhat cua n
def largest_prime_factor(n):
    res = -1
    for i in range(1, math.isqrt(n)+1):
        if n % i == 0:
            if is_prime(i):
                res = i 
            if is_prime(n // i):
                res = n // i
    if is_prime(n):
        res = max(res,n)
    return res
# cau 8: kiem tra neu n ton tai it nhat 1 so 6, neu dung in 1 sai in 0
def has_six(n):
    while n > 0:
        if n % 10 == 6:
            return 1
        n //= 10
    return 0
# cau 9: kiem tra neu tong chu so cua n chia het cho 8, neu dung in 1 sai in 0
def check_sum_divisible_by_8(n):
    return 1 if print_sum_of_digits(n) % 8 == 0 else 0
# cau 10 tinh tong giai thua cac chu so cua n va in ra. Vi du n = 123 , sum = 1! + 2! + 3!
def factorial(n):
    tich = 1
    for i in range(1, n+1):
        tich *= i
    return tich

def sum_of_factorials(n):
    sum = 0 
    while n > 0:
        sum += factorial(n%10)
        n //= 10 
    return sum
#cau 11:kiem tra n co phai chi duoc tao boi 1 so hay khong ? 222,... neu dung in ra 1 sai in ra 0
def check_single_digit_repeated(n):
    tmp = n % 10# lay chu so cuoi cung de duyet vong lap for kiem tra cac so con lai 
    while n != 0 :
        if tmp != n % 10 :
            return 0 
        n //= 10
    return 1
#cau 12: kiem tra n co phai co chu so tan cung la lon nhat hay khong, tuc la chu so hang don vi cua n
# khong co chu so nao cua n lon hon hang don vi cua no . dung in ra 1 sai in ra 0 
def check_last_digit_max(n):
    tmp = n%10 # lay chu so tan cung de kiem tra xem co so nao lon hon so nay khong 
    n //= 10 
    while n != 0:
        if tmp < n %10 : 
            return 0
        n //=10
    return 1
# cau 13: in tong chu so cua n voi so mu la so chu so. vi du 123 thi tinh 1^3 + 2^3 + 3^3
#ham dem so luong chu so cua n:
def count_digits(n):
    count = 0 
    while n > 0:
        count += 1
        n //= 10 
    return count
#ham tinh so mu cua so n :
def count_digit_power(a,b):
    tich = 1
    for i in range(1, b+1):
        tich *= a 
    return tich 
 

def sum_power_digits(n):
    sum = 0 # dung de dem so luong so mu 
    tmp = count_digits(n)# dem so luong so mu cua n
    while n > 0 :
        sum += count_digit_power(n%10 ,tmp)
        n //= 10 
    return sum 
  



if __name__ == "__main__":
    #sentence 1: call function is_prime
    n = int(input("Nhap n: "))
    if is_prime(n):
        print(n,"la so nguyen to")
    else:
        print(n,"khong phai so nguyen to")
    #sentence 2: call function print_sum_of_digits
    print("Tong chu so cua", n, "la", print_sum_of_digits(n))
    #sentence 3:call function print_sum_of_even_digits
    print("Tong chu so chan cua", n, "la", print_sum_of_even_digits(n))
    #sentence 4: call function print_sum_of_digits_if_prime
    print("Tong chu so cua", n, "la so nguyen to la", print_sum_of_digits_if_prime(n))
    #sentence 5: call function print_reverse_number
    print("So lat nguoc cua", n, "la", print_reverse_number(n))
    #sentence 6: call function count_prime_factors
    print("So luong uoc cua", n, "la so nguyen to la", count_prime_factors(n))
    # sentence 7: call function largest_prime_factor(n)
    print("uoc nguyen to lon nhat cua n la:",largest_prime_factor(n))
    # sentence 8 : call function has_six(n)
    if has_six(n):
        print("n co ton tai it nhat 1 so 6")
    else:
        print("n khong ton tai 1 so 6 nao ca")
    #sentence 9: call function check_sum_divisible_by_8
    if check_sum_divisible_by_8(n):
        print("tong chu so cua n chia het cho 8")
    else:
        print("tong chu so cua n khong chia het cho 8")
    #sentence 10: call funtion sum_of_factorial
    print("tong giai thua cac chu so cua n la:", sum_of_factorials(n))
    #sentence 11: call function check_single_digit_repeatead 
    if check_single_digit_repeated(n):
        print("n duoc tao boi 1 so ")
    else:
        print("n khong duoc tao boi 1 so ")
    # sentence 11: call function check_last_digit_max
    if check_last_digit_max(n):
        print("so n co chu so tan cung la lon nhat")
    else:
        print("so n khong co chu so tan cung la lon nhat.")
    #sentence 12: call function sum_power_digits
    print("tong chu so cua n voi so mu la so chu so la: ",sum_power_digits(n))