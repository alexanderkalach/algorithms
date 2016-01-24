def find_max_subarray(a):
    if len(a) == 1:
        return [0, 0, a[0], a[0]]

    maxSum = a[1] - a[0]
    min = 0
    max = 1
    for i in range(1, len(a)):
        sum = 0
        for j in range(i + 1, len(a)):
            sum += a[j] - a[j - 1]
            if maxSum < sum:
                maxSum = sum
                max = j
                min = i

    return [min, max, a[min], a[max]]
