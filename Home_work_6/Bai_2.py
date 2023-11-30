
def input_matrix():
    """This function is to input the matrix"""
    n = int(input("Nhap so hang: "))
    m = int(input("Nhap so cot: "))
    matrix = []
    print("Nhap gia tri cua ma tran: ")
    for i in range(n):
        row = []
        for j in range(m):
            element = int(input(f"Nhap phan tu thu{[i]}{[j]}: "))
            row.append(element)
        matrix.append(row)
    return matrix

def transpoted(matrix: list) -> list:
    """This function is to create a transported matrix"""
    print("Ma tran ban dau: ")
    for row in matrix:
        print(" ".join(map(str, row)))
    print()
    print("Ma tran chuyen vi: ")
    transpoted_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    for row in transpoted_matrix:
        print(" ".join(map(str, row)))

matrix = input_matrix()
transpoted(matrix)
#print(transpoted.__doc__)
