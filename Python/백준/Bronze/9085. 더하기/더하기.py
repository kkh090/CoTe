import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = input()
    n = list(map(int, input().split()))
    print(sum(n))
