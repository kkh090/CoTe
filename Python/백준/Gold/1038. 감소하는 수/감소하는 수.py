import sys

N = int(sys.stdin.readline())

prev = {i:[i] for i in range(10)}
ans = [i for i in range(10)]

# 9876543210 => 1e10

for i in range(1, 10):
    temp = {k:[] for k in range(10)}
    
    for num_list in prev.values():
        for n in num_list:
            t = (n//(10**(i-1)))
            for j in range(t+1, 10):
                temp[j].append((j * 10**i) + n)
    
    prev = temp
    for nums in prev.values():
        ans.extend(nums)
    
    
if N < len(ans):
    print(ans[N])
else:
    print(-1)