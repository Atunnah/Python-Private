import numpy as np

n = int(input("Nhap kich thuoc cua vector: "))
aa = input("Nhap vector a: ")
a = np.fromstring(aa, dtype=int, sep=' ')
while len(a) != n:
    print("Do dai cu vector a khong phu hop voi n.")
    aa = input("Nhap lai vector a: ")
    a = np.fromstring(aa, dtype=int, sep=' ')

bb = input("Nhap vector b: ")
b = np.fromstring(bb, dtype=int, sep=' ')
while len(b) != n:
    print("Do dai cu vector a khong phu hop voi n.")
    bb = input("Nhap lai vector b: ")
    b = np.fromstring(bb, dtype=int, sep=' ')
print()
print("Gia tri max cua a:", np.max(a))
print("Gia tri min cua a:", np.min(a))
print("Gia tri trung binh cua a:", np.mean(a))
print("Do lech chuan cua a:", np.std(a))
print("Gia tri trung vi cua a:", np.median(a))
print()
print("Gia tri max cua b:", np.max(b))
print("Gia tri min cua b:", np.min(b))
print("Gia tri trung binh cua b:", np.mean(b))
print("Do lech chuan cua b:", np.std(b))
print("Gia tri trung vi cua b:", np.median(b))

c = np.column_stack((a, b))
print("Ma tran c: \n", c)

d = np.random.normal(loc=np.mean(b), scale=np.std(b),size=(n, n))
print("Ma tran d: \n", d)

#Ma tran chuyen vi:
transpose_d = np.transpose(d)
#Ma tran nghich dao:
try:
    inverse_d = np.linalg.inv(d)
except np.linalg.LinAlgError:
    inverse_d = "Ma tran khong kha nghich."

print("Tong 2 ma tran: ", a + b)
print("Hieu 2 ma tran: ", a - b)
print("Tich 2 ma tran: ", a @ b)
print("Ma tran chuyen vi cua d: \n", transpose_d)
print("Ma tran nghich dao cua d: \n", inverse_d)
print("Tich ma tran chuyen vi cua d voi ma tran nghich dao cua d: \n", transpose_d @ inverse_d)

e = np.expand_dims(c, axis=0)
print("Tensor e (3-D): \n", e)
