import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())

line = []
line_add = []
check = [0 for _ in range(d+1)]
count = 1

check[c] += 1

for i in range(N):
    f = int(input())

    if i < k:
        line_add.append(f)
        if check[f] == 0:
            count += 1
        check[f] += 1
        
    line.append(f)

line += line_add

max_count = count

r = 0
for s in range(k, len(line)):
    if check[line[s]] == 0:
        count += 1
    check[line[s]] += 1
    
    check[line[r]] -= 1
    if check[line[r]] == 0:
        count -= 1
    r += 1
    
    if count >= max_count:
        max_count = count
print(max_count)