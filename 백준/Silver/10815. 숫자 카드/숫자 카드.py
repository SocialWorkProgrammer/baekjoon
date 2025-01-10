N = int(input())
setlst = set(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))

# 시간초과, 하지만 리스트 컴프리핸션으로 간단하죠??
# ans = [1 if x in lst else 0 for x in lst2]

ans = [1 if x in setlst else 0 for x in lst]
print(*ans)