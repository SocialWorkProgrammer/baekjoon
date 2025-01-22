N = int(input())

lst = [] # 가로수 위치 리스트
for tc in range(N):
    lst.append(int(input()))
# print(lst)

dislst = [] # 각 가로수 간 거리 리스트
for i in range(N-1):
    dislst.append(lst[i+1] - lst[i])
# print(dislst)

def Euclidean(a, b):
    while b != 0:
        [a, b] = [b, a % b]
    return a

GCDlst = dislst[0]
for j in range(len(dislst)):
    GCDlst = Euclidean(GCDlst, dislst[j])

for k in range(len(dislst)):
    dislst[k] = dislst[k] // GCDlst -1
print(sum(dislst))
