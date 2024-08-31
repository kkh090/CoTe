import sys
import heapq

input = sys.stdin.readline
output = sys.stdout.write

V, E = map(int, input().split())
K = int(input())

graph = {i:{} for i in range(1, V+1)}

for _ in range(E):
    u, v, w = map(int, input().split())
    if v in graph[u].keys():
        if w < graph[u][v]:
            graph[u][v] = w
    else:
        graph[u][v] = w
        
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        current_dist, current_dest = heapq.heappop(queue)

        if distances[current_dest] < current_dist:
            continue
            
        for new_dest, new_dist in graph[current_dest].items():
            dist = current_dist + new_dist
            if dist < distances[new_dest]:
                distances[new_dest] = dist
                heapq.heappush(queue, [dist, new_dest])

    return distances

output("\n".join(map(str, dijkstra(graph, K).values())).upper())

