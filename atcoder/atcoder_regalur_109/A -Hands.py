a, b, x, y = map(int,input().split())
ans = 0
k = abs(a-b)
if a==b:
    print(x)
elif a > b:
    ans += min((2*k-1)*x, (k-1)*y+x)
    print(ans)
else:
    ans += min((2*x*k)+x, k*y+x)
    print(ans)



