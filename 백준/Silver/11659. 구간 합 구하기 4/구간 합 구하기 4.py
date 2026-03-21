import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lstsum = [0]
sums = 0
for _ in range(N):
    sums += lst[_]
    lstsum.append(sums)
for tc in range(M):
    i, j = map(int, input().split())
    print(lstsum[j] - lstsum[i-1])