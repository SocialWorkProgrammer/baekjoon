N = int(input())
lst = sorted([int(x) for x in input().split()])
M = int(input())

s = 1
e = lst[-1]
while s <= e:
    mid = s + (e-s)//2
    sums = 0
    for i in lst:
        if i <= mid:
            sums += i
        else:
            sums += mid
    if sums <= M:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1
print(ans)