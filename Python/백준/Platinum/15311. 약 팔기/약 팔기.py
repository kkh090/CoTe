import sys
input = sys.stdin.readline

N = int(input())
print(2000)
print(*([1 for _ in range(1000)] + [1000 for _ in range(1000)]))