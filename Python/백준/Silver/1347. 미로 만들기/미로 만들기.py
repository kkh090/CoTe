import sys
input = sys.stdin.readline

N = int(input())
move = input().rstrip()

path = [(0, 0)]

next = ((1, 0), (0, -1), (-1, 0), (0, 1))

dir = 0

min_x, min_y = 0, 0
max_x, max_y = 0, 0

for m in move:
    if m == "R":
        dir = (dir + 1) % 4
    elif m == "L":
        dir = (dir + 3) % 4
    elif m =="F":
        next_x, next_y = path[-1][0]+next[dir][0], path[-1][1]+next[dir][1]
        path.append((next_x, next_y))
        
        if next_x > max_x:
            max_x = next_x
        if next_x < min_x:
            min_x = next_x
            
        if next_y > max_y:
            max_y = next_y
        if next_y < min_y:
            min_y = next_y

maze = [["#" for _ in range((max_y - min_y + 1))] for _ in range((max_x - min_x + 1))]

for px, py in path:
    maze[px - min_x][py - min_y] = "."
    
for m in maze:
    print(*m, sep="")

