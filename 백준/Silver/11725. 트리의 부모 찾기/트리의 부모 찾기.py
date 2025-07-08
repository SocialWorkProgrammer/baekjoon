import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)
for i in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    for neighbor in graph[node]:
        if visited[neighbor] == 0:
            visited[neighbor] = node
            dfs(neighbor)

visited = [0 for i in range(N+1)]
dfs(1)
for ans in visited[2:]:
    print(ans)