import sys
input = sys.stdin.readline

def cmd(opr):
    if opr == '>':
        return trueorfalse(A > B)
    elif opr == '>=':
        return trueorfalse(A >= B)
    elif opr == '<':
        return trueorfalse(A < B)
    elif opr == '<=':
        return trueorfalse(A <= B)
    elif opr == '==':
        return trueorfalse(A == B)
    elif opr == '!=':
        return trueorfalse(A != B)

def trueorfalse(bool):
    if bool == True:
        return 'true'
    else:
        return 'false'

for i, equation in enumerate(sys.stdin):
    A, opr, B = equation.rstrip().split()
    A, B = int(A), int(B)
    if opr == 'E':
        break
    print(f'Case {i+1}: {cmd(opr)}')