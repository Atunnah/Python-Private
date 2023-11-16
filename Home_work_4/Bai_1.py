def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    else:
        return days[month]

def count(date_str):
    day, month, year = map(int, date_str.split('/'))
    days_util_end_of_year = 0
    for i in range(month, 13):
        days_util_end_of_year += days_in_month(i, year)
    days_util_end_of_year -= day - 1
    return days_util_end_of_year

date_str = input("Nhap vao chuoi dd/mm/yyyy: ")
result = count(date_str)
print(f"Tu ngay nhap den cuoi nam do co {result} ngay")
