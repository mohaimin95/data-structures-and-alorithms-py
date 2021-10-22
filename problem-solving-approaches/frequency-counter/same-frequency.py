def is_same_frequency(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    frequency1 = {}
    frequency2 = {}

    for ele in arr1:
        frequency1[ele] = frequency1.get(ele, 0) + 1

    for ele in arr2:
        frequency2[ele] = frequency2.get(ele, 0) + 1

    for key in frequency1:
        if not key**2 in frequency2:
            return False

    return True

print(is_same_frequency([1,2,3],[9,1,4]))
print(is_same_frequency([1,2,3],[1,1,4]))
print(is_same_frequency([1,2],[1,1,4]))
print(is_same_frequency([1,2,3,4,5,6],[1,4,9,16,25,36]))
