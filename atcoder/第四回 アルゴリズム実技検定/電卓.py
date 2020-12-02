x, y = map(int, input().split())
if y == 0 :
    print("ERROR")
else:
    k = x/y
    print(int(k*100)/100)