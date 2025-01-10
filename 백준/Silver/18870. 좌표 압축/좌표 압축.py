N = int(input())
lst = list(map(int, input().split()))
duplst = list(sorted(set(lst)))

dupdict = {value : idx for idx, value in enumerate(duplst)}
ans = [dupdict[x] for x in lst]
print(*ans)
