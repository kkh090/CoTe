import sys

A, B, C = map(int, sys.stdin.readline().split())

result = 1

while B:
    if B & 1:
        result *= A
    A *= A
    A = A%C
    B = B >> 1

print(result%C)