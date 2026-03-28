N = int(input())

i = 2
Nlst = list()
while N > 1:
    if N % i == 0:
        N = N // i
        Nlst.append(i)
    else:
        i += 1
        pass
for j in Nlst:
    print(j)