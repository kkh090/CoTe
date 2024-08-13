import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
n = sorted(list(map(int, input().split())))

for i in permutations(n, M):
    print(*i)