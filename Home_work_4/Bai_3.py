import re

s = input("Nhap chuoi: ")
num = re.findall(r"-?\d+", s)
summ = sum(map(int, num))
print(f"Tong la: {summ}")
