import sys
input = sys.stdin.readline

S, K = map(int, input().split())
n = [S//K] * K

for i in range(S%K):
    n[i] += 1

answer = 1
for i in n:
    answer *= i 

print(answer)