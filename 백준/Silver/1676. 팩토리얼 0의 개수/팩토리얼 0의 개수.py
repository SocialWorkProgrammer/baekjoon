from math import factorial

L = factorial(int(input()))
cnt2 = 0
for i in str(L):
    if L % 10 == 0:
        cnt2 += 1
        L //= 10
print(cnt2)
