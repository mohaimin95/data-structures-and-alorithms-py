# [1,1,1,2,2,3,4,4,5]
def count_unique_values(arr):
    if len(arr) <= 1:
        return len(arr)
    i = 0
    for j in range(1, len(arr)):
        if arr[i] == arr[j]:
            j += 1
        else:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return i+1


input = [100, 100, 123, 123, 123, 123, 123, 123,
         123, 123, 200, 200, 2000, 3000, 7000, 7000]
print(count_unique_values(input))
