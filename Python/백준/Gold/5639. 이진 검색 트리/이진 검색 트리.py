import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

def solution(start, end):
    if start > end:
        return
    
    mid = end + 1
    
    for i in range(start+1, end + 1):
        if arr[i] > arr[start]:
            mid = i
            break
    
    solution(start+1, mid - 1)
    solution(mid, end)
    print(arr[start])
    
solution(0, len(arr)-1)