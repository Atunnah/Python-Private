s = input("Nhap chuoi ky tu: ")
check_1 = "hit" in s
check_2 = "HIT" in s
check_3 = "14" not in s

print(check_1 or check_2)
print(check_3)
