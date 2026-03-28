num = int(input())

def beehive(N):
    lst = [0, 1, 7]
    if N == 1:
        return 1
    if N >= 2 and N < 8:
        return 2
    i = 2
    while lst[i] <= N:
        lst.append(lst[i] + 6*i)
        i += 1
        if lst[i] >= N:
            return i

print(beehive(num))