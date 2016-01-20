def find_max_subarray(a):
    if len(a) == 1:
        return [0, 0, a[0], a[0]]
    min = 0
    max = len(a) - 1
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] < a[j] and (a[j] - a[i] > a[max] - a[min]):
                max = j
                min = i

    return [min, max, a[min], a[max]]