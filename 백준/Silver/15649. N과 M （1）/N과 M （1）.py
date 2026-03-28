import itertools

N, M = map(int, input().split())
Nlst =[]
def makeNlst(N):
    for n in range(1, N+1):
        Nlst.append(n)
    return Nlst

result = list(itertools.permutations(makeNlst(N), M))
for i in range(len(result)):
    print(*result[i])