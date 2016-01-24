import math

def find_greatest_common_divisor(a, b):
    if a == b:
        return a
    elif a < b:
        a, b = b, a

    r = math.fmod(a, b)
    while r > 0:
        a, b = b, r
        r = math.fmod(a, b)

    return b
