import sys
input = sys.stdin.readline

N = int(input())

sizes = list(map(int, input().split()))

T, P = map(int, input().split())

count = 0

for s in sizes:
    count += s // T
    count += 1 if s % T else 0

print(count)

print(N // P, N % P)