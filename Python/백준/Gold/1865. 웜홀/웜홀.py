import sys
input = sys.stdin.readline
INF = 1e9
TC = int(input())

def Bellman_Ford(start):
    dist[start] = 0
    for i in range(N):
        for j in range(2*M+W):
            curr_node, next_node, time_taken = road[j]

            if dist[next_node] > dist[curr_node] + time_taken:
                dist[next_node] = dist[curr_node] + time_taken

                if i == N-1:
                    return True
    return False

for _ in range(TC):
    N, M, W = map(int, input().split())
    
    road = []
    dist = [INF] * (N+1)
    
    for _ in range(M):
        S, E, T = map(int, input().split())
        road.append((S, E, T))
        road.append((E, S, T))
        
    for _ in range(W):
        S, E, T = map(int, input().split())
        road.append((S, E, -T))
    
    neg_cycle = Bellman_Ford(1)

    if neg_cycle:
        print("YES")
    else:
        print("NO")