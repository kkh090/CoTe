import sys

input = sys.stdin.readline

n, k = map(int, input().split())
p = 1000

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))


def matmul(A, B):
    n = len(A)
    result = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            r = 0
            for i in range(n):
                r += A[row][i] * B[i][col]
            result[row][col] = r % p
    
    return result

def square(fm, k):
    if k == 1:
        for x in range(len(fm)):
            for y in range(len(fm)):
                fm[x][y] %= p
        return fm
    
    tmp = square(fm, k//2)
    if k % 2:
        return matmul(matmul(tmp, tmp), fm)
    else:
        return matmul(tmp, tmp)

for rr in square(a, k):
    print(*rr)