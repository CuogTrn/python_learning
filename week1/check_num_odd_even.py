def check_even_odd(n):
    if n % 2 == 0:
        return "so chan"
    else:
        return "so le"
    
assert check_even_odd(10) == "so chan"
print(check_even_odd(10))
assert check_even_odd(5) == "so le"
print(check_even_odd(5))