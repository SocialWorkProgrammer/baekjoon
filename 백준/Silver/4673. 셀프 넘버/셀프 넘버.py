lst = []
def selfnumber(n):
    m = sum(map(int, str(n)))
    return n + m

numset = set([x for x in range(1, 10000)])
selfnumset = set([selfnumber(x) for x in range(1, 10000)])

print(*sorted(list(numset - selfnumset)), sep = '\n')