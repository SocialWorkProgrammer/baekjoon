# 9. 나머지
A, B, C = map(int, input().split())

def remains():
    print((A+B)%C)
    print(((A%C)+(B%C))%C)
    print((A*B)%C)
    print((A%C)*(B%C)%C)

remains()