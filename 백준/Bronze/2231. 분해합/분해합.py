N = int(input())
strN = str(N)
ans = 0

for i in range(N+1):
    arr = []
    for j in str(i):
        arr.append(int(j))
    if sum(arr) + i == N:
        ans = i
        break
print(ans)