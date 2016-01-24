import math


def find_max_crossing_subarray(a, l, m, r):
    leftSum = - float('inf')
    sum = 0
    for i in range(m, l - 1, -1):
        sum += a[i]
        if sum > leftSum:
            leftSum = sum
            min = i

    rightSum = - float('inf')
    sum = 0
    for i in range(m + 1, r + 1):
        sum += a[i]
        if sum > rightSum:
            rightSum = sum
            max = i

    return [min, max, leftSum + rightSum]

def find_max_subarray(a, l, r):
    if l == r:
        return [l, r, a[l]]

    m = int(math.floor((l + r) / 2))
    leftS = find_max_subarray(a, l, m)
    rightS = find_max_subarray(a, m + 1, r)
    crossS = find_max_crossing_subarray(a, l, m, r)

    if leftS[2] >= rightS[2] and leftS[2] >= crossS[2]:
        return leftS
    elif rightS[2] >= leftS[2] and rightS[2] >= crossS[2]:
        return rightS
    else:
        return crossS
