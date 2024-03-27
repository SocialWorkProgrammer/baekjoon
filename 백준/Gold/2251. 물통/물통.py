import sys
from collections import deque

def pour(x,y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x,y))

def bfs():
    while q:
        x, y = q.popleft()
        z = C - x - y

        if x == 0:
            answer.append(z)
        # 총 6가지(해당 물통의 현재 남아있는 물 양과 옮겨질 물 양 비교)
        water = min(x, B-y)
        pour(x - water, y + water)
        water = min(x, C-z)
        pour(x - water, y)
        water = min(y, A-x)
        pour(x + water , y-water)
        water = min(y, C-z)
        pour(x, y-water)
        water = min(z, A-x)
        pour(x + water, y)
        water = min(z, B-y)
        pour(x, y+ water)

A, B, C = map(int, sys.stdin.readline().split())

q = deque()
q.append((0,0))

# 2차원 배열로 visited 만들기
visited = [[False]*(B+1) for _ in range(A+1)]
visited[0][0] = True

answer = []

bfs()

answer.sort()
for i in answer:
    print(i, end = " ")