import sys
input = sys.stdin.readline
T = int(input())

N = []
M = []
for _ in range(T):
    n, m = map(int, input().split())
    N.append(n)
    M.append(m)

max_m = max(M)
max_n = max(N)
    
v = [[0 for _ in range(max_m)] for _ in range(max_n)]

for i in range(min(max_m, max_n)):
    v[i][i] = 1

for i in range(1, max_m+1):
    v[0][i-1] = i
    
for i in range(1, max_n):
    for j in range(i+1, max_m):
        v[i][j] = v[i][j-1] + v[i-1][j-1]
        
for i in range(T):
    print(v[N[i]-1][M[i]-1])