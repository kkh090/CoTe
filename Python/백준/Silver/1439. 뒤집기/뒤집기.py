import sys

input = sys.stdin.readline

S = input()
ans = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        ans += 1

print(ans//2)