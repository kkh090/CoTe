import sys
input = sys.stdin.readline
output = sys.stdout.write

S1 = list(input().rstrip())
S2 = list(input().rstrip())

ss = [[0 for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]

for i in range(1, len(S1)+1):
    for j in range(1, len(S2)+1):
        eq = 0
        if S1[i-1] == S2[j-1]:
            eq = ss[i-1][j-1] + 1
        ss[i][j] = max(ss[i-1][j], ss[i][j-1], eq)
        
output(str(ss[i][j]))
