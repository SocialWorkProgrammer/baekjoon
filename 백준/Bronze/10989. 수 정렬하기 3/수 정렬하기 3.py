import sys
input = sys.stdin.readline

N = int(input())
cntlst = [0] * 10001
for tc in range(N):
    cntlst[int(input())] += 1

for i in range(len(cntlst)):
    for j in range(cntlst[i]):
        print(i)