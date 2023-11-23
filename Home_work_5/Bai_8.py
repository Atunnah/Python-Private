
championLOL = ["Yasuo", "Lee Sin", "Zed", "Master Yi", "Garen", "Tryndamere"]
dataLOL = [
    {"price": 6300, "Ulti": "Trăn trối"},
    {"price": 4800, "Ulti": "Nộ Long Cước"},
    {"price": 4800, "Ulti": "Dấu Ấn Tử Thần"},
    {"price": 450, "Ulti": "Chiến Binh Sơn Cước"},
    {"price": 450, "Ulti": "Công Lý Demacia"},
    {"price": 1350, "Ulti": "Từ Chối Tử Thần"}	
]
LOL_dict = {champion: data for champion, data in zip(championLOL, dataLOL)}
s = input("Nhap champion: ")
if s in LOL_dict:
    print(f"Price cua champion {s} la: {LOL_dict[s]['price']} voi Ulti {LOL_dict[s]['Ulti']}")
else:
    print("Khong ton tai champion nay")
