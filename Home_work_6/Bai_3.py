
def input_array(n):
    """This function is to input array"""
    array = []
    for i in range(n):
        num = int(input(f"Nhap so thu {i + 1}: "))
        array.append(num)
    return array

def sum(array: list, t: int):
    """This function is to calculate sum from start index to the index of x"""
    sum_list = []
    for i in range(t):
        x = int(input(f"Nhap x{i + 1}: "))
        sum = 0
        for j in range(x + 1):
            sum += array[j]
        sum_list.append(sum)
    print("Cac tong can tim: ")
    for i in list(sum_list):
        print(i)


n = int(input("Nhap so luong phan tu cua mang: "))
array = input_array(n)
t = int(input("Nhap so luong x: "))
sum(array, t)
    