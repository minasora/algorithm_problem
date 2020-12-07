n = int(input())
flag = 0
for i in range(n):

    d_1, d_2 = map(int, input().split())
    if d_1 == d_2:
        flag += 1
    else:
        flag = 0
    if flag == 3:
        print("Yes")
        exit()
print("No")
