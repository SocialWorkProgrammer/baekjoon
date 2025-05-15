N = int(input())
graph = []
for tc in range(N):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def housedfs(graph, x, y, visited):
    global cnt
    if not visited[x][y] and graph[x][y] == 1:
        visited[x][y] = True
        cnt += 1
        for i in range(4):
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
                housedfs(graph, x + dx[i], y + dy[i], visited)
    return cnt

visited = [[False] * N for i in range(N)]
housecnt = 0
lst = []
for x in range(N):
    for y in range(N):
        cnt = 0
        if housedfs(graph, x, y, visited) != 0:
            housecnt += 1
            lst.append(cnt)

print(housecnt)
for i in sorted(lst):
    print(i)