import sys
input = sys.stdin.readline

N = int(input())

people = list(map(int, input().split()))

answer = [0] * N

for i in range(N):
    c = 0
    for j in range(N):
        if answer[j] == 0 and people[i] == c:
            answer[j] = i + 1
            break
        elif answer[j] == 0:
            c += 1

print(' '.join(map(str, answer)))
