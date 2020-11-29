from itertools import combinations, permutations

nums, K = map(int, input().split())
T = []
for i in range(nums):
    T.append(list(map(int, input().split())))
t = list(permutations([i for i in range(1, nums)]))
ans = []
for i in range(len(t)):
    a = 0
    a += T[0][t[i][0]]
    for j in range(len(t[i])-1):
        a += T[t[i][j]][t[i][j+1]]
        if a >= K:
            break
    a += T[0][t[i][-1]]
    ans.append(a)
answer = 0
for i in ans:
    if i == K:
        answer += 1
print(answer)