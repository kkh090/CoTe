import sys

input = sys.stdin.readline 

N = int(input())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

result = 0
for i in range(len(A)):
    result += (A[i] * B[i])

print(result)