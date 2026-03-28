from collections import deque

N, K = map(int, input().split())

circle = deque([x for x in range(1, N+1)])
lst = []
i = 1
while circle:
    if i % K != 0:
        a = circle.popleft()
        circle.append(a)
    else:
        b = circle.popleft()
        lst.append(b)
    i += 1
anslst = '<' + ', '.join([str(x) for x in lst]) + '>'
print(anslst)