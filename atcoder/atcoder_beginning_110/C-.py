n = int(input())
l = list(map(int, input().split()))
a_l = [i for i in range(0,len(l),2)]
b_l = [i for i in range(1, len(l),2)]
set_a = [0 for i in range(max(a_l)+1)]
set_b = [0 for i in range(max(b_l)+1)]
for i in a_l:
    set_a[i] += 1
for i in b_l:
    set_b[i] += 1
k_a = max(set_a)
k_b = max(set_b)
index_a = set_a.index(k_a)
index_b = set_b.index(k_b)
if index_a!=index_b:
    print(len(a_l)-k_a+len(b_l)-k_b)
else:
    if index_a > index_b:
        print(len(a_l))