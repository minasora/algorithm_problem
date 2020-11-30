n = int(input())
k_1 = list(map(int, input().split()))
k_2 = list(map(int, input().split()))
ans = [0 for i in range(n)]
if k_1[0] == k_2[0]:
    ans[0] = 1
for i in range(1, n):
    if k_1[i] == k_2[i]:
        ans[i] = ans[i-1]+1
    else:
        ans[i] = 0
print(max(ans))