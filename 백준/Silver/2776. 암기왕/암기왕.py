def binary_search(arr, target):
    s = 0
    e = len(arr) -1
    while s <= e:
        mid = s + (e-s) // 2
        # print(s, mid, e)
        if arr[mid] == target:
            return print(1)
        elif arr[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    return print(0)

A = int(input())
for tc in range(A):
    N = int(input())
    lst1 = sorted(list(map(int, input().split())))
    M = int(input())
    lst2 = list(map(int, input().split()))
    for i in range(M):
        binary_search(lst1, lst2[i])
