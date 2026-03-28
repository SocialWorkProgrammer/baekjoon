N, K = map(int, input().split())
a = 1
Nlst = list()
while len(Nlst) <= K:
    if len(Nlst) == K: # 만약 Nlst의 원소 개수가 K개가 되면 정답을 출력
        Nlst.append(a)
        print(Nlst[K-1])
        break
    elif a <= N:
        if N % a == 0:
            Nlst.append(a)
            a += 1
        else:
            a += 1
            pass
    else:
        print(0)
        break