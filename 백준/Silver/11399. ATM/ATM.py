import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(list(map(int, input().split())))
for i in range(N):
    if i > 0:
        lst[i] += lst[i-1]
print(sum(lst))
