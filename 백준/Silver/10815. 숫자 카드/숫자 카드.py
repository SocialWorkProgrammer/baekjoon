N = int(input())
setlst = set(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))

# 시간초과, 하지만 리스트 컴프리핸션으로 간단하죠??
# ans = [1 if x in lst else 0 for x in lst2]
for i in range(M):
    if lst2[i] in setlst:
        lst2[i] = 1
    else:
        lst2[i] = 0
print(*lst2)