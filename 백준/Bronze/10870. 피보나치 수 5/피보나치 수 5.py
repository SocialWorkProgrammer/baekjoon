N = int(input())
memorydict = {0:0, 1:1}
def fib_memoization(n):
    if n in memorydict:
        return memorydict[n]
    return fib_memoization(n-1) + fib_memoization(n-2)

print(fib_memoization(N))