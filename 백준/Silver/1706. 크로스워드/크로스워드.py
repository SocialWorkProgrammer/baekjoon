import sys

N, M = map(int, sys.stdin.readline().split())
lst = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
result = []
# 가로
for i in range(N):
    words = ''
    for j in range(M):
        if lst[i][j] == '#':
            if len(words) > 1:
                result.append(words)
            words = ''
            pass
        else:
            words += lst[i][j]
    if len(words) > 1 and '#' not in words:
        result.append(words)
    if '' in result:
        result.remove(result[result.index('')])
# 세로
for i in range(M):
    words = ''
    for j in range(N):
        if lst[j][i] == '#':
            if len(words) > 1:
                result.append(words)
            words = ''
            pass
        else:
            words += lst[j][i]
    if len(words) > 1 and '#' not in words:
        result.append(words)
    if '' in result:
        result.remove(result[result.index('')])
result = sorted(result)
print(result[0])