def reserve(a, m):
    reserved_part = 0
    for i in range(m):
        reserved_part = reserved_part * 10 + a % 10
        a //= 10
    return reserved_part, a

while True:
    n = int(input("Nhap n: "))
    if 5 <= n <= 100:
        break
    else:
        print("Yeu cau nhap lai.\n")
while True:
    m = int(input("Nhap m: "))
    if m >= 3:
        break
    else:
        print("Yeu cau nhap lai.\n")
for i in range(n):
    a = int(input("Nhap so nguyen duong: "))
    if a < 100000:
        print("So vua nhap khong du 6 chu so tro len")
    else:
        reserved_part, remaining_part = reserve(a, m)
        #result = int(str(remaining_part) + str(reserved_part))
        print("So da dao: ", remaining_part, reserved_part, sep="")

