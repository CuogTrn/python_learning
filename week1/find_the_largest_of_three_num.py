def find_max_of_three_num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

#test case
assert find_max_of_three_num(10, 4, 3) == 10
print(find_max_of_three_num(10, 4, 3))
assert find_max_of_three_num(1, 2, 3) == 3
print(find_max_of_three_num(1, 2, 3))
assert find_max_of_three_num(3, 9, 6) == 9
print(find_max_of_three_num(3, 9, 6))