from itertools import combinations,permutations
n = map(int, input())
S = input()
k = permutations(S)
flag = True
for i in k:
    tar = ""
    for j in i:
        tar += j
    if tar != S and reversed(tar) != S:
        print(tar)
        flag = False
        break
if flag:
    print("None")