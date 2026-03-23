import sys
input = sys.stdin.readline

DP = {1:-1, 2:1,3:-1, 4:2, 5:1}

for i in range(6, 100001):
    if DP[i-2] != -1:
        DP[i] = DP[i-2] + 1
    if DP[i-5] != -1:
        DP[i] = min(DP[i-2]+1, DP[i-5]+1)

N = int(input())
print(DP[N])