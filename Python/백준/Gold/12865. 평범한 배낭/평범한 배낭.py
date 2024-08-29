import sys
input = sys.stdin.readline
output = sys.stdout.write

N, K = map(int, input().split())

wv = []

dp = [[0] *(K+1) for _ in range(N+1)]

for _ in range(N):
    wv.append(list(map(int, input().split())))
    
for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= wv[i-1][0]:
            dp[i][j] = max(wv[i-1][1] + dp[i-1][j-wv[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])