import math
# [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,........Infinity]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18, 19, 20, 21,22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]


def find_from_infinite(arr, ele):
    start = 0
    end = 1

    while(arr[end] <= ele):
        start = end+1
        end = start * start

    if(arr[end] == ele):
        return end
    print(start, end)

    middle = int(math.floor(start+end)/2)

    while(start <= end and arr[middle] != ele):
        if(ele < arr[start]):
            end = middle-1
        else:
            start = middle + 1

        middle = int(math.floor(start+end)/2)

    if(arr[middle] == ele):
        return arr[middle]
    else:
        return -1


print(find_from_infinite(arr, 12))
