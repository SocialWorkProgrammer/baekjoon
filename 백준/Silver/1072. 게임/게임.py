X, Y = map(int, input().split())
s = 1
e = X * 100
ans = -1 # ans가 안 나올경우 디폴트 값 -1
while s <= e: # ans의 최댓값이 e가 될 수 있으므로
    mid = (s + e) // 2
    if X == 0 or Y == 0:
        Z = 0
    else:
        # Z = int(Y/X * 100)
        Z = int(Y * 100 / X)
    record = int((Y+mid) * 100 / (X+mid))
    if record > Z:
        e = mid - 1
        ans = mid
    else:
        s = mid + 1
print(ans)
