num = input("Nhap chuoi so: ").split(", ")
num = [int(i) for i in num]
result_dict = {}
for i in num:
    if i in result_dict:
        result_dict[i].append(i)
    else:
        result_dict[i] = [i]
result_list = list(result_dict.values())
print(result_list)
