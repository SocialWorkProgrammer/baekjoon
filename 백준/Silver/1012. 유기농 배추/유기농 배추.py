import sys
sys.setrecursionlimit(10**6)

from copy import deepcopy

def dfs(graph, y, x, visited):
    global cnt
    if graph[y][x] == 1 and visited[y][x] == 0:
        visited[y][x] = 1
        cnt += 1
        for i in range(4):
            if 0 <= y + diry[i] < N and 0 <= x + dirx[i] < M:
                dfs(graph, y + diry[i], x + dirx[i], visited)
    return cnt


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for i in range(N)]
    visited = deepcopy(graph)
    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] += 1
    dirx = [0, 0, -1, 1]
    diry = [-1, 1, 0, 0]
    ans = []
    for y in range(N):
        for x in range(M):
            cnt = 0
            if dfs(graph, y, x, visited) != 0:
                ans.append(cnt)
    print(len(ans))
