
s = input("Nhap: ").split()
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
a = []
max_value = max(d.values())
for word, count in d.items():
    if count == max_value:
        a.append((word, count))
t = tuple(a)
print(t)
