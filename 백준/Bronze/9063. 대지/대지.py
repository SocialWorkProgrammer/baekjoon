Xlst = list()
Ylst = list()

N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    Xlst.append(x)
    Ylst.append(y)
print((max(Xlst) - min(Xlst)) * (max(Ylst) - min(Ylst)))