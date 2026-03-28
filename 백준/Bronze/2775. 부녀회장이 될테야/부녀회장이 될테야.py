T = int(input())
for i in range(T):
    k, n = int(input()), int(input())
    lst = [[0 for _ in range(n)] for _ in range(k+1)]
    # 0층 채우기
    for _ in range(n):
        lst[0][_] += _ + 1
    a = 1
    while True:
        if a == k+1:
            print(lst[k][n-1])
            break
        for q in range(n):
            lst[a][q] = sum([lst[a-1][_] for _ in range(q+1)])
        a += 1
