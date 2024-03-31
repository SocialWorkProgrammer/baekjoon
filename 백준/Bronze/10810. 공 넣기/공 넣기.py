import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0 for i in range(0, N+1)]
for _ in range(M):
    start, end, n = map(int, input().split())
    for i in range(start, end+1):
        arr[i] = n
arr.pop(0)
print(*arr)