import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
deq = deque()
for i in range(N):
    cmd = list(map(str, input().split()))
    if len(cmd) == 2:
        cmd, n = cmd
        deq.append(n)
    else:
        cmd = cmd[0]
        if cmd == 'pop' and deq:
            print(deq.popleft())
        elif cmd == 'size':
            print(len(deq))
        elif cmd == 'empty':
            if deq:
                print(0)
            else:
                print(1)
        elif cmd == 'front' and deq:
            print(deq[0])
        elif cmd == 'back' and deq:
            print(deq[-1])
        else:
            print(-1)
