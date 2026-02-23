import sys
input = sys.stdin.readline

#bottomup 사용
x = int(input())
memo = {1:1, 2:1}
def dp(x):
    if x in memo:
        return memo[x]
    for i in range(2, x):
        memo[x] = dp(x-1) + dp(x-2)
    return memo[x]
print(dp(x))