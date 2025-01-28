import sys
import math

def isprime(a):
    if a == 0 or a == 1:
        return False
    if a == 2 or a == 3:
        return a
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
        return a

lst = [t for t in range(1, 123456 * 2)]

for x in lst:
    if x != 0:
        if isprime(x):
            lst[2*x-1::x] = [0] * len(lst[2*x-1::x])

lst = set(lst)
for tc in sys.stdin:
    if tc.strip() == '0':
        break
    tc = int(tc)
    cnt = 0
    for i in lst:
        if i >= tc + 1 and i <= 2 * tc:
            cnt += 1
    print(cnt)
