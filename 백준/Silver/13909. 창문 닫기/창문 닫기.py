import sys
N = int(input())

t = 1
while N > t**2:
    if (t+1) ** 2 > N:
        break
    t += 1
print(t)