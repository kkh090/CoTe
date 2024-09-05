import sys
import heapq

input = sys.stdin.readline
INF = 1e9

N, M, X = map(int, input().split()) 

graph = {}

for _ in range(M):
    a, b, w = map(int, input().split())
    
    if a not in graph.keys():
        graph[a] = [(b, w)]
    else:
        graph[a].append((b, w))
        
def dijkstra(start):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
                
    return distance

distance = dijkstra(X)
distance[0] = 0

for i in range(1, N+1):
    if i != X:
        res = dijkstra(i)
        distance[i] += res[X]

print(max(distance))