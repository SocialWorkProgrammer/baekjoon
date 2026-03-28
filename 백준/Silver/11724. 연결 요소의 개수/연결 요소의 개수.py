import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N, M = map(int, input().split())

# 무방향 그래프 만들기
graph = [[] for i in range(N+1)] # N+1개로 해야 설정하기 편해짐
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# dfs 함수
def dfs(graph, node, visited):
    if visited[node] == False:
        visited[node] = True
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# 계산
visited = [False] * (N+1)
cnt = 0
for i in range(1, N+1):
    if visited[i] == False:
        dfs(graph, i, visited)
        cnt += 1
print(cnt)