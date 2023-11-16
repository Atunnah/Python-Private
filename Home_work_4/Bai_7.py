while True:
    s = input("Nhap chuoi: ").split()
    n = int(input("Nhap n: "))
    if len(s) % n != 0:
        print("Yeu cau nhap lai.")
    else:
        break
a = len(s) // n
s_list = []
for i in range(n):
    start = i * a
    end = (i + 1) * a
    s_list.append(s[start:end])
print(s_list)
