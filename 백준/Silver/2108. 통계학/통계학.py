import sys

input = sys.stdin.readline
N = int(input())
lst = [int(input()) for i in range(N)]

def mode(lst):
    ndict = {i : 0 for i in lst}
    for i in lst:
        ndict[i] += 1
    nlst = sorted([i for i in ndict if ndict[i] == max(ndict.values())])
    if len(nlst) >= 2:
        return nlst[1]
    return nlst[0]

print(round(sum(lst)/N))
print(sorted(lst)[N//2])
print(mode(lst))
print(max(lst) - min(lst))