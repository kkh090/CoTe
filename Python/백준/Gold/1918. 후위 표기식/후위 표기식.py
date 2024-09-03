import sys
from collections import deque
input = sys.stdin.readline

eq = input().rstrip()

op = set()
op.update(('+', '-', '*', '/', '(', ')'))

def to_postfix(eq):
    stack = deque()
    result = ''
    
    for i in eq:
        if i not in op:
            result += i
        else:
            if i == '(':
                stack.append(i)
            elif (i == '*' or i == '/'):
                while stack and (stack[-1]=='*' or stack[-1] == '/'):
                    result += stack.pop()
                stack.append(i)
            elif (i == '+' or i =='-'):
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(i)
            elif i ==')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
    
    while stack:
        result += stack.pop()
    
    return result
    
    
print(to_postfix(eq))