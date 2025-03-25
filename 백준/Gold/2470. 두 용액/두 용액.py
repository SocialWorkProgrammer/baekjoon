N = int(input())
lst = list(map(int, input().split()))
lst = sorted(lst)
s = 0
e = N-1
target = lst[0] + lst[-1]
while s < e:
    mid = lst[s] + lst[e]
    if abs(mid) > abs(target):
        if mid > 0:
            e -= 1
        else:
            s += 1
    else:
        target = lst[s] + lst[e]
        ans1, ans2 = lst[s], lst[e]
        if target == 0:
            break
        if target > 0:
            e -= 1
        else:
            s += 1

print(ans1, ans2)