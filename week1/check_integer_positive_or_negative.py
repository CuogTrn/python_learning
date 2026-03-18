# a = int(input("Nhap so nguyen: "))
def check_integer(a):
    if a > 0:
        return "so nguyen duong"
    elif a < 0:
        return "so nguyen am"
    else:
        return "khong phai so nguyen duong va am"

# Test case
assert check_integer(5) == "so nguyen duong"   # số dương
print(check_integer(5))
assert check_integer(-3) == "so nguyen am"     # số âm
print(check_integer(-3))
assert check_integer(0) == "khong phai so nguyen duong va am"  # số 0
print(check_integer(0))

