def sum_zero_pair(arr):
    left = 0
    right = len(arr) - 1

    while(left < right):
        sum = arr[left] + arr[right]
        if sum == 0:
            return [arr[left], arr[right]]
        elif sum > 0:
            right -= 1
        else:
            left += 1

    return None


input = [-1, 0, 1, 2, 3, 4]
print("Find sum zero pair:", input, sum_zero_pair(input))
