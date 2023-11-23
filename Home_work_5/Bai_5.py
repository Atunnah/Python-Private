
s = set(map(int, input("Nhap: ").split()))
if 11 not in s:
    s.add(11)
print(s)
pairs = []
for num1 in s:
    for num2 in s:
        if num1 + num2 == 11:
            pairs.append((num1, num2))
t = tuple(pairs)
total = sum(map(sum, t))
if len(pairs) == 0:
    print("Khong co cap so nao co tong la 11")
else:
    print("Cac cap so da ket hop: ", t, " co tong la: ", total)
