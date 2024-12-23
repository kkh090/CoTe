import sys
input = sys.stdin.readline

N = input().rstrip()

n = [0 for i in range(9)]

for nn in N:
    if nn in {"6", "9"}:
        nn = "6"
        n[6] += 0.5
    else:
        n[int(nn)] += 1

n[6] = int(n[6]+0.5)

print(max(n))
