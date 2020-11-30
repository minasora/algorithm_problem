t = int(input())
cases = []
for i in range(t):
    cases.append(list(map(int,input().split())))
for i in range(len(cases)):
    ans = 0
    tar_x = max(cases[i][0], cases[i][2],cases[i][4])
    tar_y = max(cases[i][1],cases[i][3],cases[i][5])
    ans += max(tar_x )
