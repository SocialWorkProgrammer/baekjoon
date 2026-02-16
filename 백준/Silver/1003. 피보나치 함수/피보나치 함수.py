import sys
input = sys.stdin.readline

N = int(input())
memo = {i:[0, 0] for i in range(41)}
memo[0] = [1,0]
memo[1] = [0,1]
for tc in range(N):
    x = int(input())
    cnt0, cnt1 = 0, 0
    def fib(n):
        if memo[n] != [0,0]:
            return memo[n][0], memo[n][1]
        else:
            memo[n][0] += fib(n-1)[0] + fib(n-2)[0]
            memo[n][1] += fib(n-1)[1] + fib(n-2)[1]
        return memo[n][0], memo[n][1]
    print(*fib(x))
