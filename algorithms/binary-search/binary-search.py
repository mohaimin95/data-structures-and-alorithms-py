# [input] sorted array
# [output] index or -1

import math


def binary_search(arr, ele):
    start = 0
    end = len(arr) - 1
    middle = int(math.floor((start + end)/2))

    while(arr[middle] != ele and start <= end):
        if ele < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = int(math.floor((start + end)/2))

    if arr[middle] == ele:
        return middle
    else:
        return -1


input = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
output = binary_search(input, 5)
print(output)
