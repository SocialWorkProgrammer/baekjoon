N, M = map(int, input().split())
listen = []
seen = []
for i in range(N):
    name = input()
    listen.append(name)
for i in range(N, N+M):
    name = input()
    seen.append(name)

listen = set(listen)
seen = set(seen)
ans = sorted(list(listen & seen))
print(len(ans))
print(*ans, sep = '\n')
