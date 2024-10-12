import sys

input = sys.stdin.readline

s = input().rstrip()

b = input().rstrip()

stack = []
b_len = len(b)

for i in s:
    stack.append(i)
    if "".join(stack[-b_len:]) == b:
        for _ in range(b_len):
            stack.pop()
            
if stack:
    print(''.join(stack))
else:
    print("FRULA")
    
