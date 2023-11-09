k = int(input("Nhap so luong hoc sinh: "))
for i in range(k):
    name = input("Nhap ten: ")
    while True:
        tx1 = int(input("Nhap diem thuong xuyen 1: "))
        if 0 <= tx1 <= 100:
            break
        else:
            print("Yeu cau nhap lai.\n")
    while True:
        tx2 = int(input("Nhap diem thuong xuyen 2: "))
        if 0 <= tx2 <= 100:
            break
        else:
            print("Yeu cau nhap lai.\n")
    tong = tx1 + tx2
    if tong >= 190:
        print(name, tong, "Xuat sac")
    elif 150 <= tong < 190:
        print(name, tong, "Gioi")
    elif 100 <= tong < 150:
        print(name, tong, "Kha")
    elif tong < 100:
        print(name, tong, "Yeu")
