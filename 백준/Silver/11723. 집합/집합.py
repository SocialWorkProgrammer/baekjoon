import sys
input = sys.stdin.readline

N = int(input())

def cmdx(command):
    command, x = command
    x = int(x)
    if command == 'add':
        setx.add(x)
    elif command == 'remove':
        setx.discard(x)
    elif command == 'check':
        if x in setx:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if x in setx:
            setx.discard(x)
        else:
            setx.add(x)

def cmd(command):
    if command == 'all':
        setx.clear()
        setx.update(range(1,21))
    elif command == 'empty':
        setx.clear()

setx = set()
for i in range(N):
    command = input().split()
    if len(command) >= 2:
        cmdx(command)
    else:
        command = command[0]
        cmd(command)