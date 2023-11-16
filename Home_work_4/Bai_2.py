while True:
    n = int(input("Nhap N: "))
    if 1 <= n <= 100:
        break
    else:
        print("N khong dat yeu cau. Vui long nhap lai.\n")
while True:
    l = input("Nhap day so: ").split()
    if n == len(l):
        break
    else:
        print("Chuoi vuot qua N. Vui long nhap lai\n")
l = [int(i) for i in l]
liked_number = []
count = 0
for i in l:
    if i % 2 != 0:
        liked_number.append(i)
        count += 1
print(count)

length = len(liked_number)
liked_number.sort()
for i in liked_number:
     print(i, end=' ')
#print(liked_number)
