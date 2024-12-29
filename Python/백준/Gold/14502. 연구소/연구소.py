import sys
from collections import deque
input = sys.stdin.readline
DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())

graph = []

virus = set()

walls = []

def bfs(graph: list, node: set, w1: int, w2: int, w3: int):
    graph = [[i for i in g] for g in graph]
    graph[walls[w1][0]][walls[w1][1]], graph[walls[w2][0]][walls[w2][1]], graph[walls[w3][0]][walls[w3][1]] = 1, 1, 1
    queue = deque(node)
    visited = set()
    visited.update(node)
    
    while queue:
        cx, cy = queue.popleft()
        
        dir = [(cx + x, cy + y) for x, y in DIR if 0 <= cx + x < N and 0 <= cy + y < M]
        
        for d in dir:
            if d not in visited and graph[d[0]][d[1]] == 0:
                queue.append(d)
                visited.add(d)
                graph[d[0]][d[1]] = 2           
    
    graph = [[not(i) for i in g] for g in graph]
    return graph

for i in range(N):
    temp = list(map(int, input().split()))
    
    for j, t in enumerate(temp):
        if t == 2:
            virus.add((i, j))
        elif t == 0:
            walls.append((i, j))
    
    graph.append(temp)

max_safe_area = 0

for w1 in range(len(walls) - 2):
    for w2 in range(w1+1, len(walls)-1):
        for w3 in range(w2+1, len(walls)):
            safe_area = sum(sum(g) for g in bfs(graph, virus, w1, w2, w3))
            if safe_area > max_safe_area:
                max_safe_area = safe_area

print(max_safe_area)
