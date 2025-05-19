N = int(input())
graph = [list(map(int, input())) for i in range(N)]
visited = [[0] * N for i in range(N)]
dirx, diry = [1, -1, 0, 0], [0, 0, 1, -1]

def housedfs(graph, x, y, visited):
    global cnt
    if graph[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] = 1
        cnt += 1
        for n in range(4):
            if 0 <= x + dirx[n] < N and 0 <= y + diry[n] < N:
                housedfs(graph, x + dirx[n], y + diry[n], visited)
    return cnt

ans = []
for i in range(N):
    for j in range(N):
        cnt = 0
        if (result := housedfs(graph, i, j, visited)) != 0:
            ans.append(result)
print(len(ans))
print(*sorted(ans), sep = "\n")