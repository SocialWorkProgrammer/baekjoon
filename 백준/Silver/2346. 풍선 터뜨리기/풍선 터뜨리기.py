from collections import deque

N = int(input())
ballons = deque(enumerate(map(int,input().split())))
# +는 오른쪽으로 이동, -는 왼쪽으로 이동
ans = []
while ballons:
    idx, now = ballons.popleft()
    ans.append(idx+1)
    # print(idx, now)
    # print(ans)
    if now > 0:
        ballons.rotate(-now+1)
    elif now < 0:
        ballons.rotate(-now)
print(*ans)