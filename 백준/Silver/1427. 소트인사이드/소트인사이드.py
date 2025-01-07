import sys

N = list(map(int, input()))
cntlst = [0] * 10
ans = ''

for i in N:
    cntlst[i] += 1

for j in range(10):
    for k in range(cntlst[j]):
        ans += str(j)

print(ans[::-1])
