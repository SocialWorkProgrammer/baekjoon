import math

M, N = map(int, input().split())
lst = [x for x in range(M, N+1)]

def isprime(a):
    if a == 1:
        return False
    if a == 2 or a == 3:
        return True
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

for num in lst:
    if isprime(num):
        print(num)