import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())

graph = {i:[] for i in range(1, V+1)}

for _ in range(V):
    v = list(map(int, input().split()))
    idx = v[0]
    
    i = 1
    while v[i] != -1:
        graph[idx].append((v[i], v[i+1]))
        i += 2

visited = [-1] * (V+1)
visited[1] = 0

def dfs(start, dist):
    for i, w in graph[start]:
        if visited[i] == -1:
            visited[i] = dist + w
            dfs(i, dist + w)

dfs(1, 0)

m_idx = -1
m_val = -1
for i in range(V+1):    
    if m_val < visited[i]:
        m_val = visited[i]
        m_idx = i
        
visited = [-1] * (V+1)
visited[m_idx] = 0
dfs(m_idx, 0)

print(max(visited))

    