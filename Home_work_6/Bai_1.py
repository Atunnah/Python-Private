
def MyMultiple(*args:float) -> float:
    """This function returns the product of the input numbers."""
    result = 1
    for num in args:
        result *= num
    return result
result1 = MyMultiple(1, 2, 3, 4)
print(result1)
result2 = MyMultiple(5, 5, 5)
print(result2)
result3 = MyMultiple(1.2, 5)
print(result3)
print(MyMultiple.__doc__)
