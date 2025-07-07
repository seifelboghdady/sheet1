n, m, k = map(int, input().split())
ans = 0
# first with high 2- eye, 1- mouse, 1- body
sub = min(n//2, m, k)
n -= sub
m -= sub
k -= sub
ans += sub
# second with medium 1- eye , 1- mouse, 1- body
sub = min(n, m, k)
n -= sub
m -= sub
k -= sub
ans += sub
#third with low 2- eye , 1- body
sub = min(n //2, k)
ans += sub

#print answer
print(ans)