x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

xlst = [x1, x2, x3]
ylst = [y1, y2, y3]

for i in range(3):
    if xlst.count(xlst[i]) == 1:
        x = xlst[i]
    if ylst.count(ylst[i]) == 1:
        y = ylst[i]
print(x, y)