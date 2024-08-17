import sys
from collections import deque

A, B = map(int, input().split())

visited = set([A])
dq = deque([A])
result = -1
count = [1, 0]
i = 0
while dq and result == -1:
    v = dq.popleft()
    
    if count[i]:
        count[i] -= 1
    else:
        i += 1
        count.append(0)
        count[i] -= 1
        
    if v < B:
        for vv in [v*2, v*10+1]:
            if vv not in visited and vv < B:
                dq.append(vv)
                count[i+1] += 1
            elif vv == B:
                result = i+2
        
print(result)