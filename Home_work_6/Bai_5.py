from math import gcd

def simplify_fraction(numerator:int, denominator:int) -> int:
    """This function is to simplify the fraction"""
    common_divisor = gcd(numerator, denominator)
    simplify_numerator = numerator // common_divisor
    simplify_denominator = denominator // common_divisor
    return simplify_numerator, simplify_denominator

def product_of_fractions(n:int) -> int:
    """This function is to calculate the product of fractions"""
    pro_numerator = 1
    pro_denominator = 1
    for _ in range(n):
        a, b = map(int, input("Nhap a, b: ").split())
        pro_numerator *= a
        pro_denominator *= b
    result = simplify_fraction(pro_numerator, pro_denominator)
    return result

n = int(input("Nhap n: "))
result = product_of_fractions(n)
print(f"Phan so toi gian can tim: {result[0]} {result[1]}")
