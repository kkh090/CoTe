import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

if N > M:
    A, B = B, A
    N, M = M, N

def sol(a, b, res=[]):
    if(not a) or (not b):
        return res
    
    t1, t2 = max(a), max(b)
    
    idx1, idx2 = a.index(t1), b.index(t2)
    
    if t1 == t2:
        res.append(t1)
        return sol(a[idx1 + 1:], b[idx2 + 1:], res)
    elif t1 > t2:
        a.pop(idx1)
        return sol(a, b, res)
    else:
        b.pop(idx2)
        return sol(a, b, res)
    
answer = sol(A, B)

print(len(answer))
if answer:
    print(*answer)