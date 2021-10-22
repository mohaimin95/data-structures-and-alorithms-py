def factorial_without_recursion(num):
    result = 1
    while(num != 1):
        result *= num
        num -= 1
    return result


def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)


input = 6
output = factorial(input)
print(output, factorial_without_recursion(input))
