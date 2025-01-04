import sys
import math
input = sys.stdin.readline

mod = 10**9 + 7

def divide_and_conquer(num, exp):
    if exp == 1:
        return num
    
    if exp % 2 == 0:
        half = divide_and_conquer(num, exp//2)
        return half * half % mod
    else:
        return num * divide_and_conquer(num, exp-1) % mod 


M = int(input())

ans = 0

for _ in range(M):
    n, s = map(int, input().split())
    
    gcd = math.gcd(n, s)
    
    n, s = n//gcd, s//gcd
    
    ans = (ans + (s * divide_and_conquer(n, mod-2))) % mod
    
print(ans)