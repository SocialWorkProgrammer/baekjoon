arr = list(map(int, input().split()))

n = 0
while n != len(arr):
    if n == len(arr):
        break
    if n == 0:
        division = arr[0]
        n += 1
    else:
        division /= arr[n]
        n += 1
print(division)