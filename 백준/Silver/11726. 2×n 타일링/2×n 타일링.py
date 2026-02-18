import sys
input = sys.stdin.readline

N = int(input())
memoization = {1:1, 2:2}
def fib(n):
    if n in memoization:
        return memoization[n]
    else:
        memoization[n] = fib(n-1) + fib(n-2)
    return memoization[n]

print(fib(N)%10007)