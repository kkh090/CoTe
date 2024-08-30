import sys
from collections import deque
input = sys.stdin.readline
output = sys.stdout.write

N, K = map(int, input().split())



def bfs(N, K):
    dq = deque([(N,0)])
    visited = [100001 for _ in range(100000 * 2 + 1)]
    min_t = 100001

    while dq:
        v, t = dq.popleft()
        
        if v < K:
            for vt in [(v+1, t+1), (v-1, t+1), (v*2, t)]:
                if vt[0] > 0:
                    if vt[1] < visited[vt[0]]:
                        visited[vt[0]] = vt[1]
                        dq.append(vt)
        elif v == K:
            if t < min_t:
                min_t = t
        else:
            if t + (v - K) < min_t:
                min_t = t + (v-K)

    return min_t

print(bfs(N, K))
        
