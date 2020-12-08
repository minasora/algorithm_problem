def insert_sort(A, n, g):
    for i in range(g,n-1):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
        A[j+g] = v
def shell_sort(A, n):
    cnt = 0
    G = []
    s_n = n
    while True:
        s_n = s_n//2
        print(s_n)
        G.append(s_n)
        if s_n//2 <= 1:
            break
            print(G)
    for i in G:
        insert_sort(A,n,i)
n = int(input())
A = []
for i in range(n):
    A.append(int(input()))
shell_sort(A, n)
print(A)