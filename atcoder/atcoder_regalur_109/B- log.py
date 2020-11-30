n = int(input())
l = 0
r = 2e9
while r - l > 1:
    mid = int((l+r)/2)
    if mid*(mid+1)/2 <= n+1:
        l = mid
    else:
        r = mid
print(n - l + 1)
