N = input()
N_K = list(map(int,input().split()))
ans = [0 for i in range(2,1000)]
for i in range(998):
    for j in N_K:
        if j % (i+2) == 0:
            ans[i] += 1
print(ans.index(max(ans))+2)
