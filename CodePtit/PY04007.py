## LỚP MATRIX - 1

class Matrix:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a

    def transpose(self):
        transpose = []
        for i in range(self.m):
            row = []
            for j in range(self. n):
                row.append(self.a[j][i])
            transpose.append(row)
        return Matrix(self.m , self.n , transpose)

    def mul(self):
        transposed_matrix = self.transpose()
        res = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                value = 0
                for k in range(self.m):
                    value += self.a[i][k] * transposed_matrix.a[k][j]
                row.append(value)
            res.append(row)
        return Matrix(self.n , self.m , res)

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.a)


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    M = []
    for _ in range(n):
        row = list(map(int, input().split()))
        M.append(row)
    matrix = Matrix(n, m, M)
    ans = matrix.mul()
    print(ans)

