from math import factorial
for tc in range(int(input())):
    N, M = list(map(int, input().split()))
    ans = factorial(M) // (factorial(N) * factorial(M-N))
    print(ans)