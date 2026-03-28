X = int(input())
N = int(input())
sums = 0
for n in range(N):
    a, b = map(int, input().split())
    sums += a * b
if sums == X:
    print('Yes')
else: print('No')