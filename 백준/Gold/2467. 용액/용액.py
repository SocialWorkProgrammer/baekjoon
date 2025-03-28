N = int(input())
lst = list(map(int, input().split()))

s, e = 0, N-1
final = [lst[s], lst[e]]
while s < e:
    left, right = lst[s], lst[e]
    mid = left + right
    if abs(mid) <= abs(sum(final)):
        final = [left, right]
        if mid == 0:
            break
    if mid < 0:
        s += 1
    elif mid > 0:
        e -= 1
print(*final)