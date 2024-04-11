N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    i, j = i-1, j-1
    lst[i], lst[j] = lst[j], lst[i]
for k in lst:
    print(k, end=' ')
