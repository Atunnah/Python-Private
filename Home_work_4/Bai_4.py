n = int(input("Nhap n: "))
while True:
    num = input("Nhap mang: ").split()
    if n == len(num):
        break
    else:
        print("Yeu cau nhap lai\n")
num = [int(i) for i in num]
even_sum = 0
odd_sum = 0
for i in num:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
if even_sum > odd_sum:
    print("even")
elif even_sum < odd_sum:
    print("odd")
else:
    print("equal")
