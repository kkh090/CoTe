import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    visited = [100001 for _ in range(100001)]
    q = deque([(start, 0)])
    
    s = 1e9
    p = 0
    flag = 1
    
    if start == end:
        return 0, 1

    while q:
        pos, value = q.popleft()
        
        if pos > end:
            f_value = pos - end
            if s > f_value:
                s = pos-end
                p = 1
            elif s == f_value:
                p += 1

        else:
            next = [pos+1, pos-1, pos*2]
            next_val = value+1
            for n in next:
                if n == end:
                    if s > next_val:
                        s = next_val
                        p = 1
                    elif s == next_val:
                        p += 1
                    flag = 0

                elif flag and n >= 0:
                    if n < end:
                        if next_val <= visited[n]: 
                            visited[n] = next_val
                            q.append((n, next_val))
                        
                    else:
                        f_value = next_val + (n - end)
                        if s > f_value:
                            s = f_value
                            p = 1
                        elif s == f_value:
                            p += 1
                
    return s, p
        
N, K = map(int, input().split())

print(*bfs(N, K), sep="\n")
