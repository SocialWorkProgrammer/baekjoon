import math

N = int(input())
lst = []
for tc in range(N):
    lst.append(int(input()))

def isprime(a):
    if a == 0 or a == 1:
        return False
    if a == 2 or a == 3:
        return True
    for num in range(2, int(math.sqrt(a))+1):
        if a % num == 0:
            return False
    return True

for case in lst:
    while True:
        if isprime(case):
            print(case)
            break
        else:
            case += 1