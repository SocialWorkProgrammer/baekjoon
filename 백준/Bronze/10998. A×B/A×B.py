arr = list(map(int, input().split()))

sums = 1
for i in arr:
    sums *= i
    if i == 0:
        sums == 0
print(sums)