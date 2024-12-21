import sys
input = sys.stdin.readline

N = int(input())

floor = []

for i in range(N):
    floor.append(list(map(int, input().split())))

dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

def solution_dp():
    dp[0][0][1] = 1
    
    for i in range(2, N):
        if floor[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]
    
    for r in range(1, N):
        for c in range(1, N):
            if floor[r][c] == 0 and floor[r][c - 1] == 0 and floor[r - 1][c] == 0:
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
            
            if floor[r][c] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

    print(sum(dp[i][N - 1][N - 1] for i in range(3)))
        
solution_dp()