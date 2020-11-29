# N = map(int,str(input()).split())
# ans = 0
# while True:
#     if sum(N) % 3 == 0:
#         print(ans)
#     else:
ans = 1
for i in range(1,18):
    ans = ans * i
print(ans)