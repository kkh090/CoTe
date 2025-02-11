import sys

N, K = map(int, sys.stdin.readline().split())

pie = list(map(int, sys.stdin.readline().split()))

pie = pie + pie[:K]

answer = sum(pie[:K])
max_ans = answer

for i in range(K, len(pie)):
    
    answer += pie[i]
    answer -= pie[i-K]

    if max_ans < answer:
        max_ans = answer

print(max_ans)