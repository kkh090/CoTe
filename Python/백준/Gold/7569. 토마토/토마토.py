import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
box = []
tomato = []
for i in range(H):
    box.append([])
    for j in range(N):
        g = list(map(int, input().split()))
        
        for k, v in enumerate(g):
            if v == 1:
                tomato.append((i, j, k))
        
        box[i].append(g)
        

def bfs(box, tomato, M, N, H):
    pos = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    dq = deque(tomato)
    visitied = set(tomato)
    count = [len(tomato), 0]
    c = 0
    
    while dq:
        v = dq.popleft()
        
        count[c] -= 1
        
        pp = [(v[0] + i, v[1] + j, v[2] + k) for i, j, k in pos if 0 <= v[0] + i < H and 0 <= v[1] + j < N and 0 <= v[2] + k < M
              and box[v[0] + i][v[1] + j][v[2] + k] == 0]
    
        for p in pp:
            if p not in visitied and box[p[0]][p[1]][p[2]] == 0:
                visitied.add(p)
                dq.append(p)
                box[p[0]][p[1]][p[2]] = 1
                count[c+1] += 1
        
        if count[c] == 0:
            c += 1
            count.append(0)
        
    return c-1

c = bfs(box, tomato, M, N, H)
for i in box:
    for j in i:
        if 0 in j:
            c = -1
            break
    if c == -1:
        break

print(c)
