import sys
from collections import deque
input = sys.stdin.readline
deque = deque()
N = int(input())
for tc in range(N):
    order = list(map(int, input().split()))
    num = order[0]
    if num == 1:
        deque.appendleft(order[1])
    elif num == 2:
        deque.append(order[1])
    elif num == 3:
        print(deque.popleft() if deque else -1)
    elif num == 4:
        print(deque.pop() if deque else -1)
    elif num == 5:
        print(len(deque))
    elif num == 6:
        print(0 if deque else 1)
    elif num == 7:
        print(deque[0] if deque else -1)
    elif num == 8:
        print(deque[-1] if deque else -1)