import sys
from collections import deque

def bfs(graph, start, N): # returns the parents of each node
    info = {i:-1 for i in range(2, N+1)}
    visitied = set([start])
    dq = deque([start])
    
    while dq:
        v = dq.popleft()
        
        for vv in graph[v]:
            if vv not in visitied:
                info[vv] = v
                dq.append(vv)
                visitied.add(vv)
    
    return info

input = sys.stdin.readline

N = int(input())

graph = dict()

for i in range(N-1):
    A, B = map(int, input().split())
    
    if A not in graph.keys():
        graph[A] = [B]
    else:
        graph[A].append(B)
    if B not in graph.keys():
        graph[B] = [A]
    else:
        graph[B].append(A)

print(*bfs(graph, 1, N).values(), sep="\n")