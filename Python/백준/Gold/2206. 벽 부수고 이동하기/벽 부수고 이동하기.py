import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

move = [[[0, 0] for _ in range(M)] for _ in range(N)]
m = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(N):
    m.append(list(map(int, input().rstrip())))

def bfs(x, y):
    dq = deque([(x, y, 0)])
    move[y][x][0] = 1
    while dq:
        x, y, b = dq.popleft()
        
        if (x, y) == (M-1, N-1):
            return move[y][x][b] 
        
        for i in range(4):
            n_x, n_y = x + dx[i], y + dy[i]
            
            if 0 <= n_x < M and 0 <= n_y < N:
                if m[n_y][n_x] == 1 and b==0:
                    move[n_y][n_x][1] = move[y][x][0] + 1
                    dq.append((n_x, n_y, 1))
                if m[n_y][n_x] == 0 and move[n_y][n_x][b] == 0:
                    move[n_y][n_x][b] = move[y][x][b] + 1
                    dq.append((n_x, n_y, b))
    return -1
        
print(bfs(0, 0))