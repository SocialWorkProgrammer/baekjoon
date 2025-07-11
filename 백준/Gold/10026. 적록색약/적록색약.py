import sys
sys.setrecursionlimit(10**6)
dirx, diry = [1, 0, 0, -1], [0, 1, -1, 0]
def dfs(graph, x, y, visited):
    if visited[x][y] == 0:
        visited[x][y] += 1
        cdict[graph[x][y]] += 1
    else:
        return cdict
    for di in range(4):
        if 0 <=  x + dirx[di] < N and 0 <= y + diry[di] < N:
            if graph[x][y] == graph[x + dirx[di]][y + diry[di]]:
                dfs(graph, x + dirx[di], y + diry[di], visited)
    return cdict

def blinddfs(graph, x, y, visited):
    if visited[x][y] == 0:
        visited[x][y] += 1
        if graph[x][y] == 'B':
            cdict2['B'] += 1
        elif graph[x][y] in 'RG':
            cdict2['RG'] += 1
    else:
        return cdict2
    for di in range(4):
        if 0 <=  x + dirx[di] < N and 0 <= y + diry[di] < N:
            if graph[x][y] == graph[x + dirx[di]][y + diry[di]]:
                blinddfs(graph, x + dirx[di], y + diry[di], visited)
            elif graph[x][y] in 'RG' and graph[x + dirx[di]][y + diry[di]] in 'RG':
                blinddfs(graph, x + dirx[di], y + diry[di], visited)
    return cdict2

graph = []
N = int(input())
for tc in range(N):
    graph.append(list(map(str, input())))

# cdict = {'R': 0, 'G':0,'RG':0,'B':0}
visited = [[0 for i in range(N)] for j in range(N)]

ans1 = 0
ans2 = 0
for i in range(N):
    for j in range(N):
        cdict = {'R': 0, 'G':0,'B':0}
        if sum(dfs(graph, i, j, visited).values()) > 0:
            ans1 += 1

visited = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        cdict2 = {'RG': 0, 'B': 0}
        if sum(blinddfs(graph, i, j, visited).values()) > 0:
            ans2 += 1
print(ans1, ans2, sep = ' ')