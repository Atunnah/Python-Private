
s = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
l = [num for sublist in s for num in (sublist if isinstance(sublist, list) else [sublist])]
print(l)
