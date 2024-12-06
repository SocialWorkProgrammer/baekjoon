a, b, c = map(int,input().split())
maxL = max(a,b,c)
if maxL >= sum([a, b, c]) - maxL:
    print(2 * (sum([a,b,c]) - maxL) - 1)
else:
    print(sum([a,b,c]))