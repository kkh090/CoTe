import sys
input = sys.stdin.readline

N, K = map(int, input().split())

if N > K:
    if N % 2 == 0:
        print(N)
    else:
        if K % 2 == 0:
            print(N)
        else:
            print(N-1)
else:
    print(0)
    