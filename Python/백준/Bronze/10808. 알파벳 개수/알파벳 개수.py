
s = input()

l = {i:0 for i in "abcdefghijklmnopqrstuvwxyz"}

for ss in s:
    l[ss] += 1
    
print(*l.values(), sep=" ")