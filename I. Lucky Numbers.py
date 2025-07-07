n = int(input())

reminder = n % 10
div = n // 10

if div > reminder:
    if reminder == 0 or div % reminder == 0:
        print("YES")
    else:
        print("NO")
else:
    if div == 0 or reminder % div == 0 :
        print("YES")
    else:
        print("NO")