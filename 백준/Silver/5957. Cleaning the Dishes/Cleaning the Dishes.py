import sys
input = sys.stdin.readline

N = int(input())
dishes = [i+1 for i in range(N)][::-1]
washed = []
finished = []
while True:
    if len(finished) == N:
        break
    cmd, cnt = map(int, input().split())
    if cmd == 1:
        for i in range(cnt):
            washed.append(dishes.pop())
    elif cmd == 2:
        for i in range(cnt):
            finished.append(washed.pop())

print(*finished[::-1], sep = '\n')