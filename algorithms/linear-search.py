def linear_search(arr,ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i
    
    return -1


input = [2,3,45,4,6,234,34,234,244,2423]
output = linear_search(input,45)
print(output)