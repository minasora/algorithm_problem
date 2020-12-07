n, m = map(int, input().split())
l = list(map(int, input().split()))
ans = [999999 for i in range(5000001)]
ans[0] = 0
for i in range(n-min(l)+1):
    for j in l:
        if ans[i+j] >= ans[i] + 1:
            ans[i+j] = ans[i] + 1
print(ans[n])