def can_buy(x):
    total = 0
    i = 1
    while total < x:
        total += i
        i = i * 10 + 1
        return total == x

x = int(input("Nhap x: "))
if can_buy(x):
    print("YES")
else:
    print("NO")
