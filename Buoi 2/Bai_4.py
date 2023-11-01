def count_bits_needed(a):
    if a == 0:
        return 1
    else:
        return a.bit_length()

def check_number_properties(b):
    if isinstance(b, (int, float)):
        properties = dir(b)
        print(f"Cac thuoc tinh va phuong thuc cua bien {b}: \n{properties}")
    else:
        print("Day khong phai bien number")

a = int(input("Nhap a: "))
bits_needed = count_bits_needed(a)
print(f"So luong cac bits can thiet de bieu dien so {a} o dang nhi phan: {bits_needed}")
b = 8
check_number_properties(b)
