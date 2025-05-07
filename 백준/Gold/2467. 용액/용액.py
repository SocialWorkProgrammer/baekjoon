N = int(input())
lst = list(map(int, input().split()))

s = 0
e = N-1
inf = float("inf")
minlst = [inf, inf]
while s < e:
    mid = lst[s] + lst[e]
    if mid == 0:
        minlst = [lst[s], lst[e]]
        break
    else:
        if abs(mid) < abs(sum(minlst)):
            minlst = [lst[s], lst[e]]
        if mid < 0:
            s += 1
        else:
            e -= 1
print(*minlst)