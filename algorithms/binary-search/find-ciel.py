import math


def find_ciel(arr, ele):
    start = 0
    end = len(arr) - 1
    middle = int(math.floor(start+end)/2)
    while(start <= end and arr[middle]!=ele):
        if ele < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1

        middle = int(math.floor(start+end)/2)
    
    if(arr[middle]==ele):
        return arr[middle]
    else:
        return arr[start]

input = [1,2,3,4,5,6,7,9,10,11,12,13,14,15,100,1000,10002,100004]

print(find_ciel(input,10001))