
d = {'2022': '3.5', '2023': '2.0', '2024': '1.7', '2026': '3.9', '2021': '2.6', '2010': '1.5'}
count = 0
for id, score in d.items():
    if 2.5 <= float (score) <= 3.5:
        count += 1
print(f"Co {count} sinh vien co diem tong ket trong đoạn [2.5, 3.5].")
d['2018'] = '2.7'
for id, score in dict(d).items():
    if float (score) < 2.0:
        d.pop(id)
print(d)

