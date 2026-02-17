import sys
input = sys.stdin.readline

N = int(input())
memoization = {0:0, 1:1}
def fib(n):
    if n in memoization:
        return memoization[n]
    else:
        memoization[n] = fib(n-1) + fib(n-2)
    return memoization[n]

print(fib(N))