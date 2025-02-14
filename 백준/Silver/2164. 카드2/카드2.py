import sys

from collections import deque

N = int(input())
cardlst = deque([x for x in range(1, N+1)])

while len(cardlst) > 1:
    cardlst.popleft()
    cardlst.append(cardlst.popleft())

print(cardlst[0])