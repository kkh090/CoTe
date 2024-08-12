import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

for answer in combinations(range(1, N+1), M):
    print(*answer)