import sys
input = sys.stdin.readline

N = int(input())

def check_shom(A, B):
    mapping = dict()
    used = set()
    
    for k in range(len(A)):
        if A[k] not in mapping.keys():
            if B[k] not in used:
                mapping[A[k]] = B[k]
                used.add(B[k])
            else:
                return False
        elif mapping[A[k]] != B[k]:
            return False
        
    return True
        
words = []
count = 0
for _ in range(N):
    words.append(input().rstrip())
    
for i in range(len(words)-1):
    for j in range(i+1, len(words)):
        if check_shom(words[i], words[j]):
            count += 1
            
print(count)