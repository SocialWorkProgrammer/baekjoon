N = int(input())

def fib(N):
    lst = []
    for n in range(N+1):
        if n == 0:
            lst.append(0)
        if n == 1 or n == 2:
            lst.append(1)
        elif 2 < n <= N:
            lst.append(lst[-1] + lst[-2])
    return lst[-1]
print(fib(N))