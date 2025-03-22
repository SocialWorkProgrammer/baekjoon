lst = []
N, C = map(int, input().split())
for tc in range(N):
    lst.append(int(input()))

lst = sorted(lst)

s = 1
e = lst[-1] - lst[0]
while s <= e:
    mid = s + (e - s) // 2
    dis, cnt = 0, 1
    for i in range(1, N):
        dis += lst[i] - lst[i-1]
        if dis >= mid:
            cnt += 1
            dis = 0
    if cnt >= C:
        s = mid + 1
        ans = mid
    else:
        e = mid - 1
print(ans)