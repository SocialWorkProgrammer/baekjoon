N, M = map(int, input().split())
lst = list(map(int, input().split()))

s = max(lst)
e = sum(lst)
while s <= e:
    mid = (s + e)//2
    length = 0
    cnt = 1
    # lst2 = 길이 리스트
    for i in lst:
        if length + i > mid:
            cnt += 1
            length = 0
        length += i
    if cnt <= M:
        e = mid - 1
        ans = mid
    elif cnt > M:
        s = mid + 1
print(ans)