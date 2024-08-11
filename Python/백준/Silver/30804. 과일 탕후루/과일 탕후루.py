import sys
input = sys.stdin.readline
N = int(input())
tanghuru = list(map(int, input().split()))
fruit_count = [0] * 10
l, r, kind = 0, 0, 0
answer = 0

while r < N:
    if fruit_count[tanghuru[r]] == 0:
        kind += 1
    fruit_count[tanghuru[r]] += 1
    
    while kind > 2:
        fruit_count[tanghuru[l]] -= 1
        if fruit_count[tanghuru[l]] == 0:
            kind -= 1
        l += 1
    
    answer = max(answer, r-l+1)
    r += 1

print(answer)
    

