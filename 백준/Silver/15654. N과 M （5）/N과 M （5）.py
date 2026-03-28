import itertools

N, M = map(int, input().split())
Nlst = list(map(int, input().split()))

result = list(itertools.permutations(Nlst, M))
result.sort()
for i in range(len(result)):
    print(*result[i])