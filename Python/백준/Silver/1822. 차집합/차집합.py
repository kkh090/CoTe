import sys

A, B = map(int, sys.stdin.readline().split())

A_set = set(map(int, sys.stdin.readline().split()))

B_set = set(map(int, sys.stdin.readline().split()))

diff_set = A_set - B_set

if diff_set:
    print(len(diff_set))
    print(*sorted(diff_set))
else:
    print("0")