n, k = map(int, input().split())
s = input().split()
l = 0
r = 2**k
def search_win(l, r):
    if r - l>= 1:
        return r
    else:
        search_win((l+r+1)/2)