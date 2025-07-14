N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 이렇게만 끝나면 틀림 -> 문제에서 정점 번호가 작은 것부터 먼저 방문하라 했기 때문!
for t in graph:
    t.sort()

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
    return visited

from collections import deque
def bfs(graph, node, visited):
    queue = deque([node]) # 시작 노드를 갖고 있어야함
    while queue:
      curr_node = queue.popleft()
      for neighbor in graph[curr_node]:
          if neighbor not in visited:
              visited.append(neighbor)
              queue.append(neighbor)
    return visited

print(*dfs(graph, V, []))
print(*bfs(graph, V, [V]))