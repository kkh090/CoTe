import sys 
input = sys.stdin.readline

N = input().rstrip()
F = int(input())

N_ = N[:-2]


for i in range(100):
    if i < 10:
        n = "0" + str(i)
    else:
        n = str(i)
        
    if not(int(N_ + n) % F):
        break

print(n)