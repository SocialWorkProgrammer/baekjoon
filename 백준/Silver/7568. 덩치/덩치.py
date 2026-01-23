import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
# print(lst)
cntlst = [1 for _ in range(N)]
for idx, (x, y) in enumerate(lst):
    for i, j in lst:
        if x < i and y < j:
            cntlst[idx] += 1
print(*cntlst)