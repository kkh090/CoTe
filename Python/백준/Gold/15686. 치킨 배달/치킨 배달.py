import sys
from itertools import combinations
input = sys.stdin.readline

def get_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def min_dis(dis_h2c, chosen):
    temp = [[i for idx, i in enumerate(h_d) if idx in chosen] for h_d in dis_h2c]

    dist = 0
    
    for h_d in temp:
        dist += min(h_d)
    
    return dist

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

houses = []
chicken = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

dis_h2c = []
answer = 1e9

for hx, hy in houses:
    temp = []    
    for cx, cy in chicken:
        
        temp.append(get_distance(cx, cy, hx, hy))

    dis_h2c.append(temp)

for chosen in combinations(range(len(chicken)), M):
    dis = min_dis(dis_h2c, chosen)
    if answer > dis:
        answer = dis

print(answer)
    
