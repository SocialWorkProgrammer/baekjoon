N, K = map(int,input().split())
lancables = [int(input()) for x in range(N)]

s = 1
e = max(lancables)
while s <= e:
    mid = s + (e - s) // 2
    lancnt = 0
    for i in lancables:
        lancnt += i // mid
    if lancnt >= K:
        s = mid + 1
    elif lancnt < K:
        e = mid-1
print(e)