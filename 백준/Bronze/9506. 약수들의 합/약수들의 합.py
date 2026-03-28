while True:
    n = int(input())
    if n == -1:
        break
    else:
        Nlst = [1]
        for i in range(2, n):
            if n % i == 0:
                Nlst.append(i)

        for j in Nlst:
            div = int(n / j)
            if div not in Nlst:
                Nlst.append(div)
        Nlst.remove(n)
        if sum(Nlst) == n:
            print(f'{n} =', end='')
            for k in range(len(Nlst)):
                if k + 1 < len(Nlst):
                    print(f' {Nlst[k]} +', end='')
                if k + 1 == len(Nlst):
                    print(f' {Nlst[k]}')
        else:
            print(f'{n} is NOT perfect.')
