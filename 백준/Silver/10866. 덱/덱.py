import sys
from collections import deque
input = sys.stdin.readline

dequeue = deque(list())
for i in range(int(input())):
    ipt = list(map(str, input().split()))
    cmd = ipt[0]
    if len(ipt) == 2:
        if cmd == "push_front":
            dequeue.appendleft(int(ipt[1]))
        elif cmd == "push_back":
            dequeue.append(int(ipt[1]))
    else:
        length = len(dequeue)
        if cmd == "empty":
            if length == 0:
                print(1)
            elif length >= 1:
                print(0)
        elif cmd == "size":
            print(length)
        elif length == 0:
            print(-1)
        else:
            if cmd == "front":
                print(dequeue[0])
            elif cmd == "back":
                print(dequeue[-1])
            elif cmd == "pop_front":
                print(dequeue.popleft())
            elif cmd == "pop_back":
                print(dequeue.pop())