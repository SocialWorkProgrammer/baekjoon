M = int(input())
N = int(input())

sumlst = list()
for i in range(M, N+1):
    sumlst.append(i)
    for j in range(2, i):
        if i != j and i % j == 0:
            sumlst.remove(i)
            break

if 1 in sumlst:
    sumlst.remove(1)
    if sumlst == []:
        print(-1)
    else:
        print(sum(sumlst))
        print(min(sumlst))
elif sumlst:
    print(sum(sumlst))
    print(min(sumlst))
else:
    print(-1)