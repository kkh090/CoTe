import sys
input = sys.stdin.readline

N = int(input())

trees = list(map(int, input().split()))

answer = []

for i, n in enumerate(trees):
    answer.append(n - (N-i))

print(max(answer))