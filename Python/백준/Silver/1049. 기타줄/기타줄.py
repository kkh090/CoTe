import sys
input = sys.stdin.readline
N, M = map(int, input().split())

p = 1001
e = 1001
for _ in range(M):
    pp, ee = map(int, input().split())
    
    if pp < p:
        p = pp
    if ee < e:
        e = ee

cost = 0

i = 6

while N > 0:
    i = min(N, i)
    if p < e*i:
        N -= 6
        cost += p
    else:
        N -= i
        cost += e*i

print(cost)
