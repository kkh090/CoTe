import sys

input = sys.stdin.readline

N, M = map(int, input().split())

t_p = list(map(int, input().split()))

party_idx_full = set((range(M)))

truth = set()
party_idx = set()

party = []

for i in range(1, len(t_p)):
    truth.add(t_p[i])

for i in range(M):
    party.append(set(list(map(int, input().split()))[1:]))


if truth:
    flag = 1
    while flag:
        flag = 0
        check = party_idx_full - party_idx
        for i in check:
            if truth & party[i]:
                truth.update(party[i])
                party_idx.add(i)
                flag = 1
    
    print(M-len(party_idx))
else:
    print(M)
