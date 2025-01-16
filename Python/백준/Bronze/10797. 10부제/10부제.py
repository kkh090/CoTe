n = input()

count = 0
for i in list(input().split()):
    if i[-1] == n:
        count += 1

print(count)