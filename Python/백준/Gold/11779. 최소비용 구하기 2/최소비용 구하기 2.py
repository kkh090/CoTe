import sys
import heapq
input = sys.stdin.readline

INF = 1e9

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

backtrack = [[] for i in range(n+1)]

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
def dijkstra(start):
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
                backtrack[i[0]] = backtrack[now] + [i[0]]
                heapq.heappush(q, (dist+i[1], i[0]))

A, B = map(int, input().split())

dijkstra(A)

print(distance[B])
print(len(backtrack[B])+1)
print(*([A] + backtrack[B]))