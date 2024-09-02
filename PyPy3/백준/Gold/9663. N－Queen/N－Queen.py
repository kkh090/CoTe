import sys
from collections import deque

input = sys.stdin.readline
output = sys.stdout.write

N = int(input())

row = [0] * N
cnt = 0

def promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return True
    return False

def dfs(start):
    global cnt
    
    if start == N:
        cnt += 1
    else:
        for i in range(N):
            row[start] = i
            if not promising(start):
                dfs(start + 1)
                
dfs(0)

print(cnt)