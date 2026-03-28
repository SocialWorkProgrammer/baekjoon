import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
assey = list(map(int, sys.stdin.readline().split()))

count = Counter(arr)
for i in assey:
    if i in count:
        print(count[i], end=' ')
    else:
        print(0, end=' ')
