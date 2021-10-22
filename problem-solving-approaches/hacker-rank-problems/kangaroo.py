def kangaroo(x1, v1, x2, v2):
    i = 0
    while(x1 <= x2 and i <100):
        print(x1,x2)
        x1 = x1 + v1
        x2 = x2 + v2
        if x1 == x2:
            print("YES")
            return "YES"
        i += 1
    print("NO")
    return "NO"

kangaroo(0,2,5,3)
