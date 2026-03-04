n = int(input())
Nlst = list(map(int, input().split()))
if n == 1:
    print(Nlst[0]**2)
else:
    print(min(Nlst) * max(Nlst))