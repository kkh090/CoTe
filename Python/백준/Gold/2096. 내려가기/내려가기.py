import sys
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
steps = [[0, 0, 0], [0, 0, 0]]
minmax = [min, max]

for i in range(N):
    n1, n2, n3 = map(int, input().split())

    for i, f in enumerate(minmax):
        p1 = f(steps[i][0], steps[i][1])
        p2 = f(steps[i][0], steps[i][1], steps[i][2])
        p3 = f(steps[i][1], steps[i][2])
        steps[i] = [p1+n1, p2+n2, p3+n3]

output(str(max(steps[1])) + " " + str(min(steps[0])))