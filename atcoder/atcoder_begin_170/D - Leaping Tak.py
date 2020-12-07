N, K = map(int, input().split())
L = []
for i in range(K):
    L.append(list(map(int, input().split())))
dp = [0 for i in range(N+1)]
dp[1] = 0
def search(pos):
    if pos > N:
        return
    else:
        dp[pos] += 1
        for i in L:
            k_1 = i[0]
            k_2 = i[1]
            for j in range(k_1,k_2+1):
                search(pos+j)
search(1)
print(dp[N])


