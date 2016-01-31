import math

def find_greatest_common_divisor(a, b):
    if a == b:
        return a
    elif a < b:
        a, b = b, a

    return find_greatest_common_divisor_rec(a, b)

def find_greatest_common_divisor_rec(a, b):
    r = math.fmod(a, b)
    if r > 0:
        return find_greatest_common_divisor_rec(b, r)

    return b
