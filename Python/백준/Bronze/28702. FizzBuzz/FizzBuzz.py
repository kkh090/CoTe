import sys
input = sys.stdin.readline

for i in range(3, 0, -1):
    s = input().rstrip()
    
    if s not in "FizzBuzz":
        n = int(s) + i

answer = ""

if not(n%3):
    answer += "Fizz"
if not(n%5):
    answer += "Buzz"

print(answer if answer else n)