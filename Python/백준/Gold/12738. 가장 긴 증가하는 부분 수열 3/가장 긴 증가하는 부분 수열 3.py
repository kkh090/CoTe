import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

arr = [A[0]]

for i in range(1, len(A)):
    if A[i] > arr[-1]:
        arr.append(A[i])
    else:
        index = binary_search(arr, A[i])
        arr[index] = A[i]

print(len(arr))