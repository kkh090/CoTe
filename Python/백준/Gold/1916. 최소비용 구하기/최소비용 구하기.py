import sys
input = sys.stdin.readline
output = sys.stdout.write

INF = 1e8

N = int(input())
M = int(input())

nn = [[] for _ in range(N+1)]

for i in range(M):
    s, e, w = map(int, input().split())
    nn[s].append((e, w))

v = [False] * (N+1)
dist = [INF] * (N+1)

s, e = map(int, input().split())

def get_smallest_node():
    min_val = INF
    idx = 0
    for i in range(1, N+1):
        if dist[i] < min_val and not v[i]:
            min_val = dist[i]
            idx = i
    return idx

def dijkstra(start):
    dist[start] = 0
    v[start] = True
    
    for i in nn[start]:
        if dist[i[0]] > i[1]:
            dist[i[0]] = i[1]           
    
    for _ in range(N-1):
        now = get_smallest_node()
        v[now] = True
        
        for j in nn[now]:
            if dist[now] + j[1] < dist[j[0]]:
                dist[j[0]] = dist[now] + j[1]

dijkstra(s)
output(str(dist[e]))                
            