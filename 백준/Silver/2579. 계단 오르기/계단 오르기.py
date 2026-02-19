import sys
input = sys.stdin.readline

#topdown 사용
N = int(input())
stairs = [int(input()) for i in range(N)]

if N == 1:
    print(stairs[0])
else:
    dp = [[0, 0] for i in range(N)]
    dp[0] = [0, stairs[0]]
    dp[1] = [stairs[1], stairs[0] + stairs[1]]
    def recur(x):
        for i in range(2,x):
            dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + stairs[i]
            dp[i][1] = dp[i-1][0] + stairs[i]
        return max(dp[-1])
    print(recur(N))