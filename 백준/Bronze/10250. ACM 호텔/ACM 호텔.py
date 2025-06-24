T = int(input())
for tc in range(T):
    lst = []
    H, W, N = map(int, input().split())
    for i in range(1, W+1):
        for j in range(1, H+1):
            lst.append([j, i])
    Y, X = lst[N-1]
    if X < 10:
        X = '0' + str(X)
    print(str(Y) + str(X))