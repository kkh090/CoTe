import sys
input = sys.stdin.readline


A, B, C = map(int, input().split())
D = int(input())

temp = C + D
C = temp % 60
D = temp // 60

temp = B + D

B = temp % 60
D = temp // 60

A = (A+D) % 24

print(A, B, C)