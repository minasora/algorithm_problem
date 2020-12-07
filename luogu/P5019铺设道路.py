n = int(input())
N = list(map(int, input().split()))
def find(N,ans):
    if max(N)==0:
        return ans
    else:
        ans += 1
