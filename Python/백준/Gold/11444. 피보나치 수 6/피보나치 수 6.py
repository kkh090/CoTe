import sys

input = sys.stdin.readline

n = int(input())
p = 1000000007

fibo_matrix = [[1, 1], [1, 0]]


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

print(square(fibo_matrix, n)[0][1])