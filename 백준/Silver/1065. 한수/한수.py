N = int(input())

if N < 100:
    print(N)
else:
    cnt = 99
    for i in range(100, N+1):
        n = list(map(int, str(i)))
        if n[2] - n[1] == n[1] - n[0]:
            cnt += 1
        elif n[0] - n[1] == n[1] - n[2]:
            cnt += 1
    print(cnt)