import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    
    r = [[0] * n for i in range(2)] 

    r[0][0], r[1][0] = sticker[0][0], sticker[1][0]
    
    for j in range(1, n):
        for i in range(2):
            pos = [(i, j-2), (not(i), j-1), (not(i), j-2)]
            if j == 1:
                max_score = r[not(i)][j-1]
            else:
                max_score = max(r[i][j-2], r[not(i)][j-1], r[not(i)][j-2])
            
            r[i][j] = max_score + sticker[i][j]

    print(max(r[0][-1], r[1][-1]))