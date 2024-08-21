import sys
input = sys.stdin.readline

N, M = map(int, input().split())

n = sorted(set(map(int, input().split())))

N = len(n)
temp = []

def dfs(visited):
    if len(temp) == M:
        print(*temp)
        return
    
    v = visited.copy()
    
    for i in range(N):
        if i not in visited:
            temp.append(n[i])
            dfs(v)
            temp.pop()
            v.add(i)
        
dfs(set())
    