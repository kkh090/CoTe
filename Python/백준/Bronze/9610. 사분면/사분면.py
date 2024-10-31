import sys
input = sys.stdin.readline

n = int(input())

info = {'Q1': 0,
        'Q2': 0,
        'Q3': 0,
        'Q4': 0,
        'AXIS':0}

for _ in range(n):
    x, y = map(int, input().split())
    
    if x > 0 and y > 0:
        info['Q1'] += 1
    elif x < 0 and y > 0:
        info['Q2'] += 1
    elif x < 0 and y < 0:
        info['Q3'] += 1 
    elif x > 0 and y < 0:
        info['Q4'] += 1
    else:
        info['AXIS'] += 1
    
for k, v in info.items():
    print(f"{k}: {v}")
