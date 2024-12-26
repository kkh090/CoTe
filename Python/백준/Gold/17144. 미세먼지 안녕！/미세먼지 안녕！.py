import sys
input = sys.stdin.readline

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def spread(graph, dust_pos, air_pur, R, C):
    temp = [[0 for j in range(C)] for i in range(R)]
    add_dust_pos = set()
    len_pos = 4

    for dpx, dpy in dust_pos:
        s_v = int(graph[dpx][dpy] / 5)
        
        if s_v != 0:
            no_pos = set()
            if dpx == 0:
                no_pos.add(2)
            elif dpx == R-1:
                no_pos.add(0)
                
            if dpy == 0:
                no_pos.add(3)
            elif dpy == C-1:
                no_pos.add(1)
            
            pos = [(dpx + p[0], dpy + p[1]) for idx, p in enumerate(dir) if idx not in no_pos]
                        
            len_pos = len(pos)
            for x, y in pos:
                if graph[x][y] != -1:
                    temp[x][y] += s_v
                    add_dust_pos.add((x, y))
                else:
                    len_pos -= 1
                    
            temp[dpx][dpy] += graph[dpx][dpy] - s_v * len_pos
        else:
            temp[dpx][dpy] += graph[dpx][dpy]
    
    dust_pos.update(add_dust_pos)
    
    for x in air_pur:
        temp[x][0] = -1
        
    return temp

def clean(graph, dust_pos, air_pur, R, C):
    temp = [[0 for j in range(C)] for i in range(R)]
    add_dust_pos = set()
    curr_pos = (air_pur[0], 1)
    next = (0, 1)
    for _ in range((air_pur[0]-1) * 2 + (C * 2) - 1):
        next_pos = (curr_pos[0] + next[0], curr_pos[1] + next[1])
        
        if curr_pos in dust_pos:
            dust_pos.remove(curr_pos)
            if graph[next_pos[0]][next_pos[1]] != -1:
                temp[next_pos[0]][next_pos[1]] = graph[curr_pos[0]][curr_pos[1]]
                add_dust_pos.add(next_pos)
        
        curr_pos = next_pos
        
        if next_pos == (air_pur[0], C-1):
            next = (-1, 0)
        elif next_pos == (0, C-1):
            next = (0, -1)
        elif next_pos == (0, 0):
            next = (1, 0)

    curr_pos = (air_pur[1], 1)
    next = (0, 1)
    for _ in range((R - air_pur[1]) * 2 + (C * 2) - 1):
        next_pos = (curr_pos[0] + next[0], curr_pos[1] + next[1])
        
        if curr_pos in dust_pos:
            dust_pos.remove(curr_pos)
            if graph[next_pos[0]][next_pos[1]] != -1:
                temp[next_pos[0]][next_pos[1]] = graph[curr_pos[0]][curr_pos[1]]
                add_dust_pos.add(next_pos)

        curr_pos = next_pos
        
        if next_pos == (air_pur[1], C-1):
            next = (1, 0)
        elif next_pos == (R-1, C-1):
            next = (0, -1)
        elif next_pos == (R-1, 0):
            next = (-1, 0)

    for x in air_pur:
        temp[x][0] = -1
        
    for x, y in dust_pos:
        temp[x][y] = graph[x][y]
        
    dust_pos.update(add_dust_pos)
    
    return temp

def simulate(graph, dust_pos, air_pur, R, C, T):
    dust_left = 2

    for _ in range(T):
        graph = spread(graph, dust_pos, air_pur, R, C)
        graph = clean(graph, dust_pos, air_pur, R, C)
        
    for r in graph:
        dust_left += sum(r)
        
    return dust_left

R, C, T = map(int, input().split())

graph = [] 
dust_pos = set()
air_pur = []

for i in range(R):
    
    temp = list(map(int, input().split()))
    
    for j, t in enumerate(temp):
        if t == -1:
            air_pur.append(i)
        elif t != 0:
            dust_pos.add((i, j))
            
    graph.append(temp)

print(simulate(graph, dust_pos, air_pur, R, C, T))