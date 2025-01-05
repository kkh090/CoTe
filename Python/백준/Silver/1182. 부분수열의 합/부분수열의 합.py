# import sys
# from itertools import combinations
# input = sys.stdin.readline

# N, S = map(int, input().split())

# seq = list(map(int, input().split()))

# answer = 0

# for i in range(1, N+1):
#     for x in combinations(seq, i):
#         if sum(x) == S:
#             answer += 1

# print(answer)

import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())

seq = list(map(int, input().split()))

answer = 0

def subset_sum(idx, sub_sum):
    global answer
    
    if idx >= N:
        return

    sub_sum += seq[idx]
    
    if sub_sum == S:
        answer += 1
    
    subset_sum(idx+1, sub_sum)
    subset_sum(idx+1, sub_sum - seq[idx])
    
subset_sum(0, 0)
print(answer)
    