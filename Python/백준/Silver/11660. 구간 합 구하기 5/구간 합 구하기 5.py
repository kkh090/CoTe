import sys
input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int, input().split())

nn = []
for _ in range(N):
    nn.append(list(map(int, input().split())))
    
dp = [[0 for i in range(N+1)] for j in range(N+1)]

dp[1][1] = nn[0][0]
for i in range(2, N+1):
    dp[i][1] = dp[i-1][1] + nn[i-1][0]
    dp[1][i] = dp[1][i-1] + nn[0][i-1]


for i in range(2, N+1):
    for j in range(2, N+1):
        dp[i][j] = nn[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
            

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    result = dp[x2][y2]  + dp[x1-1][y1-1] - dp[x1-1][y2] - dp[x2][y1-1]
    
    output(str(result) + '\n')