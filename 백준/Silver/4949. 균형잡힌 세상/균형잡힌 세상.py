import sys

def remover(stack):
    fstack = []
    for i in stack:
        if i in '([':
            fstack.append(i)
        elif i in ')]':
            if not fstack:
                return 'no'
            if (fstack[-1] == '(' and i == ')') or (fstack[-1] == '[' and i == ']'):
                fstack.pop()
            else:
                return 'no'
    return 'yes' if not fstack else 'no'

for data in sys.stdin:
    if data.rstrip() == '.':
        break
    else:
        strstack = list(filter(lambda x: x in '()[]', map(str, data)))
        print(remover(strstack))
