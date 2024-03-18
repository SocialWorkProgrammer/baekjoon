# 답
T= int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 1
    while arr:
        if arr[0] < max(arr):
            arr.append(arr.pop(0))
        else:
            if M == 0: break

            arr.pop(0)
            cnt += 1

        M = M -1 if M > 0 else len(arr) -1
    print(cnt)