
class Pycon:
    count = 0

    def __init__(self, name= None, age= None) -> None:
        Pycon.count += 1
        self.id = Pycon.count
        self.name = name
        self.age = age

    def input(self):
        self.name = input("Nhap ten: ")
        self.age = int(input("Nhap tuoi: "))
        print()

    def display(self):
        print(f"ID: {self.id} || Ten: {self.name} || Tuoi: {self.age}")

    @classmethod
    def average_age(cls, pycons: list) -> float :
        """Calculate the average age of Pycons"""
        total_age = sum(pycon.age for pycon in pycons)
        return total_age / pycon.id



n = int(input("Nhap n: "))
pycons = []
for _ in range(n):
    pycon = Pycon()
    pycon.input()
    pycons.append(pycon)

for pycon in pycons:
    pycon.display()

average_age = Pycon.average_age(pycons)
print("Trung binh tuoi: ", average_age)
