T = int(input())
for tc in range(1, T+1):
    N = list(input())
    lst = []
    def VPS(N):
        for i in range(len(N)):
            if N[i] == '(':
                lst.append(N[i])
            elif lst and lst[-1] == '(' and N[i] == ')':
                lst.pop()
            elif N[i] == ')':
                lst.append(N[i])
        if len(lst) == 0:
            return 'YES'
        elif len(lst) >= 1:
            return 'NO'
    print(VPS(N))