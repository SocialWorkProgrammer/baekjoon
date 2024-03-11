K = int(input())
inequality = list(map(str, input().split()))
# visited 위한 빈 리스트
visited = [0] * 11
max_v = ""
min_v = ""

def inequalitysign(i, j, k):
    if k == '>':
        return i > j
    else:
        return i < j

def visit(depth, s):
    global max_v, min_v

    if depth == K+1:
        if len(min_v) ==0:
            min_v = s
        else:
            max_v = s
        return
    for i in range(10):
        if not visited[i]:
            if depth == 0 or inequalitysign(s[-1], str(i), inequality[depth-1]):
                visited[i] = True
                visit(depth+1, s + str(i))
                visited[i] = False
visit(0, "")
print(max_v)
print(min_v)