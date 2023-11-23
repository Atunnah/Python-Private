
while True:
    n = int(input("Nhap n: "))
    if n > 0:
        break
    else:
        print("n < 0. Yeu cau nhap lai.")
while True:
    s = set(map(int, input("Nhap set: ").split(", ")))
    if len(s) == n:
        break
    else:
        print("Yeu cau nhap lai")
s = sorted(s)
a = int(input("Nhap a: "))
sub_s = set()
sum = 0
for i in s:
    if sum + i <= a:
        sum += i
        sub_s.add(i)
    else:
        break
print(sub_s)
