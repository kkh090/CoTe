import sys
input = sys.stdin.readline 

h_n = int(input())

h = []
for i in range(h_n):
    h.append(list(map(int, input().split())))

n = [[0] * 3 for _ in range(h_n+1)]

for i in range(1, h_n+1):
    for j in range(3):
        temp = []
        if j != 0:
            temp.append(n[i-1][0])
        if j != 1:
            temp.append(n[i-1][1])
        if j != 2:
            temp.append(n[i-1][2])
            
        n[i][j] = min(temp) + h[i-1][j]
        
print(min(n[-1]))
