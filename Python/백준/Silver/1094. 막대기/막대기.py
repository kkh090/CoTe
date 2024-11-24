from collections import deque
X = int(input())

dq = deque([64])

while sum(dq) != X:
    v = dq.popleft()
    
    v = v // 2
    
    dq.appendleft(v)
    
    if sum(dq) < X:
        dq.appendleft(v)
            
print(len(dq))