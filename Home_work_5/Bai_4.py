
n = int(input("Nhap n: "))
a = []
for i in range(n):
    s = input(f"Nhap xau thu {i + 1}: ")
    a.append(s)
b = tuple(a)
count = 0
for i in b:
    if i.isdigit():
        count += 1
print("So phan tu co dang so: ", count)

