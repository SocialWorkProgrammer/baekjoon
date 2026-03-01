A,B,C = sorted(list(map(int,input().split())))

while A != 0:
    if A**2 + B**2 == C**2:
        print('right')
    else:
        print('wrong')
    A, B, C = sorted(list(map(int, input().split())))
