import sys
from collections import deque
input = sys.stdin.readline

N, K = list(map(int, input().split()))
circle = deque([i for i in range(1, N+1)])

i = 1
cnt = 0
ans = []
while len(circle) > 0:
    if i % K == 0:
        ans.append(circle.popleft())
    else:
        circle.append(circle.popleft())
    i += 1
print(f'<{', '.join(map(str, ans))}>')