import numpy as np

num_rows = 3
num_columns = 20
a = np.random.randint(0, 11, size=(num_rows, num_columns))
print("Mang luu diem: \n", a)

max_indexs = np.argmax(a, axis=1)
min_indexs = np.argmin(a, axis=1)
print("Vi tri diem lon nhat moi mon: ", max_indexs)
print("Vi tri diem nho nhat moi mon: ", min_indexs)

flat_a = a.flatten()
flat_a = np.delete(flat_a, np.where(flat_a == 0))
print("Ma tran sau khi lam phang va xoa 0: ", flat_a)

sorted_a = np.sort(a, axis=1, order=None)
print("Mang sau khi sap xep: \n", sorted_a)

k = float(input("Nhap k: "))
sorted_a = sorted_a.astype(float)
b = np.zeros((num_rows, num_columns + 1), dtype=float)
for i in range(num_rows):
    pos = [np.searchsorted(sorted_a[i], k)]
    print(f"Vi tri co the chen {k}: ", pos)
    b[i] = np.insert(sorted_a[i], pos, k)
print(f"Mang sau khi chen {k}: ", b)
