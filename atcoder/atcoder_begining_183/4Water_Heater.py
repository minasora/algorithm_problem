N, W = map(int, input().split())
T = []
for i in range(N):
    T.append(list(map(int, input().split())))
ans = [0 for i in range(2*(10**5)+5)]
for i in T:
    ans[i[0]] += i[2]
    ans[i[1]] -= i[2]
for i in range(len(ans)-1):
    ans[i+1] += ans[i]
if max(ans) <= W:
    print("Yes")
else:
    print("No")
