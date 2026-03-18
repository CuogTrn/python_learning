# km = float(input("Nhap so km: "))
def taxi_fare(km):
    if km <= 1:
        km = 10000
    elif km <= 10:
        km = 10000 + (km - 1) * 8500
    else:
        km = 10000 + 9 * 8500 + (km - 10) * 7500
    return km

#test case
assert taxi_fare(1) == 10000
assert taxi_fare(5) == 10000 + 4 * 8500
assert taxi_fare(12) == 10000 + 9 * 8500 + 2 * 7500

print("Tat ca test case deu vuot qua")
    