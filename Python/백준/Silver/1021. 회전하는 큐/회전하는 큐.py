import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

dq = deque(i for i in range(1, N+1))
elements = list(map(int, input().split()))

answer = 0
for e in elements:
    count = 0
    v = dq.popleft()
    while v != e:
        dq.append(v)
        v = dq.popleft()
        count += 1
    
    answer += count if count < len(dq) + 1 - count else len(dq) + 1 - count
    
print(answer)