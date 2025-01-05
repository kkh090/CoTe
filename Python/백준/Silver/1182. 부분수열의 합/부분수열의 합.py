import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())

seq = list(map(int, input().split()))

answer = 0

for i in range(1, N+1):
    for x in combinations(seq, i):
        if sum(x) == S:
            answer += 1

print(answer)