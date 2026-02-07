import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
circle = [i for i in range(1, N+1)]

cnt = 0
ans = []
for _ in range(N):
    cnt += K - 1
    if cnt >= len(circle):
        cnt %= len(circle)
    ans.append(circle.pop(cnt))

print(f'<{', '.join(map(str, ans))}>')