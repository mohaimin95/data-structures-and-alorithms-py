def largest_sum(arr, num):
    if num > len(arr):
        return None
    temp = 0
    for i in range(num):
        temp += arr[i]
    max = temp
    for i in range(num, len(arr)):
        temp = temp - arr[i-num] + arr[i]
        if(temp > max):
            max = temp

    return max

input = [1,2,3,4,5,6,1,7]
print(largest_sum([1,2,3,4,5,6,1,7],3))
