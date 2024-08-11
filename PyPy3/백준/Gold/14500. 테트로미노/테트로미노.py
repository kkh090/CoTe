import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pol = []
for _ in range(N):
    pol.append(list(map(int, input().split())))
    
pos = [[1, 0], [-1, 0], [0, 1], [0, -1]]

extra = [[[1, 0], [-1, 0]], [[0, 1], [0, -1]]]

visited = {i:[] for i in range(3)}
values = {i:[] for i in range(4)}

max_val = 0

def check(i, j):
    return True if i >= 0 and j >= 0 and i < N and j < M else False

for i in range(N):
    for j in range(M):
        visited[0] = [i, j]
        values[0] = pol[i][j]
        for b1_i, b1_j in pos:
            if check(i+b1_i, j+b1_j):
                visited[1] = [i+b1_i, j+b1_j]
                values[1] = pol[visited[1][0]][visited[1][1]]
                for b2_i, b2_j in pos:
                    if check(visited[1][0]+b2_i, visited[1][1]+b2_j):
                        next_pos = [visited[1][0]+b2_i, visited[1][1]+b2_j]
                        if visited[0] != next_pos:
                            visited[2] = next_pos
                            values[2] = pol[visited[2][0]][visited[2][1]]
                            for b3_i, b3_j in pos:
                                if check(visited[2][0]+b3_i, visited[2][1]+b3_j):
                                    next_pos = [visited[2][0]+b3_i, visited[2][1]+b3_j]
                                    if visited[1] != next_pos:
                                        values[3] = pol[next_pos[0]][next_pos[1]]
                                        max_val = max(max_val, sum(values.values()))
                                                                                          
                            if b1_i == b2_i and b1_j == b2_j:
                                if b1_i == 1 or b1_i == -1:
                                    idx = 1
                                else:
                                    idx = 0
                                for b3_i, b3_j in extra[idx]:
                                    if check(visited[1][0]+b3_i, visited[1][1]+b3_j):
                                        values[3] = pol[visited[1][0]+b3_i][visited[1][1]+b3_j]
                                        max_val = max(max_val, sum(values.values()))

print(max_val)
