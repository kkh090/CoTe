import sys
input = sys.stdin.readline

K = int(input())

lengths = []
include = set()
x, y = 0, 0

for _ in range(6):
    s, l = map(int, input().split())
    
    lengths.append([s, l])
    
    if s in (3, 4):
        x = max(x, l)   
    else:
        y = max(y, l)

lengths += lengths[:3]
for i in range(3, len(lengths)):
    if lengths [i][0] == lengths[i-2][0] and lengths[i-1][0] == lengths[i-3][0]:
        a = lengths[i-2][1]
        b = lengths[i-1][1]
        break

print(((x*y) - (a*b))*K)