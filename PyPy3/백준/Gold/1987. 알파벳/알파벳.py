import sys
input = sys.stdin.readline

R, C = map(int, input().split())

maps = []

for _ in range(R):
    temp = list(input().rstrip())
    maps.append(temp)

visited = [0] * 26
visited[ord(maps[0][0])-65] = 1
m = 1
d = ((1, 0), (-1, 0), (0, 1), (0, -1))

def dfs(x, y, cnt):
    global m
    m = max(m, cnt)
    
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        
        if 0 <= nx < R and 0 <= ny < C and visited[ord(maps[nx][ny]) - 65] == 0:
            visited[ord(maps[nx][ny]) - 65] = 1
            dfs(nx, ny, cnt+1)
            visited[ord(maps[nx][ny]) - 65] = 0

dfs(0, 0, m)

print(m)