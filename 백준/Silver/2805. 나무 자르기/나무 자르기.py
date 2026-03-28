import sys

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)
while start <= end:
    mid = (start + end) // 2
    key = 0
    for i in trees:
        if i >= mid:
            key += i - mid
    if key >= M:
        start = mid + 1
    elif key < M:
        end = mid - 1
print(end)
