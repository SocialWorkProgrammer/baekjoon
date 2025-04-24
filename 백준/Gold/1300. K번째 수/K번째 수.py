N = int(input())
K = int(input())
s = 1
e = N * N

def count_nums(mid):
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid // i, N)
    return cnt

while s < e:
    mid = (s + e) // 2
    # count_nums(mid) <= K는 upper bound로, K번째 값을 초과할 때 e를 구함
    if count_nums(mid) < K:
        s = mid + 1
    else:
        e = mid
print(s)