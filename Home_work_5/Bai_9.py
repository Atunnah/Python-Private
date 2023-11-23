import random

def generate_username(student_id):
    return f"2021{student_id:06d}"

def generate_password(student_id):
    majors = ["CNTT", "KHMT", "KTPM", "HTTT"]
    random_major = random.choice(majors)
    return f"{random_major}2021{student_id:06d}"

def create_student_account(N):
    student_accounts = {}
    for i in range(N):
        student_id = i + 1
        username = generate_username(student_id)
        password = generate_password(student_id)
        account_info = {"Username": username, "Password": password}
        account_id = f"Account{i + 1}"
        student_accounts[account_id] = account_info
    return student_accounts


while True:
    N = int(input("Nhap N: "))
    if 10 <= N <= 100000:
        break
    else:
        print("Yeu cau nhap lai.")
result = create_student_account(N)
for key, value in result.items():
    print(f"{key}: {value}")
