import numpy as np
n,m,r= map(int, input().split())
dis = [9999999 for i in range(n)]
e = []
dis[r] = 0
for i in range(m):
    e.append(list(map(int, input().split())))
for i in range(n-1):
    for j in e:
        if dis[j[1]] >= dis[j[0]] + j[2]:
            dis[j[1]] = dis[j[0]] + j[2]
for i in dis:
    if i== 9999999:
        print("INF")
    else:
        print(i)
