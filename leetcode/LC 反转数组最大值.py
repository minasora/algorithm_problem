class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        n = len(A)
        m = len(A[0])
        for i in range(m):
            if i == 0:
                for j in range(n):
                    if A[j][i] == 0:
                        for k in range(m):
                            A[j][k] = 1 if A[j][k]==0 else 0
            else:
                sum_l = 0
                for j in range(n):
                    sum_l += A[j][i]
                if sum_l <= n//2:
                    for j in range(n):
                            A[j][i] = 1 if A[j][i]==0 else 0
        ans = 0
        for i in range(n):
            s = 0
            for j in range(m):
                s += A[i][j] * (2**(m-j-1))
            ans += s
        return ans