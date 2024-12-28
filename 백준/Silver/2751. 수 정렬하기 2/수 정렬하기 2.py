import sys

lst = []
N = int(sys.stdin.readline())
for tc in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()
for i in lst:
    print(i)