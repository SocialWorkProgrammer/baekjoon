N = int(input())
lst = list(map(int,input().split()))
LIS = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if lst[j] < lst[i]:
            LIS[i] = max(LIS[i], LIS[j]+1)
print(max(LIS))