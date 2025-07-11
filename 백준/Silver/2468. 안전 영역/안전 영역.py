
import sys
sys.setrecursionlimit(10**6)
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))


dirx, diry = [-1, 0, 0, 1], [0, -1, 1, 0]
def dfs(graph, x, y, visited):
    global areas, height
    if visited[x][y] == 0:
        visited[x][y] = 1
        if graph[x][y] > height:
            areas += 1
            for di in range(4):
                if 0 <= x + dirx[di] < N and 0 <= y + diry[di] < N:
                    dfs(graph, x + dirx[di], y + diry[di], visited)
    return areas

ans = 0
for k in range(1, 101):
    temp = 0
    cnt = 0
    visited = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            areas = 0
            height = k
            if dfs(graph, i, j, visited) > 0:
                cnt += 1
    if cnt > ans:
        ans = cnt
if ans == 0:
    ans = 1
print(ans)