import sys
sys.setrecursionlimit(10**6)
dirx = [1, 1, 1, 0, 0, -1, -1, -1]
diry = [1, 0, -1, 1, -1, 1, 0, -1]
def dfs(graph, x, y, visited):
    global cnt
    if visited[y][x] == 0:
        visited[y][x] = 1
        if graph[y][x] == 1:
            cnt += 1
        else:
            return cnt
        for neighbor in range(8):
            if 0 <= x + dirx[neighbor] < w and 0 <= y + diry[neighbor] < h:
                dfs(graph, x + dirx[neighbor], y + diry[neighbor], visited)
    return cnt

flag = 0
while flag == 0:
    w, h = map(int, input().split())
    if w == 0:
        flag = 1
        break
    lst = []
    for i in range(h):
        lst.append(list(map(int, input().split())))
    visited = [[0 for i in range(w)] for j in range(h)]
    islands = 0
    for y in range(h):
        for x in range(w):
            cnt = 0
            if dfs(lst, x, y, visited) > 0:
                islands += 1
    print(islands)

