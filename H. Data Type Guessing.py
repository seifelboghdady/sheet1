a, b, c = map(int, input().split())
res = (a * b) / c
if res % 1 != 0:
    print("double")
else:
    if abs(res)> 2147483647 :
        print("long long")
    else:
        print("int")