import numpy as np

n = 5
a = np.random.randint(1, 15, n)
print("Mang a: ", a)
b = np.arange(2, 101, 2)
print("Mang b: \n", b)
c = np.zeros((n, n))
print("Ma tran c: \n", c)
d = np.eye(n)
print("Ma tran don vi d: \n", d)
e = np.diag(a)
print("Ma tran duong cheo e: \n", e)
