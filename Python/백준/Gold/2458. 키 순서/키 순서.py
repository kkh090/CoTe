import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = {i:[] for i in range(1, N+1)}
known = [0 for i in range(0, N+1)]
res = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(start):
    dq, visited = deque([start]), set()
    
    while dq:
        n = dq.pop()
        
        if n not in visited:
            visited.add(n)
            known[n] += 1
            dq.extend(graph[n])

    return visited

for i in range(1, N+1):
    known[i] += len(dfs(i))

for i in range(1, N+1):
    if known[i] == N:
        res += 1
print(res)