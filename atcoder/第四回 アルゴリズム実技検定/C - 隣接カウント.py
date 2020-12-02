N = int(input())
K = list(map(int, input().split()))
k = sum(K)
ans = 999999
for i in range(N):
    s = 0
    for j in range(i,N+i):
        if  j >= N:
            s += K[j - N]
        else:
            s += K[j]
        if ans > abs(s - (k - s)):
            ans = abs(s - (k - s))
        if s > k - s:
            break
print(ans)

