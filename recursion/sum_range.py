def sum_range_without_recursion(num):
    result = 0
    for i in range(1, num):
        result += num
    return result


def sum_range_with_recursion(num):
    if num <= 1:
        return 1
    return num + sum_range_with_recursion(num-1)


print(sum_range_without_recursion(3))
print(sum_range_with_recursion(3))
