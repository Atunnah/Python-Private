import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def is_rectangle(point1, point2, point3):
    side1 = distance(point1, point2)
    side2 = distance(point2, point3)
    side3 = distance(point1, point3)
    return (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)

x1, y1 = map(float, input("Nhap toa do diem 1: ").split())
x2, y2 = map(float, input("Nhap toa do diem 2: ").split())
x3, y3 = map(float, input("Nhap toa do diem 3: ").split())

point1 = (x1, y1)
point2 = (x2, y2)
point3 = (x3, y3)

if is_rectangle(point1, point2, point3):
    print("\nTAM GIAC")
else:
    print("\nKHONG PHAI TAM GIAC")
