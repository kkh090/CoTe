import sys
from collections import deque

N, K, M = map(int, sys.stdin.readline().split())

dq = deque(range(1, N+1))
res = []
removed = 0
rot = -(K - 1)

while dq:
    if removed == M:
        if rot == K:
            rot = -(K - 1)
        else: rot = K
        removed = 0
    dq.rotate(rot)
    res.append(dq.popleft())
    removed += 1

print(*res, sep='\n', end='')