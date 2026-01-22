import sys
input = sys.stdin.readline

def stack(input):
    # push일 때
    if len(input) == 2:
        lst.append(int(input[1]))
    elif input[0] == 'pop':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())
    elif input[0] == 'size':
        print(len(lst))
    elif input[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif input[0] == 'top':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])

N = int(input())
lst = []
for i in range(N):
    stack(input().split())

