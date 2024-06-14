maxarr = []
idxarr = []
for tc in range(9):
    arr = list(map(int, input().split()))
    maxarr.append(max(arr))
    idxarr.append(arr.index(max(arr)))

maxrow = idxarr[maxarr.index(max(maxarr))]+1 # 행 최댓값
maxcol = maxarr.index(max(maxarr))+1 # 열 최댓값
print(max(maxarr))
print(maxcol, maxrow)
