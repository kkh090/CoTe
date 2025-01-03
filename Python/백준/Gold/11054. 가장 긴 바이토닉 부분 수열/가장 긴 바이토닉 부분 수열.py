import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

A_rev = A[::-1]

up = [1 for i in range(N)]
down = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            up[i] = max(up[i], up[j]+1)
        if A_rev[i] > A_rev[j]:
            down[i] = max(down[i], down[j]+1)
            
print(max(up[i] + down[N-i-1] - 1 for i in range(N)))
