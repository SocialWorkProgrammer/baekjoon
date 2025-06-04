T = int(input())

def upper_bound(arr, target):
    s = 0
    e = len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    return e + 1

for tc in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        cnt += upper_bound(B, a)
    print(cnt)