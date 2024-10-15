t = int(input())

for _ in range(t):
    x = int(input())
    
    if abs(x) % 2:
        print(f"{x} is odd")
    else:
        print(f"{x} is even")