import sys
import heapq

input = sys.stdin.readline
INF = 1e9

T = int(input())

def dijkstra(start, N):
    dist = [INF] * (N+1)
    
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q:
        d, now = heapq.heappop(q)
        
        if dist[now] < d:
            continue
        
        for n, w in graph[now].items():
            if d+w < dist[n]:
                dist[n] = d+w
                heapq.heappush(q, (d+w, n))

    return dist

for _ in range(T):
    N, M = map(int, input().split())
    graph = {i:{} for i in range(1, N+1)}
    s = INF

    for _ in range(M):
        a, b, w = map(int, input().split())
        
        graph[a][b] = w
        graph[b][a] = w
    
    K = int(input())
    pos = list(map(int, input().split()))
    
    for p in range(1, N+1):
        dist = dijkstra(p, N)
        total_dist = sum(dist[i] for i in pos)
        if total_dist < s:
            s = total_dist
            res = p
    
    print(res)

