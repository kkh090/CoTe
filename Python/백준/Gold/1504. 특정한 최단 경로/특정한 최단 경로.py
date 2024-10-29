import sys
import heapq
INF = int(1e10)
input = sys.stdin.readline

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
    
v1, v2 = map(int, input().split())

def dijkstra(start): 
    distance = [INF] * (V+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                    
    return distance

dist_1 = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

v1_path = dist_1[v1] + v1_dist[v2] + v2_dist[V]
v2_path = dist_1[v2] + v2_dist[v1] + v1_dist[V]

result = min(v1_path, v2_path)
print(result if result < INF else -1)

    