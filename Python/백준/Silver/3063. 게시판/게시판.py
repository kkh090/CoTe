import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    
    # x1, y1, x2, y2, x3, y3, x4, y4
    x1, y1, x2, y2, x3, y3, x4, y4 = list(map(int, input().split()))

    if x1 > x4 or x2 < x3 or y1 > y4 or y2 < y3:
        print((x2 - x1) * (y2 - y1))
        continue
    
    x_lb = max(x1, x3)
    y_lb = max(y1, y3)
    
    x_rt = min(x2, x4)
    y_rt = min(y2, y4)

    print((x2 - x1) * (y2 - y1) - (x_rt - x_lb) * (y_rt - y_lb))

    