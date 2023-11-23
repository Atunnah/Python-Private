
table_1 = set(map(int, input("Nhap ban 1: ").split(", ")))
table_2 = set(map(int, input("Nhap ban 2: ").split(", ")))
if len(table_1.intersection(table_2)) > 0:
    print("Sinh vien dang ky hoc o 2 ban la ", table_1.intersection(table_2))
else:
    print("Khong co sinh vien nao dang ky hoc o 2 ban")
print("Danh sach tong hop sinh vien o 2 ban la: ", table_1.union(table_2))
if len(table_1.difference(table_2)) > 0:
    print("Danh sach sinh vien chi dang ky o ban 1: ", table_1.difference(table_2))
else:
    print("Sinh vien o ban 1 trung voi ban 2")
if len(table_1.symmetric_difference(table_2)) > 0:
    print("Sinh vien dang ky duy nhat o 1 ban: ", table_1.symmetric_difference(table_2))
else:
    print("Tat ca sinh vien deu dang ky ca 2 ban")
