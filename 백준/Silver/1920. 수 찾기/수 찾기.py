import sys

N = int(input())
Nlst = sorted(list(map(int, input().split())))
M = int(input())
Mlst = list(map(int, input().split()))


def binary_search(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid -1)
    else:
        return binary_search(arr, target, mid + 1, end)

for i in range(M):
    print(binary_search(Nlst, Mlst[i], 0, N-1))