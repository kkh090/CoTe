word = input().rstrip()
m = set(('a', 'e', 'i', 'o', 'u'))
count = 0
for i in word:
    if i in m:
        count += 1
print(count)