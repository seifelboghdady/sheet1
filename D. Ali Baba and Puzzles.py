# take 4 variable for user 1st, 2nd, 3th and 4th its num check a □ b □ c = d using arithmetic operators (+,−,×)
a, b, c, d = map(int, input().split())
# is exist 6 probabilty
if a + b - c == d or a + b * c == d or a - b + c == d or a - b * c == d or a * b + c == d or a * b -c ==d:
    print("YES")
else:
    print("NO")