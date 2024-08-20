import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

nn = sorted(list(map(int, input().split())))

visited = [False] * N

temp = []

def dfs():
    if len(temp) == M:
        print(*temp)
        return
    rm = 0
    for i in range(N):
        if not visited[i] and rm != nn[i]:
            visited[i] = True
            temp.append(nn[i])
            rm = nn[i]
            dfs()
            visited[i] = False
            temp.pop()

dfs()