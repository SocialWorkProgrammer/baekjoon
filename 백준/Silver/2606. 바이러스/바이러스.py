N = int(input()) # 컴퓨터 개수
line = int(input()) # 간선 개수
adjl = [[] for _ in range(N+1)]  # 각 노드가 어디에 가는지에 대한 리스트
visited = [0] * (N + 1)  # 방문한 노드 표시
for i in range(line):
    M = list(map(int, input().split())) # 번호
    adjl[M[0]].append(M[1])
    adjl[M[1]].append(M[0])

def dfs(i): # i는 시작 번호, v는 끝 번호
    visited[i] = 1
    for j in adjl[i]:
        if visited[j] == 0:
            dfs(j)

dfs(1)
print(sum(visited)-1)