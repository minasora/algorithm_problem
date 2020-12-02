n, m = map(int, input().split())
find = [i for i in range(n+1)]
def if_same_union(a, b, find):
    if find[a] == b:
        return True
    elif find[a] == a:
        return False
    else:
        return if_same_union(find[a], b, find)
for i in range(m):
    z, x, y = map(int, input().split())
    if z == 1:
        find[x] = y
    else:
        if if_same_union(x, y, find):
            print("Y")
        else:
            print("N")
