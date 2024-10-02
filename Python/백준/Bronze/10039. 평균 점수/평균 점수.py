sum = 0
for _ in range(5):
    n = int(input())
    n = 40 if n < 40 else n
    sum += n
print(sum//5)